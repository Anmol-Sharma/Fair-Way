from pydantic import BaseModel


class ResponseFormat(BaseModel):
    success: bool
    identifier: str
    file_name: str
    file_size: str
    file_type: str


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """<?xml version='1.0' encoding='utf-8'?><resource xmlns="http://datacite.org/schema/kernel-4" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4.3/metadata.xsd"><identifier identifierType="DOI">10.5281/zenodo.12345678</identifier><alternateIdentifiers><alternateIdentifier alternateIdentifierType="URL">https://zenodo.org/records/12345678</alternateIdentifier><alternateIdentifier alternateIdentifierType="oai">oai:zenodo.org:12345678</alternateIdentifier></alternateIdentifiers><creators><creator><creatorName nameType="Personal">Smith, Alex</creatorName><givenName>Alex</givenName><familyName>Smith</familyName><nameIdentifier nameIdentifierScheme="ORCID">0000-0002-5678-9101</nameIdentifier><affiliation>Global Research Institute</affiliation></creator><creator><creatorName nameType="Personal">Johnson, Emily</creatorName><givenName>Emily</givenName><familyName>Johnson</familyName><nameIdentifier nameIdentifierScheme="ORCID">0000-0001-2345-6789</nameIdentifier><affiliation>Environmental Studies Center</affiliation></creator></creators><titles><title>Comprehensive Environmental Data Archive 2024</title></titles><publisher>Zenodo</publisher><publicationYear>2024</publicationYear><dates><date dateType="Issued">2024-06-15</date><date dateType="Updated">2024-10-20</date></dates><resourceType resourceTypeGeneral="Dataset"></resourceType><relatedIdentifiers><relatedIdentifier relatedIdentifierType="URL" relationType="IsPartOf">https://zenodo.org/communities/environmental-science</relatedIdentifier></relatedIdentifiers><version>1.1</version><rightsList><rights rightsURI="https://creativecommons.org/licenses/by/4.0/legalcode" rightsIdentifierScheme="spdx" rightsIdentifier="cc-by-4.0">Creative Commons Attribution 4.0 International</rights></rightsList><files><file><filename>environmental_data_2024_v1.1.csv</filename><format>CSV</format><size>3.2 MB</size><checksum><type>MD5</type><value>a4c0b3f28c64e98312d49a7d5e0d1c5f</value></checksum></file><file><filename>environmental_data_2024_v1.2.json</filename><format>JSON</format><size>180 KB</size><checksum><type>SHA-256</type><value>5f3b2c4d1a6e3a7d4b3c9f8e2d1c0b7a3f2e9d5c7b8a6d1e3f4c2b9a1e7d8c5a</value></checksum></file></files></resource>""",
        "feedback": """{"success":true, "identifier":"10.5281/zenodo.12345678", "file_name":"environmental_data_2024_v1.1.csv", "file_type":"csv", "file_size":"3.2MB"}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@type":"https://schema.org/Dataset","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"author":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","dateModified":"2024-08-02T17:16:41.704421+00:00","datePublished":"2013-06-09","inLanguage":{"alternateName":"eng","@type":"Language","name":"English"},"version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode"}""",
        "feedback": """{"success":false, "identifier":"", "file_name":"", "file_type":"", "file_size":""}""",
    },
]
