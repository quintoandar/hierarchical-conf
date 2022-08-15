# Hierarchical Conf


 Tool for retrieving configurations from (YAML) files according to the current
  environment and files precedence.

 It receives a list of paths to search the environment configuration files and load them
  overwriting redundant keys with the value of the last loaded one.
 It will search the files based on the operational system environment's variable `ENVIRONMENT`.

E.g.: Given the respective environments `dev` and `production` configuration files below:

 File dev_conf.yml:
 ```
     foo: bar_dev
     foo2: bar_dev2
 ```

 File production_conf.yml:
 ```
     foo: bar_prod
     foo2: bar_prod2
 ```

 and given we are at development environment (ENVIRONMENT=dev), the following code will load the
  configuration file from the development environment file (/my/path/dev_conf.yml).

 ```
     hconf = HierarchicalConf(conf_files_paths=['/my/path/'])
     foo_conf = hconf.get_config("foo")
     print(foo_conf)

     # prints: bar_dev
 ```

 Given `ENVIRONMENT=production`, the code above will load the configuration file from
 the production environment file (/my/path/production_conf.yml) and print bar_prod.

 For more examples, check the folder examples.

---

## Table of contents

- [Getting Started](#getting-started)
  - [Useful Commands](#useful-commands)

## Getting Started

We suggest using a virtual environment for python development, you will need to install:

1. [pyenv](https://github.com/pyenv/pyenv): Simple Python Version Management.
2. [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv): A plugin that provides features to manage virtualenvs.

With those packages installed, you need to:

Run `make environment`: this will create a virtual environment named `hierarchical-conf` with Python 3.7.3.

### Useful Commands

You should be all set with the correct environment. Now you can use any of the following commands:

- `make requirements`: will install all packages from requirements.txt and requirements.dev.txt.
- `make check-lint`: will run pylint.
- `make tests`: will run all tests (unit and integration).

For more commands, you can check the project's [Makefile](./Makefile).

## Built With

- [Python](https://www.python.org/) - Programming language
- [Pylint](https://www.pylint.org/) - Python linter which checks the source code and also acts as a bug and quality checker. It has more verification checks and options than just PEP8(Python style guide).
- [Black](https://black.readthedocs.io/en/stable/) - Python code auto-formatter. Black reformats entire files in place and also formats the strings to have double-qoutes.
- [Sonarqube](https://www.sonarqube.org/) - Provides the capability to not only show the health of an application but also to highlight issues newly introduced. Executed automatically during deploys.
- [Sphinx](https://www.sphinx-doc.org/en/master/) - Tool that makes it easy to create intelligent and beautiful documentation.
