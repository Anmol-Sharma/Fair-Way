from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_I2_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ, t_result = self.tests["FsF_I2_01M-1"].perform_test(
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
                "resources": [],
                "comment": "LLM failed to process request correctly",
            }
        return t_result, self.tests["FsF_I2_01M-1"].test_feedback_format

    def score_test_results(self, t_results):
        score = 0.0
        if (
            ("resources" in t_results)
            and ("success" in t_results)
            and (len(t_results["resources"]) >= 1)
            and (t_results["success"])
        ):
            score = 1.0

        self.results["test_results"]["FsF_I2_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_I2_01M",
    name="Metadata uses semantic resources.",
    active=True,
    tests={"FsF_I2_01M-1": t1},
    principle="interoperable",
)
