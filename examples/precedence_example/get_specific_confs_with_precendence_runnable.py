"""
Loading confs from example's conf files with precedence.

This script can be run to be tested.
"""
from os.path import dirname

from quintoandar_hierarchical_conf.hierarchical_conf import HierarchicalConf

# Assuming you are running it in development environment, then you must
#  have assigned the OS variable ENVIROMENT. E.g.: `export ENVIRONMENT="dev"`

# This will load the confs of examples/dev_conf.yml and examples/precedence_example/dev_conf.yml
#  and prioritize values of the second one if some key repeats.

# examples/dev_conf.yml
example_confs = dirname(dirname(__file__))

# examples/precedence_example/dev_conf.yml
specific_confs = dirname(__file__)

hconf = HierarchicalConf(searched_paths=[example_confs, specific_confs])
# Loaded  confs from both files

# 2. After instantiating the HConf, you can get the configs you desire:

# Got from examples/dev_conf.yml
key1 = hconf.get_config("key1")
print(key1)

# Got from examples/precedence_example/dev_conf.yml (priority loading)
key2 = hconf.get_config("key2")
print(key2)

# Got from examples/precedence_example/dev_conf.yml
key3 = hconf.get_config("key3")
print(key3)

# When your code runs in another environment, the respective environment file will be loaded
# Therefore, there must be one file per environment, else an error will be raised.
