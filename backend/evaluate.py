import asyncio

from Evaluation.testing import TestExecutor
from Evaluation.eval_utils import load_test_items

import logging

logger = logging.getLogger(__name__)


async def main():
    """Main entry point for the program."""
    try:
        # Load test items
        test_items = load_test_items("./Evaluation/online-examples.csv")

        # Initialize test executor
        executor = TestExecutor()
        # evaluator = ResultEvaluator()

        # Run tests
        logger.info("Starting test execution phase")
        await executor.execute_all_tests(test_items)
        logger.info("Test execution phase completed")

    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
