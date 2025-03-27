import logging

logger = logging.getLogger("celery")


def clean_file_content(content):
    """Helper function to cleanup file content before being sent to LLM.
    Args:
        content: complete contents of the file

    Returns:
        cleaned up file contents
    """
    logger.info("Cleaning file contents")
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
    logger.info("Aggregating Metric Results")
    try:
        summary["title"] = results["FsF_F2_01M"]["test_results"]["FsF_F2_01M-1-2-3"][
            "title"
        ]
    except KeyError:
        logger.error("Key-Error while parsing results for title")
        summary["title"] = ""
    except Exception as e:
        logger.error("Something really bad happened")
        raise e

    try:
        summary["identifier"] = results["FsF_F1_02D"]["test_results"]["FsF_F1_02D-1"][
            "identifier"
        ]
    except KeyError:
        logger.error("Key-Error while parsing results for detected identifier")
        summary["identifier"] = ""
    except Exception as e:
        logger.error("Something really bad happened")
        raise e

    summary["total_metrics"] = len(results)

    summary["score_summary"] = {
        "score": {"F": 0, "A": 0, "I": 0, "R": 0, "U": 0.0},
        "score_out_of": {"F": 0, "A": 0, "I": 0, "R": 0, "U": 0.0},
        "score_percent": {"F": 0, "A": 0, "I": 0, "R": 0, "U": 0.0},
    }

    try:
        # Compute total score per principle, then sum them later for full score
        for metric_id, res in results.items():
            val, total = results[metric_id]["score"], results[metric_id]["out_of"]
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
            elif "FuM" in metric_id:
                summary["score_summary"]["score"]["U"] += val
                summary["score_summary"]["score_out_of"]["U"] += total

        for k in summary["score_summary"]["score_percent"]:
            if summary["score_summary"]["score_out_of"][k] > 0:
                summary["score_summary"]["score_percent"][k] = round(
                    summary["score_summary"]["score"][k]
                    / summary["score_summary"]["score_out_of"][k],
                    3,
                )
    except Exception as e:
        logger.error("Something really bad happened")
        raise e

    return summary
