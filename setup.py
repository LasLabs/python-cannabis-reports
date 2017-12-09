# -*- coding: utf-8 -*-
# Copyright 2016-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from setuptools import Command, setup
from setuptools import find_packages
from unittest import TestLoader, TextTestRunner

from os import path


PROJECT = 'cannabis-reports'
SHORT_DESC = 'This library allows you to interact with Cannabis Reports ' \
             'using Python.'
README_FILE = 'README.rst'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup_vals = {
    'name': PROJECT,
    'author': 'LasLabs Inc.',
    'author_email': 'support@laslabs.com',
    'description': SHORT_DESC,
    'url': 'https://laslabs.github.io/python-%s' % PROJECT,
    'download_url': 'https://github.com/LasLabs/python-%s' % PROJECT,
    'license': 'MIT',
    'classifiers': CLASSIFIERS,
}


if path.exists(README_FILE):
    with open(README_FILE) as fh:
        setup_vals['long_description'] = fh.read()


class FailTestException(Exception):
    """ It provides a failing build """
    pass


class Tests(Command):
    """ Run test & coverage, save reports as XML """

    user_options = []  # < For Command API compatibility

    def initialize_options(self, ):
        pass

    def finalize_options(self, ):
        pass

    def run(self, ):
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = TextTestRunner(verbosity=1)
        res = t.run(tests)
        if not res.wasSuccessful():
            raise FailTestException()


if __name__ == "__main__":
    setup(
        packages=find_packages(exclude='tests'),
        use_scm_version=True,
        cmdclass={'test': Tests},
        install_requires=[
            'properties',
            'pytz',
            'requests',
        ],
        setup_requires=[
            'setuptools_scm',
        ],
        tests_require=[
            'mock',
            'vcrpy',
        ],
        **setup_vals
    )
