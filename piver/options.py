import os.path as osp
import sys
from typing import List, Dict

from piver.util import get_file_type, file_type_mapping


class ConfigOptions:
    def __init__(self):
        self.config_type: str = ""
        self.config_name: str = ""
        self.config_file_encoding: str = "utf-8"
        self.config_file_full_path: str = ""

        self.from_env: bool = False
        self.env_prefix: str = ""

        self.from_args: bool = False
        self.args: List[str] = sys.argv

        self.config_paths: Dict[str, bool] = {}
        self.dirct_config_path: bool = False

    def set_config_type(self, config_type: str):
        """
        Sets the config type for the current session.
        :param config_type: The type of config file to use.
        :return: None
        """
        config_type = config_type.lower()
        if config_type not in file_type_mapping.values():
            raise ValueError(f"Invalid config type: {config_type}")

        if self.config_type != "" and self.config_type != config_type:
            raise ValueError(f"Config type mismatch: {self.config_type} vs {config_type}")

        self.config_type = config_type

    def add_config_path(self, path: str, is_recursion: bool):
        """
        Adds a path to the search path for config files.
        :param path: The full path to the config file.
        :param is_recursion: Whether the config path should be recursive or not.
        :return: None
        """
        self.config_paths[path] = is_recursion


    def set_config_file(self, file: str):
        """
        Explicitly defines the path, name and extension of the config file.
        piver will use this and not check any of the config paths.
        :param file: The full path to the config file.
        :return: None
        """
        self.config_paths = {
            osp.dirname(file): False
        }
        self.config_name = osp.basename(file)
        self.config_type = get_file_type(file)
        self.dirct_config_path = True

    def set_config_name(self, name: str):
        """
        Sets the name of the config file to use.
        :param name: The name of the config file to use.
        :return: None
        """
        if name.find(".") != -1:
            base_name, _ = osp.splitext(name)

            file_type = get_file_type(name)
            if self.config_type != "" and self.config_type != file_type:
                raise ValueError(f"Config type mismatch: {self.config_type} vs {file_type}")

            self.config_type = file_type
            self.config_name = base_name
            return

        self.config_name = name

    def set_config_encoding(self, encoding: str):
        """
        Sets the encoding of the config file to use.
        :param encoding: The encoding of the config file to use.
        :return: None
        """
        self.config_file_encoding = encoding

    def set_env_prefix(self, prefix: str):
        """
        Sets the prefix for environment variables to use.
        :param prefix: The prefix for environment variables to use.
        :return: None
        """
        prefix = prefix.upper()
        if not prefix.endswith("_"):
            prefix = prefix + "_"
        self.env_prefix = prefix

    def automatic_env(self):
        """
        Sets the config to be loaded from environment variables.
        :return: None
        """
        self.from_env = True

    def automatic_args(self):
        """
        Sets the config to be loaded from command line arguments.
        :return: None
        """
        self.from_args = True
