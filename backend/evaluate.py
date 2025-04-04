import asyncio

from Evaluation.testing import TestExecutor

# from Evaluation.testing import TestExecutor, ResultEvaluator
from Evaluation.eval_utils import load_test_items
from config import get_env_settings
import logging

logger = logging.getLogger(__name__)
env_settings = get_env_settings()


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

        # Then evaluate the results
        # logger.info("Starting result evaluation phase")

        # # TODO: Save the final result summary somewhere for reference.
        # await evaluator.run_evaluation(test_items)

        # logger.info("Result evaluation phase completed")

    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)


if __name__ == "__main__":
    if env_settings.environment.lower() != "eval":
        raise Exception(
            "Enviroment Variables File doesn't have 'Environment' variable set to `EVAL`. Please Fix!"
        )
    asyncio.run(main())
