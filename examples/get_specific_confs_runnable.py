"""
Loading confs from example's conf file.

This script can be run to be tested.
"""
from os.path import dirname

from hierarchical_conf.hierarchical_conf import HierarchicalConf

# Assuming you are running it in development environment, then you must
# have assigned the OS variable ENVIROMENT. E.g.: `export ENVIRONMENT="dev"`

this_file_folder = dirname(__file__)
hconf = HierarchicalConf(searched_paths=[this_file_folder])
# Loaded  confs from the file examples/dev_conf.yml

# 2. After instantiating the HConf, you can get the configs you desire:
s3_bucket_name = hconf.get_config("key2")
print(s3_bucket_name)

# When your code runs in another environment, the respective environment file will be loaded
# Therefore, there must be one file per environment, else an error will be raised.
