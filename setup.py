#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='procure',
        version='0.0.1',
        description='AWS server procurement',
        keywords = 'AWS',
        url='http://github.com/philipcristiano/procure',
        author='Philip Cristiano',
        author_email='philipcristiano@gmail.com',
        license='',
        packages=['procure'],
        install_requires=[
        ],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        entry_points="""
        [console_scripts]
        """,
    )

if __name__ == '__main__':
    run_setup()
