#!/usr/bin/env python

import os
import setuptools


setuptools.setup(
  name='bumper-lib',
  version='0.1.1',

  author='Max Zheng',
  author_email='maxzheng.os @t gmail.com',

  description=open('README.rst').read(),

#  entry_points={
#    'console_scripts': [
#      'script_name = package.module:entry_callable',
#    ],
#  },

  install_requires=open('requirements.txt').read(),

  license='MIT',

  package_dir={'': 'src'},
  packages=setuptools.find_packages('src'),
  include_package_data=True,

  setup_requires=['setuptools-git'],

#  scripts=['bin/cast-example'],

  classifiers=[
    'Development Status :: 5 - Production/Stable',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Development Utilities',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
  ],

  keywords='library bump pin requirements requirements.txt pinned.txt',
)
