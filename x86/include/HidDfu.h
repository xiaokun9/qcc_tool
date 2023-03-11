/********************************************************************************
 *
 *  HidDfu.h
 *
 *  Copyright (c) 2012-2022 Qualcomm Technologies International, Ltd.
 *  All Rights Reserved.
 *  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
 *
 *  Defines the HidDfu API functions used to perform a Device Firmware Update on 
 *  a Qualcomm BlueCore device using the USB HID interface.
 *
 *******************************************************************************/

#ifndef HID_DFU_H
#define HID_DFU_H

/* This file used in conjunction with a def file gives us undecorated stdcall C exports from the DLL */
#define HIDDFU_API(T) T _stdcall

#include "common/types.h"

/* Error codes - for description use hidDfuGetLastError() */
#define HIDDFU_ERROR_NONE                                   0
#define HIDDFU_ERROR_SEQUENCE                              -1
#define HIDDFU_ERROR_CONNECTION                            -2
#define HIDDFU_ERROR_FILE_OPEN_FAILED                      -3
#define HIDDFU_ERROR_FILE_WRITE_FAILED                     -4
#define HIDDFU_ERROR_FILE_INVALID_FORMAT                   -5
#define HIDDFU_ERROR_FILE_CRC_INCORRECT                    -6
#define HIDDFU_ERROR_FILE_READ_FAILED                      -7
#define HIDDFU_ERROR_UPGRADE_FAILED                        -8
#define HIDDFU_ERROR_RESET_FAILED                          -9
#define HIDDFU_ERROR_OUT_OF_MEM                            -10
#define HIDDFU_ERROR_INVALID_PARAMETER                     -11
#define HIDDFU_ERROR_DRIVER_INTERFACE_FAILURE              -12
#define HIDDFU_ERROR_OPERATION_FAILED_TO_START             -13
#define HIDDFU_ERROR_BUSY                                  -14
#define HIDDFU_ERROR_CLEAR_STATUS_FAILED                   -15
#define HIDDFU_ERROR_DEVICE_FIRMWARE                       -16
#define HIDDFU_ERROR_UNSUPPORTED                           -17
#define HIDDFU_ERROR_OPERATION_PARTIAL_SUCCESS             -18
#define HIDDFU_ERROR_PARAM_TOO_SMALL                       -19
#define HIDDFU_ERROR_UNKNOWN                               -20
#define HIDDFU_ERROR_VERSION_MISMATCH                      -21
#define HIDDFU_ERROR_NO_OP_IN_PROGRESS                     -22
#define HIDDFU_ERROR_NO_RESPONSE                           -23
#define HIDDFU_ERROR_OP_PARTIAL_SUCCESS_NO_RESPONSE        -24

// The sequence of Upgrading CSRA681xx, QCC302x-8x and QCC512x-8x devices with binary image
// necessitates restart after the image has been copied, we presume that this is 95% of
// the upload process, at which point display a relevant message (for restart duration).
static const int32 PROGRESS_REBOOT_VALUE = 95;

// The wait time after data validation has completed and device is rebooting before attempting to reconnect.
static const uint32 RESTART_DELAY_SEC = 60;

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

/*******************************************************************************

    Function :      int32 hidDfuGetFirmwareVersions(char* versionString,
                                                    uint16* maxLength,
                                                    uint8 checkMatch);

    Parameters :    versionString - 
                        Pointer to a buffer where the comma/semicolon separated
                        string representing device version information for all
                        the connected devices will be written. The format of the
                        string is:
                        "dev1_ver_major,dev1_ver_minor,dev1_config_ver;dev1_ver_major,..."

                    maxLength -
                        Length of the versionString buffer, returns expected
                        length if the length given is less than is required to
                        store the version string.

                    checkMatch -
                        Boolean value - set to 1 to check if all the devices
                        have the same version, 0 otherwise.

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   This function gets the version information of the connected
                    devices. A device connection is required.

*******************************************************************************/
HIDDFU_API(int32) hidDfuGetFirmwareVersions(char* versionString,
                                            uint16* maxLength,
                                            uint8 checkMatch);

