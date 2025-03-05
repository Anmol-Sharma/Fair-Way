from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_I1_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_I1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result

    def score_test_results(self, t_results):
        score = 0.0
        if t_results["success"]:
            score = 1.0

        self.results["test_results"]["FsF_I1_01M-1"] = {
            "result": t_results,
            "score": score,
            "out_of": 1,
        }

        return self.results


M = Metric(
    metric_id="FsF_I1_01M",
    name="Metadata represented using a formal knowledge representation language.",
    active=True,
    tests={"FsF_I1_01M-1": t1},
    principle="interoperable",
)
