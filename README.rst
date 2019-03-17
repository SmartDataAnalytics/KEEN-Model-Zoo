KEEN Model Zoo
==============
A model zoo for the KEEN-Universe

Installation
------------
Preparing MongoDB
~~~~~~~~~~~~~~~~~
The web application relies on `MongoDB <https://www.mongodb.com/>`_ which can be installed with
``brew`` on Mac with:

.. code-block:: bash

   $ brew install mongodb

A test database can be instantiated in the ``mongo`` shell with:

.. code-block:: bash

   $ use test

Preparing Python
~~~~~~~~~~~~~~~~
This code requires ``pipenv`` for installation:

.. code-block:: bash

   $ pip install pipenv
   $ pipenv install
   $ pipenv update

Running
-------
Locally
~~~~~~~
.. code-block:: bash

   $ pipenv run python zoo.py run

Inside Docker
-------------
There is included a `Dockerfile` and docker-compose configuration. This is currently
under development and doesn't work yet.

The app can be run on port 80 with docker with:

.. code-block:: bash

   $ docker-compose up
