from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_I3_01M.fair_tests.t1_samples import (
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
            items = [i["entity"] for i in ch_res["entities"]]
            unique = list(set(items))
            if len(unique) == 1 and unique[0] == "":
                continue
            _r.append(ch_res)
        return _r


t1 = Test(
    name="Metadata contains information about related entities.",
    feedback_format=ResponseFormat,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for mention of the related entities for the given dataset and extract them from the data. Related entities include information about other datasets or resources like funder, git repository etc. You don't have to include all, only include the ones which are present in the metadata.",
    test_instruction="Check if metadata includes information about related entities. Check carefully as similar words could have been used for it.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
