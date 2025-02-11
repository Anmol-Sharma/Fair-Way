#########################################################
# Define the class object for perform split operations  #
#########################################################
import json
import xml.etree.ElementTree as ET
from typing import List

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveJsonSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

from config import get_global_settings

global_settings = get_global_settings()

# TODO: Add logic logic to handle parsing errors for JSON, HTML, XML etc.


class Splitter:
    def __init__(
        self,
    ):
        global global_settings
        self.JSONSplitter = RecursiveJsonSplitter(
            max_chunk_size=global_settings["JSON_MAX_CHUNK_SIZE"],
            min_chunk_size=global_settings["JSON_MIN_CHUNK_SIZE"],
        )

        self.MDSplitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
            ]
        )

        self.PlainTextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=global_settings["TEXT_MAX_CHAR_COUNT"],
            chunk_overlap=10,
            length_function=len,
            is_separator_regex=False,
        )

        self.HTMLSplitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.HTML,
            chunk_size=global_settings["HTML_CHUNK_SIZE"],
            chunk_overlap=0,
        )

    def __split_xml(self, xml_content: str, min_size: int, max_size: int):
        """Helper function to perform splits on XML Content
        Args:
            xml_content: XML file contents
            min_size: minimum chunk size (in Bytes)
            max_size: maximum chunk size (in Bytes)
        Returns:
            list of chunks of XML content based defined limits
        """
        root = ET.fromstring(xml_content)
        elements = list(root)

        def recursive_split(elements, current_chunk=""):
            if not elements:
                return [current_chunk]
            element = elements[0]
            chunk_size = len(ET.tostring(element))

            # Check if adding this element exceeds max size
            if current_chunk and (len(current_chunk) + chunk_size) > max_size:
                return [current_chunk] + recursive_split(elements[1:], "")

            # Add the current element to the chunk
            current_chunk += ET.tostring(element).decode()

            # Check if the chunk meets min and max size criteria
            if len(current_chunk) >= min_size and len(current_chunk) <= max_size:
                return [current_chunk] + recursive_split(elements[1:], "")

            # Continue processing with the next element
            return recursive_split(elements[1:], current_chunk)

        chunks = recursive_split(elements)
        xml_chunks = []
        for chunk in chunks:
            if chunk.strip():  # Ensure non-empty chunks
                wrapped = f"<root>{chunk}</root>"
                xml_chunks.append(wrapped)

        return xml_chunks

    def split_file(
        self, file_type: str, file_size: str, file_content: str
    ) -> List[str]:
        """Helper function to perform splits on file content.
        Accepted File Types:- json, html, json-ld, xml, markdown, text
        Args:
            file_type: type of file contents
            file_size: size of the file (in Bytes)
            file_content: contents of the file
        Returns:
            list of chunks of content based defined limits and file type
        """
        chunks = None
        if file_type == "application/json" or file_type == "application/ld+json":
            chunks = self.JSONSplitter.split_json(json_data=json.loads(file_content))

        elif file_type == "text/html":
            chunks = self.HTMLSplitter.split_text(text=file_content)

        elif file_type == "text/xml":
            chunks = self.__split_xml(
                xml_content=file_content,
                min_size=global_settings["XML_MIN_CHUNK_SIZE"],
                max_size=global_settings["XML_MAX_CHUNK_SIZE"],
            )
        elif file_type in ["text/markdown", "text/x-markdown"]:
            chunks = self.MDSplitter.split_text(text=file_content)
        elif file_type == "text/plain":
            chunks = self.PlainTextSplitter.create_documents([file_content])
        else:
            raise Exception(f"File Type '{file_type}' Not yet Supported")

        return chunks
