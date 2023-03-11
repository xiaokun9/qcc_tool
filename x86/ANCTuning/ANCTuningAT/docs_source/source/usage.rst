
Using the API
=============

Defining your own AT command
############################

To create new AT command simply initialize ATCommand class and provide
command parameter to the constructor. The command parameter must not
include "AT" prefix. Example if your command is 'AT+POWERON' the
right syntax will be:

.. code-block:: python

    at_power_on = ATCommand('+POWERON')

If your AT command has value in it e.g 'AT+POWERON=15,20' the right syntax is:

.. code-block:: python

    at_power_on = ATCommand('+POWERON=15,20')

.. autoclass:: py_anc_calibration.anc_commands.at_anc_commands.ATCommand
    :members:

Sending commands to the device
##############################

Example sending an AT command over serial transport:

.. code-block:: python

    serial_transport = SerialTransport()
    serial_transport.connect('com_port'='COM1')
    generic_at_command = ATCommand('Generic')
    payload, success = serial.execute(generic_at_command)
    if success:
        print(payload)

.. autoclass:: py_anc_calibration.transport.serial_transport.SerialTransport
    :members: execute

.. HINT::
    To see more code examples take a loot at test folder
