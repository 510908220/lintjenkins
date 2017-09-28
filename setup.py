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
    # TODO: put package requirements here
    'jenkinsapi',
    'python-jenkins',
    'pyquery',
    'pendulum'
]

setup_requirements = [
    # TODO(510908220): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='lintjenkins',
    version='0.1.2',
    description="jenkins pylint api.",
    long_description=readme + '\n\n' + history,
    author="westdoorblowcola",
    author_email='510908220@qq.com',
    url='https://github.com/510908220/lintjenkins',
    packages=find_packages(include=['lintjenkins']),
    entry_points={
        'console_scripts': [
            'lintjenkins=lintjenkins.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='lintjenkins',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