/*******************************************************************************

    Function :      int32 hidDfuGetVersion(uint16* major, uint16* minor, 
                                           uint16* release, uint16* build)

    Parameters :    major - 
                        Location to store the major version number.

                    minor -
                        Location to store the minor version number.

                    release -
                        Location to store the release number.

                    build -
                        Location to store the build number.

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   This function gets the version information of the HidDfu 
                    DLL. A device connection is not required.

*******************************************************************************/
HIDDFU_API(int32) hidDfuGetVersion(uint16* major, uint16* minor, 
                                   uint16* release, uint16* build);

/*******************************************************************************

    Function :      int32 hidDfuConnect(uint16 vid, uint16 pid, uint16 usage,
                                        uint16 usagePage, uint16* count)

    Parameters :    vid -
                        Target device USB Vendor ID.

                    pid -
                        Target device USB Product ID.

                    usage -
                        Target device USB usage value. Set this value to 0 to 
                        ignore the device usage value.

                        <p>For QCC304x-8x and QCC514x-8x devices usage must be
                        0x1.

                    usagePage -
                        Target device USB usagePage value. Set this value to 
                        0 to ignore the device usagePage value.

                        <p>For CSRA681xx, QCC302x-8x and QCC512x-8x devices
                        usagePage must be 0xFF00.

                    count -
                        The number of HidDfu devices found.

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Attempts to connect to the specified USB devices. If
                    multiple matching devices are connected to the system, a
                    connection attempt will be made with all the matching
                    devices found.

                    <p>Consecutive calls to hidDfuConnect cannot be made unless
                    hidDfuDisconnect is called in between. If any of the devices
                    are to be plugged in/out after calling hidDfuConnect, then
                    they should be disconnected first using hidDfuDisconnect,
                    and only then plugged in/out; after which hidDfuConnect
                    could be called again to connect to HID devices.

*******************************************************************************/
HIDDFU_API(int32) hidDfuConnect(uint16 vid, uint16 pid, uint16 usage,
        uint16 usagePage, uint16* count);

/*******************************************************************************

    Function :      int32 hidDfuDisconnect(void)

    Parameters :    None

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Disconnects from currently connected devices. If a device is
                    not connected, does nothing and returns HIDDFU_ERROR_NONE.

*******************************************************************************/
HIDDFU_API(int32) hidDfuDisconnect(void);

/*******************************************************************************

    Function :      int32 hidDfuBackup(const char* fileName, uint8 resetAfter)

    Parameters :    fileName -
                        Name of backup image file to write

                    resetAfter -
                        Reset the devices after backup

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Reads the image from the connected BlueCore chip and saves
                    to the specified file. If there are multiple devices, files
                    are suffixed with a "-" and a number. The number is based on
                    the order in which the devices were enumerated by the system.
                    This function starts the operation. Use hidDfuGetProgress
                    to check for completion and hidDfuGetResult to get the final
                    status.

                    <p>This function is not supported for CSRA681xx,
                    QCC302x-8x and QCC512x-8x devices.

*******************************************************************************/
HIDDFU_API(int32) hidDfuBackup(const char* fileName, uint8 resetAfter);

/*******************************************************************************

    Function :      int32 hidDfuUpgrade(const char* fileName, uint8 resetAfter)

    Parameters :    fileName -
                        Name of upgrade image file

                    resetAfter -
                        Reset the devices after upgrade

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Reads an image from the specified file and upgrades the 
                    connected BlueCore devices. This function starts the 
                    operation. Use hidDfuGetProgress to check for completion 
                    and hidDfuGetResult to get the final status.

                    <p>For a particular device there can be only one instance of
                    upgrade/backup running at any time.

                    <p>This function is not supported for CSRA681xx,
                    QCC302x-8x and QCC512x-8x devices - use hidDfuUpgradeBin
                    instead.

*******************************************************************************/
HIDDFU_API(int32) hidDfuUpgrade(const char* fileName, uint8 resetAfter);

/*******************************************************************************

    Function :      int32 hidDfuUpgradeBin(const char* fileName)

    Parameters :    fileName -
                        Name of upgrade binary image file

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Reads a binary image from the specified file and upgrades
                    the connected device(s). This function starts the operation.
                    Use hidDfuGetResult to get the final status.

                    <p>For a particular device there can be only one instance of
                    upgrade/backup running at any time.

                    <p>This function is supported for CSRA681xx, QCC302x-8x
                    and QCC512x-8x devices only.

*******************************************************************************/
HIDDFU_API(int32) hidDfuUpgradeBin(const char* fileName);

