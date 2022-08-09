#!/usr/bin/env python

__package_name__ = "quintoandar_hierarchical_conf"
__version__ = "0.0.1"
__repository_url__ = "https://github.com/quintoandar/hierarchical-conf"

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = [line for line in f.read().splitlines() if len(line) > 0]

with open("requirements.dev.txt") as f:
    test_requirements = [line for line in f.read().splitlines() if len(line) > 0]

setup(
    name=__package_name__,
    description="A tool for loading settings from files hierarchically",
    long_description=readme,
    keywords="hierarchical-conf",
    version=__version__,
    url=__repository_url__,
    packages=find_packages(
        include=[
            "quintoandar_hierarchical_conf",
            "quintoandar_hierarchical_conf.*",
        ]
    ),
    author="QuintoAndar",
    install_requires=requirements,
    python_requires=">=3.7, <4",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    test_suite="tests",
    tests_require=test_requirements,
)
