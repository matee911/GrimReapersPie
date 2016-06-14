
==============
GrimReapersPie
==============


.. image:: https://img.shields.io/pypi/dm/GrimReapersPie.svg
.. image:: https://img.shields.io/pypi/v/GrimReapersPie.svg
.. image:: https://img.shields.io/github/tag/matee911/GrimReapersPie.svg
.. image:: https://img.shields.io/github/release/matee911/GrimReapersPie.svg
.. image:: https://img.shields.io/github/commits-since/matee911/GrimReapersPie/0.1.0a1.svg
.. image:: https://img.shields.io/pypi/pyversions/GrimReapersPie.svg
.. image:: https://img.shields.io/pypi/wheel/GrimReapersPie.svg
.. image:: https://img.shields.io/pypi/status/GrimReapersPie.svg
.. image:: https://img.shields.io/pypi/l/GrimReapersPie.svg
.. image:: https://codeclimate.com/repos/55f5e976e30ba07f94005456/badges/de9b8f237d1a71daab27/gpa.svg
   :target: https://codeclimate.com/repos/55f5e976e30ba07f94005456/feed
   :alt: Code Climate

.. image:: https://scrutinizer-ci.com/g/matee911/GrimReapersPie/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/matee911/GrimReapersPie/

.. image:: https://img.shields.io/github/issues/matee911/GrimReapersPie.svg
   :target: https://github.com/matee911/GrimReaper/issues

.. image:: https://img.shields.io/twitter/url/https/github.com/matee911/GrimReapersPie.svg?style=social
    :target: https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D

.. image:: https://img.shields.io/twitter/url/https/pypi.python.org/pypi/GrimReapersPie.svg?style=social
   :target: https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D



Introduction
============

The GrimReapersPie is an Apache2 Licensed library, written in python, to (un)register
long-running processes with the `GrimReaper`_.
Processes running longer than the time given during the registration, will be killed
by the `GrimReaper`_ daemon.

Prerequisites
=============

Install and run the `GrimReaper`_.


Installation
============

To install this library, simply:

.. code-block:: bash

    $ pip install --pre GrimReapersPie

Usage
=====

.. code-block:: python

   >>> from grimreaper import GrimReaper
   >>> grim_reaper = GrimReaper(process_timeout=5)  # set the global (default is 30s) timeout for 5 seconds
   >>> grim_reaper.register(timeout=10)  # or override the global timeout here
   # long-running job
   >>> grim_reaper.unregister()  # please, don't kill me, I had done my job before time has passed.

Contribution
============

Please see CONTRIBUTING.rst


.. _GrimReaper: http://github.com/matee911/GrimReaper
.. _flup: https://pypi.python.org/pypi/flup/1.0.2
