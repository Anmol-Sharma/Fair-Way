import httpx
import json
from urllib.parse import quote_plus
import extruct
from w3lib.html import get_base_url
import logging
import re

from typing import Tuple, Dict
from config import get_env_settings

env_settings = get_env_settings()
logger = logging.getLogger("fastapi")

# Repository URL patterns
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
        "title",
        "created",
        "modified",
        "updated",
    ],
    "dryad": ["id", "lastModificationDate"],
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


async def fetch_metadata_from_url(
    url: str, force_api: bool = False
) -> Tuple[bool, Dict]:
    """Extract metadata from any URL, regardless of repository type."""
    logger.info(f"Attempting to extract metadata from URL: {url}")

    # Try generic metadata extraction first
    success, metadata = await extract_embedded_metadata(url)
    if success:
        return True, metadata.get("metadata", {})

    # Try to identify repository type and record ID from URL
    repository_type, record_id = identify_repository_and_id(url)

    if record_id:
        logger.info(f"Identified as {repository_type} with record_id: {record_id}")
        return await fetch_metadata(record_id, force_api)

    return False, {"error": f"Could not extract metadata from URL: {url}"}


def identify_repository_and_id(url: str) -> Tuple[str, str]:
    """Extract repository type and record ID from URL."""
    patterns = {
        "zenodo": (
            r"^(https?://)?zenodo\.org/records/(\d+)$",
            lambda m: ("zenodo", f"10.5281/zenodo.{m.group(2)}"),
        ),
        "dryad": (
            r"^(https?://)?datadryad\.org/stash/dataset/(doi:10\.\d+/dryad\.[a-zA-Z0-9-]+)$",
            lambda m: ("dryad", m.group(2).replace("doi:", "")),
        ),
        "huggingface": (
            r"^(https?://)huggingface\.co\/(?:api\/)?datasets\/([\w-]+(?:\/[\w-]+)*)$",
            lambda m: ("huggingface", m.group(2)),
        ),
        "doi": (r"(10\.\d+\/[^\/]+)", lambda m: ("doi", m.group(1))),
    }

    for repo, (pattern, id_extractor) in patterns.items():
        match = re.search(pattern, url)
        if match:
            return id_extractor(match)

    return "unknown", None


async def extract_embedded_metadata(url: str) -> Tuple[bool, Dict]:
    """Extract embedded metadata from a URL, with manual handling for HTTP 301 redirects."""
    try:
        client = HttpClient.get_client()
        # Disable automatic redirection to handle 301 manually
        response = await client.get(url, follow_redirects=False)
        if response.status_code == 301:
            new_location = response.headers.get("location")
            if new_location:
                logger.info(
                    f"Received 301 redirect, fetching from new location: {new_location}"
                )
                response = await client.get(new_location, follow_redirects=False)
        response.raise_for_status()

        html_content = response.text
        base_url = get_base_url(html_content, str(response.url))
        metadata = extruct.extract(
            html_content,
            base_url=base_url,
            uniform=True,
            syntaxes=["json-ld", "microdata", "rdfa", "dublincore"],
        )

        # Check if we have any metadata
        if not any(metadata.values()):
            return False, {"error": "No embedded metadata found"}

        # Try metadata formats in order of preference
        for format_type in ["json-ld", "microdata", "rdfa", "dublincore"]:
            if metadata.get(format_type):
                data = metadata[format_type]
                return True, {
                    "source": format_type,
                    "metadata": data[0] if isinstance(data, list) and data else data,
                }

        return False, {"error": "Could not process embedded metadata"}

    except httpx.HTTPStatusError as exc:
        logger.warning(f"HTTP Error: {exc.response.status_code} for URL: {url}")
        return False, {"error": f"HTTP error: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(f"Error extracting metadata from {url}: {str(e)}")
        return False, {"error": str(e)}


async def fetch_metadata(record_id: str, force_api: bool = False) -> Tuple[bool, Dict]:
    """Fetch metadata using record ID."""
    repository_type = identify_repository_type(record_id)

    # Try embedded metadata first if not forcing API
    if not force_api and repository_type in REPOSITORY_URL_PATTERNS:
        url = construct_repository_url(repository_type, record_id)
        success, embedded_data = await extract_embedded_metadata(url)
        if success:
            return True, clean_metadata(
                embedded_data.get("metadata", {}), repository_type
            )

    # Fall back to API
    return await fetch_repository_api(repository_type, record_id)


def identify_repository_type(record_id: str) -> str:
    """Identify repository type from record ID."""
    if record_id.startswith("10.5281/zenodo."):
        return "zenodo"
    elif record_id.startswith("10.5061/dryad."):
        return "dryad"
    elif "/" in record_id and not record_id.startswith("10."):
        return "huggingface"
    elif record_id.startswith("10."):
        return "doi"
    return "unknown"


def construct_repository_url(repository_type: str, record_id: str) -> str:
    """Construct repository URL from type and ID."""
    base_url = REPOSITORY_URL_PATTERNS.get(repository_type, "")
    if repository_type == "dryad":
        return f"{base_url}{quote_plus(record_id)}"
    return f"{base_url}{record_id}"


def clean_metadata(metadata: Dict, repository_type: str) -> Dict:
    """Clean metadata by removing repository-specific unwanted keys."""
    if not metadata:
        return {}

    cleaned = json.loads(json.dumps(metadata))
    keys_to_remove = REMOVABLE_KEYS.get(repository_type, [])

    for key in keys_to_remove:
        if key in cleaned:
            cleaned.pop(key, None)

    return cleaned


async def fetch_repository_api(
    repository_type: str, record_id: str
) -> Tuple[bool, Dict]:
    """Fetch metadata from repository-specific API, handling HTTP 301 redirects."""
    try:
        client = HttpClient.get_client()
        url = construct_repository_url(repository_type, record_id)
        logger.info(f"Fetching from {repository_type} API: {url}")
        # Disable automatic redirects to manually process 301 status
        response = await client.get(url, follow_redirects=False)
        if response.status_code == 301:
            new_location = response.headers.get("location")
            if new_location:
                logger.info(
                    f"Received 301 redirect for API, fetching from new URL: {new_location}"
                )
                response = await client.get(new_location, follow_redirects=False)
        response.raise_for_status()

        data = json.loads(response.text)

        # Special handling for DOI API
        if repository_type == "doi":
            if data.get("responseCode") in [2, 100, 200]:
                return False, {"error": "Invalid response code from DOI service"}
            return True, data["values"][1]["data"]

        return True, clean_metadata(data, repository_type)

    except httpx.HTTPStatusError as exc:
        logger.warning(
            f"HTTP Error: {exc.response.status_code} for {repository_type} record: {record_id}"
        )
        return False, {"error": f"HTTP error: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(f"Error fetching {repository_type} record {record_id}: {str(e)}")
        return False, {"error": str(e)}
