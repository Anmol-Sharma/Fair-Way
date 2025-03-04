from typing import Dict
from ollama import Client
from ollama import ChatResponse
from typing import Optional
from pydantic import BaseModel


class ModelBase:
    def __init__(self, model_name: str, options: Dict, client_url: str) -> None:
        self.__model_name = model_name
        self.__model_options = options
        self.__client = Client(host=client_url)

    def send_request(self, ResponseFormat: Optional[BaseModel], messages):
        """
        Helper function to send requests to the LLM model
        """
        if ResponseFormat:
            response: ChatResponse = self.__client.chat(
                model=self.__model_name,
                messages=messages,
                options=self.__model_options,
                format=ResponseFormat.model_json_schema(),
            )
        else:
            response: ChatResponse = self.__client.chat(
                model=self.__model_name, messages=messages, options=self.__model_options
            )
        return response
