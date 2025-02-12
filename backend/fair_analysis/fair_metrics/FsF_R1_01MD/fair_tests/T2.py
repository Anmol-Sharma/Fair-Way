from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_R1_01MD.fair_tests.t2_samples import (
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
            if len(ch_res["files"]) == 0 and len(ch_res["variables"]) == 0:
                continue
            f_items = [i["name"] for i in ch_res["files"]]
            f_unique = list(set(f_items))
            v_items = list(set(ch_res["variables"]))
            if len(f_unique) == 1 and f_unique[0] == "":
                continue
            if len(v_items) == 1 and v_items[0] == "":
                continue
            _r.append(ch_res)
        return _r


t2 = Test(
    name="Metadata contains information about content of the data.",
    feedback_format=ResponseFormat,
    test_main_cmd="Your task is to help analyze the metadata provided at the end for content of the data, which includes file types, file sizes and measured variables. Check carefully if information explicitly about files has been mentioned and also carefully look if metadata includes information about variables/ observations which were measured.",
    test_instruction="Check if metadata includes information about data content. Check carefully as different vocabulary could have been used for them.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
