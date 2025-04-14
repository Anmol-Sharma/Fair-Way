from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_I3_01M.fair_tests.T1 import t1
from typing import Dict
from celery import current_task


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        succ, t_result = self.tests["FsF_I3_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        if not succ:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id}"
            )
            t_result = {
                "entities": [],
                "comment": "LLM failed to process request correctly",
            }
        return t_result

    def analyze_metric(self, model, metadata):
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        All_Results = {}
        resp_format = self.tests["FsF_I3_01M-1"].test_feedback_format
        for k in metadata.keys():
            res = self.execute_tests(
                model,
                metadata[k]["metadata_chunks"],
                metadata[k]["source"],
            )
            name = ""
            if k == "api":
                name = "Harvested Metadata"
            elif k == "embedded":
                name = "Embedded Metadata"
            else:
                name = "Uploaded Metadata File"
            All_Results[name] = res

        if len(metadata.keys()) <= 1:
            return self.score_test_results(list(All_Results.values())[0])
        else:
            combined_results = self.combine_multi_metric_results(
                model, All_Results, resp_format
            )
            return self.score_test_results(combined_results)

    def score_test_results(self, t_results):
        score = 0.0
        if ("entities" in t_results) and len(t_results["entities"]) >= 1:
            score = 1.0

        self.results["test_results"]["FsF_I3_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_I3_01M",
    name="Metadata includes links between the data and its related entities",
    active=True,
    tests={"FsF_I3_01M-1": t1},
    principle="interoperable",
)
