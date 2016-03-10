#!/usr/bin/env python3

import setuptools

import doxygen_junit


setuptools.setup(
    name='doxygen-junit',
    version=doxygen_junit.__version__,

    description='Converts doxygen errors and warnings to JUnit XML format.',
    long_description=open('README.rst').read(),
    keywords='doxygen C++ JUnit',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/doxygen-junit',
    license='MIT',

    py_modules=['doxygen_junit'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],

    scripts=['doxygen_junit.py'],

    entry_points={
        'console_scripts': [
            'doxygen_junit = doxygen_junit:main',
        ],
    }
)