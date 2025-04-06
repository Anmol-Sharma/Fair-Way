from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_01MD.fair_tests.T2 import t2
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ, t_result = self.tests["FsF_R1_01MD-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        if not succ:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id}"
            )
            t_result = {
                "files": [],
                "variables": [],
                "comment": "LLM failed to process request correctly",
            }
        return t_result, self.tests["FsF_R1_01MD-1"].test_feedback_format

    def score_test_results(self, t_results):
        score = 0.0
        if (
            t_results.get("files")
            and t_results.get("variables")
            and (len(t_results["files"]) >= 1 or len(t_results["variables"]) >= 1)
        ):
            score = 1.0
        if score > 0.0:
            if t_results.get("files") and len(t_results["files"]) > 1:
                for file_info in t_results["files"]:
                    if (
                        (file_info["name"].strip() != "")
                        and (file_info["f_type"].strip() != "")
                        and (file_info["size"].strip() != "")
                    ):
                        score += 1.0
                        break

            if t_results.get("variables") and len(t_results["variables"]) > 1:
                score += 1.0

        self.results["test_results"]["FsF_R1_01MD-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 4

        return self.results


M = Metric(
    metric_id="FsF_R1_01MD",
    name="Metadata specifies the content of the data",
    active=True,
    tests={"FsF_R1_01MD-1": t2},
    principle="reusable",
)
