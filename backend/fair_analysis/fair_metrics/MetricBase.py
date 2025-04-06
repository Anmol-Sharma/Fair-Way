# Define individual metrics and utilize them with many tests associated with them here and then test for each metric in its principles module
from abc import abstractmethod
import logging
from celery import current_task
from typing import List, Any, Dict
from inspect import cleandoc
import json


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
        Define this down in derived classes for interdependence of tests.

        NOTE: To perform test on the whole file contents, simply provide a single chunk with complete file contents.

        Should return back the results as well as a response format to be used for combining results
        """
        pass

    @abstractmethod
    def score_test_results(self, t_results):
        """
        Define this down in derived classes to compute test score based on result of different tests.
        """
        # If there are multiple test results the scoring function will handle it.
        pass

    def combine_multi_metric_results(self, model, results, response_format):
        messages = []
        Base_MSG = """Your Task is to combine the results from separate data extraction tests. All will have the same json structure however they are on different metadata sources. Your task is to combine them together. Key Steps to follow are :-
        1. Check carefully if and extracted key is present in one of them, then the final result should reflect that by including all the necessary keys from the succeeded test.
        2. Only fail the test which doesn't succeed in both and set the relevant string keys as empty.
        3. If there are partial results in both, select the one with more details. The returned feedback should look like an actual useful test result (on the task) to the user and not just a direct combination of two results.
        4. Select the source for each extracted key and its source of results (eg. Embedded or Harvested) by adding a `source` key to the final results for each key.
        5. Also, ONLY answer back in the common json data format of both the test results with no comments or explanation since you are interacting with an api and not a human and the json results need to be parsed. Combine the test items given below.\n"""
        self.logger.info(f"Combining the Results for the metric :- {self.metric_id}")
        for k, result in results.items():
            msg = f"""Result source: '{k}'\n```{json.dumps(result, separators=(',', ':'))}```"""
            Base_MSG = "\n".join([Base_MSG, msg])
        messages.append(
            {
                "role": "user",
                "content": cleandoc(Base_MSG),
            }
        )

        try:
            response = model.send_request(
                messages=messages, ResponseFormat=response_format
            )
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            return {
                "success": False,
                "comment": "LLM failed to generate proper json results",
            }
        except Exception:
            return {"success": False, "comment": "Request failed to be processed"}

    def analyze_metric(self, model, metadata):
        """
        Default method to analyze metric on chunks. Override in derived if any custom logic is required.
        """
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        # Perform the relevant test on each of the metadata items and combine them together
        All_Results = {}
        resp_format = None
        for k in metadata.keys():
            res, fmt = self.execute_tests(
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
            if fmt is not None:
                resp_format = fmt

        if len(metadata.keys()) <= 1:
            return self.score_test_results(list(All_Results.values())[0])
        else:
            combined_results = self.combine_multi_metric_results(
                model, All_Results, response_format=resp_format
            )
            return self.score_test_results(combined_results)
