"""Hierarchical Conf main class."""
import os
from unittest import mock

import pytest

from hierarchical_conf.hierarchical_conf import HierarchicalConf


class TestHierarchicalConf:
    @mock.patch.object(HierarchicalConf, "_load_configurations_from_files")
    @mock.patch.object(HierarchicalConf, "_search_configurations_files")
    @mock.patch.object(HierarchicalConf, "_get_environment")
    def test_init_object(
        self,
        mock_get_environment,
        mock_search_configurations_files,
        mock_load_configurations_from_files,
    ):
        # arrange
        env = "_dev_"
        path1 = "my_path_1"
        searched_paths = [path1]
        mock_get_environment.return_value = env

        # act
        hconf = HierarchicalConf(searched_paths=[path1])

        # assert
        mock_get_environment.assert_called_once_with()
        mock_search_configurations_files.assert_called_once_with(searched_paths)
        mock_load_configurations_from_files.assert_called_once_with()

    @mock.patch.object(HierarchicalConf, "_config_file_exists")
    @mock.patch.object(HierarchicalConf, "_read_configuration")
    def test_get_conf_with_one_file(
        self, mock_read_configuration, mock_config_file_exists
    ):
        # arrange
        expected_confs = {"key1": "val1", "key2": "val2"}
        first_file_confs = {"key1": "val1", "key2": "val2"}
        mock_read_configuration.return_value = "asdasd"
        mock_read_configuration.side_effect = [first_file_confs]

        # act
        hconf = HierarchicalConf(searched_paths=[mock.ANY])

        # assert
        assert hconf.configs == expected_confs

    @mock.patch.object(HierarchicalConf, "_config_file_exists")
    @mock.patch.object(HierarchicalConf, "_read_configuration")
    def test_get_conf_with_multiple_files(
        self, mock_read_configuration, mock_config_file_exists
    ):
        # arrange
        expected_confs = {
            "key1": "val1",
            "key2": "another value",
            "key3": "val3",
            "key4": "val4",
        }
        first_file_confs = {"key1": "val1", "key2": "val2", "key4": "val4"}
        second_file_confs = {"key2": "another value", "key3": "val3"}
        third_file_confs = {"key4": "val4"}

        mock_read_configuration.return_value = "asdasd"
        mock_read_configuration.side_effect = [
            first_file_confs,
            second_file_confs,
            third_file_confs,
        ]

        path1 = mock.ANY
        path2 = mock.ANY
        path3 = mock.ANY

        # act
        hconf = HierarchicalConf(searched_paths=[path1, path2, path3])

        # assert
        assert hconf.configs == expected_confs
        assert hconf.get_config("key2") == "another value"

    @mock.patch.object(HierarchicalConf, "_config_file_exists")
    @mock.patch.object(HierarchicalConf, "_read_configuration")
    def test_existent_config(self, mock_read_configuration, mock_config_file_exists):
        # arrange
        mock_configs = {"a": 1, "b": 2}

        # act
        hconf = HierarchicalConf(searched_paths=[mock.ANY])
        hconf._configs = mock_configs

        # assert
        assert hconf.get_config("a") == 1

    @mock.patch.object(HierarchicalConf, "_config_file_exists")
    @mock.patch.object(HierarchicalConf, "_read_configuration")
    def test_nonexistent_config(self, mock_read_configuration, mock_config_file_exists):
        # arrange
        mock_configs = {"a": 1, "b": 2}

        # act & assert
        hconf = HierarchicalConf(searched_paths=[mock.ANY])
        hconf._configs = mock_configs

        with pytest.raises(IndexError):
            hconf.get_config("c")

    @mock.patch("hierarchical_conf.hierarchical_conf.yaml")
    @mock.patch("builtins.open")
    def test__read_configuration(self, mock_open, mock_yaml, hierarchical_conf):
        # arrange
        file_path = "path"
        expected_content = "<content>"
        mock_yaml.safe_load.return_value = expected_content

        # act
        content = hierarchical_conf._read_configuration(file_path)

        # assert
        assert content == expected_content

    def test__config_file_exists_with_non_existent_file(self, hierarchical_conf):
        # arrange
        path = "some_path"

        # act
        returned_value = hierarchical_conf._config_file_exists(path)

        # assert
        assert not returned_value

    @mock.patch("hierarchical_conf.hierarchical_conf.isfile")
    def test__config_file_exists_with_file(self, mock_is_file, hierarchical_conf):
        # arrange
        path = ""
        mock_is_file.return_value = True

        # act
        returned_value = hierarchical_conf._config_file_exists(path)

        # assert
        assert returned_value
        mock_is_file.assert_called_once_with(path)

    @mock.patch.dict(os.environ, {}, clear=True)
    def test_invalid_enviroment(self, hierarchical_conf):
        # act & assert
        with pytest.raises(ValueError):
            hierarchical_conf._get_environment()

    def test_invalid_configuration_files(self):
        # act & assert
        with pytest.raises(FileNotFoundError) as e:
            HierarchicalConf(searched_paths=[])
        assert (
            str(e.value)
            == "msg=No configuration file(s) found in the path(s) specified."
        )

    def test_deep_update(self, hierarchical_conf):
        # arrange
        expected_value = {"key1": "val1", "key2": "new value", "key3": {"a": 1}}
        source = {
            "key1": "val1",
            "key2": "val2",
        }
        overrides = {"key2": "new value", "key3": {"a": 1}}

        # act
        returned_value = hierarchical_conf._deep_update(source, overrides)

        # assert
        assert returned_value == expected_value

    def test_deep_update_deleting_nulls(self, hierarchical_conf):
        # arrange
        expected_value = {"key2": "new value", "key3": {"a": 1}}
        source = {
            "key1": "val1",
            "key2": "val2",
        }
        overrides = {"key1": None, "key2": "new value", "key3": {"a": 1}}

        # act
        returned_value = hierarchical_conf._deep_update(source, overrides)

        # assert
        assert returned_value == expected_value
