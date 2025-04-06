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
    test_main_cmd="""Your task is to help analyze the metadata provided and detect and extract related entities them from the given metadata. Key Steps:-
    1. Related entities include information about references to other datasets or resources. Check for 'funder', 'git repository', 'citations', 'versions' and 'contributor'.
    2. They can be referenced by fields like 'RelatedIdentifier' and 'RelationType' 'ORCID' for contributors, 'ROR' for institutions, 'HasVersion' for Version in a more formal metadata and using casually related terms in informal metadata.
    3. Analyze carefully the final list of related entities. Each entry should look like an actual related entity which is part of the given metadata and not some random text.
    Answer back in the provided response format.
    """,
    test_instruction="Check if metadata includes information about related entities.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
