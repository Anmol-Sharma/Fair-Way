import logging
from typing import Tuple
from inspect import cleandoc
from pydantic import BaseModel
import json

logger = logging.getLogger("celery")


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
    try:
        summary["title"] = results["FsF_F2_01M"]["test_results"]["FsF_F2_01M-1"][
            "result"
        ]["title"]

        summary["identifier"] = results["FsF_F1_02D"]["test_results"]["FsF_F1_02D-1"][
            "result"
        ]["identifier"]
    except KeyError:
        logger.error("Key-Error while parsing results for title")
        summary["title"] = ""

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
        # TODO: Remove this if condition later on and compute the max results for all.
        if "FsF" in metric_id:
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


def combined_results(model, results) -> Tuple[str, str]:
    """
    Helper function to send LLM results to be combined together
    """
    # Check the length of keys of metadata to decide the next step

    messages = [
        {
            "role": "system",
            "content": """Your Task is to combine the results from two separate fair assessment test. Both will have the same json structure however they are on different metadata sources (eg. embedded or retrieved through metadata harvest). Your task is to combine them together. Check carefully if a test succeeds in one of them, then the final result should reflect that. Only fail the test which doesn't succeed in both. Only answer back in the provided data format of the test since you are interacting with a backend api and not a human. Also provide metadata without additional indentation since it will be handled by explicitly programmed logic.""",
        },
        {
            "role": "user",
            "content": cleandoc(
                f"""Combine the two test items. First Test Result.\n```{str(results[0])}```\nSecond Test Result```{str(results[1])}```"""
            ),
        },
    ]
    # Metadata from multiple sources
    response = model.send_request(messages=messages, ResponseFormat=None)
    logger.info("Model Combined Result:-", response["message"]["content"])
    return json.loads(response["message"]["content"])
