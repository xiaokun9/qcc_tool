API Reference
=============

.. autoclass:: py_anc_calibration.calibrator.ANCCalibrator
    :members:

Available AT Commands
#####################

.. autoclass:: py_anc_calibration.anc_commands.at_anc_commands.ATCommands
    :members:


Valid arguments for AT commands above can be found in :ref:`validators`.



.. _validators:

Valid values for ANC Command parameters
#######################################

ANC Mode
--------

.. autoclass:: py_anc_calibration.input_validators.ANCModeValidator
   :members: expected_input

Authentication key
------------------

.. autoclass:: py_anc_calibration.input_validators.Key32BitValidator
   :members: expected_input

Gain Path
---------

.. autoclass:: py_anc_calibration.input_validators.GainPathValidator
   :members: expected_input

Gain Value
----------

.. autoclass:: py_anc_calibration.input_validators.GainValueValidator
   :members: expected_input

