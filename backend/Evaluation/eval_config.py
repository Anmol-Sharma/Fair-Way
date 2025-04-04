import logging
from dataclasses import dataclass
from typing import List, Dict
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ApiConfig:
    """Configuration for API endpoints."""

    base_url: str = "http://backend:8000/"

    @property
    def request_url(self) -> str:
        return urljoin(self.base_url, "/api/EvaluateOnlineResource")

    @property
    def status_url(self) -> str:
        return urljoin(self.base_url, "/api/Status/")

    @property
    def results_url(self) -> str:
        return urljoin(self.base_url, "/api/Results/")


@dataclass
class TestConfig:
    """Configuration for test parameters."""

    # How many times to repeat a single test entry for a given model, temp. combination
    test_repeat_n: int = 2

    # List of Models to test on
    model_list: List[Dict[str, str]] = None

    # List of temperatures
    temperatures: List[float] = None

    def __post_init__(self):
        if self.model_list is None:
            self.model_list = [
                {"model_name": "phi4:14b-q8_0", "service": "ollama"},
                {
                    "model_name": "mistral-small:24b-instruct-2501-q8_0",
                    "service": "ollama",
                },
                {"model_name": "qwen2.5-coder:32b-instruct-q8_0", "service": "ollama"},
                {"model_name": "llama3.3:70b-instruct-q5_K_M", "service": "ollama"},
                {"model_name": "gpt-4o-2024-08-06", "service": "openai"},
            ]

        if self.temperatures is None:
            self.temperatures = [0.3, 0.5, 0.7]
