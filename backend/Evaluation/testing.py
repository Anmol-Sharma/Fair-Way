import copy
import asyncio
from typing import List, Dict, Any, Tuple
import os

# import json

from Evaluation.eval_utils import fetch_results
from utils.network_utils import HttpClient, fetch_metadata_using_url

from Evaluation.eval_config import ApiConfig, TestConfig
from Evaluation.file_handler import FileManager

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
        self.client = HttpClient.get_client()

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
            response = await self.client.post(self.api_config.request_url, json=meta)
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
                client=self.client,
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

    async def execute_model_tests(
        self, model: Dict[str, str], test_items: List[Tuple[str, str]]
    ) -> None:
        """Run tests for a specific model across all test items and temperatures."""
        tests_executed = False  # Add a flag to track if any tests were executed

        for temperature in self.test_config.temperatures:
            logger.info(
                f"Testing for model: {model['model_name']} with temperature: {temperature}"
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
                            metadata, model, temperature, url, test_id, i + 1
                        )

                    tests_executed = True  # Set the flag to true as a test was executed

                except Exception as e:
                    logger.error(
                        f"Error processing test item {url}: {e}", exc_info=True
                    )

        # Only perform sleep logic if tests were actually executed
        if tests_executed:
            if model["service"].lower() == "ollama":
                # Wait for model to be evicted before testing the next model
                keep_alive_minutes = int(env_settings.keep_alive.strip("m"))
                logger.info(
                    f"Sleeping for {keep_alive_minutes} minutes until {model['model_name']} is evicted"
                )
                await asyncio.sleep(keep_alive_minutes * 60)
            elif model["service"].lower() == "openai":
                # Sleep for 2 minutes
                logger.info(
                    f"Sleeping for 2 minutes after testing {model['model_name']}"
                )
                await asyncio.sleep(2 * 60)

    async def execute_all_tests(self, test_items: List[Tuple[str, str]]) -> None:
        """Execute tests for all models."""
        for model in self.test_config.model_list:
            await self.execute_model_tests(model, test_items)


# class ResultEvaluator:
#     """Handles the evaluation of test results against reference outputs."""

#     def __init__(
#         self,
#         test_config: TestConfig = TestConfig(),
#         file_manager: FileManager = FileManager(),
#     ):
#         self.test_config = test_config
#         self.file_manager = file_manager

#     def is_structurally_matching(self, json1, json2):
#         """
#         Check if two JSON objects have the same structure (same keys and value types),
#         regardless of the actual values.

#         Args:
#             json1: First JSON object (dict, list, or primitive)
#             json2: Second JSON object (dict, list, or primitive)

#         Returns:
#             bool: True if structures match, False otherwise
#         """
#         # Check if both are dictionaries
#         if isinstance(json1, dict) and isinstance(json2, dict):
#             # Check if they have the same keys
#             if set(json1.keys()) != set(json2.keys()):
#                 return False

#             # Check each key-value pair recursively
#             for key in json1:
#                 if not self.is_structurally_matching(json1[key], json2[key]):
#                     return False
#             return True

#         # Check if both are lists
#         elif isinstance(json1, list) and isinstance(json2, list):
#             # Check if they have the same length
#             if len(json1) != len(json2):
#                 return False

#             # If lists are empty, they match
#             if len(json1) == 0:
#                 return True

#             # For non-empty lists, we need to check if all items follow the same structure
#             # This is tricky because list items can be in different order
#             # For simplicity, we'll check if the first item's structure appears in all items

#             # Get structure of first item in json1
#             sample_item = json1[0]

#             # Check if all items in both lists match the structure of the sample item
#             for item1 in json1:
#                 if not self.is_structurally_matching(item1, sample_item):
#                     return False

#             for item2 in json2:
#                 if not self.is_structurally_matching(item2, sample_item):
#                     return False

#             return True

#         # Check if they are the same primitive type
#         else:
#             return type(json1) == type(json2)

