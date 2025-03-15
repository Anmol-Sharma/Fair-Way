from pydantic import BaseModel


class ResponseFormat(BaseModel):
    success: bool
    identifier: str


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################


FEW_SHOT_SAMPLES = [
    {
        "ex": """<?xml version='1.0' encoding='utf-8'?><resource xmlns="http://datacite.org/schema/kernel-4" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4.3/metadata.xsd"><alternateIdentifiers><alternateIdentifier alternateIdentifierType="URL">https://zenodo.org/records/99999999</alternateIdentifier><alternateIdentifier alternateIdentifierType="oai">oai:zenodo.org:99999999</alternateIdentifier></alternateIdentifiers><creators><creator><creatorName nameType="Personal">Smith, Alex</creatorName><givenName>Alex</givenName><familyName>Smith</familyName><nameIdentifier nameIdentifierScheme="ORCID">0000-0003-1234-5678</nameIdentifier><affiliation>Global Research Institute</affiliation></creator></creators><titles><title>Environmental Data Archive</title></titles><publisher>Zenodo</publisher><publicationYear>2024</publicationYear><dates><date dateType="Issued">2024-11-03</date><date dateType="Updated">2024-11-11</date></dates><resourceType resourceTypeGeneral="Dataset"></resourceType><relatedIdentifiers><relatedIdentifier relatedIdentifierType="URL" relationType="IsPartOf">https://zenodo.org/communities/environmental-data</relatedIdentifier></relatedIdentifiers><version>2024-11-03</version><rightsList><rights rightsURI="https://creativecommons.org/licenses/by/4.0/legalcode" rightsIdentifierScheme="spdx" rightsIdentifier="cc-by-4.0">Creative Commons Attribution 4.0 International</rights></rightsList></resource>""",
        "feedback": """{"success":true, "identifier":"https://zenodo.org/records/99999999"}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@id":"https://doi.org/10.5281/zenodo.1227121","@type":"https://schema.org/Dataset","identifier":"https://doi.org/10.5281/zenodo.1227121","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","dateModified":"2024-08-02T17:16:41.704421+00:00","datePublished":"2013-06-09","inLanguage":{"alternateName":"eng","@type":"Language","name":"English"},"contentSize":"6.86 GB","size":"6.86 GB","version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode","url":"https://zenodo.org/records/1227121","distribution":[{"@type":"DataDownload","contentUrl":"https://zenodo.org/api/records/1227121/files/DWASHING_48k.zip/content","encodingFormat":"application/zip"}]}""",
        "feedback": """{"success":true, "identifier":"https://doi.org/10.5281/zenodo.1227121"}""",
    },
]
