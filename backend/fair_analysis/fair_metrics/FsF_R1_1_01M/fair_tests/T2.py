from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_R1_1_01M.fair_tests.t2_samples import (
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
        chunk_results = [ch_res for ch_res in chunk_results if ch_res["success"]]
        return chunk_results


t2 = Test(
    name="License used falls in SPDX licence registry.",
    feedback_format=ResponseFormat,
    test_main_cmd="""You will be given licence information detected in a metadata. Your task is to check if this licence is part of some common licences in SPDX registry which will are provided to you below.
    Some common licences used in spdx registery:- 'Apapche-1.0', 'CC-BY-4.0', 'CC0-1.0', 'FSFAP(FsF All Permisive)', 'NOSL(netizen open source licence)', 'NPL-1.0(netscape public licence)', 'OSL-1.1(Open software licence)', 'AFL (Academic Free licence)', 'CPL(Common public licence)', 'EUDatagrid licence', 'MIT', 'MPL (Mozilla public licence)', 'OSL (Open Software licence)', 'PDDL', 'ODC'.
    """,
    test_instruction="Check if licence used is listed in SPDX registry.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
