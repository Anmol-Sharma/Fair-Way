# Define individual metrics and utilize them with many tests associated with them here and then test for each metric in its principles module
from abc import abstractmethod
import logging
from celery import current_task
from typing import Dict, Any, List
from inspect import cleandoc
import json
from pydantic import create_model
import random


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
        Base_MSG = """Your Task is to combine the results from separate data extraction tests. All will have the same json structure however they are on different metadata sources. Your task is to combine them together. Key Steps to follow are :-
        1. Check carefully if and extracted key is present in one of them, then the final result should reflect that by including all the necessary keys from the succeeded test.
        2. Only fail the test which doesn't succeed in both.
        3. If there are partial results in both, select the one with more details. The returned feedback should look like an actual or real test result to the user and not just a direct combination of two test.
        4. Select the source for each extracted key and its source of results (eg. Embedded or Harvested) by adding a `source` key to the final results for each key.
        5. Also, ONLY answer back in the common json data format of both the test results with no comments or explanation since you are interacting with an api and not a human and the json results need to be parsed. Combine the test items given below.\n"""
        self.logger.info(
            f"Combining the Result Results for the metric :- {self.metric_id}"
        )

        for k, result in results.items():
            msg = f"""Result source: '{k}'\n```{json.dumps(result, separators=(',', ':'))}```"""
            Base_MSG = "\n".join([Base_MSG, msg])
        messages.append(
            {
                "role": "user",
                "content": cleandoc(Base_MSG),
            }
        )

        # TODO: I Might have to use 2-shot example for reference.
        # Select a random key (both have the same structure)
        random_key = random.choice(list(results.keys()))

        # create a Dynamic Model with Test Results to be supplied to LLM to output results
        DynamicModel = create_model(
            "DynamicModel", **{k: (type(v), v) for k, v in results[random_key].items()}
        )
        response = model.send_request(messages=messages, ResponseFormat=DynamicModel)
        return json.loads(response["message"]["content"])

    def analyze_metric(self, model, metadata):
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        # Perform the relevant test on each of the metadata items and combine them together
        # Scoring will take of that
        All_Results = {}
        for k in metadata.keys():
            res = self.execute_tests(
                model, metadata[k]["metadata_chunks"], metadata[k]["source"]
            )
            name = ""
            if k == "api":
                name = "Harvested Metadata"
            elif k == "embedded":
                name = "Embedded Metadata"
            else:
                name = "Uploaded Metadata File"
            All_Results[name] = res

        combined_results = self.combine_multi_metric_results(model, All_Results)
        return self.score_test_results(combined_results)
