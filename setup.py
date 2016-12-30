#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import os
import sys
import codecs

from setuptools import setup

try:
    from os import dirname
except ImportError:
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

if sys.argv[-1] == "publish":
    os.system("Python setup.py sdist bdist_wheel upload")
    sys.exit()

required = [
    'datetime',
    'time',
    'tzlocal',
]

setup(
    name='humantime',
    version='0.0.2',
    description='Datetime By myself',
    long_description=long_description,
    author='uzjY',
    author_email='qiufeng****@gmail.com',
    url='htpps://zider.github.io',
    py_modules=['humantime'],
    install_requires=required,
    license='MIT',
    classifiers=(),
        )
