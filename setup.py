from setuptools import setup, find_packages

__package_name__ = "hierarchical_conf"
__version__ = "1.0.2"
__repository_url__ = "https://github.com/quintoandar/hierarchical-conf"


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = [line for line in f.read().splitlines() if len(line) > 0]

with open("requirements.test.txt") as f:
    test_requirements = [line for line in f.read().splitlines() if len(line) > 0]

setup(
    name=__package_name__,
    description="A tool for loading settings from files hierarchically",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=[
        "hierarchical-conf",
        "configuration by environment",
        "configuration files",
        "configuration as code",
        "hierarchical configuration",
    ],
    version=__version__,
    url=__repository_url__,
    packages=find_packages(
        include=[
            "hierarchical_conf",
            "hierarchical_conf.*",
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
