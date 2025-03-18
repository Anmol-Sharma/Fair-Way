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
        t_result = self.tests["FsF_R1_1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )

        t_result2 = self.tests["FsF_R1_1_01M-2"].perform_test(
            model=model,
            file_chunks=(json.dumps(t_result),),
            file_type="json",
        )
        return {**t_result, **t_result2}, ResponseFormat

    def score_test_results(self, t_results):
        self.logger.info(f"Received Results:-{t_results}")
        score = 0
        if t_results["license"] != "":
            score = 1
            if t_results["success"]:
                score = 2
        del t_results["success"]
        self.results["test_results"]["FsF_R1_1_01M-1"] = t_results
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
