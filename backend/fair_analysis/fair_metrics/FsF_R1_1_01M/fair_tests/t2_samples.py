from pydantic import BaseModel


class ResponseFormat(BaseModel):
    success: bool
    comment: str


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """{"licence":"NASA Open Source Agreement (NOSA)"}""",
        "feedback": """{"success":false, comment:"Doesn't belong to SPDX registry"}""",
    },
    {
        "ex": """{"license":"https://creativecommons.org/licenses/by/4.0/legalcode"}""",
        "feedback": """{"success":true, "comment":"Belongs to SPDX registry"}""",
    },
]
