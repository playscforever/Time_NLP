#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 15:10
# @Author  : zhm
# @File    : setup.py.py
# @Software: PyCharm
# @Changed : tianyuningmou

from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chinatime",
    version="1.0.7",
    keywords=("time", "nlp", "china"),
    description="Analysis China time in sentence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/playscforever/Time_NLP",
    author="playSCforever",
    author_email="playSCforever@gmail.com",
    packages=['cntm', 'tests'],
    package_data={'cntm': ['resource/*.json', 'resource/*.pkl', 'resource/*.txt']},
    include_package_data=True,
    platforms="any",
    install_requires=['regex>=2017',
                      'arrow>=0.10'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
