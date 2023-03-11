Overview
========

How to use
##########

To start script install py_anc_calibration package and type in command line.

.. code-block:: python

    python -m py_anc_calibration --device_settings KEY=VALUE ANOTHER_KEY=ANOTHER_VALUE

You must provide at least one argument for --device_settings
parameter. If your device connected through serial transport you have
to provide com_port value. Example::

    python -m py_anc_calibration --device_settings com_port=COM3

You can also provide multiple arguments for device_setting parameter. Example::

    python -m py_anc_calibration --device_settings com_port=COM3 timeout=5 baudrate=200000

Note: different transport might require different set of device settings.

After script started please follow user interface to calibrate ANC.
