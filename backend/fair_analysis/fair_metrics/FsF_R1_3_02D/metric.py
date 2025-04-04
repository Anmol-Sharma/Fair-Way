from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_3_02D.fair_tests.T1 import t1
from fair_analysis.fair_metrics.FsF_R1_3_02D.fair_tests.T2 import t2
from typing import Dict
from pydantic import BaseModel


class ResponseFormat(BaseModel):
    success: bool
    comment: str
    scientific_fmt: bool
    info: str


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        if len(file_chunks) > 1:
            succ1, t_result = self.tests["FsF_R1_3_02D-1"].perform_test(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            if not succ1:
                self.logger.warning(
                    f"LLM failed to process request correctly for {self.metric_id}"
                )
                t_result = {
                    "success": False,
                    "comment": "LLM failed to process request correctly",
                }
            succ2, t_result_2 = self.tests["FsF_R1_3_02D-2"].perform_test(
                model=model,
                file_chunks=file_chunks,
                file_type=file_type,
            )
            if not succ2:
                self.logger.warning(
                    f"LLM failed to process request correctly for {self.metric_id}"
                )
                t_result_2 = {
                    "scientific_fmt": False,
                    "info": "",
                }
        else:
            t_result = {"success": False, "comment": "No File information found"}
            t_result_2 = {
                "scientific_fmt": False,
                "info": "No File information found, cannot check for scientific format",
            }
        return ({**t_result, **t_result_2}, ResponseFormat)

    def score_test_results(self, t_results):
        score = 0.0
        if t_results["success"] or t_results["scientific_fmt"]:
            score = 1.0

        self.results["test_results"]["FsF_R1_3_02D-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_R1_3_02D",
    name="Data is available in a file format recommended by the target research community.",
    active=True,
    tests={"FsF_R1_3_02D-1": t1, "FsF_R1_3_02D-2": t2},
    principle="reusable",
)
