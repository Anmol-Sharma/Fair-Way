from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_01MD.fair_tests.T2 import t2
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_R1_01MD-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result, self.tests["FsF_R1_01MD-1"].test_feedback_format

    def score_test_results(self, t_results):
        score = 0.0
        counter = 1
        if len(t_results["files"]) > 1 or len(t_results["variables"]) > 1:
            score = 1.0
        # For each file and variable increase score
        if score > 0.0:
            if len(t_results["files"]) > 1:
                score += len(t_results["files"])
                counter += len(t_results["files"])

            if len(t_results["variables"]) > 1:
                score += len(t_results["variables"])
                counter += len(t_results["variables"])

        self.results["test_results"]["FsF_R1_01MD-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = counter

        return self.results


# TODO: Finish updating the prompts for this when scoring mechanism is reviewed

M = Metric(
    metric_id="FsF_R1_01MD",
    name="Metadata specifies the content of the data",
    active=True,
    tests={"FsF_R1_01MD-1": t2},
    principle="reusable",
)
