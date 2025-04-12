# Define test for vocabulary test

from fair_analysis.fair_metrics.TestBase import BaseTest
from pydantic import BaseModel


class V_ResponseFormat(BaseModel):
    success: bool
    comment: str


########################################
#          DEFINE TEST OBJECT          #
########################################


# derive from base class and utilize
class Test(BaseTest):
    def __init__(self, vocab_item: dict):
        # Based on the provided instructions, domain define the base test.

        name = f"Metadata contains user defined vocabulary items for the domain {vocab_item["domain"]}."
        test_main_cmd = f"Your task is to help analyze the metadata provided for custom vocabulary item for the domain {vocab_item["domain"]}. The exact vocab item to check is: `{vocab_item["name"]}` and its description is: `{vocab_item["desc"]}`. Only return true if it is explicitly defined in the metadata."
        test_instruction = f"Check if metadata includes information explicitly about `{vocab_item["name"]}`"
        feedback_format = V_ResponseFormat

        super().__init__(
            name,
            feedback_format,
            test_main_cmd,
            test_instruction,
            use_few_shot_prompting=False,
            few_shot_samples=[],
        )

    def filter_chunk_results(self, chunk_results):
        # If all empty, return false, full empty (return chunks as empty)
        chunk_results = [ch_res for ch_res in chunk_results if ch_res["success"]]
        return chunk_results
