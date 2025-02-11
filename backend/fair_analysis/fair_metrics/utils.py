"""
"""
# TODO: Import all the necessary test from the test list and put under metric
# For all define metrics in global settings build up each metric
import os
import importlib

########################################
#    Define Tool Call Functions Here   #
########################################

def resolve_doi(doi:str)->bool:
    """
    Checks if the provided DOI is resolvable or not
    Args:
        doi (str): The DOI identifier

    Returns:
        bool: If the identifier was resolved or not
    """
    return False

def resolve_arxiv(id:str)->bool:
    """
    Checks if the provided arxiv link or id is resolvable or not

    Args:
        id (str): The arxiv identifier or link

    Returns:
        bool: If the identifier was resolved or not
    """

def resolve_url(url:str)->bool:
    """
    Checks if the provided link is resolvable or not

    Args:
        url (str): url to be checked

    Returns:
        bool: If the url was resolved or not
    """
    pass