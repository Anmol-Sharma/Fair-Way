from fair_analysis.fair_metrics.MetricBase import BaseMetric
from fair_analysis.fair_metrics.FsF_F2_01M.fair_tests.T2 import t21, t22, t23
from typing import Dict
from pydantic import BaseModel


class ResponseFormat(BaseModel):
    creator: str
    title: str
    publisher: str
    publication_date: str
    summary: str
    keywords: str


class Metric(BaseMetric):
    def __init__(
        self, metric_id: str, name: str, active: bool, tests: Dict, principle: str
    ):
        super().__init__(metric_id, name, active, tests, principle)

    def execute_tests(self, model, file_chunks, file_type):
        # For this particular metric we have split up the main test into multiple parts for validation.
        succ1, t21_result = self.tests["1"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        succ2, t22_result = self.tests["2"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        succ3, t23_result = self.tests["3"].perform_test(
            model=model,
            file_chunks=file_chunks,
            file_type=file_type,
        )
        if not succ1:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id} for creator and title information"
            )
            t21_result = {"creator": "", "title": ""}
        if not succ2:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id} for publisher and publication_date information"
            )
            t22_result = {"publisher": "", "publication_date": ""}
        if not succ3:
            self.logger.warning(
                f"LLM failed to process request correctly for {self.metric_id} for summary and keyword information"
            )
            t23_result = {"summary": "", "keywords": ""}

        return {**t21_result, **t22_result, **t23_result}, ResponseFormat

    def score_test_results(self, t_results):
        """
        Score values :-
            * Some - 0.5
            * Core data cite - 1
            * Core descriptve metadata - 2
        """
        SCORE_RECEIVED = 0.0
        MAIN_SCORE = 2
        for k, v in t_results.items():
            if v != "":
                # Atleast one non-null entity
                SCORE_RECEIVED = 0.5
                break
        if SCORE_RECEIVED > 0.0:
            # Check for data cite core
            for k, v in t_results.items():
                if k in ("creator", "title", "publisher", "publication_date"):
                    if v == "" or v.lower() == "none" or v.lower() == "null":
                        # Atleast one null entity
                        SCORE_RECEIVED = 0.5
                        break
            else:
                SCORE_RECEIVED = 1

        # Check for core descriptive if core data cite there
        if SCORE_RECEIVED == 1:
            for k, v in t_results.items():
                if k in ("summary", "keywords"):
                    if v == "" or v.lower() == "none" or v.lower() == "null":
                        SCORE_RECEIVED = 1
                        break
            else:
                SCORE_RECEIVED = 2

        self.results["test_results"]["FsF_F2_01M-1-2-3"] = t_results
        self.results["score"] = SCORE_RECEIVED
        self.results["out_of"] = MAIN_SCORE

        return self.results


M = Metric(
    metric_id="FsF_F2_01M",
    name="Metadata includes descriptive core elements to support data findability",
    active=True,
    tests={"1": t21, "2": t22, "3": t23},
    principle="findable",
)
