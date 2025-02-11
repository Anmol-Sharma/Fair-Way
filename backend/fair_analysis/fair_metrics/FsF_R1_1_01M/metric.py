from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_R1_1_01M.fair_tests.T1 import t1


class Metric(BaseMetric):
    def __init__(self, metric_id: str, name: str, active: bool, tests):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_content, file_size, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "reusable",
        }
        t_result = self.tests["FsF_R1_1_01M-1"].perform_test(
            model=model,
            file_content=file_content,
            file_size=file_size,
            file_type=file_type,
        )

        score = 0
        if t_result["license"] != "":
            score = 1
        results["test_results"]["FsF_R1_1_01M-1"] = {
            "result": t_result,
            "score": score,
            "out_of": 1,
        }

        return results


# TODO: License approval test to be added

M = Metric(
    metric_id="FsF_R1_1_01M",
    name="Metadata includes license information under which data can be reused",
    active=True,
    tests={"FsF_R1_1_01M-1": t1},
)
