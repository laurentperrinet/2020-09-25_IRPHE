#!/usr/bin/env python3
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

NAME = "slides"
version = "0.2"

setup(
    name = NAME,
    version = version,
    packages=find_packages('src', exclude='docs'),
    py_modules = ['slides'],
    install_requires=['numpy'],
    package_dir = {'': 'slides'},
    author = "Laurent Perrinet INT - CNRS",
    author_email = "Laurent.Perrinet@univ-amu.fr",
    description = " **slides.py** is a framework to programmatically generate presentations.",
    license = "GPLv2",
    keywords = ('computational neuroscience', 'simulation', 'analysis', 'visualization', 'parameters'),
    url = 'https://github.com/laurentperrinet/' + NAME, # use the URL to the github repo
    download_url = 'https://github.com/laurentperrinet/' + NAME + '/tarball/' + version,
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                  ],
     )
