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
        "ex": """{"@context":{"dcterms":"http://purl.org/dc/terms/","void":"http://rdfs.org/ns/void#","foaf":"http://xmlns.com/foaf/0.1/","chebi":"http://purl.obolibrary.org/obo/chebi.owl#"},"@type":"dcterms:Dataset","@id":"https://example.org/dataset/chemicals","dcterms:title":"Biomedical Chemical Compounds Dataset","dcterms:description":"A dataset containing chemical compound data relevant to biomedical research, categorized using the ChEBI ontology.","dcterms:creator":{"@type":"foaf:Person","foaf:name":"Dr. Jane Doe","foaf:mbox":"mailto:jane.doe@example.org"},"dcterms:publisher":{"@type":"foaf:Organization","foaf:name":"Institute for Biomedical Research","foaf:homepage":"https://example.org/ibr"},"dcterms:issued":"2024-02-25","dcterms:modified":"2025-02-25","dcterms:license":"https://creativecommons.org/licenses/by/4.0/","void:sparqlEndpoint":"https://example.org/sparql","void:triples":500000,"void:exampleResource":{"@id":"http://purl.obolibrary.org/obo/CHEBI_15377","@type":"chebi:MolecularEntity","dcterms:title":"Water","dcterms:description":"Water (CHEBI:15377) is a chemical compound essential for life."},"dcterms:subject":[{"@id":"http://purl.obolibrary.org/obo/CHEBI_23888","dcterms:title":"Pharmaceutical compound","dcterms:description":"A compound used in medicinal applications."},{"@id":"http://purl.obolibrary.org/obo/CHEBI_33232","dcterms:title":"Organic molecule","dcterms:description":"A molecule containing carbon, typically found in living systems."}]}""",
        "feedback": """{"success":true,"comment":"The JSON-LD document is a well-formed formal knowledge representation that follows linked data principles and ontology standards for semantic web."}""",
    },
    {
        "ex": """# Dataset Metadata: Urban Air Quality Measurements (2024)
        ## Overview
        This dataset contains hourly air quality measurements collected from multiple monitoring stations across New York City for the year 2024.

        ## Dataset Details
        - **Title:** Urban Air Quality Measurements - NYC 2024
        - **Description:** Hourly data on major pollutants including PM2.5, PM10, NO2, CO, and O3, collected from 15 monitoring sites.
        - **Creator:** NYC Department of Environmental Protection
        - **Version:** 1.0
        - **License:** CC BY 4.0
        - **DOI:** 10.1234/urban-air-nyc-2024

        ## File Information
        - **Format:** CSV
        - **Size:** 200MB
        - **Number of Records:** ~131,400 (15 stations × 365 days × 24 hours)

        ## Columns
        | Column Name | Description                 | Data Type |
        |-------------|-----------------------------|-----------|
        | station_id  | Monitoring station ID       | String    |
        | timestamp   | Date and time of recording  | Datetime  |
        | pm25        | PM2.5 concentration (µg/m³) | Float     |
        | o3          | O3 concentration (ppb)      | Float     |

        ## Usage
        This dataset is intended for use in urban environmental research, machine learning models for air quality prediction, and public health analysis.""",
        "feedback": """{"success":false, "comment":"Markdown data detected. Not formal representation."}""",
    },
]