#     def is_exact_json_match(self, json1, json2):
#         """
#         Check if two JSON objects match exactly (same keys, types, and values).

#         Args:
#             json1: First JSON object (dict, list, or primitive)
#             json2: Second JSON object (dict, list, or primitive)

#         Returns:
#             bool: True if they match exactly, False otherwise
#         """
#         # Check if both are dictionaries
#         if isinstance(json1, dict) and isinstance(json2, dict):
#             # Check if they have the same keys
#             if set(json1.keys()) != set(json2.keys()):
#                 return False

#             # Check each key-value pair recursively
#             for key in json1:
#                 if not self.is_exact_json_match(json1[key], json2[key]):
#                     return False
#             return True

#         # Check if both are lists
#         elif isinstance(json1, list) and isinstance(json2, list):
#             # Check if they have the same length
#             if len(json1) != len(json2):
#                 return False

#             # For exact matching, order matters in JSON, so compare each position
#             for i in range(len(json1)):
#                 if not self.is_exact_json_match(json1[i], json2[i]):
#                     return False
#             return True

#         # For primitives, use direct equality comparison
#         else:
#             return json1 == json2

#     async def compare_results(
#         self, model: Dict[str, str], test_items: List[Tuple[str, str]]
#     ) -> Dict[str, Any]:
#         """
#         Compare test results against reference outputs for a specific model.
#         Args:
#             model: The model information
#             test_items: List of test items (url, test_id)

#         Returns:
#             Dict containing comparison results
#         """
#         comparison_results = {
#             "model": model["model_name"],
#             "service": model["service"],
#             "tests": [],
#         }

#         for temperature in self.test_config.temperatures:
#             for url, test_id in test_items:
#                 test_result = {
#                     "url": url,
#                     "test_id": test_id,
#                     "temperature": temperature,
#                     "iterations": [],
#                 }

#                 # Get reference output path for this test
#                 reference_path = self.file_manager.get_reference_path(url, test_id)

#                 if not os.path.exists(reference_path):
#                     logger.warning(f"Reference output not found at {reference_path}")
#                     test_result["error"] = "Reference output not found"
#                     comparison_results["tests"].append(test_result)
#                     continue

#                 # Load reference output
#                 try:
#                     with open(reference_path, "r") as f:
#                         reference_output = json.load(f)
#                 except Exception as e:
#                     logger.error(f"Error loading reference output: {e}", exc_info=True)
#                     test_result["error"] = f"Failed to load reference output: {str(e)}"
#                     comparison_results["tests"].append(test_result)
#                     continue

#                 # Check each iteration
#                 for i in range(1, self.test_config.test_repeat_n + 1):
#                     result_path = self.file_manager.get_results_path(
#                         model["model_name"], temperature, url, test_id, i
#                     )

#                     if not os.path.exists(result_path):
#                         logger.warning(f"Result file not found: {result_path}")
#                         test_result["iterations"].append(
#                             {"iteration": i, "error": "Result file not found"}
#                         )
#                         continue

#                     # Load test result
#                     try:
#                         with open(result_path, "r") as f:
#                             test_output = json.load(f)
#                     except Exception as e:
#                         logger.error(f"Error loading test result: {e}", exc_info=True)
#                         test_result["iterations"].append(
#                             {
#                                 "iteration": i,
#                                 "error": f"Failed to load test result: {str(e)}",
#                             }
#                         )
#                         continue

#                     # Compare results
#                     structure_match = self.is_structurally_matching(
#                         test_output, reference_output
#                     )
#                     exact_match = self.is_exact_json_match(
#                         test_output, reference_output
#                     )

#                     iteration_result = {
#                         "iteration": i,
#                         "structural_match": structure_match,
#                         "exact_match": exact_match,
#                         "result_path": result_path,
#                     }

#                     test_result["iterations"].append(iteration_result)

#                 comparison_results["tests"].append(test_result)

#         return comparison_results

#     async def evaluate_all_models(
#         self, test_items: List[Tuple[str, str]]
#     ) -> List[Dict[str, Any]]:
#         """
#         Evaluate test results for all models.

