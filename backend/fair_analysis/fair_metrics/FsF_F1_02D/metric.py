from fair_analysis.fair_metrics.MetricBase import BaseMetric

from fair_analysis.fair_metrics.FsF_F1_02D.fair_tests.T1 import t1


class Metric(BaseMetric):
    def __init__(self, metric_id: str, name: str, active: bool, tests):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_content, file_size, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "findable",
        }
        t_result = self.tests["FsF_F1_02D-1"].perform_test(
            model=model,
            file_content=file_content,
            file_size=file_size,
            file_type=file_type,
        )
        score = 0
        if t_result["success"]:
            score = 0.5

        results["test_results"]["FsF_F1_02D-1"] = {
            "result": t_result,
            "score": score,
            "out_of": 0.5,
        }

        return results


# TODO: Define test to check if the identifier is web-accessible

M = Metric(
    metric_id="FsF_F1_02D",
    name="Data is assigned a persistent identifier",
    active=True,
    tests={"FsF_F1_02D-1": t1},
)
