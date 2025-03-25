from ollama import Client
from ollama import ChatResponse
from typing import Optional, List, Dict
from httpx import ReadTimeout
from pydantic import BaseModel
import logging
from openai import OpenAI
from time import sleep
import openai


class OllamaModel:
    def __init__(
        self, model_name: str, options: Dict, client_url: str, keep_alive: str
    ) -> None:
        self.__model_name = model_name
        self.__model_options = options
        self.__client = Client(host=client_url, timeout=75.0)
        self.__logger = logging.getLogger("celery")
        self.__keep_alive = keep_alive

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
                options=self.__model_options,
                format=ResponseFormat,
                keep_alive=self.__keep_alive,
            )
            return response["message"]["content"]
        except ReadTimeout:
            # Retry request if failed
            self.__logger.warning("Request Timedout Retrying!")
            response: ChatResponse = self.__client.chat(
                model=self.__model_name,
                messages=messages,
                options=self.__model_options,
                format=ResponseFormat,
                keep_alive=self.__keep_alive,
            )
            return response["message"]["content"]
        except Exception as e:
            self.__logger.warning("Something Unexpected happened!")
            raise e


class OpenAiModel:
    def __init__(
        self,
        model_name: str,
        openai_key: str,
        temperature: float,
        top_p: Optional[float] = None,
    ) -> None:
        self.__model_name = model_name
        self.__client = OpenAI(api_key=openai_key)
        self.__logger = logging.getLogger("celery")
        self.temp = temperature
        self.top_p = top_p

    def send_request(self, messages, ResponseFormat: Optional[BaseModel] = None):
        """
        Helper function to send requests to the LLM model
        """
        retries = 3  # Set number of retries
        backoff = 5  # Initial backoff time in seconds

        for attempt in range(retries):
            try:
                response = self.__client.beta.chat.completions.parse(
                    model=self.__model_name,
                    messages=messages,
                    temperature=self.temp,
                    top_p=self.top_p,
                    response_format=ResponseFormat,
                )
                # Necessary sleep to still avoid 429 even with rate limit exceptions
                sleep(2.0)
                return response.choices[0].message.content
            except openai.RateLimitError:
                # Handle rate limit error Even with sleep delay (Very Rare Case but still have to be handled)
                self.__logger.warning(
                    f"Rate limit exceeded. Attempt {attempt + 1} of {retries}. Retrying in {backoff} seconds..."
                )
                sleep(backoff)
                backoff *= 2
            except Exception as e:
                # Handle other exceptions
                self.__logger.warning(
                    f"Something went wrong. Retrying! Error: {str(e)}"
                )
                sleep(2)  # Fixed wait time for errors

        # If we exhaust all retries, we raise an exception to indicate failure
        self.__logger.error("Max retries reached. Could not complete the request.")
        raise Exception("Max retries reached. Could not complete the request.")
