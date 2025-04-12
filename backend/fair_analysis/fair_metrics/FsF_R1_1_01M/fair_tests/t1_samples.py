from pydantic import BaseModel


class ResponseFormat(BaseModel):
    license: str


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """# Project: Diabetes Prediction Model ## Overview This is an open-source diabetes prediction model built using Python and TensorFlow. The model uses historical medical records to predict patient outcomes. ## Dataset * **Source**: National Institutes of Health (NIH) [Diabetes dataset](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5465115/) * **Version**: v1.0 * **License**: CC BY 4.0 ## Resources * **Funding**: Supported by the National Science Foundation (NSF) grant #1234567 * **Repository**: [GitHub repository](https://github.com/project-diabetes/diabetes-prediction-model) * **Website**: [Project website](http://diabetesprediction.org) ## Citing this project If you use this dataset or model in your research, please cite the following paper: [1] Smith et al. (2020). "Diabetes prediction using machine learning." Journal of Medical Systems. ## Acknowledgments We would like to thank the NIH for providing the diabetes dataset and the NSF for supporting this project.""",
        "feedback": """{"licence":""}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@id":"https://doi.org/10.5281/zenodo.1227121","@type":"https://schema.org/Dataset","identifier":"https://doi.org/10.5281/zenodo.1227121","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"author":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","dateModified":"2024-08-02T17:16:41.704421+00:00","datePublished":"2013-06-09","inLanguage":{"alternateName":"eng","@type":"Language","name":"English"},"contentSize":"6.86 GB","size":"6.86 GB","version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode","url":"https://zenodo.org/records/1227121"}""",
        "feedback": """{"licence":"Creative Commons Public Licence (CC-4.0)"}""",
    },
]
