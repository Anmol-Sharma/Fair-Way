import time
from urllib.parse import urljoin
import logging
import asyncio
import csv
from typing import List, Tuple

logger = logging.getLogger(__name__)


# Define helper function to fetch results
async def fetch_results(initiated_task_str: str, client, STATUS_URL, RESULTS_URL):
    """
    Helper function to poll for task completion and fetch results when ready.

    Args:
        initiated_task_str: Task ID string to check
        client: HTTP client for making requests
        STATUS_URL: Base URL for status endpoint
        RESULTS_URL: Base URL for results endpoint

    Returns:
        Parsed results JSON when task completes successfully

    Raises:
        ValueError: If task_id is invalid or doesn't match
        TimeoutError: If task doesn't complete within 30 minutes
        RuntimeError: For server errors
    """
    if not initiated_task_str:
        raise ValueError("No initiated task found")

    # Sleep for 4 seconds before starting to look for status updates.
    # Allow task to be initiated on the celery side.
    await asyncio.sleep(4)

    # Configuration
    start_time = time.time()
    timeout = 2700  # 45 minutes
    initial_delay = 120  # Start with a larger delay
    min_delay = 3  # Lowest time difference between check
    decrease_factor = 0.5  # Decrease delay by this factor each time

    delay = initial_delay
    attempt = 0

    while True:
        # Check for timeout
        elapsed = time.time() - start_time
        if elapsed >= timeout:
            raise TimeoutError(f"Timeout exceeded after {timeout // 60} minutes")

        attempt += 1
        logger.info(
            f"Checking task status (attempt {attempt}, elapsed: {elapsed:.1f}s): {initiated_task_str}"
        )

        try:
            # Check task status
            status_response = await client.get(urljoin(STATUS_URL, initiated_task_str))
            status_response.raise_for_status()  # Raise exception for 4XX/5XX responses

            status = status_response.json()

            if status["success"]:
                logger.info(f"Task {initiated_task_str} completed, fetching results")
                # Fetch results
                results_response = await client.get(
                    urljoin(RESULTS_URL, initiated_task_str)
                )
                results_response.raise_for_status()

                parsed_results = results_response.json()

                if parsed_results["task_id"] == initiated_task_str:
                    logger.info(
                        f"Successfully retrieved results for task {initiated_task_str}"
                    )
                    return parsed_results
                else:
                    raise ValueError(
                        f"Task ID mismatch. Expected: {initiated_task_str}, Got: {parsed_results.get('task_id')}"
                    )
            else:
                remaining = timeout - elapsed
                logger.info(
                    f"Task in progress. Waiting {delay:.1f}s. Timeout in {remaining:.1f}s"
                )

                # Ensure we don't sleep longer than our timeout
                sleep_time = min(delay, remaining)
                await asyncio.sleep(sleep_time)

                # Decrease delay for next iteration by given factor, but don't go below min_delay
                delay = max(delay * decrease_factor, min_delay)

        except (ValueError, TimeoutError):
            # Re-raise these specific exceptions
            raise
        except Exception as error:
            logger.error(f"Error checking task {initiated_task_str}: {error}")

            # For HTTP errors, check if we need to handle them specially
            if hasattr(error, "status_code") and error.status_code == 500:
                raise RuntimeError(
                    f"Internal Server Error when fetching task {initiated_task_str}"
                )

            # For other errors, provide context and re-raise
            raise RuntimeError(f"Failed to fetch results: {error}") from error


# Load test items from reference csv files
def load_test_items(csv_path: str) -> List[Tuple[str, str]]:
    """Load test items from CSV file."""
    test_items = []

    try:
        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                test_items.append((row[0], row[1]))

        logger.info(f"Loaded {len(test_items)} test items from {csv_path}")
        return test_items

    except Exception as e:
        logger.error(f"Error loading test items: {e}", exc_info=True)
        raise
