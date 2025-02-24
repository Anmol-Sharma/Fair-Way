from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F2_01M.fair_tests.T2 import t21, t22, t23


class Metric(BaseMetric):
    # super()
    # For this particular test we have split up the single test into multiple chunks.
    # So define scoring function here and set the score value in individual test to 0
    def __init__(self, metric_id: str, name: str, active: bool, tests):
        super().__init__(metric_id, name, active, tests)

    def execute_tests(self, model, file_chunks, file_type):
        results = {
            "metric_id": self.metric_id,
            "test_results": {},
            "metric_name": self.name,
            "principle": "findable",
        }

        t21_result = self.tests["1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        t22_result = self.tests["2"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        t23_result = self.tests["3"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )

        results = self.determine_score(
            t21_result, t22_result, t23_result, final_results=results
        )

        return results

    def determine_score(self, t21_result, t22_result, t23_result, final_results):
        """
        Score values :-
            * Some - 0.5
            * Core data cite - 1
            * Core descriptve metadata - 2
        """
        SCORE_RECEIVED = 0.0
        MAIN_SCORE = 2
        for k, v in {**t21_result, **t22_result, **t23_result}.items():
            if v != "":
                # Atleast one non-null entity
                SCORE_RECEIVED = 0.5
                break
        final_results["test_results"]["FsF_F2_01M-1"] = {
            "result": {**t21_result, **t22_result, **t23_result},
            "score": SCORE_RECEIVED,
            "out_of": 0.5,
        }

        if SCORE_RECEIVED > 0.0:
            # Check for data cite core
            for k, v in {**t21_result, **t22_result}.items():
                if v == "":
                    # Atleast one null entity
                    SCORE_RECEIVED = 0.5
                    break
            else:
                SCORE_RECEIVED = 1
        final_results["test_results"]["FsF_F2_01M-2"] = {
            "result": {**t21_result, **t22_result, **t23_result},
            "score": SCORE_RECEIVED,
            "out_of": 1,
        }

        # Check for core descriptive if core data cite there
        if SCORE_RECEIVED == 1:
            for _, v in t23_result.items():
                if v == "":
                    SCORE_RECEIVED = 1
                    break
            else:
                SCORE_RECEIVED = 2
        final_results["test_results"]["FsF_F2_01M-3"] = {
            "result": {**t21_result, **t22_result, **t23_result},
            "score": SCORE_RECEIVED,
            "out_of": MAIN_SCORE,
        }

        return final_results


M = Metric(
    metric_id="FsF_F2_01M",
    name="Metadata includes descriptive core elements to support data findability",
    active=True,
    tests={"1": t21, "2": t22, "3": t23},
)
