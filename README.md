# Hierarchical Conf
_A library for loading configurations (or other metadata) hierarchically based on the current environment_

<img height="200" src="hierarchical_conf_logo.png" />

[![Release](https://img.shields.io/github/v/release/quintoandar/hierarchical-conf)]((https://pypi.org/project/hierarchical-conf/))
![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8-brightgreen.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

| Source    | Downloads                                                                                                       | Page                                                 | Installation Command                       |
|-----------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| **PyPi**  | [![PyPi Downloads](https://pepy.tech/badge/hierarchical-conf)](https://pypi.org/project/hierarchical-conf/) | [Link](https://pypi.org/project/hierarchical-conf/)        | `pip install hierarchical-conf `                  |

### Build status
| Develop                                                                     | Stable                                                                            | Documentation                                                                                                                                           | Sonar                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Test](https://github.com/quintoandar/hierarchical-conf/workflows/Test/badge.svg) | ![Publish](https://github.com/quintoandar/hierarchical-conf/workflows/Publish/badge.svg) | [![Documentation Status](https://readthedocs.org/projects/hierarchical-conf/badge/?version=latest)](https://hierarchical-conf.readthedocs.io/en/latest/?badge=latest) | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=quintoandar_hierarchical-conf&metric=alert_status)](https://sonarcloud.io/dashboard?id=quintoandar_hierarchical-conf) |


This library supports Python version 3.7+.

To check library main features you can check [Hierarchical Conf's Documentation](https://hierarchical-conf.readthedocs.io/en/latest/), which is hosted by Read the Docs.

### How to use

#### Short
An example of how to use the library getting configurations:

```python
from hierarchical_conf.hierarchical_conf import HierarchicalConf

hierarchical_conf = HierarchicalConf(searched_paths=[PROJECT_ROOT])
my_config = hierarchical_conf.get_config("my_config_key")
```

#### Long

This tool retrieve the configurations from (YAML) files according to the current
environment and files precedence.

It receives a list of paths and searches each one for environment configuration files in an **orderly 
fashion**, loading them when found and **overwriting duplicated** configuration keys by the value of the key 
available in the file loaded at last.
The YAML configuration files are expected to be named with prefixes based on the working environment, 
retrieved by the value of a pre-existent operational system environment's variable named `ENVIRONMENT`.


E.g.: Given the respective environments `dev` and `production` configuration files below:

dev_conf.yml:
```yaml
 foo: bar_dev
 foo2: bar_dev2
```

production_conf.yml:
```yaml
 foo: bar_prod
 foo2: bar_prod2
```

and given we are at development environment (`ENVIRONMENT=dev`), the following code will load the
configuration file from the development environment file (`/my_path/dev_conf.yml`).

```python
hconf = HierarchicalConf(conf_files_paths=['/my_path/'])
foo_conf = hconf.get_config("foo")
print(foo_conf)
# prints: bar_dev
```

Given `ENVIRONMENT=production`, the code above will load the configuration file from
the production environment file (`/my_path/production_conf.yml`) and print: `bar_prod`.

To learn more use cases in practice (and about the keys overwriting), see [Hierarchical Conf examples](https://github.com/quintoandar/hierarchical-conf/tree/main/examples)  

---

## Requirements and Installation
The Hierarchical Conf depends on **Python 3.7+**

[Python Package Index](https://pypi.org/project/hierarchical-conf/) hosts reference to a pip-installable module of this library, using it is as straightforward as including it on your project's requirements.

```bash
pip install hierarchical-conf
```

## License
[Apache License 2.0](https://github.com/quintoandar/hierarchical-conf/blob/main/LICENSE)

## Contributing
All contributions are welcome! Feel free to open Pull Requests. Check the development and contributing **guidelines** 
described in [CONTRIBUTING.md](https://github.com/quintoandar/hierarchical-conf/blob/main/CONTRIBUTING.md)

Made with :heart: by the **Data Engineering** team from [QuintoAndar](https://github.com/quintoandar/)
