# Hierarchical Conf

Service to retrieve configuration variables from YAML files and enable their access
    according to priority rules based on the scope on which each variable was set, with
    `general` scope as the lowest priority rule and `DAG` or `Spark Job` scopes as the
    highest ones. The environment affects the selection of each variable as well, requiring
    all variables to be replicated in each environment in order to be retrieved and used.
    To override the configuration variables defined in the general scope, we just need
    to use the same key, nested or not, in the DAG or Spark Job scope. For example:

---

## Table of contents

- [Getting Started](#getting-started)
  - [Useful Commands](#useful-commands)
  - [Known issues](#known-issues)
- [Folder structure](#folder-structure)

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
