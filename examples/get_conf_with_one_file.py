"""
Loading confs from some conf file.

To test this script you must create a conf file and place in path1.
"""

from quintoandar_hierarchical_conf.hierarchical_conf import HierarchicalConf

# Assuming you are running it in development environment, then you must
# have assigned the OS variable ENVIROMENT. E.g.: `export ENVIRONMENT="dev"`

# 1. Define where your configurations will be placed.
# Let's say you placed it at the folder global_conf in the project's root:
path1 = "your_project_root_path/global_conf/"

# You must declare this path in instantiation
hconf = HierarchicalConf(searched_paths=[path1])

# The lib searched for the file `your_project_root_path/global_conf/dev_conf.yml`

# 2. After instantiating the HConf, you can get the configs you desire:
conf = hconf.get_config("foo")
print(conf)

# When your code runs in another environment, the respective environment file will be loaded
# Therefore, there must be one file per environment, else an error will be raised.
