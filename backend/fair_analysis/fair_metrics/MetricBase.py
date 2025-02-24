# Define individual metrics and utilize them with many tests associated with them here and then test for each metric in its principles module
from abc import abstractmethod
import logging
from celery import current_task
from typing import Dict, Any, List


class BaseMetric:
    def __init__(self, metric_id: str, name: str, active: bool, tests: Dict[str, Any]):
        self.tests = tests
        self.metric_id = metric_id
        self.active = active
        self.name = name
        self.logger = logging.getLogger("celery")

    @abstractmethod
    def execute_tests(self, model, file_chunks: List[str], file_type: str):
        """
        Define this down in base classes for order and interdependence of tests
        Also define the test score logic inside and return an object with test results and scores
        """
        pass

    def analyze_metric(self, model, file_chunks: List[str], file_type: str):
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        return self.execute_tests(model, file_chunks, file_type)
