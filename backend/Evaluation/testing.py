import copy
from typing import List, Dict, Any, Tuple
import os
import asyncio
import time
import bert_score
import numpy as np
from sentence_transformers import SentenceTransformer, util

from Evaluation.eval_utils import fetch_results
from utils.network_utils import HttpClient, fetch_metadata_using_url

from Evaluation.eval_config import ApiConfig, TestConfig
from Evaluation.file_handler import FileManager, ReferenceManager

import logging
from config import get_env_settings

logger = logging.getLogger(__name__)
env_settings = get_env_settings()


class TestExecutor:
    """Handles the execution of model evaluation tests."""

    def __init__(
        self,
        api_config: ApiConfig = ApiConfig(),
        test_config: TestConfig = TestConfig(),
        file_manager: FileManager = FileManager(),
    ):
        self.api_config = api_config
        self.test_config = test_config
        self.file_manager = file_manager
        self._execution_lock = asyncio.Lock()  # Lock to ensure sequential execution

    async def fetch_or_load_metadata(self, url: str, test_id: str) -> Dict[str, Any]:
        """Fetch metadata from URL or load from disk if already present."""
        embedded_path, api_path = self.file_manager.get_metadata_paths(url, test_id)

        # Check if metadata files already exist
        if os.path.exists(embedded_path) and os.path.exists(api_path):
            logger.info(f"Loading metadata for item {url} from disk")
            return self.file_manager.load_metadata(embedded_path, api_path)

        # Fetch new metadata
        logger.info("Fetching metadata from URL")
        success, metadata = await fetch_metadata_using_url(url.strip("/"))

        if not success:
            raise RuntimeError(f"Failed to retrieve metadata for URL: {url}")

        # Save metadata to disk
        self.file_manager.save_metadata(embedded_path, api_path, metadata)
        logger.info("Metadata files stored on disk")

        return metadata

    async def run_test_iteration(
        self,
        metadata: Dict[str, Any],
        model: Dict[str, str],
        temperature: float,
        url: str,
        test_id: str,
        iteration: int,
        client,
    ) -> None:
        """Run a single test iteration for a model with given parameters."""
        meta = copy.deepcopy(metadata)
        meta["model"] = model
        meta["model_options"] = {
            "temp": temperature,
            "top_p": env_settings.top_p,
            "num_ctx": env_settings.num_ctx,
            "keep_alive": env_settings.keep_alive,
        }

        try:
            # Submit evaluation request
            response = await client.post(self.api_config.request_url, json=meta)
            response.raise_for_status()
            req = response.json()

            if not req.get("success"):
                logger.warning(f"Test request was not successful: {req}")
                return

            # Fetch results
            logger.info("Starting to fetch results")
            logger.info(self.api_config.status_url)
            logger.info(self.api_config.results_url)

            results = await fetch_results(
                initiated_task_str=req["task_id"],
                client=client,
                STATUS_URL=self.api_config.status_url,
                RESULTS_URL=self.api_config.results_url,
            )

            if results is None:
                logger.warning(f"No results returned for task ID: {req['task_id']}")
                return

            # Save results
            results_path = self.file_manager.get_results_path(
                model["model_name"], temperature, url, test_id, iteration
            )
            self.file_manager.save_results(results_path, results)
            logger.info(f"Results written to {results_path}")
        except Exception as e:
            logger.error(f"Error in test iteration: {e}", exc_info=True)
            raise e

    async def run_model_tests(
        self, model: Dict[str, str], test_items: List[Tuple[str, str]]
    ) -> None:
        """Run tests (for a specific model with strict isolation) for a specific model across all test items and temperatures."""
        # Use a lock to ensure only one model runs at a time across all instances
        async with self._execution_lock:
            logger.info(f"Starting tests for model: {model['model_name']}")
            client = HttpClient.get_client()  # Create a client within this context
            tests_executed = False
            try:
                for temperature in self.test_config.temperatures:
                    logger.info(
                        f"Testing model: {model['model_name']} with temperature: {temperature}"
                    )
                    for url, test_id in test_items:
                        try:
                            # Check if results already exist for this combination
                            if self.file_manager.check_results_exist(
                                model["model_name"], temperature, url, test_id
                            ):
                                logger.info(
                                    f"Skipping test for model={model['model_name']}, temp={temperature}, "
                                    f"url={url}, test_id={test_id} as results already exist."
                                )
                                continue

                            logger.info(
                                f"Executing test for model={model['model_name']}, temp={temperature}, "
                                f"url={url}, test_id={test_id}"
                            )

                            # Get metadata
                            metadata = await self.fetch_or_load_metadata(url, test_id)

                            # Run test iterations
                            for i in range(self.test_config.test_repeat_n):
                                await self.run_test_iteration(
                                    metadata,
                                    model,
                                    temperature,
                                    url,
                                    test_id,
                                    i + 1,
                                    client,
                                )

                            # Set the flag to true as a test was executed
                            tests_executed = True

                        except Exception as e:
                            logger.error(
                                f"Error processing test item {url}: {e}", exc_info=True
                            )

            finally:
                # Only perform sleep logic if tests were actually executed
                if tests_executed:
                    if model["service"].lower() == "ollama":
                        # Wait for model to be evicted before testing the next model
                        keep_alive_minutes = int(env_settings.keep_alive.strip("m"))
                        logger.info(
                            f"Sleeping for {keep_alive_minutes + 2} minutes until {model['model_name']} is evicted"
                        )
                        # Use Blocking sleep function
                        time.sleep((keep_alive_minutes + 2) * 60)
                        logger.info(
                            f"Wait complete. Model {model['model_name']} should be unloaded now."
                        )
                    elif model["service"].lower() == "openai":
                        logger.info(
                            f"Sleeping for 2 minutes after testing {model['model_name']}"
                        )
                        # Use Blocking sleep function
                        time.sleep(2 * 60)
                        logger.info(
                            f"Wait complete. Model {model['model_name']} should be unloaded now."
                        )

    def execute_all_tests(self, test_items: List[Tuple[str, str]]) -> None:
        """Execute tests for all models."""
        # Create a single event loop for the entire execution
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            # Process each model sequentially
            for model in self.test_config.model_list:
                logger.info(
                    f"=== Starting execution for model: {model['model_name']} ==="
                )
                # Run this model's tests to completion before moving to the next
                loop.run_until_complete(self.run_model_tests(model, test_items))
                logger.info(
                    f"=== Completed execution for model: {model['model_name']} ==="
                )
        finally:
            # Close the loop only after all tests are completed
            loop.close()


