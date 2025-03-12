from typing import Dict
from ollama import Client
from ollama import ChatResponse
from typing import Optional
from httpx import ReadTimeout
from pydantic import BaseModel
import logging


class ModelBase:
    def __init__(self, model_name: str, options: Dict, client_url: str) -> None:
        self.__model_name = model_name
        self.__model_options = options
        self.__client = Client(host=client_url, timeout=75.0)
        self.__logger = logging.getLogger("celery")

    def send_request(self, ResponseFormat: Optional[BaseModel], messages):
        """
        Helper function to send requests to the LLM model
        """
        try:
            if ResponseFormat:
                response: ChatResponse = self.__client.chat(
                    model=self.__model_name,
                    messages=messages,
                    options=self.__model_options,
                    format=ResponseFormat.model_json_schema(),
                )
            else:
                response: ChatResponse = self.__client.chat(
                    model=self.__model_name,
                    messages=messages,
                    options=self.__model_options,
                )
            return response
        except ReadTimeout:
            # Retry request if failed
            self.__logger.warning("Request Timedout Retrying!")
            if ResponseFormat:
                response: ChatResponse = self.__client.chat(
                    model=self.__model_name,
                    messages=messages,
                    options=self.__model_options,
                    format=ResponseFormat.model_json_schema(),
                )
            else:
                response: ChatResponse = self.__client.chat(
                    model=self.__model_name,
                    messages=messages,
                    options=self.__model_options,
                )
            return response
