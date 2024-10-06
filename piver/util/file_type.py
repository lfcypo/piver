import os
from typing import Dict, Optional

from piver.exception import UnknownFileTypeException

file_type_mapping: Dict[str, str] = {
    ".toml": "toml",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
}


def get_file_type(fullname: str) -> Optional[str]:
    """
    Get the file type of a file based on its extension.
    :param fullname:  The full name of the file.
    :return:  The file type.
    :raises UnknownFileTypeException: If the file type is not recognized.
    """

    _, ext = os.path.splitext(fullname)

    if not ext:
        return ""

    key = file_type_mapping.get(ext)

    if key is None:
        raise UnknownFileTypeException(
            f"{fullname} is not a valid file type, you can use set_config_type() to specify the type.")

    return key


def get_file_extension(file_type: str) -> str:
    """
    Get the file extension of a file based on its type.
    :param file_type:  The file type.
    :return:  The file extension.
    :raises UnknownFileTypeException: If the file type is not recognized.
    """
    for key, value in file_type_mapping.items():
        if value == file_type:
            return key
    raise UnknownFileTypeException(f"{file_type} is not a valid file type.")
