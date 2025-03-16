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
    test_main_cmd="""Your task is to help analyze the metadata provided for data access conditions and extract them. Data access conditions can be `public` where data is available with open licence and available without any restrictions. Access condition can be `embargoed` if it is available after a time period or `restricted` where data is available only under certain conditions or only to certain people. Another access condition can also be `metadata-only` where users can only have access to metadata. Key Steps:-
    1. Check if access condition is mentioned in the metadata.
    2. If the condition is embargoed, check for date.
    3. If it is restricted, check for the condition for restricted.
    4. If there is no information about access, return back empty value for the access_condition variable.
    Answer in the provide JSON format.
    """,
    test_instruction="Check if metadata contains access conditions about data.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
