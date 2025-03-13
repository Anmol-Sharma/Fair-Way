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
        print(chunk_results)
        for ch_res in chunk_results["file_list"]:
            if (
                ch_res["size"].strip() == ""
                or ch_res["file_name"].strip == ""
                or ch_res["d_type"].strip() == ""
            ):
                continue
            _r.append(ch_res)
        return _r


t1 = Test(
    name="Metadata identifier information about data for its size, type and files",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata provided at the end for `file name`, `file size` and `data type of file` and extract them from the data. Key Steps:-
    1. Check carefully if any information regarding file name or file type or file size is mentioned.
    2. Analyze file names carefully and reject any false positives. For eg. special characters like `:` or '}' as single characters cannot be valid file names.
    3. File Types which you select should reflect actual file types as well.
    4. Correctly match the information for each file including its name, type and size.
    5. Answer back in the provided response format.
    Only extract information that is explicitly mentioned in the metadata and if that information is not found leave the field as empty""",
    test_instruction="Check if metadata below has information about files.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
