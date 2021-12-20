#!/usr/bin/env python

"""
Flask-HTMLmin
-------------

Minify flask text/html mime type responses
"""

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Flask-HTMLmin',
    version='2.2.0',
    url='https://github.com/hamidfzm/Flask-HTMLmin',
    license='BSD-3-Clause',
    author='Hamid FzM',
    author_email='hamidfzm@gmail.com',
    description="Minify flask text/html mime type responses",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['HTMLMIN'],
    packages=['flask_htmlmin'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'htmlmin',
        'cssmin'
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
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
