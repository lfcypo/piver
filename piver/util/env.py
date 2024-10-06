from typing import Dict
import os

def get_env(prefix: str) -> Dict[str, any]:
    """
    Get environment variables with a specific prefix.
    :param prefix:
    :return:
    """
    env = {}
    for key, value in os.environ.items():
        if key.startswith(prefix):
            env[key] = value
    return env
