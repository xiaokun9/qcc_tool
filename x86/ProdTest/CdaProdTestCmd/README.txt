################################################################################
#
#  Copyright (c) 2020-2022 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
################################################################################

These instructions describe how to run the CdaProdTestCmd Production test example application for Windows.

NOTE: The CdaProdTestCmd application is not intended to be a complete or appropriate production test solution for any
specific product. The source code is available within the BlueSuite 3.x source release package.


Prerequisites
-----------------------------------------------------------------------------------------------------------------------
1. A Qualcomm BlueSuite (binary) release for Windows (v3.x or later) must be installed in order to install the
   necessary dependencies.
   NOTE: During installation of a BlueSuite release, the optional "Drivers and DLLs for CSR 1455 reference endpoint
   control" components must be selected in order to use the reference endpoint hardware.
2. The CSR 1455 Reference Endpoint can be used for crystal trim instead of a spectrum analyser or other measurement
   hardware. If a spectrum analyser or other measurement hardware is to be used, the project and code must be updated
   to use a GPIB/VISA or other implementation for instrument control. The code is provided with the relevant code to
   use the National Instruments GPIB (ni4882) implementation, but it is compiled out by default with the NOGPIB
   preprocessor definition. If the NOGPIB definition is removed, the ni4882.h and ni4882.obj files must be added to
   the include and lib locations specified in the preparation steps, with the ni4882.obj file being added to the
   additional (library) dependencies of the project.
5. A test ready DUT must be connected. For BT DUTs (earbud,headphone), a Qualcomm CDA chip (e.g. QCC302x-8x or
   QCC512x-8x) must be connected. An appropriate device firmware image must either be available or loaded prior to
   running tests. A firmware image can be deployed as part of the connection sequence - see the "FwPath" setting in
   "ptsetup.txt".
6. For charger devices, the firmware image can be deployed as part of the connection sequence using a 3rd party
   command-line tool invoked by CdaProdTestCmd. Therefore a 3rd party tool appropriate for the charger processor needs
   to be installed, for example, the ST-LINK utility (which includes the ST-LINK_CLI.exe command-line tool), which can
   be downloaded from www.st.com. See the "fwBurn*" settings in "ptsetup_charger.txt" for how to configure
   CdaProdTestCmd to use the 3rd party tool.


Note regarding USB serial port enumeration
-----------------------------------------------------------------------------------------------------------------------
For charger case devices, each DUT with a unique serial number will, when connected by USB, result in the next
available port number being used for the virtual COM port. Eventually, the available COM port numbers will be
exhausted, and due to the port number changing, the "Transport" setting in the setup file has to be updated to match.
This can be avoided by adding a registry value named "IgnoreHWSerNum<VID><PID>" to
"Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags". E.g. for a USB VID of 0x0A12 and PID of 0x5740
the value name would be "IgnoreHWSerNum0A125740". The type must be set to REG_BINARY and data to 01. With this setting
in place, the same port number will be used for each DUT of that type (as long as only one DUT is connected at any one
time).


Running the tool
-----------------------------------------------------------------------------------------------------------------------
Configure the tool as required by editing the setup file. Default configurations are provided as:
    "ptsetup.txt" - for Qualcomm CDA IC based BT devices (earbuds/headset/headphones), using a wired debug connection.
    "ptsetup_dts.txt" - for Qualcomm CDA IC based BT devices (earbuds/headset/headphones), using a BT connection.
    "ptsetup_charger.txt" - for charger case devices.
The setup file must either be present in the working directory, or alternatively, it can be specified using the -setup
option on the command-line.

Run the tool with "-help" to see the usage instructions.

To simplify running continuously, only requiring serial number input for each unit, a template .bat file has been
provided - "CdaProdTestCmd_Launch.bat". The path to the BlueSuite installation may need to be edited, and the file must
be updated to provide the path to the setup file (as indicated by the comments in the template file).

A log file for each test is written to the directory specified by the "LogFileDir" configuration setting. In addition,
a file named "pt_results.txt" in that directory is updated with the result for each test run.


Test descriptions
-----------------------------------------------------------------------------------------------------------------------
CdaProdTestCmd can run a number of pre-defined tests as specified by the "Tests" setting in the setup file.

Tests for CDA-PCB DutType
-----------------------------------------------------------------------------------------------------------------------
The test functionality for BT earbuds/headphones devices using a debug connection (see "ptsetup.txt") is as follows:

SET-PTMODE:
Sets the PS key defined by setting "ProdTestPsKey" to 1, to enable prodtest mode, which prevents peer pairing,
and also allows in-case test modes to be cycled through using button presses. A reset is performed to activate
the prodtest mode.

SET-SN:
Writes the serial number to the device.
The serial number to write is provided using the -sernum command-line argument.

