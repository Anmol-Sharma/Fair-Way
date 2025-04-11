from Evaluation.eval_utils import load_test_items
import csv
from Evaluation.testing import TestExecutor, ResultEvaluator
from config import get_env_settings
import logging

logger = logging.getLogger(__name__)
env_settings = get_env_settings()


def main():
    """Main entry point for the program."""
    try:
        # Load test items
        test_items = load_test_items("./Evaluation/online-examples.csv")

        # Initialize test executor
        executor = TestExecutor()
        evaluator = ResultEvaluator()

        # Run tests
        logger.info("Starting test execution phase")
        executor.execute_all_tests(test_items)
        logger.info("Test execution phase completed")

        # Then evaluate the results
        logger.info("Starting result evaluation phase")
        results = evaluator.compile_results(test_items)
        logger.info("Result evaluation phase completed")

        # First, get the headers - LLM, Temperature followed by all metric names
        headers = ["LLM", "Temperature"] + list(next(iter(results.values())).keys())

        # Initialize a list to store all rows
        rows = []
        # Iterate through each entry in the dictionary
        for (llm, temp), metrics in results.items():
            # Create a row with LLM name, temperature and all metric values
            row = [llm, temp] + list(metrics.values())
            rows.append(row)

        # Write to CSV file
        with open("./Evaluation/llm_performance_metrics.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)  # Write headers
            writer.writerows(rows)  # Write all rows

    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)


if __name__ == "__main__":
    if env_settings.environment.lower() != "eval":
        raise Exception(
            "Enviroment Variables File doesn't have 'Environment' variable set to `EVAL`. Please Fix!"
        )
    main()
