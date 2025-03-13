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
        "ex": """{"files":[{"name":"GLOBAL_LND_1982-2024_CSO","f_type":"csv","size":"","source":"Embedded Metadata"},{"name":"GLOBAL_S2_2015","f_type":"csv","size":"","source":"Embedded Metadata"},{"name":"file_stream","f_type":"zip","size":"","source":"Embedded Metadata"},{"name":"Landsat_Sentinel_Usable_Data.pdf","f_type":"pdf","size":"45 MB","source":"Harvested Metadata"}]}""",
        "feedback": """{"success": true, "comment":"all listed file formats are open"}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@id":"https://doi.org/10.5281/zenodo.1227121","@type":"https://schema.org/Dataset","identifier":"https://doi.org/10.5281/zenodo.1227121","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","contentSize":"6.86 GB","size":"6.86 GB","version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode","url":"https://zenodo.org/records/1227121"}""",
        "feedback": """{"success": false, "comment":"no file information present"}""",
    },
]
