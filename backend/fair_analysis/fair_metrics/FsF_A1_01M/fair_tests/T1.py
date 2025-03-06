from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_A1_01M.fair_tests.t1_samples import (
    FEW_SHOT_SAMPLES,
    ResponseFormat,
)

########################################
#          DEFINE TEST OBJECT          #
########################################


# derive from base class and utilize
class Test(BaseTest):
    def __init__(
        self,
        name: str,
        feedback_format: str,
        test_main_cmd: str,
        test_instruction: str,
        few_shot_samples=[],
    ):
        super().__init__(
            name,
            feedback_format,
            test_main_cmd,
            test_instruction,
            use_few_shot_prompting=True,
            few_shot_samples=few_shot_samples,
        )

    def filter_chunk_results(self, chunk_results):
        # If all empty, return false, full empty (return chunks as empty)
        chunk_results = [
            ch_res for ch_res in chunk_results if ch_res["access_condition"] != ""
        ]
        return chunk_results


t1 = Test(
    name="Metadata contains access level and access conditions of the data",
    feedback_format=ResponseFormat,
    test_main_cmd="Your task is to help analyze the metadata provided for data access conditions and extract them. Data access conditions can be `public` where data is available with open licence and available without any restrictions. Access condition can be `embargoed` if it is available after a time period or `restricted` where data is available only under certain conditions. Another access condition can be `metadata-only` where users can only have access to metadata",
    test_instruction="Check the data access conditions carefully. If there is no information about the same, return back empty value for the access condition. Analyze carefully as different vocabulary terms could have been used for it.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
