==============
GrimReapersPie
==============

Introduction
------------

The GrimReapersPie is an Apache2 Licensed library, written in python, to (un)register
long-running processes with the `GrimReaper`_.
Processes running longer than, the time given during the registration, will be killed
by the `GrimReaper`_ daemon.

Prerequisites
-------------

Install and run the `GrimReaper`_.


Installation
------------

To install this library, simply:

.. code-block:: bash

    $ pip install GrimReaperPie

Usage
-----

.. code-block:: python

   >>> from grimreaper import GrimReaper
   >>> grim_reaper = GrimReaper(process_timeout=5)  # set the global (default is 30s) timeout for 5 seconds
   >>> grim_reaper.register(timeout=10)  # or override the global timeout here
   # long-running job
   >>> grim_reaper.unregister()  # please, don't kill me, I had done my job before time has passed.

Contribution
------------

Please see CONTRIBUTING.rst


.. _GrimReaper: http://github.com/matee911/GrimReaper
.. _flup: https://pypi.python.org/pypi/flup/1.0.2
