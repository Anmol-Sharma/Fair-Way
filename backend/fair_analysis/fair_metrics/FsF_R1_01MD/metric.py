from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_01MD.fair_tests.T2 import t2


class Metric(BaseMetric):
    def __init__(self, metric_id: str, name: str, active: bool, tests):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_chunks, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "reusable",
        }
        t_result = self.tests["FsF_R1_01MD-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )

        score = 0.0
        counter = 1
        if len(t_result["files"]) > 1 or len(t_result["variables"]) > 1:
            score = 1.0
        # For each file and variable increase score
        if score > 0.0:
            if len(t_result["files"]) > 1:
                score += len(t_result["files"])
                counter += len(t_result["files"])

            if len(t_result["variables"]) > 1:
                score += len(t_result["variables"])
                counter += len(t_result["variables"])

        results["test_results"]["FsF_R1_01MD-1"] = {
            "result": t_result,
            "score": score,
            "out_of": counter,
        }

        return results


M = Metric(
    metric_id="FsF_R1_01MD",
    name="Metadata specifies the content of the data",
    active=True,
    tests={"FsF_R1_01MD-1": t2},
)
