from typing import List, Dict

from piver.util.env import get_env

import copy

def parse_args(args: List[str]) -> Dict[str, any]:
    """
    Parse command line arguments in the format '-key value'.
    :param args: List of command line arguments.
    :return: Dictionary of parsed arguments.
    """
    parsed_args = {}
    i = 0

    while i < len(args):
        arg = args[i]
        if arg.startswith('-') and (i + 1) < len(args):
            key = arg[1:]
            value = args[i + 1]
            parsed_args[key] = value
            i += 2
        else:
            raise ValueError(f"Argument '{arg}' is not in the '-key value' format.")

    return parsed_args


def parse_env(prefix: str) -> Dict[str, any]:
    """
    Parse environment variables.
    :param prefix: Suffix of environment variables.
    :return: Dictionary of parsed environment variables.
    """
    return get_env(prefix)


def parse_file(content: str, f_type: str) -> Dict[str, any]:
    """
    Parse file contents.
    :param content: File contents.
    :param f_type: Type of file.
    :return: Dictionary of parsed file contents.
    """
    # TODO: Add support for more file types
    if f_type == "json":
        import json
        return json.loads(content)
    elif f_type == "yaml":
        import yaml
        return yaml.load(content, Loader=yaml.FullLoader)
    elif f_type == "toml":
        import toml
        return toml.loads(content)
    else:
        raise ValueError(f"Unsupported file type: {f_type}")


def parse(options, content: str) -> Dict[str, any]:
    """
    Parse file contents.
    :param options: Config options.
    :param content: Config File contents.
    :return: Dictionary of parsed file contents.
    """
    result = {}

    """
    # // The priority of the sources is the following:
    # // 2. flags
    # // 3. env. variables
    # // 4. config file
    # // 6. defaults
    """  # just like viper for golang :)

    result.update(parse_file(content, options.config_type))

    if options.from_env:
        envs = parse_env(options.env_prefix)
        envs_copy = copy.deepcopy(envs)
        for key, value in envs_copy.items():
            del envs[key]
            clean_key = key[len(options.env_prefix):].lower()
            keys = clean_key.split('_')
            current = envs
            for part in keys[:-1]:
                current = current.setdefault(part, {})
            current[keys[-1]] = value
        result.update(envs)
        del envs_copy

    if options.from_args:
        result.update(parse_args(options.args))

    return result
