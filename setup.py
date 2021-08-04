# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in visitor_management/__init__.py
from visitor_management import __version__ as version

setup(
	name='visitor_management',
	version=version,
	description='Visitor Management',
	author='Yamaan',
	author_email='aymenit2008@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
