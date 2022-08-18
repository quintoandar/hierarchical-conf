"""Hierarchical Conf main class."""
import logging
import os
from collections.abc import Mapping
from os.path import isfile
from typing import Union, List, Dict, Any, Mapping as MappingType

import yaml


class HierarchicalConf:
    """User main interface with the lib operations."""

    def __init__(self, searched_paths: List[str]) -> None:
        """
        Searches for the configuration files and load their values.

        :param searched_paths: the list of paths where the conf files will be
         searched
        """
        self._config_file_name = f"{self._get_environment()}_conf.yml"
        self._configuration_files = self._search_configurations_files(searched_paths)
        self._configs = self._load_configurations_from_files()

    @property
    def configs(self) -> Dict[str, Union[str, List[Any], Dict[str, Any]]]:
        """Returns all loaded configurations."""
        return self._configs.copy()

    @property
    def _configuration_files(self) -> List[str]:
        """The configuration files."""
        return self.__configuration_files

    @_configuration_files.setter
    def _configuration_files(self, configuration_files: List[str]) -> None:
        """_configuration_files setter."""
        if not configuration_files:
            raise FileNotFoundError(
                "msg=No configuration file(s) found in the path(s) specified."
            )
        self.__configuration_files = configuration_files

    @staticmethod
    def _get_environment() -> str:
        env = os.environ.get("ENVIRONMENT")
        if not env:
            raise ValueError(
                "The required operational system variable `ENVIRONMENT` is not "
                "declared."
            )

        return env

    def _load_configurations_from_files(self) -> Dict[str, Any]:
        configs = {}  # type: ignore
        for config_file in self._configuration_files:
            conf_content = self._read_configuration(config_file)
            configs = self._deep_update(configs, conf_content)

        return configs

    def _search_configurations_files(self, searched_paths: List[str]) -> List[str]:
        """
        Search for the configuration files inside given directories.

        :param searched_paths: the list of paths where the conf files will be
         searched
        :return: an ordered list with the files.
        :raises: an exception if file is not found inside the directories.
        """
        configuration_files = []
        for path in searched_paths:
            environment_conf_file = f"{path}/{self._config_file_name}"
            if self._config_file_exists(environment_conf_file):
                configuration_files.append(environment_conf_file)
        return configuration_files

    @staticmethod
    def _config_file_exists(config_file_path: str) -> bool:
        """
        Checks if the configuration file path exists.

        :param config_file_path: the configuration file path
        """
        if isfile(config_file_path):
            return True

        logging.warning(
            f"msg=This configuration file was not found in the given path,"
            f"file={config_file_path}"
        )
        return False

    @staticmethod
    def _read_configuration(conf_file_path: str) -> Union[Any, Dict[str, Any]]:
        """
        Open files.

        :param conf_file_path: path to the configuration file
        :return: the contents of the configuration file
        """
        with open(conf_file_path) as f:
            return yaml.safe_load(f)

    def _deep_update(
        self, source: Dict[str, Any], overrides: MappingType[str, Any]
    ) -> Dict[str, Any]:
        """
        Updates the dicts given priority to the last loaded one.

        Update a nested dictionary or similar mapping.
        Modify `source` in place.

        For more examples check the folder examples.

        :param source: the nested dictionary to update
        :param overrides: the dictionary with overrides
        :return: the updated dictionary
        """
        for key, value in overrides.items():
            if isinstance(value, Mapping) and value:
                returned = self._deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    def get_config(self, key: str) -> Union[str, List[Any], Dict[str, Any]]:
        """
        Gets the value of a specific key.

        :returns: The key's value if exists
        :raises: error if key is invalid
        """
        if key not in self._configs:
            raise IndexError(
                f"configuration_key={key}, "
                f"env_configuration_files={self._configuration_files}, "
                "msg=Configuration is not registered in the configuration files."
            )

        return self.configs[key]
