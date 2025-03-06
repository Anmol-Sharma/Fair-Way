from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_F2_01M.fair_tests.t2_samples import (
    FEW_SHOT_SAMPLES_21,
    ResponseFormat_21,
)
from fair_analysis.fair_metrics.FsF_F2_01M.fair_tests.t2_samples import (
    FEW_SHOT_SAMPLES_22,
    ResponseFormat_22,
)
from fair_analysis.fair_metrics.FsF_F2_01M.fair_tests.t2_samples import (
    FEW_SHOT_SAMPLES_23,
    ResponseFormat_23,
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
            unique = list(set(ch_res.values()))
            if len(unique) == 1 and unique[0] == "":
                continue
            _r.append(ch_res)
        return _r


t21 = Test(
    name="Metadata provides metadata core description items 'creator' and 'title'",
    feedback_format=ResponseFormat_21,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for creator and title/ name and extract them from the data.",
    test_instruction="Check if metadata below has 'creator' and 'title' information. Analyze carefully as different vocabulary terms could have been used for both.",
    few_shot_samples=FEW_SHOT_SAMPLES_21,
)

t22 = Test(
    name="Metadata provides metadata core description items 'publisher' and 'publication_date'",
    feedback_format=ResponseFormat_22,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for publisher and publication date and extract them from the data.",
    test_instruction="Check if metadata below has 'publisher' and 'publication_date' information. Analyze carefully as different vocabulary terms could have been used for both.",
    few_shot_samples=FEW_SHOT_SAMPLES_22,
)

t23 = Test(
    name="Metadata provides metadata core description items 'summary' and 'keywords'",
    feedback_format=ResponseFormat_23,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for summary/ description and keywords and extract them from the data.",
    test_instruction="Check if metadata below has 'summary' and 'keywords' information. Analyze carefully as different vocabulary terms could have been used for both.",
    few_shot_samples=FEW_SHOT_SAMPLES_23,
)
