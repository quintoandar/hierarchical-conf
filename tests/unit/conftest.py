from unittest import mock

import pytest

from hierarchical_conf.hierarchical_conf import HierarchicalConf


@pytest.fixture()
@mock.patch.object(HierarchicalConf, "_config_file_exists")
@mock.patch.object(HierarchicalConf, "_read_configuration")
def hierarchical_conf(mock_read_configuration, mock_config_file_exists):
    return HierarchicalConf(searched_paths=[mock.ANY])
