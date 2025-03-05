from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F3_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_F3_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result

    def score_test_results(self, t_results):
        # Custom score rules for this, if all mentioned then 0.5 else 0.25 if anything mentionec
        score = 0
        if (
            t_results["size"] != ""
            or len(t_results["file_names"]) > 1
            or t_results["d_type"] != ""
        ):
            score = 0.25
        # Check if all present
        if (
            t_results["size"] != ""
            and len(t_results["file_names"]) > 1
            and t_results["d_type"] != ""
        ):
            score = 0.5

        self.results["test_results"]["FsF_F3_01M-1"] = {
            "result": t_results,
            "score": score,
            "out_of": 0.5,
        }

        return self.results


# TODO: Add the second test for PID or URL for content

M = Metric(
    metric_id="FsF_F3_01M",
    name="Metadata includes the identifier of the data it describes",
    active=True,
    tests={"FsF_F3_01M-1": t1},
    principle="findable",
)
