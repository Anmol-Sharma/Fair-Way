from fair_analysis.fair_metrics.MetricBase import BaseMetric
from typing import Dict
from fair_analysis.fair_metrics.FsF_F1_01D.fair_tests.T1 import t1

# from fair_analysis.fair_metrics.FsF_F1_01D.Tests.T2 import t2


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_F1_01D-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result

    def score_test_results(self, t_results):
        score = 0
        if t_results["success"]:
            score = 0.5

        self.results["test_results"]["FsF_F1_01D-1"] = {
            "result": t_results,
            "score": score,
            "out_of": 0.5,
        }

        return self.results


# TODO: Define test for resolvable/ web-accessible

M = Metric(
    metric_id="FsF_F1_01D",
    name="Data is assigned a globally unique identifier",
    active=True,
    tests={"FsF_F1_01D-1": t1},
    principle="findable",
)