#         Args:
#             test_items: List of test items (url, test_id)

#         Returns:
#             List of comparison results for each model
#         """
#         evaluation_results = []

#         for model in self.test_config.model_list:
#             logger.info(f"Evaluating results for model: {model['model_name']}")
#             model_results = await self.compare_results(model, test_items)
#             evaluation_results.append(model_results)

#             # Save evaluation results
#             results_path = self.file_manager.get_evaluation_path(model["model_name"])
#             try:
#                 with open(results_path, "w") as f:
#                     json.dump(model_results, f, indent=2)
#                 logger.info(f"Evaluation results saved to {results_path}")
#             except Exception as e:
#                 logger.error(f"Error saving evaluation results: {e}", exc_info=True)

#         return evaluation_results

#     def compile_summary(
#         self, evaluation_results: List[Dict[str, Any]]
#     ) -> Dict[str, Any]:
#         """
#         Compile summary statistics from evaluation results.

#         Args:
#             evaluation_results: List of evaluation results for each model

#         Returns:
#             Dict containing summary statistics
#         """
#         summary = {
#             "models": [],
#             "test_items": set(),
#             "total_tests": 0,
#             "total_iterations": 0,
#             "overall_structural_match_rate": 0,
#             "overall_exact_match_rate": 0,
#         }

#         total_structural_matches = 0
#         total_exact_matches = 0
#         total_iterations_count = 0

#         for model_result in evaluation_results:
#             model_summary = {
#                 "model": model_result["model"],
#                 "service": model_result["service"],
#                 "test_count": len(model_result["tests"]),
#                 "structural_match_rate": 0,
#                 "exact_match_rate": 0,
#             }

#             model_structural_matches = 0
#             model_exact_matches = 0
#             model_iterations_count = 0

#             for test in model_result["tests"]:
#                 summary["test_items"].add((test["url"], test["test_id"]))
#                 summary["total_tests"] += 1

#                 for iteration in test.get("iterations", []):
#                     if "error" not in iteration:
#                         model_iterations_count += 1
#                         if iteration.get("structural_match", False):
#                             model_structural_matches += 1
#                         if iteration.get("exact_match", False):
#                             model_exact_matches += 1

#             if model_iterations_count > 0:
#                 model_summary["structural_match_rate"] = (
#                     model_structural_matches / model_iterations_count
#                 )
#                 model_summary["exact_match_rate"] = (
#                     model_exact_matches / model_iterations_count
#                 )

#             model_summary["iterations_count"] = model_iterations_count
#             summary["models"].append(model_summary)

#             total_structural_matches += model_structural_matches
#             total_exact_matches += model_exact_matches
#             total_iterations_count += model_iterations_count

#         summary["test_items"] = list(summary["test_items"])
#         summary["total_iterations"] = total_iterations_count

#         if total_iterations_count > 0:
#             summary["overall_structural_match_rate"] = (
#                 total_structural_matches / total_iterations_count
#             )
#             summary["overall_exact_match_rate"] = (
#                 total_exact_matches / total_iterations_count
#             )

#         return summary

#     async def run_evaluation(self, test_items: List[Tuple[str, str]]) -> Dict[str, Any]:
#         """
#         Run the complete evaluation process: evaluate results and compile summary.

#         Args:
#             test_items: List of test items (url, test_id)

#         Returns:
#             Dict containing summary of evaluation
#         """
#         # Evaluate results for all models
#         evaluation_results = await self.evaluate_all_models(test_items)

#         # Compile summary statistics
#         summary = self.compile_summary(evaluation_results)

#         # Save summary
#         summary_path = self.file_manager.get_summary_path()
#         try:
#             with open(summary_path, "w") as f:
#                 json.dump(summary, f, indent=2)
#             logger.info(f"Evaluation summary saved to {summary_path}")
#         except Exception as e:
#             logger.error(f"Error saving evaluation summary: {e}", exc_info=True)

#         return summary
