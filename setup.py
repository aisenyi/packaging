# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in packaging/__init__.py
from packaging import __version__ as version

setup(
	name='packaging',
	version=version,
	description='packing slip',
	author='xyz',
	author_email='xyz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
