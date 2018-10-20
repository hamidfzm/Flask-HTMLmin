
"""
Flask-HTMLmin
-------------

minimize your flask rendered html
"""

from setuptools import setup

setup(
    name='Flask-HTMLmin',
    version='1.5.0',
    url='https://github.com/hamidfzm/Flask-HTMLmin',
    license='BSD-3-Clause',
    author='Hamid FzM',
    author_email='hamidfzm@gmail.com',
    description='Minimize render templates html',
    long_description=__doc__,
    py_modules=['HTMLMIN'],
    packages=['flask_htmlmin'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'htmlmin'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    setup_requires=['pytest-runner'],
    test_requires=['pytest']
)
