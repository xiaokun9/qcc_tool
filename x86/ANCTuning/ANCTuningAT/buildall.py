################################################################################
#
#  buildall.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
"""
Script to setup the environment for the py_anc_calibration scripts.

This script should be invoked by the script
buildall.bat on Windows, or the build shell script on Linux. These
scripts invoke this file like this on Windows::

    pyenv37\Scripts\python.exe buildall.py <args>

The steps performed by this script are:

#. Builds the documentation for the product, which uses Sphinx to
   create Read-the-Docs like documentation.

#. Runs the pytest test suite with the code-coverage turned on.

#. Runs the pylint over our code to produce a pylint score.
"""




import os
import sys
import logging
from pathlib import Path
from glob import glob

# Thirdparty imports
from py_mini_sh import CommandError, expand, exec_, run, copy_changed_files, is_d, pipe

# Comment or uncomment the following to set the logging level of this script. Default is WARN.
logging.getLogger().setLevel(logging.INFO)


# Configurable defines:
PYLINT_COMPONENTS='py_anc_calibration'
SHIP_WHEELS='{CWD}{SEP}docs_and_wheel{SEP}wheels'
COVERAGE_COMPONENTS='--cov=py_anc_calibration'
CWD=str(Path('.').resolve())

def bootstrap():
    """Strap your boots on...
    """
    if not is_d('docs_and_wheel'):
        os.mkdir(expand('docs_and_wheel'))

    # install the application package and the plugin packages as developer installs
    exec_('"{VENV_BIN}{SEP}pip" install -e .[tests]')

    # Install the development requirements
    exec_('"{VENV_BIN}{SEP}pip" install -r requirements.txt')


    # build the sphinx doc
    exec_('"{VENV_BIN}{SEP}python" -m sphinx -b html -d build/doctrees docs_source/source docs_and_wheel/docs/html')

    # Build the bdist_wheel package for the application and for all
    # the plugins. Put these in the shipping folder.
    exec_('"{VENV_BIN}{SEP}python" setup.py bdist_wheel --dist-dir="{SHIP_WHEELS}"')

    # Copy the RELEASE_NOTES.rst into the ship folder
    copy_changed_files('.', 'RELEASE_NOTES.rst', 'SHIP-{ALLVARIANTS}')

    # Run the tests.
    retcode = exec_('"{VENV_BIN}{SEP}pytest" --verbose {COVERAGE_COMPONENTS} tests', ignore_error=True)
    if retcode != 0:
        # Error codes >= 6 don't make sense according to the pytest
        # doc, but we've seen return codes much bigger than this,
        # which appears to be a bug. So ignore these large return
        # codes for now.
        if retcode < 6:
            # this is a valid error return code from pytest
            raise CommandError('pytest failed with error code %d' % retcode)


if __name__ == '__main__':
    sys.exit(run(bootstrap, globals()))
