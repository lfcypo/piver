from piver.exception import ConfigNotInitializedError

class Store:
    store: any = None

    def __check(self):
        if self.store is None:
            raise ConfigNotInitializedError("Config is not initialized. Please call piver.read_in_config() first.")

    def get(self, k: str, default=None) -> any:
        """
        Get a value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The value for the key, or the default value if the key is not found.
        """
        self.__check()
        keyStream = k.split(".")

        value = self.store
        for k in keyStream:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def get_str(self, k: str, default=None) -> str:
        """
        Get a string value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The string value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, str):
            return value
        else:
            try:
                return str(value)
            except ValueError:
                raise ValueError(f"Value {k} is not a string.")

    def get_int(self, k: str, default=None) -> int:
        """
        Get an integer value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The integer value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, int):
            return value
        else:
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Value {k} is not an integer.")

    def get_float(self, k: str, default=None) -> float:
        """
        Get a float value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The float value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, float):
            return value
        else:
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Value {k} is not a float.")

    def get_bool(self, k: str, default=None) -> bool:
        """
        Get a boolean value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The boolean value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        else:
            try:
                return bool(value)
            except ValueError:
                raise ValueError(f"Value {k} is not a boolean.")

    def get_list(self, k: str, default=None) -> list:
        """
        Get a list value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The list value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, list):
            return value
        else:
            try:
                return list(value)
            except ValueError:
                raise ValueError(f"Value {k} is not a list.")

    def get_dict(self, k: str, default=None) -> dict:
        """
        Get a dictionary value from the config.
        :param k: The key to get the value for.
        :param default: Default value to return if the key is not found.
        :return: The dictionary value for the key, or the default value if the key is not found.
        """
        value = self.get(k, default)
        if value is None:
            return default
        if isinstance(value, dict):
            return value
        else:
            try:
                return dict(value)
            except ValueError:
                raise ValueError(f"Value {k} is not a dictionary.")

    def set(self, k: str, v: any):
        """
        Set a value in the config.
        :param k: The key to set the value for.
        :param v: The value to set.
        """
        self.__check()
        keyStream = k.split(".")
        value = self.store
        for k in keyStream[:-1]:
            if k not in value:
                value[k] = {}
            value = value[k]
        value[keyStream[-1]] = v
