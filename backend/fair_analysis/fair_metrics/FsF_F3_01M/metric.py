from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F3_01M.fair_tests.T1 import t1
from typing import Dict


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        t_result = self.tests["FsF_F3_01M-1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        self.logger.info(t_result)
        for idx, _ in enumerate(t_result["file_list"]):
            t_result["file_list"][idx] = {
                "size": t_result["file_list"][idx]["size"].strip(),
                "file_name": t_result["file_list"][idx]["file_name"].strip(),
                "d_type": t_result["file_list"][idx]["d_type"].strip(),
            }
        return t_result, self.tests["FsF_F3_01M-1"].test_feedback_format

    def score_test_results(self, t_results):
        # Custom score rules for this, if all mentioned then 0.5 else 0.25 if anything mentionec
        score = 0
        if len(t_results["file_list"]) > 1:
            for file_info in t_results:
                # Check if all present
                if (
                    file_info["size"] == ""
                    or file_info["file_name"] == ""
                    or file_info["d_type"] == ""
                ):
                    break
            else:
                # proper file information present
                score = 0.5

        self.results["test_results"]["FsF_F3_01M-1"] = t_results
        self.results["score"] = score
        self.results["out_of"] = 1

        return self.results


M = Metric(
    metric_id="FsF_F3_01M",
    name="Metadata includes the identifier of the data it describes",
    active=True,
    tests={"FsF_F3_01M-1": t1},
    principle="findable",
)
