from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_A1_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_A1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result

    def score_test_results(self, t_results):
        score = 0
        if t_results["access_condition"].strip() != "":
            score = 0.5

        self.results["test_results"]["FsF_A1_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 0.5

        return self.results


# TODO: Decide what to do for 2nd test. F-UJI checks for 2nd test against a closed set of vocabs.

M = Metric(
    metric_id="FsF_A1_01M",
    name="Metadata contains access level and access conditions of the data",
    active=True,
    tests={"FsF_A1_01M-1": t1},
    principle="accessible",
)