class ResultEvaluator:
    """Handles the evaluation of test results against reference outputs."""

    def __init__(
        self,
        test_config: TestConfig = TestConfig(),
        file_manager: FileManager = FileManager(),
    ):
        self.test_config = test_config
        self.file_manager = file_manager
        self.ref_mgr = ReferenceManager()

        self.sim_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Define evaluation keys in a more structured way
        self._initialize_evaluation_keys()

    def _initialize_evaluation_keys(self):
        """Initialize test keys for different evaluation methods."""
        # Structure test keys
        self.structure_test_keys = (
            ("FsF_F1_01D", "FsF_F1_01D-1"),
            ("FsF_F1_02D", "FsF_F1_02D-1"),
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3"),
            ("FsF_F3_01M", "FsF_F3_01M-1"),
            ("FsF_A1_01M", "FsF_A1_01M-1"),
            ("FsF_I1_01M", "FsF_I1_01M-1"),
            ("FsF_I2_01M", "FsF_I2_01M-1"),
            ("FsF_I3_01M", "FsF_I3_01M-1"),
            ("FsF_R1_1_01M", "FsF_R1_1_01M-1"),
            ("FsF_R1_1_01M", "FsF_R1_1_01M-2"),
            ("FsF_R1_01MD", "FsF_R1_01MD-1"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1"),
            ("FsF_R1_3_02D", "FsF_R1_3_02D-1"),
        )

        # BERT score keys
        self.bert_score_keys = (
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "summary"),
            ("FsF_A1_01M", "FsF_A1_01M-1", "comment"),
            ("FsF_I1_01M", "FsF_I1_01M-1", "comment"),
            ("FsF_R1_1_01M", "FsF_R1_1_01M-2", "comment"),
            ("FsF_R1_3_02D", "FsF_R1_3_02D-1", "comment"),
            ("FsF_R1_3_02D", "FsF_R1_3_02D-1", "info"),
        )

        # keys on which to perform string similarity using sentence tokenizer for as close to exact match
        self.exact_string_similarity_keys = (
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "creator"),
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "title"),
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "keywords"),
            ("FsF_R1_1_01M", "FsF_R1_1_01M-1", "license"),
        )

        # Exact match keys
        self.exact_match_keys = (
            ("FsF_F1_01D", "FsF_F1_01D-1", "success"),
            ("FsF_F1_01D", "FsF_F1_01D-1", "identifier"),
            ("FsF_F1_02D", "FsF_F1_02D-1", "success"),
            ("FsF_F1_02D", "FsF_F1_02D-1", "identifier"),
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "publisher"),
            ("FsF_F2_01M", "FsF_F2_01M-1-2-3", "publication_date"),
            ("FsF_F3_01M", "FsF_F3_01M-1", "identifier"),
            ("FsF_A1_01M", "FsF_A1_01M-1", "access_condition"),
            ("FsF_I1_01M", "FsF_I1_01M-1", "success"),
            ("FsF_I2_01M", "FsF_I2_01M-1", "success"),
            ("FsF_R1_1_01M", "FsF_R1_1_01M-2", "success"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1", "version"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1", "curation_date"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1", "modification_date"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1", "formal_vocab"),
            ("FsF_R1_3_02D", "FsF_R1_3_02D-1", "success"),
            ("FsF_R1_3_02D", "FsF_R1_3_02D-1", "scientific_fmt"),
        )

        # List match keys
        self.list_match_keys = (
            ("FsF_I2_01M", "FsF_I2_01M-1", "resources"),
            ("FsF_I3_01M", "FsF_I3_01M-1", "entities"),
            ("FsF_R1_01MD", "FsF_R1_01MD-1", "files"),
            ("FsF_R1_01MD", "FsF_R1_01MD-1", "variables"),
            ("FsF_R1_2_01M", "FsF_R1_2_01M-1", "contributors"),
        )

    def is_structurally_matching(self, ref_json, compare_json):
        """
        Check if two JSON objects have the same structure.

        Args:
            ref_json: Reference JSON object (dict, list, or primitive)
            compare_json: JSON object to compare against the reference (dict, list, or primitive)

        Returns:
            float: 1.0 if perfect match, 0.5 if partial match, 0.0 if type mismatch
        """
        # Check if types match at the current level
        if type(ref_json) != type(compare_json):
            return 0.0  # Type mismatch

        # Handle dictionaries
        if isinstance(ref_json, dict):
            return self._check_dict_structure(ref_json, compare_json)

        # Handle lists
        elif isinstance(ref_json, list):
            return self._check_list_structure(ref_json, compare_json)

        # For primitive values, they match structurally regardless of actual values
        return 1.0

    def _check_dict_structure(self, ref_dict, compare_dict):
        """Helper method to check structure of dictionary objects."""
        # Get reference keys and compare keys
        ref_keys = set(ref_dict.keys())
        compare_keys = set(compare_dict.keys())

        # If no keys match at all
        if len(ref_keys.intersection(compare_keys)) == 0:
            return 0.0

        # If all reference keys are present in compare_dict
        if ref_keys.issubset(compare_keys):
            # Check each reference key-value pair recursively
            scores = []
            for key in ref_keys:
                # Only apply recursive check for complex types (dict or list)
                if isinstance(ref_dict[key], (dict, list)):
                    scores.append(
                        self.is_structurally_matching(ref_dict[key], compare_dict[key])
                    )
                else:
                    # For primitive types, they match structurally regardless of actual values
                    scores.append(1.0)

            # If any substructure completely mismatches, return 0.0
            if 0.0 in scores:
                return 0.0
            # If any substructure partially matches, return 0.5
            elif 0.5 in scores:
                return 0.5
            # If all substructures match perfectly, return 1.0
            else:
                return 1.0

        # If some reference keys are missing, it's a partial match
        return 0.5

    def _check_list_structure(self, ref_list, compare_list):
        """Helper method to check structure of list objects."""
        # If both lists are empty, they match perfectly
        if len(ref_list) == 0 and len(compare_list) == 0:
            return 1.0

        # For non-empty lists, only perform recursive checks if the elements are complex objects
        if len(ref_list) > 0 and len(compare_list) > 0:
            # Check if first items in both lists are complex objects
            if isinstance(ref_list[0], (dict, list)) and isinstance(
                compare_list[0], (dict, list)
            ):
                # Recursively check structure of the first items
                # This assumes that all items in a list have the same structure
                return self.is_structurally_matching(ref_list[0], compare_list[0])
            else:
                # If elements are primitive types, they match structurally
                return 1.0

        return 1.0  # Default case for lists

    def _short_str_similarity(self, word1, word2):
        """
        Compute semantic similarity between two words/phrases using MiniLM embeddings.
        Returns cosine similarity (0 to 1).
        """
        embeddings = self.sim_model.encode([word1, word2], convert_to_tensor=True)
        similarity = util.cos_sim(embeddings[0], embeddings[1])
        return similarity.item()

    def dictionaries_match(self, dict1, dict2):
        """
        Compare two dictionaries with case-insensitive comparison for string keys
        and BERT score matching for string values.

        Args:
            dict1: First dictionary to compare
            dict2: Second dictionary to compare

        Returns:
            bool: True if dictionaries match according to the criteria, False otherwise
        """
        # Check if dictionaries have the same keys (case-insensitive for string keys)
        dict1_keys = set(k.lower() if isinstance(k, str) else k for k in dict1.keys())
        dict2_keys = set(k.lower() if isinstance(k, str) else k for k in dict2.keys())

        if dict1_keys != dict2_keys:
            return False

        # Create normalized dictionaries (only normalizing keys)
        normalized_dict1 = self._normalize_dict_keys(dict1)
        normalized_dict2 = self._normalize_dict_keys(dict2)

        # Check if all values match according to type-specific rules
        for key in normalized_dict1:
            # Handle corresponding keys between dictionaries
            dict1_value = normalized_dict1[key]
            dict2_value = normalized_dict2[key]

            # Apply different comparison methods based on value type
            if isinstance(dict1_value, str) and isinstance(dict2_value, str):
                # For string values, use BERT score matching instead of direct string matching
                len1 = len(dict1_value)
                len2 = len(dict2_value)
                sim_score = self._short_str_similarity(dict1_value, dict2_value)

                # Depending on the size of the two strings, set the threshold

                if (len1 <= 6) or (len2 <= 6):
                    if sim_score < 0.75:
                        return False
                elif (len1 >= 40) or (len2 >= 40):
                    if sim_score < 0.7:
                        return False
                else:
                    if sim_score < 0.4:
                        return False
            else:
                # For non-string values, use direct equality comparison
                if dict1_value != dict2_value:
                    return False
        return True

    def _normalize_dict_keys(self, input_dict):
        """Helper function to normalize dictionary keys to lowercase if they are strings."""
        normalized_dict = {}
        for key, value in input_dict.items():
            normalized_key = key.lower() if isinstance(key, str) else key
            normalized_dict[normalized_key] = value
        return normalized_dict

    def string_similarity(
        self,
        str1: str,
        str2: str,
        big_str_threshold: float = 0.96,
        small_str_threshold: float = 0.75,
    ):
        len1 = len(str1)
        len2 = len(str2)
        sim_score = self._short_str_similarity(str1, str2)
        # Depending on the size of the two strings, set the threshold
        if (len1 >= 20) or (len2 >= 20):
            if sim_score < big_str_threshold:
                return False
        else:
            if sim_score < small_str_threshold:
                return False
        return True

    def list_match(self, ref_list, output_list):
        """
        Compare reference list against an output list.

        Args:
            ref_list: Reference list to compare against
            output_list: Output list to evaluate

        Returns:
            float: Match score (0.0, 0.5, or 1.0)
        """
        if not isinstance(output_list, list):
            # Not a list
            return 0.0

        if len(ref_list) < 1 and len(output_list) > 0:
            # Reference length zero but output has entries
            return 0.0

        if len(ref_list) == 0 and len(output_list) == 0:
            return 1.0

        not_found = []
        for item in ref_list:
            for obj in output_list:
                # Compare item against all output objects
                if type(item) == type(obj):
                    # String item match
                    if isinstance(item, str):
                        if self.string_similarity(item.lower(), obj.lower()):
                            break
                    # Dict Item match
                    if isinstance(item, dict):
                        if self.dictionaries_match(item, obj):
                            # Match found
                            break
            else:
                # Object not found
                not_found.append(item)

        if len(ref_list) < len(output_list):
            if len(ref_list) > len(not_found):
                # Atleast one found, else both lists would be same length
                return 0.5
            else:
                return 0.0

        # Both of same length or more for reference list
        if len(not_found) > 0:
            return 0.5

        # return 1.0 from here indicates everything matching correctly
        return 1.0

    def exact_match(self, ref_obj, output_obj):
        """
        Check if two objects match exactly.

        Args:
            ref_obj: Reference object
            output_obj: Output object to compare against

        Returns:
            float: 1.0 if match, 0.0 if not match
        """
        # Check if both have the same type
        if type(ref_obj) == type(output_obj):
            if isinstance(ref_obj, str):
                # Case-insensitive string comparison
                if ref_obj.lower() == output_obj.lower():
                    return 1.0
            # For non-string types, direct equality comparison
            elif ref_obj == output_obj:
                return 1.0
        return 0.0

    def bert_score_match(self, reference, outputs):
        """
        Calculate BERT score for text matching.

        Args:
            reference: Reference text tuple
            outputs: Output text tuple

        Returns:
            float: F1 score from BERT score
        """
        P, R, F1 = bert_score.score(outputs, reference, lang="en")
        f1 = round(float(F1.numpy()[0]), 3)
        return f1

    def _get_test_value(self, data, key_tuple):
        """
        Extract value from nested dict based on key tuple.

        Args:
            data: Dictionary containing test results
            key_tuple: Tuple containing path to desired value

        Returns:
            The extracted value at the specified path
        """
        # Special case handling for FsF_R1_2_01M keys
        if (key_tuple[0] == "FsF_R1_2_01M") and (
            key_tuple[2]
            in ("version", "curation_date", "modification_date", "contributors")
        ):
            return data[key_tuple[0]]["test_results"][key_tuple[1]]["entities"][
                key_tuple[2]
            ]
        # Default case
        return data[key_tuple[0]]["test_results"][key_tuple[1]][key_tuple[2]]

    def compile_results(self, test_items: List[Tuple[str, str]]) -> Dict[str, Any]:
        """
        Compare test results against reference outputs for a specific model.

        Args:
            test_items: List of test items (url, test_id)

        Returns:
            Dict containing comparison results
        """
        results = {}
        scores_types = (
            "bert-score",
            "exact_match",
            "sequence_match",
            "structural_match",
        )

        for url, domain in test_items:
            # Process each model sequentially
            for model in self.test_config.model_list:
                for temp in self.test_config.temperatures:
                    # Prepare filenames
                    filename = url.split("/")[-1]
                    complete_filename = f"{domain}_{filename}.json"
                    reference_results = self.ref_mgr.get_reference(complete_filename)

                    # Generate output result filenames
                    output_result_files = [
                        f"{complete_filename.split('.json')[0]}_{i + 1}.json"
                        for i in range(self.test_config.test_repeat_n)
                    ]

                    # Initialize scores structure
                    scores = self._initialize_scores_structure(output_result_files)

                    # Evaluate each output file
                    for file in output_result_files:
                        self._evaluate_single_file(
                            model["model_name"],
                            temp,
                            file,
                            reference_results,
                            scores,
                        )

                    # Store results
                    # Compute the average scores across the two files (avg value)
                    # for the given example for the given model, temp parameter
                    combined = {sc: {} for sc in scores_types}
                    for score_type in scores.keys():
                        file1, file2 = tuple(scores[score_type].keys())
                        for k, v in scores[score_type][file1].items():
                            mean_val = round(
                                np.mean((v, scores[score_type][file2][k])), 3
                            )
                            combined[score_type][k] = mean_val

                    if not results.get((model["model_name"], temp)):
                        # Set the result template for this model and temp combination
                        results[(model["model_name"], temp)] = {}

                    # Store the final values for this example for this given (model, temp) combination
                    results[(model["model_name"], temp)][f"{domain}_{url}"] = combined
        # Combine the test results for a given (model, temp) combination across all examples
        final_res = {k: {sc: {} for sc in scores_types} for k in results.keys()}
        for k in final_res:
            # This loop below remove file information and simply collect for a given model, temp combination the list of test scores for each score types. i.e. if score type is bert-score then collect all bert-score values across all files for a given test item like 'FsF_A1_01M;FsF_A1_01M-1;comment'
            for score in final_res[k].keys():
                for file in results[k]:
                    for test_item in results[k][file][score].keys():
                        if test_item not in final_res[k][score]:
                            final_res[k][score][test_item] = [
                                results[k][file][score][test_item],
                            ]
                        else:
                            final_res[k][score][test_item].append(
                                results[k][file][score][test_item]
                            )

            # Compute the final scores
            # First compute avg val for each test_item across each score type
            for score in final_res[k].keys():
                for t, v in final_res[k][score].items():
                    final_res[k][score][t] = round(np.mean(v), 3)

            for score in final_res[k].keys():
                it_ = tuple(final_res[k][score].values())
                final_res[k][score] = round(np.mean(it_), 3)

            final_res[k]["combined"] = round(
                (final_res[k]["exact_match"] + final_res[k]["sequence_match"]) / 2, 3
            )
        return final_res

    def _initialize_scores_structure(self, output_files):
        """Initialize the scores data structure for all files."""
        scores = {
            "structural_match": {},
            "exact_match": {},
            "sequence_match": {},
            "bert-score": {},
        }

        for file in output_files:
            for metric in scores:
                scores[metric][file] = {}

        return scores

    def _evaluate_single_file(
        self, model_name, temperature, file, reference_results, scores
    ):
        """Evaluate a single output file against reference results."""
        # Load and preprocess output data
        output = self.file_manager.load_test_result(model_name, temperature, file)[
            "fair_assessment"
        ]["metrics"]

        # Create a copy and clean output for evaluation
        output_clean = self._clean_output_for_comparison(output)

        # Perform structural matching
        self._evaluate_structural_match(output_clean, reference_results, file, scores)

        # Perform exact matching
        self._evaluate_exact_match(output_clean, reference_results, file, scores)

        # Perform list matching
        self._evaluate_list_match(output_clean, reference_results, file, scores)

        # Perform BERT score matching
        self._evaluate_bert_score(output_clean, reference_results, file, scores)

    def _clean_output_for_comparison(self, output):
        """Remove unnecessary keys from output for comparison."""
        output_clean = output.copy()
        for k in output_clean.keys():
            del output_clean[k]["metric_id"]
            del output_clean[k]["metric_name"]
            del output_clean[k]["principle"]
            del output_clean[k]["score"]
            del output_clean[k]["out_of"]
        return output_clean

    def _evaluate_structural_match(self, output, reference, file, scores):
        """Evaluate structural matching for all structure test keys."""
        for k in self.structure_test_keys:
            struct_match_score = self.is_structurally_matching(
                reference[k[0]]["test_results"][k[1]],
                output[k[0]]["test_results"][k[1]],
            )
            scores["structural_match"][file][";".join(k)] = struct_match_score

    def _evaluate_exact_match(self, output, reference, file, scores):
        """Evaluate exact matching for all exact match keys."""
        for k in self.exact_match_keys:
            try:
                ref_val = self._get_test_value(reference, k)
                output_val = self._get_test_value(output, k)
                exact_match_score = self.exact_match(ref_val, output_val)
                scores["exact_match"][file][";".join(k)] = exact_match_score
            except KeyError:
                # Handle missing keys gracefully
                scores["exact_match"][file][";".join(k)] = 0.0

        for k in self.exact_string_similarity_keys:
            try:
                ref_val = self._get_test_value(reference, k)
                output_val = self._get_test_value(output, k)
                if k[1] == "FsF_R1_1_01M-1" and k[2] == "license":
                    match_score = self.string_similarity(
                        ref_val, output_val, big_str_threshold=0.42
                    )
                else:
                    match_score = self.string_similarity(ref_val, output_val)
                if match_score:
                    scores["exact_match"][file][";".join(k)] = 1.0
                else:
                    scores["exact_match"][file][";".join(k)] = 0.0
            except KeyError:
                # Handle missing keys gracefully (Specially for llama3.3)
                scores["exact_match"][file][";".join(k)] = 0.0

    def _evaluate_list_match(self, output, reference, file, scores):
        """Evaluate list matching for all list match keys."""
        for k in self.list_match_keys:
            try:
                ref_val = self._get_test_value(reference, k)
                output_val = self._get_test_value(output, k)
                list_score = self.list_match(ref_val, output_val)
                scores["sequence_match"][file][";".join(k)] = list_score
            except KeyError:
                # Handle missing keys gracefully
                scores["sequence_match"][file][";".join(k)] = 0.0

    def _evaluate_bert_score(self, output, reference, file, scores):
        """Evaluate BERT score matching for all BERT score keys."""
        bert_scores = []
        for k in self.bert_score_keys:
            try:
                ref_text = self._get_test_value(reference, k)
                output_text = self._get_test_value(output, k)
                bert_score_value = self.bert_score_match((ref_text,), (output_text,))
                scores["bert-score"][file][";".join(k)] = bert_score_value
                bert_scores.append(bert_score_value)
            except KeyError:
                # Handle missing keys gracefully
                scores["bert-score"][file][";".join(k)] = 0.0
