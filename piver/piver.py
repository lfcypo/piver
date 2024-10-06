import os

from piver.options import ConfigOptions
from piver.store import Store
from piver.util import search_file, parse, get_file_extension

options = ConfigOptions()
store = Store()

def reset():
    """
    Resets the config options and store.
    :return:
    """
    global options, store
    options = ConfigOptions()
    store = Store()


def set_config_type(config_type: str):
    """
    Sets the config type for the current session.
    :param config_type: The type of config file to use.
    :return: None
    """
    options.set_config_type(config_type)


def add_config_path(path: str, is_recursion: bool = False):
    """
    Adds a path to the search path for config files.
    :param path: The full path to the config file.
    :param is_recursion: Whether to recursively search for config files.
    :return: None
    """
    options.add_config_path(path, is_recursion)


def set_config_file(file: str):
    """
    explicitly defines the path, name and extension of the config file.
    piver will use this and not check any of the config paths.
    :param file:
    :return:
    """
    options.set_config_file(file)


def set_config_encoding(encoding: str):
    """
    Sets the encoding of the config file.
    :param encoding: The encoding of the config file.
    :return: None
    """
    options.set_config_encoding(encoding)


def set_config_name(name: str):
    """
    Sets the name of the config file to use.
    :param name: The name of the config file to use.
    :return: None
    """
    options.set_config_name(name)


def set_env_prefix(prefix: str):
    """
    Sets the prefix for environment variables to use.
    :param prefix: The prefix for environment variables to use.
    :return: None
    """
    automatic_env()
    options.set_env_prefix(prefix)

def automatic_env():
    """
    Reads in the config from environment variables.
    :return: None
    """
    options.automatic_env()

def automatic_args():
    """
    Reads in the config from command line arguments.
    :return: None
    """
    options.automatic_args()


def read_in_config():
    """
    Reads in the config file and sets the options accordingly.
    :return: None
    """
    if options.config_type == "":
        raise ValueError("Config type not set. Please use set_config_type() to set the config type.")
    if not options.dirct_config_path:
        config_paths = options.config_paths
        config_name = options.config_name
        config_type = get_file_extension(options.config_type)
        if config_paths == {}:
            config_paths = {"./": False}
        for config_path in config_paths.keys():
            config_file_full_path = search_file(config_name + config_type, config_path, config_paths[config_path])
            if config_file_full_path:
                break
        else:
            raise FileNotFoundError(f"Config file \"{config_name + config_type}\" not found in any of the search paths: {list(config_paths.keys())}")
    else:
        config_file_full_path = os.path.join(list(options.config_paths.keys())[0], options.config_name)

    with open(config_file_full_path, "r", encoding=options.config_file_encoding or "utf-8") as config_file:
        config_data = config_file.read()

    # load
    store.store = parse(options, config_data)


def get(k: str, default=None):
    """
    Get a value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The value for the key, or the default value if the key is not found.
    """
    return store.get(k, default)


def get_str(k: str, default=None) -> str:
    """
    Get a string value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The string value for the key, or the default value if the key is not found.
    """
    return store.get_str(k, default)


def get_int(k: str, default=None) -> int:
    """
    Get an integer value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The integer value for the key, or the default value if the key is not found.
    """
    return store.get_int(k, default)


def get_float(k: str, default=None) -> float:
    """
    Get a float value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The float value for the key, or the default value if the key is not found.
    """
    return store.get_float(k, default)


def get_bool(k: str, default=None) -> bool:
    """
    Get a boolean value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The boolean value for the key, or the default value if the key is not found.
    """
    return store.get_bool(k, default)


def get_list(k: str, default=None) -> list:
    """
    Get a list value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The list value for the key, or the default value if the key is not found.
    """
    return store.get_list(k, default)


def get_dict(k: str, default=None) -> dict:
    """
    Get a dictionary value from the config.
    :param k: The key to get the value for.
    :param default: Default value to return if the key is not found.
    :return: The dictionary value for the key, or the default value if the key is not found.
    """
    return store.get_dict(k, default)


def set(k: str, v: any):
    """
    Set a value in the config.
    :param k: The key to set the value for.
    :param v: The value to set.
    """
    return store.set(k, v)
