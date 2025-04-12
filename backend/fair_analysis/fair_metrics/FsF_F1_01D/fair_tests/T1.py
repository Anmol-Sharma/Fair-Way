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
    name="Data is assigned global unique identifier in the provided metadata.",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata and carefully check the condition if metadata contains a Global Unique Identifier for the Data. It should follow a unique syntax which are common to unique identifiers. Examples of unique identifiers of data are Internationalized Resource Identifier (IRI), Website URL, Digital Object Identifier (DOI) etc. Records associated with common data repositories are also globally unique. Key Steps to follow:-
    1. Check for a GUID like a DOI or URL or URN or IRI or any other globally unique identifier explicitly mentioned int the metadata.
    2. Also check carefully if identifier is web accessble i.e. can be verified over internet. Random Text Cannot be a Persistent Identifier and SHOULD be explicitly mentioned in the metadata.
    3. If yes, then return success as true alongisde the detected identifier.
    4. If there is no detected global identifier, success should be false and identifier as empty.""",
    test_instruction="Check carefully if metadata has a globally unique identifier linked to the dataset or not.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
