from pydantic import BaseModel
from typing import List, Dict


class File(BaseModel):
    name: str
    f_type: str
    size: str


class ResponseFormat(BaseModel):
    files: List[File]
    variables: List[str]


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """# Project: Global Temperature Anomaly Model ## Overview This is an open-source climate modeling project built using Python and NumPy. The model uses historical temperature data to predict global temperature anomalies. ## Data Files The following data files are included in the repository: | File Name | Type | Size (MB) | Description | | --- | --- | --- | --- | | `temperature_data.csv` | CSV | 100 | Historical daily temperature records (1940-2022) | | `station_metadata.csv` | CSV | 50 | Metadata for temperature stations, including location and elevation | | `grid.nc` | NetCDF | 500 | Global grid data for climate model output | ## Measured Variables The following variables are included in the dataset: * **Temperature (°C)**: daily mean temperature at each station * **Elevation (m)**: elevation of each temperature station above sea level * **Latitude**: geographic latitude of each temperature station * **Longitude**: geographic longitude of each temperature station ## Data Format All data files are in CSV or NetCDF format and can be easily read using Python libraries such as pandas and netcdf4. ## Notes Please note that the `temperature_data.csv` file is a large file (100 MB) and may take some time to download or process.""",
        "feedback": """{"files":[{"name":"temperature_data", "f_type":"csv", "size":"100MB"}, {{"name":"grid", "f_type":"netcdf4", "size":"500MB"}}], "variables":["temperature", "Elevation", "Latitude"]}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@id":"https://doi.org/10.5281/zenodo.1227121","@type":"https://schema.org/Dataset","identifier":"https://doi.org/10.5281/zenodo.1227121","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","contentSize":"6.86 GB","size":"6.86 GB","version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode","url":"https://zenodo.org/records/1227121"}""",
        "feedback": """{"files":[], "variables":[]}""",
    },
]
