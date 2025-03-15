import logging
from openai import OpenAI
from typing import Optional
from pydantic import BaseModel
from pprint import pprint

logger = logging.getLogger("fastapi")


class OpenAiModel:
    def __init__(self, model_name: str, openai_key: str) -> None:
        self.__model_name = model_name
        self.__client = OpenAI(api_key=openai_key)
        self.__logger = logging.getLogger("celery")

    def send_request(self, messages, ResponseFormat: Optional[BaseModel] = None):
        """
        Helper function to send requests to the LLM model
        """
        try:
            if ResponseFormat:
                response = self.__client.chat.completions.create(
                    model=self.__model_name, messages=messages, format=ResponseFormat
                )
            else:
                response = self.__client.chat.completions.create(
                    model=self.__model_name,
                    messages=messages,
                )
            return response
        except Exception as e:
            # Retry request if failed
            self.__logger.error("Bhasad!")
            raise e
            # if ResponseFormat:
            #     response = self.__client.chat.completions.create(
            #         model=self.__model_name, messages=messages, format=ResponseFormat
            #     )
            # else:
            #     response = self.__client.chat.completions.create(
            #         model=self.__model_name,
            #         messages=messages,
            #     )
            # return response


if __name__ == "__main__":
    openai_key = "DkLut8zrLq2gMBNuAfFVYgN8M4Mpnr8b78cizi3Fr6RI2cPHrPOBJQQJ99AJACfhMk5XJ3w3AAABACOGispl"
    model = OpenAiModel("gpt-4o", openai_key)
    messages = [{"role": "user", "content": "This is a test message."}]
    resp = model.send_request(messages=messages)
    pprint(resp)
