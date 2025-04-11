import os
from typing import Dict, Any, Tuple
import logging
from Evaluation.eval_config import TestConfig
import json

logger = logging.getLogger(__name__)


class FileManager:
    """Manages file operations and directories."""

    def __init__(self, base_path: str = "/var/tmp/Evaluate"):
        self.base_path = base_path
        self.metadata_path = os.path.join(base_path, "Retrieved Metadata")
        self.results_path = os.path.join(base_path, "Results")
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        for path in [
            self.base_path,
            self.metadata_path,
            self.results_path,
        ]:
            os.makedirs(path, exist_ok=True)

    def get_metadata_paths(self, url: str, test_id: str) -> Tuple[str, str]:
        """Generate paths for metadata files storage."""
        filename = url.split("/")[-1]
        embedded_path = os.path.join(
            self.metadata_path, f"{test_id}_{filename}_embedded.json"
        )
        api_path = os.path.join(self.metadata_path, f"{test_id}_{filename}_api.json")
        return embedded_path, api_path

    def get_results_path(
        self,
        model_name: str,
        temperature: float,
        url: str,
        test_id: str,
        iteration: int,
    ) -> str:
        """Generate path for result file."""
        model_dir = f"{model_name.split(':')[0]}__{str(temperature).replace('.', '_')}"
        base_dir = os.path.join(self.results_path, model_dir)
        os.makedirs(base_dir, exist_ok=True)
        filename = url.split("/")[-1]
        return os.path.join(base_dir, f"{test_id}_{filename}_{iteration}.json")

    def check_results_exist(
        self, model_name: str, temperature: float, url: str, test_id: str
    ) -> bool:
        """Check if all result files for a test already exist."""
        model_dir = f"{model_name.split(':')[0]}__{str(temperature).replace('.', '_')}"
        base_dir = os.path.join(self.results_path, model_dir)
        if not os.path.exists(base_dir):
            return False
        filename = url.split("/")[-1]
        # Check if all iterations exist
        for i in range(1, TestConfig().test_repeat_n + 1):
            result_path = os.path.join(base_dir, f"{test_id}_{filename}_{i}.json")
            if not os.path.exists(result_path):
                logger.warning(
                    f"File:- {result_path} does not exist for {model_name} and temperature : {temperature}"
                )
                return False
        return True

    def save_metadata(
        self, embedded_path: str, api_path: str, metadata: Dict[str, Any]
    ) -> None:
        """Save metadata to files."""
        with open(embedded_path, "w") as f:
            json.dump(metadata["embedded"], f)

        with open(api_path, "w") as f:
            json.dump(metadata["api"], f)

    def load_metadata(self, embedded_path: str, api_path: str) -> Dict[str, Any]:
        """Load metadata from files."""
        metadata = {"embedded": {"source": "json"}, "api": {"source": "json"}}

        with open(embedded_path, "r") as f:
            metadata["embedded"]["metadata"] = f.read()

        with open(api_path, "r") as f:
            metadata["api"]["metadata"] = f.read()

        return metadata

    def save_results(self, path: str, results: Dict[str, Any]) -> None:
        """Save test results to file."""
        with open(path, "w") as f:
            json.dump(results, f)

    def load_test_result(
        self, model_name: str, temperature: float, filename: str
    ) -> Dict[str, Any]:
        model_dir = f"{model_name.split(':')[0]}__{str(temperature).replace('.', '_')}"
        with open(os.path.join(self.results_path, model_dir, filename), "r") as f:
            return json.load(f)


class ReferenceManager:
    """."""

    def __init__(self, base_path: str = "./Evaluation/reference_outputs"):
        self.base_path = base_path

    def get_reference(self, file_name: str) -> Dict:
        """Generate path for result file."""
        file_path = os.path.join(self.base_path, file_name)

        if not os.path.exists(file_path):
            raise Exception(
                f"Reference file:- {file_name} does not exist in reference directory"
            )
        with open(file_path, "r") as f:
            ref = json.load(f)
            return ref
