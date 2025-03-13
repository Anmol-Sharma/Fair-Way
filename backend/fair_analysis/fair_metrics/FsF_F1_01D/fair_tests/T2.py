import logging
import httpx
from httpx import Client

########################################
#          DEFINE TEST OBJECT          #
########################################

logger = logging.getLogger("celery")


# derive from base class and utilize
class Test:
    def __init__(
        self,
        name: str,
    ):
        self.name = name

    def perform_test(self, url):
        """
        URL: Identifier to resolve
        """
        try:
            client = Client()
            logger.info(f"Fetching {url}")
            response = client.get(url, follow_redirects=True)
            response.raise_for_status()
            return {"success": True, "comment": "Identifier resolved"}
        except httpx.HTTPStatusError as exc:
            logger.warning(
                f"HTTP Error: {exc.response.status_code} while trying to resolve the identifier"
            )
            return {
                "success": False,
                "comment": f"Identifier could not be resolved. Status code :- {exc.response.status_code}",
            }


t2 = Test(
    name="URL is Resolvable",
)
