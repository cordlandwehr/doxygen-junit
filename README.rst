doxygen JUnit Converter
=======================

.. image:: https://travis-ci.org/johnthagen/doxygen-junit.svg
    :target: https://travis-ci.org/johnthagen/doxygen-junit

.. image:: https://codeclimate.com/github/johnthagen/doxygen-junit/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/doxygen-junit

.. image:: https://codeclimate.com/github/johnthagen/doxygen-junit/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/doxygen-junit

.. image:: https://codecov.io/github/johnthagen/doxygen-junit/coverage.svg
    :target: https://codecov.io/github/johnthagen/doxygen-junit

.. image:: https://img.shields.io/pypi/v/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/status/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/pyversions/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit/

.. image:: https://img.shields.io/pypi/dm/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit/

Tool that converts `doxygen <http://www.stack.nl/~dimitri/doxygen/>`_ XML output to JUnit XML format.
Use on your CI servers to get more helpful feedback.

Installation
------------

You can install, upgrade, and uninstall ``doxygen-junit`` with these commands:

.. code:: shell-session

    $ pip install doxygen-junit
    $ pip install --upgrade doxygen-junit
    $ pip uninstall doxygen-junit

Usage
-----
Redirect ``doxygen`` ``stderr`` to a file:

.. code:: shell-session

    $ doxygen 2> doxygen-stderr.txt

Convert it to JUnit XML format:

.. code:: shell-session

    $ doxygen_junit --input doxygen-stderr.txt --output doxygen-junit.xml

Contributors
------------

Credit to `@theandrewdavis <https://github.com/theandrewdavis>`_ for the initial development of
the conversion tool.


Releases
--------

1.1.0 - 2016-12-31
^^^^^^^^^^^^^^^^^^

Support Python 3.6.

1.0.1 - 2016-10-06
^^^^^^^^^^^^^^^^^^

Handle warning labels without a space before the preceding colon.

1.0.0 - 2016-09-13
^^^^^^^^^^^^^^^^^^

First release.
