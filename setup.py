#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "requests",
    "psycopg2",
    "flask",
]

setup(
    name='traceroutedb',
    version='0.1.0',
    description="An experiment in full mesh historical traceroutes",
    author="Ryan Carter",
    author_email='ryan@cloudflare.com',
    url='https://github.com/eiginn/traceroutedb',
    packages=[
        'traceroutedb',
    ],
    entry_points='''
                 [console_scripts]
                 trdb=traceroutedb.main:cli_entry
                 ''',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
