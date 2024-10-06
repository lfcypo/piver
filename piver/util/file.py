from typing import List
import os

def search_file(filename: str, search_path: str, is_recursion: bool = True) -> str:
    """
    Searches for a file in the specified directory and its subdirectories.

    :param is_recursion: Whether or not to search for subdirectories recursively.
    :param filename: The name of the file to search for.
    :param search_path: The path of the directory to search in.
    :return: The full path of the file if found, otherwise an empty string.
    """
    if not is_recursion:
        if filename in os.listdir(search_path):
            return os.path.join(search_path, filename)
        return ""

    # Recursively search for the file using os.walk
    for root, _, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return ""
