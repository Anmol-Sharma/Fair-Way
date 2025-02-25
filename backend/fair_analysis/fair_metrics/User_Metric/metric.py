from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.User_Metric.fair_tests.t1 import Test as Vocab_Test
from typing import Dict, List


class Metric(BaseMetric):
    def __init__(self, tests: List[Dict]):
        metric_id = "FuM-Vocab"
        name = "Metadata satisfies user defined domain Vocabulary Constraints."
        active = True
        custom_tests = dict()

        for idx, t in enumerate(tests):
            # Parse the test condition
            name, desc = t["condition"].split(",")
            if t["type"] == "Vocabulary Check":
                custom_tests[f"t_{str(idx + 1)}"] = Vocab_Test(
                    {"domain": t["domain"], "name": name.strip(), "desc": desc.strip()}
                )

        super().__init__(metric_id, name, active, custom_tests)

    def execute_tests(self, model, file_chunks, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
        }
        for tid, t in self.tests.items():
            t_result = t.perform_test(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )

            score = 0
            if t_result["success"]:
                score = 1

            # Each Test corresponds to a single vocab check, thus 1 point for each test
            results["test_results"][tid] = {
                "result": t_result,
                "score": score,
                "out_of": 1,
            }
        return results
