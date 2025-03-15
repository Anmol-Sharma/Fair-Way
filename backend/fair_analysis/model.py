from ollama import Client
from ollama import ChatResponse
from typing import Optional, List, Dict
from httpx import ReadTimeout
from pydantic import BaseModel
import logging


class OllamaModel:
    def __init__(self, model_name: str, options: Dict, client_url: str) -> None:
        self.__model_name = model_name
        self.__model_options = options
        self.__client = Client(host=client_url, timeout=75.0)
        self.__logger = logging.getLogger("celery")

    def send_request(
        self, messages: List[Dict], ResponseFormat: Optional[BaseModel] = None
    ):
        """
        Helper function to send requests to the LLM model
        """
        if ResponseFormat is not None:
            ResponseFormat = ResponseFormat.model_json_schema()
        try:
            response: ChatResponse = self.__client.chat(
                model=self.__model_name,
                messages=messages,
                format=ResponseFormat,
            )
            return response
        except ReadTimeout:
            # Retry request if failed
            self.__logger.warning("Request Timedout Retrying!")
            response: ChatResponse = self.__client.chat(
                model=self.__model_name,
                messages=messages,
                format=ResponseFormat,
            )
            return response
        except Exception as e:
            self.__logger.warning("Something Unexpected happened!")
            raise e
