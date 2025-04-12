from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_R1_3_02D.fair_tests.t1_samples import (
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
            _r.append(ch_res)
        return _r


t1 = Test(
    name="File formats listed in the metadata are an open file formats.",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the provided metadata and check if data files listed used open data file formats. An open file format is format which can be used by anyone royalty free. Key Tasks :-
    1. Check if file formats information is listed in the metadata.
    2. If yes, check if the formats formats are open. You are given a list for open formats.
    3. If any format is not open, return success as false. Also KEEP the comment as brief.
    List of some open formats:-
    ```
    'apng', 'av1', 'flif', 'gif', 'jpeg', jpeg-'xl', 'png', 'webp', 'svg', 'xpm', 'alac', 'flac', 'mp3', 'ogg', 'vorbis', 'av1', 'webm', 'plaintext', 'csv', 'html', 'markdown', 'epub', 'latex', 'OpenXPS', 'Office_Open_XML', 'PDF' (open since v1.7), 'XHTML', '7z', 'bzip2', 'lzip', 'gzip', 'sqx', 'tar', 'xz', 'zip', 'css', 'hdf', 'json', 'netcdf', 'nzb', 'rss', 'xml', 'yaml', 'DjVu'
    ```
    """,
    test_instruction="Check if data files listed in the metadata are open file formats.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
