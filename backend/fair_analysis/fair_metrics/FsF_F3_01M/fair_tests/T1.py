from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_F3_01M.fair_tests.t1_samples import (
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
            unique = list(set(ch_res.values()))
            if len(unique) == 1 and unique[0] == "":
                continue
            _r.append(ch_res)
        return _r


t1 = Test(
    name="Metadata identifier information about data for its size, type and files",
    feedback_format=ResponseFormat,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for `file names`, `dataset size` and `type of files` and extract them from the data.",
    test_instruction="Check if metadata below has file names, sizes and type information. Check carefully as similar words could have been used for them.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
