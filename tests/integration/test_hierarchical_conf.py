import os
from os.path import dirname
from unittest import mock

from hierarchical_conf.hierarchical_conf import HierarchicalConf


class TestHierarchicalConf:
    @mock.patch.dict(os.environ, {"ENVIRONMENT": "integration_env"})
    def test_load_confs(self):
        # arrange
        expected_confs = {
            "key1": "value of key1...",
            "key2": "value of key2...",
            "key3": "value of key3...",
        }
        integration_tests_folder = dirname(__file__)

        # act
        hierarchical_conf = HierarchicalConf(searched_paths=[integration_tests_folder])

        # assert
        assert hierarchical_conf.configs == expected_confs

    @mock.patch.dict(os.environ, {"ENVIRONMENT": "integration_env"})
    def test_load_confs(self):
        # arrange
        expected_confs = {
            "key1": "value of key1...",
            "key2": "This is another value from "
            "precedence_example/integration_env_conf.yml...",
            "key3": {"foo": "new value of key3.foo"},
        }
        integration_tests_folder = dirname(__file__)
        precedence_case_folder = dirname(__file__) + "/precedence_case/"

        # act
        hierarchical_conf = HierarchicalConf(
            searched_paths=[integration_tests_folder, precedence_case_folder]
        )

        # assert
        assert hierarchical_conf.configs == expected_confs