/*******************************************************************************

    Function :      int32 hidDfuStop(uint16 waitForStopMs)

    Parameters :    waitForStopMs -
                        Wait time (in milliseconds) for operation to stop.

    Returns :       An error code, either HIDDFU_ERROR_NONE if a running
                    operation has been stopped, HIDDFU_ERROR_NO_OP_IN_PROGRESS
                    if no operation is running or HIDDFU_ERROR_UNKNOWN on failure.

    Description :   Stop an ongoing hidDfuUpgrade, hidDfuBackup or
                    hidDfuUpgradeBin operation.

*******************************************************************************/
HIDDFU_API(int32) hidDfuStop(uint16 waitForStopMs);

/*******************************************************************************

    Function :      int32 hidDfuResetDevice(void)

    Parameters :    None

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   This function resets the connected devices, causing the
                    devices to exit DFU mode. If the reset is successful, the
                    device connections are also closed.

                    <p>The reset is performed in a single thread (i.e. main
                    thread) for all devices. After the devices are reset,
                    hidDfuConnect should be called before any other API
                    function in order to reconnect with the devices.

                    <p>This function is not supported for CSRA681xx,
                    QCC302x-8x and QCC512x-8x devices.

*******************************************************************************/
HIDDFU_API(int32) hidDfuResetDevice(void);

/*******************************************************************************

    Function :      uint8 hidDfuGetProgress(void)

    Parameters :    None

    Returns :       The progress of an operation (percentage).

    Description :   This function gets the progress of on-going upgrade or
                    backup operations for the devices. For operations performed
                    on multiple devices, the average (mean) percentage for all
                    devices is returned. If an operation has finished, 100 is
                    returned.

*******************************************************************************/
HIDDFU_API(uint8) hidDfuGetProgress(void);

/*******************************************************************************

    Function :      int32 hidDfuGetResult(void)

    Parameters :    None

    Returns :       The result for the last completed operation, either
                    HIDDFU_ERROR_NONE if successful, or one of the other
                    HIDDFU_ERROR_ codes defined in this file.

    Description :   This function gets the result of the last completed
                    operation. Returns an error if an operation has not been
                    run, if an operation is ongoing, or if the last operation
                    failed.

                    <p>If there are multiple devices, and all failed devices
                    have the same error, then that error code is returned. If
                    there are different errors, HIDDFU_ERROR_UNKNOWN will be
                    returned.

                    <p>Use hidDfuGetLastError to get the description in the 
                    case of an error.

*******************************************************************************/
HIDDFU_API(int32) hidDfuGetResult(void);

/*******************************************************************************
    
    Function :      const char* hidDfuGetLastError(void)

    Parameters :    None

    Returns :       The details of the last error.

    Description :   This function gets a description of the last error.

*******************************************************************************/
HIDDFU_API(const char*) hidDfuGetLastError(void);

/*******************************************************************************
    
    Function :      uint8 hidDfuGetFailedDevicesCount(void)

    Parameters :    None

    Returns :       The number of devices which failed for the last upgrade or
                    backup operation.

    Description :   This function gets the count of failed devices, in the event
                    of an upgrade or backup failure.

*******************************************************************************/
HIDDFU_API(uint8) hidDfuGetFailedDevicesCount(void);

/*******************************************************************************

    Function :      int32 hidDfuSendCommand(const uint8* data, uint32 length)

    Parameters :    data -
                        The command data to send.

                    length -
                        Length of the data (in bytes).

    Returns :       An error code, either HIDDFU_ERROR_NONE if successful, or 
                    one of the other HIDDFU_ERROR_ codes defined in this file.

    Description :   Sends a custom command to a connected devices. This function
                    can be used to cause the connected devices to switch from
                    normal mode to DFU mode (after which hidDfuDisconnect and
                    hidDfuConnect can be called to reconnect using the DFU mode
                    connection parameters).

                    <p>The operation runs in a single thread (i.e. main thread)
                    for all devices.

                    <p>This function is not supported for CSRA681xx,
                    QCC302x-8x and QCC512x-8x devices.

*******************************************************************************/
HIDDFU_API(int32) hidDfuSendCommand(const uint8* data, uint32 length);

#ifdef __cplusplus
}
#endif /* __cplusplus */


#endif /* HID_DFU_H */
