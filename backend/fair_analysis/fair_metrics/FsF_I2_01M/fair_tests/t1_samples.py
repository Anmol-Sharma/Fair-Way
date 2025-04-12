from pydantic import BaseModel
from typing import List


class ResponseFormat(BaseModel):
    success: bool
    resources: List[str]


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """{"@context":{"dcterms":"http://purl.org/dc/terms/","void":"http://rdfs.org/ns/void#","foaf":"http://xmlns.com/foaf/0.1/","chebi":"http://purl.obolibrary.org/obo/chebi.owl#"},"@type":"dcterms:Dataset","@id":"https://example.org/dataset/chemicals","dcterms:title":"Biomedical Chemical Compounds Dataset","dcterms:description":"A dataset containing chemical compound data relevant to biomedical research, categorized using the ChEBI ontology.","dcterms:creator":{"@type":"foaf:Person","foaf:name":"Dr. Jane Doe","foaf:mbox":"mailto:jane.doe@example.org"},"dcterms:publisher":{"@type":"foaf:Organization","foaf:name":"Institute for Biomedical Research","foaf:homepage":"https://example.org/ibr"},"dcterms:issued":"2024-02-25","dcterms:modified":"2025-02-25","dcterms:license":"https://creativecommons.org/licenses/by/4.0/","void:sparqlEndpoint":"https://example.org/sparql","void:triples":500000,"void:exampleResource":{"@id":"http://purl.obolibrary.org/obo/CHEBI_15377","@type":"chebi:MolecularEntity","dcterms:title":"Water","dcterms:description":"Water (CHEBI:15377) is a chemical compound essential for life."},"dcterms:subject":[{"@id":"http://purl.obolibrary.org/obo/CHEBI_23888","dcterms:title":"Pharmaceutical compound","dcterms:description":"A compound used in medicinal applications."},{"@id":"http://purl.obolibrary.org/obo/CHEBI_33232","dcterms:title":"Organic molecule","dcterms:description":"A molecule containing carbon, typically found in living systems."}]}""",
        "feedback": """{"success":true,"resources":["http://purl.obolibrary.org/obo/chebi.owl"]}""",
    },
    {
        "ex": """<?xml version="1.0" encoding="UTF-8"?><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:foaf="http://xmlns.com/foaf/0.1/" xmlns:geo="http://www.geonames.org/ontology#" xmlns:void="http://rdfs.org/ns/void#"><dcterms:Dataset rdf:about="https://geospatial-data.io/dataset/geospatial"><dcterms:title>Global Geographic Locations Dataset</dcterms:title><dcterms:description>A dataset containing geospatial data, including cities, landmarks, and natural features, categorized using the GeoNames ontology.</dcterms:description><dcterms:creator><foaf:Person><foaf:name>Dr. John Smith</foaf:name><foaf:mbox>mailto:john.smith@geospatial-data.io</foaf:mbox></foaf:Person></dcterms:creator><dcterms:publisher><foaf:Organization><foaf:name>Geospatial Data Institute</foaf:name><foaf:homepage rdf:resource="https://geospatial-data.io/gdi" /></foaf:Organization></dcterms:publisher><dcterms:issued>2024-02-25</dcterms:issued><dcterms:modified>2025-02-25</dcterms:modified><void:triples>1000000</void:triples><dcterms:subject><geo:Feature rdf:about="http://sws.geonames.org/6295630/"><dcterms:title>Earth</dcterms:title><dcterms:description>Our planet, categorized in the GeoNames ontology.</dcterms:description><geo:Feature></dcterms:subject></dcterms:Dataset></rdf:RDF>""",
        "feedback": """{"success":true,"resources":["http://www.geonames.org/ontology"]}""",
    },
]
