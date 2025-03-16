from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_I1_01M.fair_tests.t1_samples import (
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
    name="Parsable, structured metadata (JSON-LD, RDFa) is embedded in the landing page XHTML/HTML code.",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to analyze the metadata provided and check if the provided file format alongside the given metadata is represented using a formal knowledge representation language. A formal language representation format are structured metadata formats with certain vocabulary rules. Examples include OWL, RDFa, JSON-LD ('@context' or `@id` keywords) , RDF/XML ('rdf' defined vocabulary terms), Turtle etc. which make them suitable for machine readability. File content and formats like plain-text and markdown are not formal representations. Similarly normal json or normal xml syntaxes are also not formal representation formation.
    Key Steps to follow:-
    1. Check the metadata to see if it represented using a structured data format. Any sort of plain text or raw text like markdown etc. are not those.
    2. If a structured format is detected, check syntax.
    3. Finally check for formal repsentation by check the necessary vocabulary terms for either of the formal representation formats like `OWL`, `RDF` etc. are correctly used.
    Answer back in the provide format.""",
    test_instruction="Check if metadata is represented using a formal language representation format.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
