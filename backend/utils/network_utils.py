import httpx
import json
from urllib.parse import quote_plus, urljoin
import extruct
from w3lib.html import get_base_url
import logging
import re
from bs4 import BeautifulSoup

from typing import Tuple, Dict, Optional
from config import get_env_settings

env_settings = get_env_settings()
logger = logging.getLogger("fastapi")

# Define Repository URL patterns for the list of supported repositories
REPOSITORY_URL_PATTERNS = {
    "zenodo": f"{env_settings.base_zenodo_resolver}",
    "dryad": f"{env_settings.base_dryad_resolver}",
    "huggingface": f"{env_settings.base_hugging_face_resolver}",
    "doi": f"{env_settings.base_doi_resolver}",
}

# Consolidated removable keys
REMOVABLE_KEYS = {
    "zenodo": [
        "swh",
        "owners",
        "stats",
        "id",
        "recid",
        "conceptrecid",
        "conceptdoi",
        "created",
        "modified",
        "updated",
    ],
    "dryad": ["id", "lastModificationDate", "_links"],
    "huggingface": ["sha", "downloads", "likes", "_id"],
}


# HTTP client singleton
class HttpClient:
    _client = None

    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None:
            cls._client = httpx.AsyncClient()
        return cls._client


async def fetch_metadata_using_url(
    url: str, force_api: bool = False
) -> Tuple[bool, Dict]:
    """Extract metadata from any URL, combining embedded and API metadata as needed."""
    # Identify repository type and record ID from URL
    repository_type, record_id = identify_repository_and_id(url)

    # For Huggingface and DOI, immediately use API metadata
    if repository_type in ("huggingface", "doi") and record_id:
        logger.info(
            "Detected Huggingface/ DOI URL. Using API metadata retrieval directly."
        )
        succ, meta = await fetch_repository_api(repository_type, record_id)
        if not succ:
            return succ, meta
        else:
            if repository_type == "huggingface":
                return succ, {"api": {"metadata": meta, "source": "json"}}
            else:
                return succ, meta

    logger.info(f"Attempting to extract embedded metadata from URL: {url}")
    # First, attempt to extract embedded metadata from the landing page
    success_embedded, embedded_metadata = await extract_embedded_metadata(url)

    # For Zenodo and Dryad, also fetch API metadata and combine
    if repository_type in ["zenodo", "dryad"] and record_id:
        logger.info(f"Detected {repository_type} URL. Fetching API metadata as well.")
        success_api, api_metadata = await fetch_repository_api(
            repository_type, record_id
        )
        combined_metadata = {
            "embedded": embedded_metadata if success_embedded else {},
            "api": {"metadata": api_metadata, "source": "json"},
        }
        return True, combined_metadata

    # For other repository types, if embedded metadata extraction succeeded, return it.
    if success_embedded:
        return True, {"embedded": embedded_metadata}

    return False, {"error": f"Could not extract metadata from URL: {url}"}


def identify_repository_and_id(url: str) -> Tuple[str, Optional[str]]:
    """
    Extract repository type and record ID from URL.

    Expected behaviors:
      - Zenodo URLs, e.g., "https://zenodo.org/records/14791443"
        return: ("zenodo", "14791443")
      - Dryad URLs, e.g., "https://datadryad.org/stash/dataset/doi:10.5061/dryad.s1rn8pkcq"
        return: ("dryad", "doi:10.5061/dryad.s1rn8pkcq")
      - DOI URLs, e.g., "https://doi.org/api/handles/10.5281/zenodo.6673464"
        return: ("doi", "10.5281/zenodo.6673464")
      - Huggingface URLs similarly extract the record id.
    """
    patterns = {
        "zenodo": (
            r"^(?:https?://)?zenodo\.org/records?/(\d+)$",
            lambda m: ("zenodo", m.group(1)),
        ),
        "dryad": (
            # Include "doi:" in the captured group so that it remains part of the record ID
            r"^(?:https?://)?datadryad\.org(?:/stash)?/dataset/(doi:10\.\d+/dryad\.[a-zA-Z0-9-]+)$",
            lambda m: ("dryad", m.group(1)),
        ),
        "huggingface": (
            r"^(?:https?://)?huggingface\.co/(?:api/)?datasets/([\w-]+(?:/[\w-]+)*)$",
            lambda m: ("huggingface", m.group(1)),
        ),
        "doi": (
            r"^(?:https?://)?(?:doi\.org|dx\.doi\.org)/(?:api/handles/)?(10\.\d+\/\S+)$",
            lambda m: ("doi", m.group(1)),
        ),
    }

    # Iterate over the patterns in the defined order and return as soon as a match is found
    for repo, (pattern, extractor) in patterns.items():
        match = re.search(pattern, url)
        if match:
            return extractor(match)

    return "unknown", None


