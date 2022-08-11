from unittest import mock

import pytest

<<<<<<< HEAD
from hierarchical_conf.hierarchical_conf import HierarchicalConf
=======
from quintoandar_hierarchical_conf.hierarchical_conf import HierarchicalConf
>>>>>>> 44377d5 (Add unit tests)


@pytest.fixture()
@mock.patch.object(HierarchicalConf, "_validate_if_config_file_exists")
@mock.patch.object(HierarchicalConf, "_read_configuration")
def hierarchical_conf(mock_read_configuration, mock_validate_if_config_file_exists):
    return HierarchicalConf(searched_paths=[mock.ANY])
