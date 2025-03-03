from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_I1_01M.fair_tests.T1 import t1


class Metric(BaseMetric):
    def __init__(self, metric_id: str, name: str, active: bool, tests):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_chunks, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "interoperable",
        }
        t_result = self.tests["FsF_I1_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )

        score = 0.0
        if t_result["success"]:
            score = 1.0

        results["test_results"]["FsF_I1_01M-1"] = {
            "result": t_result,
            "score": score,
            "out_of": 1,
        }

        return results


M = Metric(
    metric_id="FsF_I1_01M",
    name="Metadata represented using a formal knowledge representation language.",
    active=True,
    tests={"FsF_I1_01M-1": t1},
)
