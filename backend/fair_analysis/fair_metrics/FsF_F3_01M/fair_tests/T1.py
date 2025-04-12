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
            if not ch_res["success"]:
                continue
            else:
                if ch_res["identifier"].strip() != "":
                    _r.append(ch_res)
        return _r


t1 = Test(
    name="Metadata contains data identifier information to download content like links to download files",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata provided for data files and detect identifiers to access them i.e. detect URLs or identifying information to download file content. Key Steps:-
    1. Check carefully if any information regarding file name or file type or file size is mentioned.
    2. Check all the listed urls and which one is explicitly used to identify where files can be downloaded from. Some special keywords like `/download` or `/files` or `/package`, `/content` can be useful to narrow down useful urls. Persistent Identifiers or landing page can be useful ones as last resort.
    3. Detect and update the keys for file name, size and type if provided in the given metadata.
    Only extract information that is explicitly mentioned in the metadata. Also make sure to detect identifiers ONLY for actual file/data and not any other entitiy like contributor etc. If that information is not found leave the field as empty and success as false.""",
    test_instruction="Check if metadata below has information about files.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
