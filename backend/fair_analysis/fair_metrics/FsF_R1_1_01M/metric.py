from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_1_01M.fair_tests.T1 import t1
from fair_analysis.fair_metrics.FsF_R1_1_01M.fair_tests.T2 import t2
from typing import Dict
import json
from pydantic import BaseModel


class ResponseFormat(BaseModel):
    license: str
    comment: str
    success: bool


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ1, t_result = self.tests["FsF_R1_1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        if not succ1:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id}"
            )
            t_result = {
                "license": "",
                "comment": "LLM failed to process request correctly",
            }

        succ2, t_result2 = self.tests["FsF_R1_1_01M-2"].perform_test(
            model=model,
            file_chunks=(json.dumps(t_result),),
            file_type="json",
        )
        if not succ2:
            t_result2 = {
                "success": False,
                "comment": "LLM failed to process request correctly",
            }
        return {**t_result, **t_result2}, ResponseFormat

    def score_test_results(self, t_results):
        score = 0
        if t_results.get("license") and t_results["license"].strip() != "":
            score = 1
            if t_results.get("success") and t_results["success"]:
                score = 2
        self.results["test_results"]["FsF_R1_1_01M-1"] = {
            "license": t_results.get("license")
        }
        self.results["test_results"]["FsF_R1_1_01M-2"] = {
            "success": t_results.get("success"),
            "comment": t_results.get("comment"),
        }
        self.results["score"] = score
        self.results["out_of"] = 2

        return self.results


M = Metric(
    metric_id="FsF_R1_1_01M",
    name="Metadata includes license information under which data can be reused",
    active=True,
    tests={"FsF_R1_1_01M-1": t1, "FsF_R1_1_01M-2": t2},
    principle="reusable",
)
