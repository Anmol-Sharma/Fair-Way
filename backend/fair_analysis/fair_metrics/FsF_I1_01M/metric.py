from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_I1_01M.fair_tests.T1 import t1
from typing import Dict
from celery import current_task


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_I1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        return t_result

    def analyze_metric(self, model, metadata):
        self.logger.info(
            f"Analyzing Metric: {self.metric_id}-{self.name} for task: {current_task.request.id}"
        )
        # Perform the relevant test on each of the metadata items and combine them together
        All_Results = {}
        for k in metadata.keys():
            # Perform the test on complete metadata
            res = self.execute_tests(
                model,
                (metadata[k]["metadata"],),  # Single complete chunk --> full metadata
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
            return All_Results.values()[0]
        else:
            combined_results = self.combine_multi_metric_results(model, All_Results)
            return self.score_test_results(combined_results)

    def score_test_results(self, t_results):
        score = 0.0
        if t_results["success"]:
            score = 1.0

        self.results["test_results"]["FsF_I1_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_I1_01M",
    name="Metadata represented using a formal knowledge representation language.",
    active=True,
    tests={"FsF_I1_01M-1": t1},
    principle="interoperable",
)
