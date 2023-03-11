1) Generating the documentation and Python wheel:

run "buildall.bat 37" to generate both the documentation and Python wheel.

The documentation can be found in docs_and_wheel\docs.
The Python wheel can be found in docs_and_wheel\wheels

2) Directly installing the ANCTuningAT package:

You can directly install this package by executing "python setup.py install" command in the project directory.
Note: Only Python3.X is supported.

3) Changing the authentication key:

To change the key used to authenticate with the device, update the key in the py_anc_calibration\unlock.key file.
After changing the key, reinstall the wheel:
"python -m pip install --force-reinstall ."
The new key will be used for authentication the next time ANCTuningAT is executed.