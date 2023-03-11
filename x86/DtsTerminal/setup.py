################################################################################
#
#  setup.py
#
#  Copyright (c) 2021 Qualcomm Technologies International, Ltd.
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
    'pycryptoplus',
    'aioconsole'
]

tests_require = [
    'pytest',
    'mock',
]

setup(
    name='DtsTerminal',
    version='1.0.0',
    description='',
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
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'tests': tests_require,
    },
    install_requires=requires,
    package_data={'dts_terminal': ['*.key']},
    entry_points={
        'console_scripts': [
            'dts_terminal = dts_terminal.__main__:main'
        ],
    },
)