CHECK-SN:
Checks the provided serial number against the serial number read from the DUT.
This is intended for use at test stations after that which set the serial number, to confirm the user input / label
matches the DUT's SN. There is no value in running this test following SET-SN at the same test station, as the SN
is not committed to the device until tests are completed.

LEDS:
Tests each LED specified by the "Leds" setting by switching the LED to the specified first state, asking the user for
confirmation, then doing the same for the other state.

BUTTONS:
Tests each button specified by the "Buttons" setting by asking the user to either press-and-hold or release the button
(depending on the specified first state), checking the detected state, then doing the same for the other state.
This test can also be used for any other on/off PIO input, e.g. a hall sensor.

CHARGER:
Checks whether the device is in one of the states indicating that the USB charger is connected.

AUDIO-TONE:
Generates an audio tone through the speaker and asks the user for confirmation.

AUDIO-LOOP:
Tests each audio loop path specified by the "AudioLoopTests" setting, by enabling the loop, then asking the user for
confirmation that audio is passing through. The loop is then disconnected.

XTAL-TRIM:
Calibrates the crystal trim coarse and fine trim values, writing the values to the relevant MIB keys in device storage.
A spectrum analyser is required for this test, as defined by the "SpectrumAnalyser" and "SpecAnPortId" settings.
The "RfTestChannel" setting defines the channel used for calibration, and the "XtalCoarseMarginHz" and
"XtalFineMarginHz" settings define the target windows used during calibration. The "XtalTrimIncremental" setting
determines what search algorithm is used.

RF-POWER:
Checks the RF output power against the "ExpectedPowerDbm" and "PowerMarginDbm" settings.
A spectrum analyser is required, and if controled by CdaProdTestCmd is as defined by the "SpectrumAnalyser" and
"SpecAnPortId" settings. If "SpectrumAnalyser" is not specified the user is asked to confirm the output power.
The "RfTestChannel" setting defines the channel used for the test.

SET-BDADDR:
Writes the Bluetooth device address to the device.
The address to write is provided by either the -bdaddr command-line argument, or automatically from a Bluetooth
address file specified by the "BdAddrFile" setting. An example of the file content is included ("BdAddrs.txt").
The file specifies a range of Bluetooth addresses to use, where the last 6 hex digits (the LAP) are incremented by the
"BdAddrIncrement" setting value after an address is written to a device.
A record file, specified by the "BdAddrRecordFile" setting, is updated to record the Bluetooth address assigned to each
device serial number.

SET-BDNAME:
Writes the Bluetooth device name to the device.
The name to write is specified by the "DeviceName" setting.

CFG-MERGE:
Merges MIB configuration settings and writes PS store settings to the device.
MIB keys to merge are specified in a standard configuration text (HTF) file. The path to the file is specified by the
"CfgMergeMibFile" setting.
PS store keys to write are specified by the "CfgMergePs" setting.

I2C-DEVS:
Tests connectivity of I2C devices.
The I2C configuration and test sequences are defined by the "I2c*" settings ("I2cConnTests" for the test data).

I2C-TOUCH:
Tests connectivity of I2C touchpad devices which use a reset PIO.
The I2C configuration and test sequences are defined by the "I2c*" settings ("I2cTouchTests" for the test data).

USER-HC:
Runs tests driven via the device application using user defined host comms messages.
The tests are defined by the "UserHcTests" setting.
This test requires the device application to be running, i.e., "DisableDutApp" must be set to 0.


Tests for CDA-DTS DutType
-----------------------------------------------------------------------------------------------------------------------
The test functionality for BT earbuds/headphones devices (see "ptsetup_dts.txt") using a BT connection is as follows:

DTS:LEDS:
Tests each LED specified by the "Leds" setting by switching the LED on, asking the user for confirmation, then
switching it off, again asking the user for confirmation.

DTS:TOUCHPAD:
Tests the touchpad device by checking that no touch is detected, then asking the user to perform one or more action
types specified by the "TouchTests" setting after hitting a key. If no touch events are detected initially, and if each
of the specified action types are detected within the specified "TouchTestTimeoutSeconds" period, the test passes.

DTS:PROXIMITY:
Tests the proximity sensor asking the user to place/remove a hand near the proximity sensor after hitting a key. If a
change in state is detected within the specified "ProximityTestTimeoutSeconds" period, the test passes.

DTS:HALL-SENSOR:
Tests the hall effect sensor asking the user to place/remove a magnet near the DUT after hitting a key. If a change in
state is detected within the specified "HallSensorTestTimeoutSeconds" period, the test passes.

DTS:TEMP:
Tests the temperature sensor by checking that the reported temperature is within the range specified by the
"TempTestRangeDegC" setting.

