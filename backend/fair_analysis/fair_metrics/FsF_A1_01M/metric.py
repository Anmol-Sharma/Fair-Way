from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_A1_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(self, metric_id: str, name: str, active: bool, tests: Dict):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_content, file_size, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "accessible",
        }
        t_result = self.tests["FsF_A1_01M-1"].perform_test(
            model=model,
            file_content=file_content,
            file_size=file_size,
            file_type=file_type,
        )
        score = 0
        if t_result["access_condition"] != "":
            score = 0.5

        results["test_results"]["FsF_A1_01M-1"] = {
            "result": t_result,
            "score": score,
            "out_of": 0.5,
        }
        return results


# TODO: Decide what to do for 2nd test. F-UJI checks for 2nd test against a closed set of vocabs.

M = Metric(
    metric_id="FsF_A1_01M",
    name="Metadata contains access level and access conditions of the data",
    active=True,
    tests={"FsF_A1_01M-1": t1},
)
