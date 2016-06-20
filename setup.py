#!/usr/bin/env python

import re
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    version = ''
    with open('grimreaper.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            fd.read(), re.MULTILINE).group(1)

    if not version:
        raise RuntimeError("Cannot find version's information")
    return version


def get_long_description():
    with open('README.rst', 'r', 'utf-8') as f:
        readme = f.read()

    with open('CHANGES.rst', 'r', 'utf-8') as f:
        changes = f.read()

    return readme + '\n\n' + changes

setup(
    name='GrimReapersPie',
    version=get_version(),
    description='Python client to the GrimReaper process killer.',
    long_description=get_long_description(),
    author='Mateusz Pawlik',
    author_email='matee+grimreaperspie@matee.net',
    url='https://github.com/matee911/GrimReapersPie',
    py_modules=['grimreaper'],
    package_data={'': ['LICENSE', 'CHANGES.rst', 'README.rst']},
    license='Apache 2.0',
    keywords='management',
    classifiers=(
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ),
)
