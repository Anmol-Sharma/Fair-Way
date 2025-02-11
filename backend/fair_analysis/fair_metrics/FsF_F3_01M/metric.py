from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F3_01M.fair_tests.T1 import t1


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
        t_result = self.tests["FsF_F3_01M-1"].perform_test(
            model=model,
            file_content=file_content,
            file_size=file_size,
            file_type=file_type,
        )

        # Custom score rules for this, if all mentioned then 0.5 else 0.25 if anything mentionec
        score = 0
        if (
            t_result["size"] != ""
            or len(t_result["file_names"]) > 1
            or t_result["d_type"] != ""
        ):
            score = 0.25
        # Check if all present
        if (
            t_result["size"] != ""
            and len(t_result["file_names"]) > 1
            and t_result["d_type"] != ""
        ):
            score = 0.5

        results["test_results"]["FsF_F3_01M-1"] = {
            "result": t_result,
            "score": score,
            "out_of": 0.5,
        }

        return results


# TODO: Add the second test for PID or URL for content

M = Metric(
    metric_id="FsF_F3_01M",
    name="Metadata includes the identifier of the data it describes",
    active=True,
    tests={"FsF_F3_01M-1": t1},
)
