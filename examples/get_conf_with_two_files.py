"""
Loading confs from some conf file.

To test this script you must create the conf files and place them in path1 and path2.
"""

from hierarchical_conf.hierarchical_conf import HierarchicalConf

# Assuming you are running it in development environment, then you must
# have assigned the OS variable ENVIROMENT. E.g.: `export ENVIRONMENT="dev"`

# 1. Define where your configurations will be placed.
# Let's say you placed a GLOBAL configuration file at the folder global_conf in the project's root:
path1 = "your_project_root_path/global_conf"

# And let's say you defined one other specific configuration file for specific use:
path2 = "your_project_root_path/my_specific_scripts/"

# You must declare both paths in instantiation, according to the precedence:
hconf = HierarchicalConf(searched_paths=[path1, path2])

# The lib searched for the files:
#   `your_project_root_path/global_conf/dev_conf.yml` and `your_project_root_path/my_specific_scripts/dev_conf.yml`
# Since the second one is loaded lastly, their values will overwrite the keys if they exist in both.
# I.e.: if the key `s3_bucket` exists in the global confs and in the specifics one, then the value of the
#  my_specific_scripts/dev_conf.yml is the one which will be loaded.

# 2. After instantiating the HConf, you can get the configs you desire:
s3_bucket_name = hconf.get_config("s3_bucket")
print(s3_bucket_name)

# When your code runs in another environment, the respective environment file will be loaded
# Therefore, there must be one file per environment, else an error will be raised.
