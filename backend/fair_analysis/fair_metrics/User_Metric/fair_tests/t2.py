# Define test for vocabulary test

from fair_analysis.fair_metrics.TestBase import BaseTest
from pydantic import BaseModel


class ResponseFormat(BaseModel):
    success: bool
    comment: str


########################################
#          DEFINE TEST OBJECT          #
########################################

# TODO : See if you want to include few-shot examples here for reference.


# derive from base class and utilize
class Test(BaseTest):
    def __init__(self, standard: dict):
        name = "Metadata satisfies user defined domain standard check."
        test_main_cmd = f"Your task is to help analyze the metadata provided for domain specific standard check. The domain is `{standard["domain"]}`. You will be given specific condition to check. Only return true if the condition is explicitly satisfied in the metadata."
        test_instruction = (
            f"Check if metadata satisifies the condition `{standard["condition"]}`"
        )
        feedback_format = ResponseFormat

        print(test_main_cmd)
        print(test_instruction)

        super().__init__(
            name,
            feedback_format,
            test_main_cmd,
            test_instruction,
            use_few_shot_prompting=True,
            few_shot_samples=[],
        )

    def filter_chunk_results(self, chunk_results):
        # If all empty, return false, full empty (return chunks as empty)
        chunk_results = [ch_res for ch_res in chunk_results if ch_res["success"]]
        return chunk_results
