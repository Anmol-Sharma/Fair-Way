import copy
import asyncio
from typing import List, Dict, Any, Tuple
import os

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

    async def execute_model_tests(
        self, model: Dict[str, str], test_items: List[Tuple[str, str]]
    ) -> None:
        """Run tests for a specific model across all test items and temperatures."""
        logger.info(f"Testing for model: {model['model_name']}")
        tests_executed = False  # Add a flag to track if any tests were executed

        for temperature in self.test_config.temperatures:
            logger.info(f"Testing with temperature: {temperature}")

            for url, test_id in test_items:
                try:
                    # Check if results already exist for this combination
                    if self.file_manager.check_results_exist(
                        model["model_name"], temperature, url, test_id
                    ):
                        logger.info(
                            f"Skipping test for model={model['model_name']}, temp={temperature}, "
                            f"url={url}, test_id={test_id} as results already exist"
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
