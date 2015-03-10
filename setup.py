#!/usr/bin/env python

# Setup script for the `preview-markup' package.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 10, 2015
# URL: https://github.com/xolox/python-preview-markup

import os
import re
import setuptools
import sys

# Find the directory where the source distribution was unpacked.
source_directory = os.path.dirname(os.path.abspath(__file__))

# Add the directory with the source distribution to the search path.
sys.path.append(source_directory)

# Import the module to find the version number (this is safe to do because we
# don't import any external dependencies from preview_markup/__init__.py).
from preview_markup import __version__ as version_string

# Fill in the long description (for the benefit of PyPI)
# with the contents of README.rst (rendered by GitHub).
readme_file = os.path.join(source_directory, 'README.rst')
readme_text = open(readme_file, 'r').read()

# Fill in the installation requirements based on requirements.txt.
requirements_file = os.path.join(source_directory, 'requirements.txt')
requirements = list(filter(None, (re.sub('^\s*#.*|\s#.*', '', line).strip() for line in open(requirements_file))))

setuptools.setup(
    name='preview-markup',
    version=version_string,
    description="Live preview Markdown and reStructuredText files as HTML in a web browser",
    long_description=readme_text,
    url='https://github.com/xolox/python-preview-markup',
    author="Peter Odding",
    author_email='peter@peterodding.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points=dict(console_scripts=['preview-markup = preview_markup.cli:main']),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities'])
