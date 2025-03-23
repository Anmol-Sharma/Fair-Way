#######################################################
#  Define all the testing base classes necessary here #
#######################################################
from config import get_env_settings, get_global_settings
from typing import Sequence, Dict, Any, List
from inspect import cleandoc
import json
from abc import abstractmethod
from fair_analysis.model import OllamaModel

_env_settings = get_env_settings()
_global_settings = get_global_settings()


# Test Base Class
class BaseTest:
    SystemPrompt: str = (
        """You are a helpful assistant who will help with FAIR data assessment and metadata analysis. You are given metadata in various formats like json, json-ld, rdfs/xml and even plaintext or markdown and specific instructions on the tasks below. Analyze carefully and make sure to answer using given json format ONLY as you are interacting with a programming API and not a human. The format of the response to be returned will be provided to you explicitly and there may or may not be some examples for reference on how to perform a given Task."""
    )

    def __init__(
        self,
        name: str,
        feedback_format: str,
        test_main_cmd: str,
        test_instruction: str,
        few_shot_samples: Sequence[Dict[str, str]] = [],
        active: bool = True,
        use_few_shot_prompting: bool = True,
    ):
        self.test_name = name
        self.test_active = active
        self.__test_main_cmd = test_main_cmd
        self.test_feedback_format = feedback_format
        self.__test_instruction = test_instruction
        self.use_few_shot_prompting = use_few_shot_prompting

        if use_few_shot_prompting:
            self.__test_few_shot_examples = few_shot_samples
        else:
            self.__test_few_shot_examples = []

    def perform_test(
        self, model: OllamaModel, file_type: str, file_chunks: str
    ) -> Dict[str, str]:
        """Method to perform the given test
        Args:
            file_type: type of file contents
            file_content: contents of the file
        Returns:
            test results
        """

        # There will be a single chunk if there is no need to generate chunks
        if isinstance(file_chunks, list) and len(file_chunks) == 1:
            return self.__perform_test_on_full_contents(
                model, file_content=file_chunks[0], file_type=file_type
            )

        # More than one chunk, so perform operation on different chunks
        return self.__perform_test_on_chunks(
            model, chunks=file_chunks, file_type=file_type
        )

    def __perform_test_on_full_contents(
        self, model: OllamaModel, file_content: str, file_type: str
    ) -> Dict[str, str]:
        """Helper Method to perform the test on the whole file content
        Args:
            model: model created in the file fair_analysis.model.py file
            file_content: contents of the file
        Returns:
            test results
        """
        messages = self.__build_messages(file_content, file_type)

        response = model.send_request(
            messages=messages, ResponseFormat=self.test_feedback_format
        )

        return self.__parse_response(response=response)

    @abstractmethod
    def filter_chunk_results(
        self, chunk_results: List[Dict[str, str]]
    ) -> List[Dict[str, str]]:
        pass

    def __combine_chunk_results(
        self,
        model: OllamaModel,
        chunk_results,
        export_chunk_results: bool = False,
    ) -> Dict[str, str]:
        combine_prompt = f"""Here are some results for the test: '{self.test_name}' detected by you on different split sections of a metadata file. Combine them together in a single result. Key Steps:-
        1. Carefully analyze results, remove duplicate results and answer as precisely as possible which reflect the final result.
        2. If a test succeeded in one of the chunks, then the final result should be successful. If a test failed in all chunks ONLY then the result of the test should be false.
        3. Similarly if a key is empty in all but one chunk, then the test is a success and return the given key value.
        4. Avoid returning generic statements return back precise results and answer in the provided JSON format."""
        chunk_results = self.filter_chunk_results(chunk_results)
        messages = [
            {
                "role": _env_settings.role_user,
                "content": cleandoc(f"""{combine_prompt}\n{str(chunk_results)}"""),
            }
        ]

        response = model.send_request(
            messages=messages, ResponseFormat=self.test_feedback_format
        )
        feedback = self.__parse_response(response)

        # Decide on whether to export chunk results or not.
        if export_chunk_results:
            feedback["chunk_results"] = chunk_results

        return feedback

    def __perform_test_on_chunks(
        self, model: OllamaModel, chunks: Sequence[str], file_type: str
    ) -> Dict[str, str]:
        """Helper Method to perform the test on a sequence of file chunks
        Args:
            model: model created in the file fair_analysis.model.py file
            chunks: list of file Chunks
        Returns:
            test results
        """
        chunk_results = []
        for idx, chunk in enumerate(chunks):
            messages = self.__build_messages(chunk, file_type)
            response = model.send_request(
                messages=messages, ResponseFormat=self.test_feedback_format
            )
            chunk_results.append(self.__parse_response(response))

        # TODO: Check this after reading the paper by other student on techniques being used for passing back the results.
        chunk_results = self.filter_chunk_results(chunk_results)
        return self.__combine_chunk_results(model, chunk_results)

    def __build_messages(
        self, file_content: str, file_type: str
    ) -> List[Dict[str, Any]]:
        # For the very first message add the Main CMD to the list of samples
        messages = [
            {
                "role": "system",
                "content": f"""{self.SystemPrompt}\n{self.__test_main_cmd}\n""",
            }
        ]

        if self.use_few_shot_prompting:
            messages[0]["content"] += "Here are some examples showing how to do this.\n"
            for idx, example in enumerate(self.__test_few_shot_examples):
                messages.append(
                    {
                        "role": _env_settings.role_user,
                        "content": f"""{self.__test_instruction}\n{example["ex"]}""",
                    }
                )

                # Add the few shot feedback of Model
                messages.append(
                    {
                        "role": _env_settings.role_model,
                        "content": f"""{example["feedback"]}""",
                    }
                )

        # Add the actual test example to list of messages
        messages.append(
            {
                "role": _env_settings.role_user,
                "content": f"""{self.__test_instruction}\nThe provided file is of type `{file_type}` and here are its contents.\n```{file_content}```""",
            }
        )

        return messages

    def __parse_response(self, response) -> Dict[str, str]:
        """Helper Method to parse the response received back from LLM model.
        Args:
            response: response object from OLLAMA python API
        Returns:
            parsed json response
        """
        try:
            feedback = json.loads(response)
            return feedback
        except Exception as e:
            print(f"Error parsing the json response from the model: {response}")
            raise e
