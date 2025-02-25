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
    test_main_cmd="Your task is to help analyze the metadata provided at the end and check if any known vocabulary namespace URIs are found. There are certain default namesspaces like rdf, rdfs, owl, xsd, schema.org etc. You can ignore these since these are common namspaces. Some examples of other uncommon semantic resources include `bioportal`, `bartoc`, `linked open vocabularies (lov)`, purl linked vocabularies (eg. purl.org/net/VideoGameOntology), `ontohub` etc. You don't have to include all, only include the ones which are present in the metadata. Carefully check and answer back.",
    test_instruction="Check if metadata includes information about related semantic resources.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
