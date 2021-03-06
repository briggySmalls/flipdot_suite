#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pillow',
    'darkskylib',
    'geocoder',
    'pyserial',
    'grpcio',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Sam Briggs",
    author_email='briggySmalls90@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Smart Hanover flipdot sign powered by Google Assistant",
    entry_points={
        'console_scripts': [
            'flipapps=flipapps.flipapps:main',
            'flipdot_assistant=flipdot_assistant.flipdot_assistant:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='flipapps',
    name='flipapps',
    packages=find_packages(include=['flipapps']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/briggySmalls/flipapps',
    version='0.1.0',
    zip_safe=False,
)
