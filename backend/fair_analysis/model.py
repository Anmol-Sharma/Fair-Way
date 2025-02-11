from typing import Dict
from ollama import Client
from ollama import ChatResponse


class ModelBase:

    def __init__(self, model_name: str, options: Dict, client_url: str) -> None:
        self.__model_name = model_name
        self.__model_options = options
        self.__client = Client(host=client_url)

    def send_request(self, ResponseFormat, messages, available_functions=[]):
        """
        Steps:-
          3. Once Test finishes create final summary either on chunks or full contents
        """
        response: ChatResponse = self.__client.chat(
            model=self.__model_name,
            messages=messages,
            options=self.__model_options,
            format=ResponseFormat.model_json_schema(),
            tools=available_functions,
        )
        return response
