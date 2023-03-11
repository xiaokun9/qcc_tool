@echo off
REM ****************************************************************************
REM *
REM *  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
REM *  All Rights Reserved.
REM *  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
REM *
REM ****************************************************************************
REM
REM This folder builds an environment to run scripts to send AT
REM commands to a compatible Qualcomm CDA device device to set ANC tuning parameters.  It
REM performs the following steps:
REM
REM a) It checks that the argument "37" is given. This
REM indicates which version of Python the code should be built with.
REM
REM b) A virtualenv is created in this folder if one doesn't exist already.
REM
REM c) The packages pip, wheel, and setuptools are updated to the
REM latest version in this virtualenv.
REM
REM d) It then runs the buildall.py file using the Python env that was
REM installed by the above script.
REM

set VENV=
set PY_LOC=
set PYVER=
set PY_BITS=

IF "%1"=="" (
    GOTO :BADARG
) ELSE IF "%1"=="37" (
    set PYVER=3.7
) ELSE (
    GOTO :BADARG
)
set VENV=pyenv%1

REM See if Py Lanucher has been installed just for the current user or all users
set PY_LAUNCHER=%WINDIR%\py.exe
if not exist %PY_LAUNCHER% (
    set PY_LAUNCHER=%LOCALAPPDATA%\Programs\Python\Launcher\py.exe
)
if not exist %PY_LAUNCHER% (
    echo Failed to find py launcher. Install Python %PYVER% with this option selected.
    GOTO :FAILED
)

REM Let's see if Python 3.7 has been installed elsewhere before.
for /F "usebackq tokens=*" %%P in (`%PY_LAUNCHER% -%PYVER% -c "import sys,os; print(os.path.dirname(sys.executable))"`) do set PY_LOC=%%P

IF "%PY_LOC%"=="" (
    echo Failed to find python version %PYVER%. Install this first.
    GOTO :FAILED
)

echo Using the Python in %PY_LOC%

REM Build the virtualenv if it doesn't exist already.
IF exist %VENV% (
    echo Virtualenv %VENV% exists.
) ELSE (
    "%PY_LOC%\python" -m venv %VENV%
    REM Install/upgrade wheel, setuptools and pip to ensure we can install everything
    %VENV%\Scripts\python -m pip install -U wheel setuptools pip
    REM Install the py_mini_sh utility
    %VENV%\Scripts\python -m pip install git+https://bitbucket.org/abelana/py_mini_sh.git
)

REM Delegate everything else to the buildall.py script.
%VENV%\Scripts\python.exe buildall.py

REM Activate this shell with the created virtualenv
call %VENV%\Scripts\activate.bat

GOTO DONE

:BADARG
ECHO Specify 37 as an argument
:FAILED
ECHO Failed to build
set ERRORLEVEL=1
:DONE
EXIT /B %ERRORLEVEL%
