import httpx
import json
from urllib.parse import quote_plus
from config import get_env_settings
import logging

from typing import Tuple, Dict

import sqlite3
from contextlib import contextmanager

env_settings = get_env_settings()


# Initialize Async Client for HTTPX
class HttpClient:
    _client: httpx.AsyncClient = None

    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None:
            cls._client = httpx.AsyncClient()
        return cls._client


ZENODO_REMOVABLE_KEYS = [
    "swh",
    "owners",
    "stats",
    "id",
    "recid",
    "conceptrecid",
    "conceptdoi",
    # These below are not metdata keys but rather the keys of the zenodo record
    "title",
    "created",
    "modified",
    "updated",
]

logger = logging.getLogger("fastapi")

DRYAD_REMOVABLE_KEYS = ["id", "lastModificationDate"]


async def fetch_zenodo_record(record_num: str) -> Tuple[bool, Dict]:
    """Helper Function to fetch Metadata for a dataset from Zenodo

    Args:
        record_num: id of the Zenodo dataset

    Returns:
        Tuple Containing operation Success and the received JSON metadata.
    """
    logger.info(f"Fetching Zenodo Record: {record_num}")
    global ZENODO_REMOVABLE_KEYS
    try:
        Client = HttpClient.get_client()
        response = await Client.get(f"{env_settings.base_zenodo_resolver}{record_num}")
        response.raise_for_status()
        resp = json.loads(response.text)
        for key in ZENODO_REMOVABLE_KEYS:
            resp.pop(key, None)
        return True, resp
    except httpx.HTTPStatusError as exc:
        logger.warning(
            f"HTTP Error occurred during fetching Zenodo record: {record_num}, response code: {exc.response.status_code}"
        )
        return False, {"error": f"HTTP error occurred: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(
            f"Error occurred during fetching Zenodo record: {record_num}, error: {str(e)}"
        )
        return False, {"error": str(e)}


async def fetch_dryad_record(record_num: str) -> Tuple[bool, Dict]:
    """Helper Function to fetch Metadata for a dataset from Dyrad

    Args:
        record_num: id of the dryad dataset

    Returns:
        Tuple Containing operation Success and the received JSON metadata.
    """
    logger.info(f"Fetching Dryad Record: {record_num}")
    global DRYAD_REMOVABLE_KEYS
    try:
        Client = HttpClient.get_client()
        logger.info(
            f"URL being sent==> {env_settings.base_dryad_resolver}{quote_plus(record_num)}"
        )
        response = await Client.get(
            f"{env_settings.base_dryad_resolver}{quote_plus(record_num)}"
        )
        response.raise_for_status()
        resp = json.loads(response.text)
        # Remove unecessary tags from the DRYAD DOI records before returning
        for key in DRYAD_REMOVABLE_KEYS:
            resp.pop(key, None)
        return True, resp
    except httpx.HTTPStatusError as exc:
        logger.warning(
            f"HTTP Error occurred during fetching Dryad record: {record_num}, response code: {exc.response.status_code}"
        )
        return False, {"error": f"HTTP error occurred: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(
            f"Error occurred during fetching Dryad record: {record_num}, error: {str(e)}"
        )
        return False, {"error": str(e)}


async def fetch_doi(id: str) -> Tuple[bool, Dict]:
    """Method to fetch a DOI from the service DOI.org

    Args:
        id: id of the doi object

    Returns:
        Tuple Containing operation Success and the Value Representing the value URI for the DOI.
    """
    try:
        Client = HttpClient.get_client()
        response = await Client.get(f"{env_settings.base_doi_resolver}{id}")
        response.raise_for_status()
        resp = json.loads(response.text)
        # reference here :- https://www.doi.org/doi-handbook/HTML/rest-api-response-format.html
        if resp["responseCode"] in [2, 100, 200]:
            return False, {
                "error": "Response Code returned by DOI service not appropriate"
            }
        return True, resp["values"][1]["data"]
    except httpx.HTTPStatusError as exc:
        logger.warning(
            f"HTTP Error occurred during fetching DOI: {id}, response code: {exc.response.status_code}"
        )
        return False, {"error": f"HTTP error occurred: {exc.response.status_code}"}
    except Exception as e:
        logger.warning(
            f"Error occurred during fetching DOI record: {id}, error: {str(e)}"
        )
        return False, {"error": str(e)}


def clean_file_content(content):
    """Helper function to cleanup file content before being sent to LLM.
    Args:
        content: complete contents of the file

    Returns:
        cleaned up file contents
    """
    # Step 1: Normalize newlines by replacing multiple consecutive newlines with a single newline
    content = "\n".join(line for line in content.split("\n") if line.strip())
    # Step 2: Remove tabs or replace them with a single space
    content = content.replace("\t", " ")
    # Step 3: Strip leading/trailing whitespace from each line
    content = "\n".join(line.strip() for line in content.split("\n"))
    # Step 4: Condense multiple spaces within lines to a single space
    content = " ".join(content.split())

    return content


def aggregate_results(results):
    """
    Things to compute/extract :-
        * Total FAIR Score
        * Total score for each principle
        * Percentage FAIR Score
    """
    summary = {}
    summary["title"] = results["FsF_F2_01M"]["test_results"]["FsF_F2_01M-1"]["result"][
        "title"
    ]
    summary["total_metrics"] = len(results)

    summary["score_summary"] = {
        "score": {"F": 0, "A": 0, "I": 0, "R": 0},
        "score_out_of": {"F": 0, "A": 0, "I": 0, "R": 0},
        "score_percent": {"F": 0, "A": 0, "I": 0, "R": 0},
    }

    def get_max_result_vals(test_results):
        max_score = 0
        max_out_of = 0
        for res in test_results:
            if test_results[res]["score"] > max_score:
                max_score = test_results[res]["score"]
            if test_results[res]["out_of"] > max_out_of:
                max_out_of = test_results[res]["out_of"]
        return max_score, max_out_of

    # Compute total score per principle, then sum them later for full score
    for metric_id, res in results.items():
        val, total = get_max_result_vals(results[metric_id]["test_results"])
        if "FsF_F" in metric_id:
            summary["score_summary"]["score"]["F"] += val
            summary["score_summary"]["score_out_of"]["F"] += total
        elif "FsF_A" in metric_id:
            summary["score_summary"]["score"]["A"] += val
            summary["score_summary"]["score_out_of"]["A"] += total
        elif "FsF_I" in metric_id:
            summary["score_summary"]["score"]["I"] += val
            summary["score_summary"]["score_out_of"]["I"] += total
        elif "FsF_R" in metric_id:
            summary["score_summary"]["score"]["R"] += val
            summary["score_summary"]["score_out_of"]["R"] += total

    for k in summary["score_summary"]["score_percent"]:
        if summary["score_summary"]["score_out_of"][k] > 0:
            summary["score_summary"]["score_percent"][k] = round(
                summary["score_summary"]["score"][k]
                / summary["score_summary"]["score_out_of"][k],
                3,
            )

    return summary


def init_db():
    """Initialize the database and create the feedback table"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128) NOT NULL,
            email VARCHAR(128) NULL,
            feedback TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )
        conn.commit()


@contextmanager
def get_db():
    """Context manager for database connections"""
    conn = sqlite3.connect(env_settings.feedback_db_path)
    try:
        yield conn
    finally:
        conn.close()


def save_feedback(name: str, email: str, feedback: str) -> bool:
    """Save feedback to the database"""
    with get_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)""",
                (name, email, feedback),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error saving feedback: {e}")
            return False
