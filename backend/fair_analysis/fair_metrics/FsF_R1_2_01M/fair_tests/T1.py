from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_R1_2_01M.fair_tests.t1_samples import (
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
        _r = []
        for ch_res in chunk_results:
            if len(ch_res["entities"]) == 0:
                continue
            _r.append(ch_res)
        return _r


t1 = Test(
    name="Metadata contains provenance information about creators of the data.",
    feedback_format=ResponseFormat,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for provenance information about data. Carefully check if metadata contains information about all the following elements:- `creator`, `contributors`, `date of curation`, `version information`, `modification date` and `source`. Return True if and only if all these elements are present except contributor (it is optional), else return success as false.",
    test_instruction="Check if metadata includes provenance information about data.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