async def extract_embedded_metadata(url: str) -> Tuple[bool, Dict]:
    """Extract embedded metadata from a URL, with manual handling for HTTP 301/302 redirects."""
    try:
        client = HttpClient.get_client()
        # Disable automatic redirection to handle 301/302 manually
        response = await client.get(url, follow_redirects=False)
        if response.status_code in (301, 302):
            new_location = response.headers.get("location")
            if new_location:
                # Use urljoin to properly handle relative redirects
                new_url = urljoin(url, new_location)
                logger.info(
                    f"Received {response.status_code} redirect, fetching from new location: {new_url}"
                )
                response = await client.get(new_url, follow_redirects=False)
        response.raise_for_status()

        logger.info("Reading local html example for reference and testing")
        html_content = response.text

        base_url = get_base_url(html_content, str(response.url))
        metadata = extruct.extract(
            html_content,
            base_url=base_url,
            uniform=True,
            syntaxes=["json-ld", "microdata", "rdfa", "dublincore"],
        )

        rdf_data = None
        # Check if we have any metadata
        if not any(metadata.values()):
            logger.info("Checking for embedded Rdf/XML data")
            soup = BeautifulSoup(html_content, "html.parser")
            for tag in soup.find_all("script", type="application/rdf+xml"):
                rdf_data = tag.string  # Extract RDF content
            if not rdf_data:
                return False, {"error": "No embedded metadata found"}

        # Process different metadata formats
        for format_type in ["json-ld", "microdata", "rdfa", "dublincore"]:
            if metadata.get(format_type):
                # Convert the metadata to a string representation
                if format_type == "json-ld":
                    # For JSON-LD, use json.dumps to get a string representation
                    metadata_str = json.dumps(
                        (
                            metadata[format_type][0]
                            if isinstance(metadata[format_type], list)
                            else metadata[format_type]
                        ),
                        separators=(",", ":"),
                    )
                else:
                    # For other formats, use str() representation
                    data = (
                        metadata[format_type][0]
                        if isinstance(metadata[format_type], list)
                        else metadata[format_type]
                    )
                    metadata_str = str(data)

                return True, {
                    "source": format_type,
                    "metadata": metadata_str,
                }

        if rdf_data:
            return True, {
                "source": "rdf/xml",
                "metadata": rdf_data,
            }

        return False, {"error": "Could not process embedded metadata"}

    except httpx.HTTPStatusError as exc:
        logger.warning(f"HTTP Error: {exc.response.status_code} for URL: {url}")
        return False, {"error": f"HTTP error: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(f"Error extracting metadata from {url}: {str(e)}")
        return False, {"error": str(e)}


def construct_repository_url(repository_type: str, record_id: str) -> str:
    """Construct repository URL from type and ID."""
    base_url = REPOSITORY_URL_PATTERNS.get(repository_type, "")
    if repository_type == "dryad":
        return f"{base_url}{quote_plus(record_id)}"
    return f"{base_url}{record_id}"


def clean_metadata(metadata: Dict, repository_type: str) -> Dict:
    """
    Clean metadata by removing repository-specific unwanted keys.

    For Metadata Retrieved from Repository API Only.
    """
    if not metadata:
        return {}

    cleaned = json.loads(json.dumps(metadata, separators=(",", ":")))
    keys_to_remove = REMOVABLE_KEYS.get(repository_type, [])

    for key in keys_to_remove:
        if key in cleaned:
            cleaned.pop(key, None)

    return json.dumps(cleaned, separators=(",", ":"))


async def fetch_repository_api(
    repository_type: str, record_id: str
) -> Tuple[bool, Dict]:
    """
    Fetch metadata using record ID from the provided repository type.
    """

    # Try embedded metadata first if not forcing API
    if repository_type not in REPOSITORY_URL_PATTERNS:
        return False, {"error": "Unsupported Repository Detected"}

    try:
        client = HttpClient.get_client()
        url = construct_repository_url(repository_type, record_id)

        # Disable automatic redirects to manually process 301/302 status
        response = await client.get(url, follow_redirects=False)
        if response.status_code in (301, 302):
            new_location = response.headers.get("location")
            if new_location:
                # Use urljoin to properly handle relative redirects
                new_url = urljoin(url, new_location)
                logger.info(
                    f"Received {response.status_code} redirect, fetching from new location: {new_url}"
                )
                response = await client.get(new_url, follow_redirects=False)
        response.raise_for_status()

        # Parse the JSON responses from the repository provider
        data = json.loads(response.text)
        # Special handling for DOI API (Redirect to the actual service hosting the data)
        if repository_type == "doi":
            if data.get("responseCode") in [2, 100, 200]:
                return False, {
                    "error": f"Invalid response code from DOI service: {data.get("responseCode")}"
                }

            logger.info(
                f"Detected URL: {data["values"][1]["data"]["value"]} from the given DOI URL."
            )
            # Determine the actual Repository hosting the dataset
            return await fetch_metadata_using_url(data["values"][1]["data"]["value"])

        return True, clean_metadata(data, repository_type)

    except httpx.HTTPStatusError as exc:
        logger.warning(
            f"HTTP Error: {exc.response.status_code} for {repository_type} record: {record_id}"
        )
        return False, {"error": f"HTTP error: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(f"Error fetching {repository_type} record {record_id}: {str(e)}")
        return False, {"error": str(e)}
