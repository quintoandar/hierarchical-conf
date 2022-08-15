Hierarchical Conf
===========================
Made with |:heart:| by the **Data Engineering** team from `QuintoAndar <https://github.com/quintoandar/>`_.

A library for loading configurations (or other metadata) hierarchically based on the current environment.

How to use
----------

**Short**

An example of how to use the library getting configurations:

.. code-block:: python

    from hierarchical_conf.hierarchical_conf import HierarchicalConf

    hierarchical_conf = HierarchicalConf(searched_paths=[PROJECT_ROOT])
    my_config = hierarchical_conf.get_config("my_config_key")


**Long**

This tool retrieve the configurations from (YAML) files according to the current
environment and files precedence.

It receives a list of paths and searches each one for environment configuration files in an **orderly
fashion**, loading them when found and **overwriting duplicated** configuration keys by the value of the key
available in the file loaded at last.
The YAML configuration files are expected to be named with prefixes based on the working environment,
retrieved by the value of a pre-existent operational system environment's variable named ``ENVIRONMENT``.

E.g.: Given the respective environments ``dev`` and ``production`` configuration files below:

dev_conf.yml:

.. code-block:: yaml

    foo: bar_dev
    foo2: bar_dev2

production_conf.yml:

.. code-block:: yaml

    foo: bar_prod
    foo2: bar_prod2

and given we are at development environment (``ENVIRONMENT=dev``), the following code will load the
configuration file from the development environment file (``/my_path/dev_conf.yml``).

.. code-block:: python

    hconf = HierarchicalConf(conf_files_paths=['/my_path/'])
    foo_conf = hconf.get_config("foo")
    print(foo_conf)
    # prints: bar_dev

Given ``ENVIRONMENT=production``, the code above will load the configuration file from
the production environment file (``/my_path/production_conf.yml``) and print: ``bar_prod``.

To learn more use cases in practice (and about the keys overwriting), see `Hierarchical Conf examples <https://github.com/quintoandar/hierarchical-conf/tree/main/examples>`_.


Navigation
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   getstarted
   modules

