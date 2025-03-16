from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_I2_01M.fair_tests.t1_samples import (
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
    name="Namespaces of known semantic resources can be identified in metadata.",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the metadata provided and detect if any known vocabulary namespace URIs are found. Key Tasks:-
    1. Check if metadata container any URI(Univeral Resource Identifiers) and extract them.
    2. Check if extracted URI belong to either 'rdf', 'rdfs', 'owl', 'xsd', 'schema.org'. These are common and you can ignore them.
    3. From the pending detected URIs check for examples like `bioportal`, `bartoc`, `linked open vocabularies (lov)`, purl linked vocabularies (eg. with url purl.org), `ontohub` etc. The metadata should explicilty list these with a distinct URI.
    4. Normal URLs or Universal Identifiers like DOI are NOT vocabulary namespace URIs.
    5. If there is no detected vocabulary namespaces, success should be false, and resources field as empty.""",
    test_instruction="Check if metadata includes information about used vocabulary namespace URIs.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
