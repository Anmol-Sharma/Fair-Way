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
    name="Data is assigned global unique identifier",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata and carefully check and extract if Data is assigned a global unique identifier. The unique identifier should be mentioned explicitly for data and not metadata and should follow a unique identifier syntax. Examples of unique identifiers of data are Internationalized Resource Identifier (IRI), URL, Digital Object Identifier (DOI), ORCID etc. Records associated with data repositories like Zenodo or Dryad are also globally unique. Key Steps :-
    1. Check for a GUID like a DOI or URL or URN or IRI etc.
    2. Also check carefully if they follow the defined syntax for each of those individual GUID.
    3. If there is no detected GUID, success cannot be true, so make sure to check that.""",
    test_instruction="Check carefully if metadata below has a globally unique identifier for data or not.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