DTS:BATT:
Tests the battery by checking that the reported level is within the range specified by the "BattTestRangeMv" setting.

DTS:AUDIO-TONE:
Generates audio tones as specified by the "AudioToneTests" setting, asking the user for confirmation in each case.

DTS:AUDIO-LOOP:
Tests each audio loop path specified by the "AudioLoopTests" setting, by enabling the loop, then asking the user for
confirmation that audio is passing through. The loop is then disconnected.

DTS:RSSI:
Tests the RSSI for the connection by checking that it is within the range specified by the "RssiTestRangeDbm" setting.

DTS:RF-POWER:
Checks the RF output power against the "ExpectedPowerDbm" and "PowerMarginDbm" settings.
A spectrum analyser is required, and if controled by CdaProdTestCmd is as defined by the "SpectrumAnalyser" and
"SpecAnPortId" settings. If "SpectrumAnalyser" is not specified the user is asked to confirm the output power.
The "RfTestChannel" setting defines the channel used for the test, and the "RfTestStopMethod" setting defines how the
RF test mode is stopped (required because with DTS, running an RF test drops the DTS-SPP link).

DTS:CFG-SET:
Writes PS store settings to the device as specified by the "CfgSetPs" setting.


Tests for CHARGER-PCB DutType
-----------------------------------------------------------------------------------------------------------------------
For charger devices, the firmware image can be deployed as part of the connection sequence by specifying
appropriate values for the "fwBurn*" settings (see "ptsetup_charger.txt").
The test functionality for charger devices is as follows:

CHG:SET-SN:
Writes the serial number to the device.
The serial number to write is provided using the -sernum command-line argument (can be entered as dec/hex depending on
the "SerNumFormat" setting, must fit within 64 bits).

CHG:CHECK-SN:
Checks the provided serial number against the serial number read from the DUT.
This is intended for use at test stations after that which set the serial number, to confirm the user input / label
matches the DUT's SN.

CHG:LED:
Tests each LED specified by the "ChgrLedModes" setting, asking the user for confirmation.

CHG:VBATT:
Tests the VBAT ADC. If "VbattTestUserSet" is set to 1, the user is asked to connect a voltage to the line (specified
by the "VbattTestMv" setting), otherwise the specified voltage is assumed to be already present (e.g. battery
connected). The voltage is read by the device, and if it is within the margin specified by the "VbattTestMarginMv"
setting, it's a pass.

CHG:VBUS:
Tests the VBUS output for each level defined by the "VbusTests" setting, by putting the DUT into each specified mode
before asking the user to check the voltage is between the specified limits.

CHG:CUR-SENSE:
Tests that the current sense ADC reads are within the expected range specified by the "CurSenseRange" setting.
No load should be present for this test.

CHG:LID-SENSOR:
Tests that the case can detect both open and closed lid states.

CHG:BUD-COMMS:
Tests that the charger case can communicate with connected earbuds.

CHG:BATT-DIS:
Tests the battery discharge current by asking the user to connect a load, then to check that the current is within
the expected range specified by the "BattDischargeRangeMa" setting. The user is then asked to disconnect the load.

CHG:BATT-CHARGE:
Tests the charger by doing the following:
1. Asks the user to connect the charger (connect USB).
2. Checks that the charger is detected by the DUT.
3. Tests the charger modes defined by the "BattChargeTests" setting, by putting the DUT into each specified mode before
   asking the user to check the charging current is between the specified limits.
4. Asks the user to disconnect the charger (disconnect USB).
5. Checks that the charger is no longer detected by the DUT.
NOTE: This test cannot be performed with the DUT connected via USB for comms (i.e. the hardware UART must be used).

CHG:STANDBY:
Tests the charger standby mode by asking the user to apply the case magnet (i.e. close the lid),
and ensuring that the charger (USB) is disconnected.
The DUT is then taken out of test mode and put into low power standby mode, and the user is asked
to check that the standby current is within the range specified by the "StandbyRangeUa" setting.
Finally the DUT is put back into test mode.
NOTE: This test cannot be performed with the DUT connected via USB for comms (i.e. the hardware UART must be used).

CHG:THERM:
Tests the thermistor and potential divider by reading the voltage from the DUT and checking that it is within the
range specified by the "ThermistorRangeMv" setting. 

CHG:SET-SHIPMODE:
Puts the charger and connected earbuds into shipping mode (ready to ship).
Optionally logs the earbud Bluetooth device addresses (see the "ShipModeLogBdAddrs" setting).

CHG:CFG-SET:
Writes configuration values to the device.
Values are specified by the "CfgSetItems" setting.

CHG:BC-TXRX:
Tests the charger bud communications TX/RX components (supported only for fast comms hardware).
Performs a loopback test for low and high states through the TX and RX component chains.
