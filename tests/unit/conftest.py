from unittest import mock

import pytest

from quintoandar_hierarchical_conf.hierarchical_conf import HierarchicalConf


@pytest.fixture()
@mock.patch.object(HierarchicalConf, "_validate_if_config_file_exists")
@mock.patch.object(HierarchicalConf, "_read_configuration")
def hierarchical_conf(mock_read_configuration, mock_validate_if_config_file_exists):
    return HierarchicalConf(searched_paths=[mock.ANY])
