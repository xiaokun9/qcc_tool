################################################################################
#
#  setup.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

requires = [
    'PySerial',
    'python-doc-inherit',
    'pycryptoplus'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-bdd',
    'mock',
]

setup(
    name='py_anc_calibration',
    version='0.1.0',
    description='Send ANC gain parameters to a QCC chip over UART',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Pyramid',
        'Topic :: System :: Software Distribution',
    ],
    author='Qualcomm Technologies International Ltd',
    license="Qualcomm Proprietary",
    author_email='',
    url='',
    keywords='CDA UART serial ANC',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'tests': tests_require,
    },
    install_requires=requires,
    package_data={'py_anc_calibration': ['*.key']},
    entry_points={
        'console_scripts': [
            'anc_calibration = py_anc_calibration.__main__:main',
        ],
    },
)
