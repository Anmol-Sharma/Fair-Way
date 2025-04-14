from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F3_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ, t_result = self.tests["FsF_F3_01M-1"].perform_test(
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
                "identifier": "",
                "file_name": "",
                "file_type": "",
                "file_size": "",
                "comment": "LLM failed to process request correctly",
            }
        return t_result, self.tests["FsF_F3_01M-1"].test_feedback_format

    def score_test_results(self, t_results):
        score = 0
        if ("success" in t_results) and t_results["success"]:
            if ("identifier" in t_results) and t_results["identifier"].strip() != "":
                score = 1.0
        else:
            if (
                (("file_name" in t_results) and t_results["file_name"].strip() != "")
                or (("file_size" in t_results) and t_results["file_size"].strip() != "")
                or (("file_type" in t_results) and t_results["file_type"].strip() != "")
            ):
                score = 0.5

        self.results["test_results"]["FsF_F3_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_F3_01M",
    name="Metadata includes the identifier of the data it describes",
    active=True,
    tests={"FsF_F3_01M-1": t1},
    principle="findable",
)
