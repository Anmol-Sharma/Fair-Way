from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_F1_01D.fair_tests.t1_samples import (
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
        chunk_results = [ch_res for ch_res in chunk_results if ch_res["success"]]
        return chunk_results


t1 = Test(
    name="Data is assigned a persistent identifier in the provided metadata",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata and carefully the condition if contains a persistent identifier for the Data. Examples of persistent identifiers are Digital Object Identifier (DOI), arXiv ID, orcid id (orcid.org), handle system (handle.net), ARK (Archival Resource Key) since they persist over long periods. Many metadata items also use common vocabulary terms. For example Schema.org Dataset keys have explicit keys like `pid` to reflect that. Key Steps to follow:-
    1. Check data is assigned a persistent identifier in the metadata.
    2. Also check carefully if the identifier follows defined syntax to qualify as a Persistent Identifiers. Random Text Cannot be a Persistent Identifier and SHOULD be explicitly mentioned in the metadata.
    3. If yes, then return success as true alongisde the detected identifier.
    4. If there is no detected identifier, success should be false and identifier as empty.
    """,
    test_instruction="Check if metadata below has a persistent identifier for data.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
