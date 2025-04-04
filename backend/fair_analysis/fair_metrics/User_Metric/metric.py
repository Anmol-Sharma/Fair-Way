from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.User_Metric.fair_tests.t1 import (
    Test as Vocab_Test,
    V_ResponseFormat,
)
from fair_analysis.fair_metrics.User_Metric.fair_tests.t2 import Test as Standard_Test
from typing import Dict, List


class CustomMetric(BaseMetric):
    def execute_tests(self, model, file_chunks, file_type):
        all_results = {}
        for tid, t in self.tests.items():
            succ, t_result = t.perform_test(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            if not succ:
                self.logger.warning(
                    f"LLM failed to process request correctly for {self.metric_id}"
                )
                t_result = {
                    "success": False,
                    "comment": "LLM failed to process request correctly",
                }
            all_results[tid] = t_result
        return all_results

    def analyze_metric(self, model, metadata):
        resp_format = V_ResponseFormat
        Source_Results = {}
        for k in metadata.keys():
            res = self.execute_tests(
                model,
                (metadata[k]["metadata_chunks"],),
                metadata[k]["source"],
            )
            name = ""
            if k == "api":
                name = "Harvested Metadata"
            elif k == "embedded":
                name = "Embedded Metadata"
            else:
                name = "Uploaded Metadata File"
            Source_Results[name] = res

        all_vocab_results = {}
        if len(metadata.keys()) <= 1:
            return self.score_test_results((Source_Results.values())[0])
        else:
            # Get all unique keys in the second level of dictionaries for each unique test
            second_level_keys = set()
            for outer_key in Source_Results:
                second_level_keys.update(Source_Results[outer_key].keys())

            # Create split results for each test (vocab test) so that combining
            # of the test results on different metadata can function
            split_results = {}
            for key in second_level_keys:
                current_split = {}
                for outer_key in Source_Results:
                    if key in Source_Results[outer_key]:
                        current_split[outer_key] = Source_Results[outer_key][key]
                split_results[key] = current_split
            for k, sp_res in split_results.items():
                combined_result = self.combine_multi_metric_results(
                    model, sp_res, resp_format
                )
                all_vocab_results[k] = combined_result
            return self.score_test_results(all_vocab_results)


class V_Metric(CustomMetric):
    def __init__(self, tests: List[Dict]):
        metric_id = "FuM-Vocab"
        name = "Metadata satisfies user defined domain Vocabulary Constraints."
        active = True
        custom_tests = dict()

        # Explicitly define custom objects for tests but with common functional properties
        for idx, t in enumerate(tests):
            # Parse the test condition
            v_name, desc = t["condition"].split(",")
            if t["type"] == "Vocabulary Check":
                custom_tests[f"t_{str(idx + 1)}"] = Vocab_Test(
                    {
                        "domain": t["domain"],
                        "name": v_name.strip(),
                        "desc": desc.strip(),
                    }
                )

        super().__init__(
            metric_id,
            name,
            active,
            custom_tests,
            principle="user-defined-domain-checks",
        )

    def score_test_results(self, t_results):
        increment = 0.5
        score = 0.0
        out_of = 0.0
        for k, t in t_results.items():
            if t["success"]:
                score += increment
                out_of += increment
            self.results["test_results"][f"FuM-Vocab-{k}"] = t

        self.results["score"] = score
        self.results["out_of"] = out_of

        return self.results


class S_Metric(CustomMetric):
    def __init__(self, tests: List[Dict]):
        metric_id = "FuM-Standard"
        name = "Metadata satisfies user defined domain specific standards."
        active = True
        custom_tests = dict()

        for idx, t in enumerate(tests):
            # Parse the test condition
            if t["type"] == "Standard Check":
                custom_tests[f"t_{str(idx + 1)}"] = Standard_Test(
                    {"domain": t["domain"], "condition": t["condition"].strip()}
                )

        super().__init__(
            metric_id,
            name,
            active,
            custom_tests,
            principle="user-defined-domain-checks",
        )

    def score_test_results(self, t_results):
        increment = 1.0
        score = 0.0
        out_of = 0.0
        for k, t in t_results.items():
            if t["success"]:
                score += increment
                out_of += increment
            self.results["test_results"][f"FuM-Standard-{k}"] = t

        self.results["score"] = score
        self.results["out_of"] = out_of

        return self.results
