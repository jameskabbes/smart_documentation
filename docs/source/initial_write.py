import sys
import os
sys.path.insert(0, os.path.abspath('../..'))
from project.load_config import instance

def write(file_name, mode, text):
    open(file_name, "w").close()
    f = open(file_name, mode)
    f.write(text)
    f.close()

index_file_name = 'index.rst'
index = f"""
Welcome to {instance.project_name.title()}
===================================

{instance.desc}

Check out the :doc:`usage` section for further information, including how to
:ref:`install <installation>` the project.

Contents
--------

.. toctree::

   usage
"""

for file_name in instance.files:
    i = file_name.rfind('.')
    plain_name = (file_name[i+1:])
    index += "   " + plain_name + "\n"

usage_file_name = 'usage.rst'
usage = f"""
Usage
=====

.. _installation:

Installation
------------

To use {instance.project_name.title()}, first install it using `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: console

   (.venv) $ pip install {instance.project_name}

Indices & Tables
----------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

active = """
.. note::

   This project is under active development.
"""

if instance.active:
    index += active

write(index_file_name, 'a', index)
write(usage_file_name, 'a', usage)

for file_name in instance.files:
    text = f""".. automodule:: {file_name}
    :members:
    """

    index = file_name.rfind('.')
    plain_name = (file_name[index+1:])
    
    write(plain_name + '.rst', 'a', text)