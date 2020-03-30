#!/usr/bin/env python

"""
Flask-HTMLmin
-------------

Minify flask text/html mime type responses
"""

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-HTMLmin',
    version='2.0.1',
    url='https://github.com/hamidfzm/Flask-HTMLmin',
    license='BSD-3-Clause',
    author='Hamid FzM',
    author_email='hamidfzm@gmail.com',
    description=__doc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['HTMLMIN'],
    packages=['flask_htmlmin'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'htmlmin'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
