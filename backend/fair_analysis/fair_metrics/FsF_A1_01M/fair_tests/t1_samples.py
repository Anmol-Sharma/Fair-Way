from pydantic import BaseModel


class ResponseFormat(BaseModel):
    access_condition: str
    comment: str


############################################
#    Define the few shot examples below    #
#                                          #
# The few shot sample LLM responses should #
# match the Response format provided above #
############################################

FEW_SHOT_SAMPLES = [
    {
        "ex": """{"access":{"embargo":{"active":true,"reason":null,"until":"9999-12-31"},"files":"restricted","record":"public","status":"embargoed"},"created":"2023-10-15T09:30:45.123456+00:00","files":{"enabled":true},"metadata":{"creators":[{"affiliations":[{"name":"Center for Advanced Research, Boston, MA, USA"}],"person_or_org":{"family_name":"Smith","name":"John Smith","type":"personal"}},{"affiliations":[{"name":"Institute of Technology, Sydney, NSW, Australia;University of Cambridge, Cambridge, UK"}],"person_or_org":{"family_name":"Chen","name":"Li Wei Chen","type":"personal"}}],"publication_date":"2023-10-14","publisher":"Open Science Framework","resource_type":{"id":"dataset","title":{"de":"Datensatz","en":"Dataset"}},"subjects":[{"subject":"Climate Change Analysis"},{"subject":"Environmental Science"}],"title":"Global Climate Patterns Dataset (GCPD)","version":"2.1"},"pids":{"doi":{"client":"datacite","identifier":"10.5281/zenodo.12345678","provider":"datacite"},"oai":{"identifier":"oai:zenodo.org:12345678","provider":"oai"}},"revision_id":15,"status":"published","swh":{},"updated":"2024-11-29T14:46:34.653417+00:00","versions":{"index":2,"is_latest":true}}""",
        "feedback": """{"access_condition":"embargoed", comment:"Embargoed until 9999-12-31"}""",
    },
    {
        "ex": """{"@context":"http://schema.org","@id":"https://doi.org/10.5281/zenodo.1227121","@type":"https://schema.org/Dataset","identifier":"https://doi.org/10.5281/zenodo.1227121","name":"DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments","creator":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"author":[{"name":"Thiemann, Joachim","givenName":"Joachim","familyName":"Thiemann","affiliation":[{"@type":"Organization","name":"IRISA-CNRS"}],"@id":"https://orcid.org/0000-0002-8617-8330","@type":"Person"}],"publisher":{"@type":"Organization","name":"Zenodo"},"keywords":"Noise, Multichannel Audio, Microphone Array","dateCreated":"2018-04-24T10:46:21.267306+00:00","dateModified":"2024-08-02T17:16:41.704421+00:00","datePublished":"2013-06-09","inLanguage":{"alternateName":"eng","@type":"Language","name":"English"},"contentSize":"6.86 GB","size":"6.86 GB","version":"1.0","license":"https://creativecommons.org/licenses/by/4.0/legalcode","url":"https://zenodo.org/records/1227121"}""",
        "feedback": """{"access_condition":"public", "comment":"Provided with Open Creative Commons Licence"}""",
    },
]
