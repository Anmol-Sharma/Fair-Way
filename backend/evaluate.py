import asyncio

from Evaluation.test_executor import TestExecutor
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

        # Run tests
        await executor.execute_all_tests(test_items)

    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
