from fair_analysis.fair_metrics.MetricBase import BaseMetric
from typing import Dict
from fair_analysis.fair_metrics.FsF_F1_01D.fair_tests.T1 import t1
from fair_analysis.fair_metrics.FsF_F1_01D.fair_tests.T2 import t2
import re


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ, t_result_1 = self.tests["FsF_F1_01D-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        if not succ:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id}"
            )
            t_result_1 = {
                "success": False,
                "identifier": "",
                "comment": "LLM failed to process request correctly",
            }
        return t_result_1, self.tests["FsF_F1_01D-1"].test_feedback_format

    def score_test_results(self, t_results):
        score = 0
        if ("success" in t_results) and t_results["success"]:
            score = 0.5

        if (
            ("success" in t_results)
            and t_results["success"]
            and re.match(
                "^(https?:\/\/)?([\w\-]+\.)+[\w]{2,}(:\d+)?(\/[^\s]*)?$",
                t_results["identifier"],
            )
        ):
            self.logger.info(f"Detect GUID:-{t_results}")
            try:
                if "identifier" in t_results:
                    t_results_2 = self.tests["FsF_F1_01D-2"].perform_test(
                        t_results["identifier"]
                    )
                else:
                    t_results_2 = {
                        "success": False,
                        "comment": "Identifier not found by llm",
                    }
            except Exception:
                self.logger.info("Couldn't resolve the GUI")
                t_results_2 = {"success": False, "comment": "Identifier unresolvable"}
        else:
            t_results_2 = {"success": False, "comment": "Identifier unresolvable"}

        if score > 0.0 and t_results_2["success"]:
            score = 1.0

        self.results["test_results"]["FsF_F1_01D-1"] = t_results
        self.results["test_results"]["FsF_F1_01D-2"] = t_results_2
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_F1_01D",
    name="Data is assigned a globally unique identifier",
    active=True,
    tests={
        "FsF_F1_01D-1": t1,
        "FsF_F1_01D-2": t2,
    },
    principle="findable",
)
