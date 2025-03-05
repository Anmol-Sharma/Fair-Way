# Define individual metrics and utilize them with many tests associated with them here and then test for each metric in its principles module
from abc import abstractmethod
import logging
from celery import current_task
from typing import Dict, Any, List
from inspect import cleandoc
import json
from pydantic import create_model


class BaseMetric:
    def __init__(
        self,
        metric_id: str,
        name: str,
        active: bool,
        tests: Dict[str, Any],
        principle: str,
    ):
        self.tests = tests
        self.metric_id = metric_id
        self.active = active
        self.name = name
        self.logger = logging.getLogger("celery")

        self.results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": principle,
        }

    @abstractmethod
    def execute_tests(self, model, file_chunks: List[str], file_type: str):
        """
        Define this down in derived classes for order and interdependence of tests
        Also define the test score logic inside and return an object with test results and scores
        """
        pass

    @abstractmethod
    def score_test_results(self, t_results):
        """
        Define this down in derived classes for order and interdependence of combining test scores
        """
        pass

    def combine_multi_metric_results(self, model, results):
        messages = []
        Base_MSG = """Your Task is to combine the results from separate fair assessment tests. All will have the same json structure however they are on different metadata sources (eg. embedded or retrieved through metadata harvest). Your task is to combine them together. Check carefully if a test succeeds in one of them, then the final result should reflect that. Only fail the test which doesn't succeed in both. Only answer back in the common json data format of both the test results with no comments or explanation since you are interacting with an api and not a human and the json results need to be parsed. Combine the test items given below.\n"""
        self.logger.info(
            f"Combining the Result Results for the metric :- {self.metric_id}"
        )

        for idx, result in enumerate(results):
            msg = f"""Result {idx + 1}\n```{json.dumps(result, separators=(',', ':'))}```"""
            Base_MSG = "\n".join([Base_MSG, msg])
        messages.append(
            {
                "role": "user",
                "content": cleandoc(Base_MSG),
            }
        )

        # create a Dynamic Model with Test Results to be supplied to LLM to output results
        DynamicModel = create_model(
            "DynamicModel", **{k: (type(v), v) for k, v in results[0].items()}
        )
        response = model.send_request(messages=messages, ResponseFormat=DynamicModel)
        return json.loads(response["message"]["content"])

    def analyze_metric(self, model, metadata):
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        # Perform the relevant test on each of the metadata items and combine them together
        # Scoring will take of that
        All_Results = []
        for k in metadata.keys():
            res = self.execute_tests(
                model, metadata[k]["metadata_chunks"], metadata[k]["source"]
            )
            All_Results.append(res)

        combined_results = self.combine_multi_metric_results(model, All_Results)
        return self.score_test_results(combined_results)
