# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = '0.0.1'
__description__ = 'Api para buscar a lista de senadres'
__long_description__ = 'Python library for comunicate API Brazilian Senators'

__author__ = 'Lucas Simon'
__author_email__ = 'lucassrod@gmail.com'

requires = [i.strip() for i in open("requirements.txt").readlines()]

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='python-senado',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com:lucassimon/python-senado.git',
    keywords='API, SOAP, Senators, Brazil',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)