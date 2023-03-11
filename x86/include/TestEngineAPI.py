################################################################################
#  TestEngineAPI.py : Declares the DLL functions for Python.
#  Copyright (c) 2022 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Auto-generated Python wrapper for TestEngine DLL.
#  Created on 2022-11-18 15:48 from TestEngine.h file"
################################################################################

import os
import ctypes as ct
from typing import Tuple

class TestEngine():
    """
    A python wrapper class for TestEngine DLL.
    Usage:
        myDll = TestEngine("<DLL_PATH>" [, debug=False])    
    """
    def __init__(self, path_to_dll):
        """Load the TestEngine DLL"""
        self.TestEngineDLL = None
        try:
            full_path = os.path.realpath(path_to_dll)
            if full_path.strip().lower().endswith('.dll'):
                path_to_dll = os.path.dirname(full_path) + '\\'  # Extract directory from DLL name
                
            if not path_to_dll.endswith('\\'):
                path_to_dll += '\\'

            if not path_to_dll + ';' in os.environ['PATH']: # add this to the path if not already present
                os.environ['PATH'] = path_to_dll + ';' + os.environ['PATH']

            self.TestEngineDLL = ct.windll.LoadLibrary(path_to_dll + 'TestEngine')
        except Exception as e:
            print("Cannot load TestEngine.dll from " + path_to_dll)
            if ct.sizeof(ct.c_void_p) == 8:
                print("Check that the DLL is present and 64 bit.\n"
                      "64 bit Python can only be used with 64 bit DLL")
            else:
                print("Check that the DLL is present and 32 bit\n"
                      "32 bit Python can only be used with 32 bit DLL")
            raise e
    # end __init__

    #
    # Pre-defined constants that may be used as parameter values or returns from the TestEngine API
    #
    TE_INVALID_HANDLE_VALUE = 0
    TE_INVALID_HANDLE = -1
    TE_ERROR = 0
    TE_OK = 1
    TE_UNSUPPORTED_FUNCTION = 2
    SQIF_APP_VALIDATION_RUNNING = 0x0
    SQIF_APP_VALIDATION_PASS = 0x1
    SQIF_APP_VALIDATION_PASS_NO_APP = 0x2
    TE_CLOSE_EX_RESET_RELOCK_NO_WAIT = 0
    TE_CLOSE_EX_RESET_RELOCK_WAIT = 1
    TE_CLOSE_EX_NO_RESET_NO_RELOCK = 2

    BER_BIT_COUNT = 0
    BER_BIT_ERRORS = 1
    BER_ACCESS_CODE = 2
    BER_RCVD_PKTS = 3
    BER_EXP_PKTS = 4
    BER_HDR_ERRORS = 5
    BER_CRC_ERRORS = 6
    BER_UNCORR_ERRORS = 7
    BER_SYNC_ERRORS = 8
    BER_MAX = 9
    VM_STATUS_BOOT = 0
    VM_STATUS_FAIL = 1
    VM_STATUS_RUN = 2
    VM_STATUS_PANIC = 3
    VM_STATUS_EXIT = 4
    CVC_PRODTEST_PASS = 1
    CVC_PRODTEST_FAIL = 2
    CVC_PRODTEST_NO_CHECK = 3
    CVC_PRODTEST_FILE_NOT_FOUND = 4
    TE_ERROR_NONE = 0x000000
    TE_ERROR_BCCMD_NO_SUCH_VARID = 0x000001
    TE_ERROR_BCCMD_DATA_EXCEEDED = 0x000002
    TE_ERROR_BCCMD_VAR_HAS_NO_VALUE = 0x000003
    TE_ERROR_BCCMD_BAD_VALUE = 0x000004
    TE_ERROR_BCCMD_NO_ACCESS = 0x000005
    TE_ERROR_BCCMD_READ_ONLY = 0x000006
    TE_ERROR_BCCMD_WRITE_ONLY = 0x000007
    TE_ERROR_BCCMD_OTHER_ERROR = 0x000008
    TE_ERROR_BCCMD_PERMISSION_DENIED = 0x000009
    TE_ERROR_HCI_UNKNOWN_COMMAND = 0x010000
    TE_ERROR_HCI_UNKNOWN_CONNECTION_ID = 0x020000
    TE_ERROR_HCI_HARDWARE_FAILURE = 0x030000
    TE_ERROR_HCI_PAGE_TIMEOUT = 0x040000
    TE_ERROR_HCI_AUTHENTICATION_FAILURE = 0x050000
    TE_ERROR_HCI_PIN_MISSING = 0x060000
    TE_ERROR_HCI_MEMORY_CAPACITY_EXCEEDED = 0x070000
    TE_ERROR_HCI_CONNECTION_TIMEOUT = 0x080000
    TE_ERROR_HCI_CONNECTION_LIMIT_EXCEEDED = 0x090000
    TE_ERROR_HCI_SYNCHRONOUS_CONNECTION_LIMIT_EXCEEDED = 0x0a0000
    TE_ERROR_HCI_ACL_CONNECTION_ALREADY_EXISTS = 0x0b0000
    TE_ERROR_HCI_COMMAND_DISALLOWED = 0x0c0000
    TE_ERROR_HCI_CONNECTION_REJECTED_LIMITED_RESOURCES = 0x0d0000
    TE_ERROR_HCI_CONNECTION_REJECTED_SECURITY_REASONS = 0x0e0000
    TE_ERROR_HCI_CONNECTION_REJECTED_UNACCEPTABLE_BD_ADDR = 0x0f0000
    TE_ERROR_HCI_CONNECTION_ACCEPT_TIMEOUT_EXCEEDED = 0x100000
    TE_ERROR_HCI_UNSUPPORTED_FEATURE = 0x110000
    TE_ERROR_HCI_INVALID_COMMAND_PARAMETERS = 0x120000
    TE_ERROR_HCI_REMOTE_USER_TERMINATED_CONNECTION = 0x130000
    TE_ERROR_HCI_REMOTE_DEVICE_TERMINATED_CONNECTION_LOW_RESOURCES = 0x140000
    TE_ERROR_HCI_REMOTE_DEVICE_TERMINATED_CONNECTION_POWER_OFF = 0x150000
    TE_ERROR_HCI_CONNECTION_TERMINATED_BY_LOCAL_HOST = 0x160000
    TE_ERROR_HCI_REPEATED_ATTEMPTS = 0x170000
    TE_ERROR_HCI_PAIRING_NOT_ALLOWED = 0x180000
    TE_ERROR_HCI_UNKNOWN_LMP_PDU = 0x190000
    TE_ERROR_HCI_UNSUPPORTED_REMOTE_FEATURE = 0x1a0000
    TE_ERROR_HCI_SCO_OFFSET_REJECTED = 0x1b0000
    TE_ERROR_HCI_SCO_INTERVAL_REJECTED = 0x1c0000
    TE_ERROR_HCI_SCO_AIR_MODE_REJECTED = 0x1d0000
    TE_ERROR_HCI_INVALID_LMP_PARAMETERS = 0x1e0000
    TE_ERROR_HCI_UNSPECIFIED_ERROR = 0x1f0000
    TE_ERROR_HCI_UNSUPPORTED_LMP_PARAMETER_VALUE = 0x200000
    TE_ERROR_HCI_ROLE_CHANGE_NOT_ALLOWED = 0x210000
    TE_ERROR_HCI_LMP_RESPONSE_TIMEOUT = 0x220000
    TE_ERROR_HCI_LMP_ERROR_TRANSACTION_COLLISION = 0x230000
    TE_ERROR_HCI_LMP_PDU_NOT_ALLOWED = 0x240000
    TE_ERROR_HCI_ENCRYPTION_MODE_NOT_ACCEPTABLE = 0x250000
    TE_ERROR_HCI_LINK_KEY_CANNOT_BE_CHANGED = 0x260000
    TE_ERROR_HCI_REQUESTED_QOS_NOT_SUPPORTED = 0x270000
    TE_ERROR_HCI_INSTANT_PASSED = 0x280000
    TE_ERROR_HCI_PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED = 0x290000
    TE_ERROR_HCI_DIFFERENT_TRANSACTION_COLLISION = 0x2a0000
    TE_ERROR_HCI_RESERVED_1 = 0x2b0000
    TE_ERROR_HCI_QOS_UNACCEPTABLE_PARAMETER = 0x2c0000
    TE_ERROR_HCI_QOS_REJECTED = 0x2d0000
    TE_ERROR_HCI_CHANNEL_CLASSIFICATION_NOT_SUPPORTED = 0x2e0000
    TE_ERROR_HCI_INSUFFICIENT_SECURITY = 0x2f0000
    TE_ERROR_HCI_PARAMETER_OUT_OF_MANDATORY_RANGE = 0x300000
    TE_ERROR_HCI_RESERVED_2 = 0x310000
    TE_ERROR_HCI_ROLE_SWITCH_PENDING = 0x320000
    TE_ERROR_HCI_RESERVED_3 = 0x330000
    TE_ERROR_HCI_RESERVED_SLOT_VIOLATION = 0x340000
    TE_ERROR_HCI_ROLE_SWITCH_FAILED = 0x350000
    TE_ERROR_OUT_OF_MEMORY = 0x01000001
    TE_ERROR_BAD_PARAM = 0x01000002
    TE_ERROR_CONNECTION_SETUP = 0x01000003
    TE_ERROR_FILE_OPEN = 0x01000004
    TE_ERROR_INSUFFICIENT_SPACE = 0x01000005
    TE_ERROR_INVALID_SEQUENCE = 0x01000006
    TE_ERROR_MIBCMD_NO_SESSION = 0x01000010
    TE_ERROR_MIBCMD_GET = 0x01000011
    TE_ERROR_MIBCMD_SET = 0x01000012
    TE_ERROR_CONFIG_READ = 0x01000020
    TE_ERROR_CONFIG_WRITE = 0x01000021
    TE_ERROR_CONFIG_ELEMENT_NOT_FOUND = 0x01000022
    TE_ERROR_CONFIG_DATABASE = 0x01000023
    TE_ERROR_CONFIG_GENERAL = 0x01000024
    TE_CHIP_FAMILY_UNKNOWN = 0x00
    TE_CHIP_FAMILY_BLUECORE = 0x01
    TE_CHIP_FAMILY_MULTI = 0x04
    TE_SUBSYSTEM_BT = 0
    TE_SUBSYSTEM_AUDIO = 1
    TE_SUBSYSTEM_APPS0 = 2
    TE_SUBSYSTEM_APPS1 = 3
    TE_TRANS_CRIT_NOLOCK = 0x00000001
    TE_TRANS_CRIT_UNLOCKED = 0x00000002
    TE_TRANS_CRIT_LOCKED = 0x00000004
    TE_TRANS_CRIT_ALL = 0x00000007
    TE_TRANS_CRIT_DEFAULT = 0x00000003
    BCSP = 0x1
    USB = 0x2
    H4 = 0x4
    H5 = 0x8
    H4DS = 0x10
    PTAP = 0x40
    TRB = 0x80
    USBDBG = 0x100
    DEBUG_LPTSPI = 1
    DEBUG_USBSPI = 2
    DEBUG_USBTRB = 3
    DEBUG_USBDBG = 4
    SPI_LPT = DEBUG_LPTSPI
    SPI_USB = DEBUG_USBSPI

    #
    # Exported routines for the TestEngine API
    #

    def teGetVersion(self, versionStr: str='') -> Tuple[int, str]:
        r"""Function TestEngine::teGetVersion() wrapper for teGetVersion in TestEngine DLL.

        Python API:
            teGetVersion(versionStr: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, versionStr = myDll.teGetVersion()
            print(retval, versionStr)

        Detail From Wrapped C API:
            Function :      int32 teGetVersion(char* versionStr)

            Parameters :    versionStr -
                                A pointer to a pre-allocated string that will have the
                                version string copied to it.

            Returns :       Always 1.

            Description :   Retrieves the current version string.

            Example :

                char versionStr[255];
                teGetVersion(versionStr);

                cout << "TestEngine version = " << versionStr << endl;

        """
        self.TestEngineDLL.teGetVersion.restype = ct.c_int32
        self.TestEngineDLL.teGetVersion.argtypes = [ct.c_char_p]
        local_versionStr = None if versionStr is None else ct.create_string_buffer(bytes(versionStr, encoding="UTF-8"), 1024)
        retval = self.TestEngineDLL.teGetVersion(local_versionStr)
        versionStr = local_versionStr.value.decode()
        return retval, versionStr
    # end of teGetVersion


    def openTestEngine(self, transport: int, transportDevice: str, dataRate: int, retryTimeOut: int, usbTimeOut: int) -> int:
        r"""Function TestEngine::openTestEngine() wrapper for openTestEngine in TestEngine DLL.

        Python API:
            openTestEngine(transport: int, transportDevice: str, dataRate: int, retryTimeOut: int, usbTimeOut: int) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngine(transport=0, transportDevice='abc', dataRate=0, retryTimeOut=0, usbTimeOut=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngine(int32 transport,
                                                  const char* transportDevice,
                                                  uint32 dataRate, int32 retryTimeOut,
                                                  int32 usbTimeOut)

            Parameters :    transport -
                                Defines the protocol to be used when setting up the
                                communication with the device, where:
                                <table>
                                    <tr><td>BCSP = 1
                                    <tr><td>USB = 2
                                    <tr><td>H4 = 4
                                    <tr><td>H5 = 8
                                    <tr><td>H4DS = 16
                                    <tr><td>PTAP = 64
                                    <tr><td>TRB = 128
                                    <tr><td>USBDBG = 256
                                </table>

                            transportDevice -
                                Defines the physical port to use. A string which defines which
                                port is used, e.g. "\\.\COMn" where 'n' is the number of the
                                COM port. USB device names take the form "\\.\CSRn".
                                <p>
                                NOTE: In C/C++, and possibly some other languages, literal '\'
                                characters are written as "\\", otherwise they are interpreted
                                as the start of an escape sequence. So for these languages,
                                the literal string "\\.\COMn" is written as "\\\\.\\COMn" in
                                the code. The prefix can be dropped for COM ports 1 to 9, i.e.
                                "COM1" works the same as "\\\\.\\COM1". If using PTAP then
                                this is the HifId followed by an optional COM port name if
                                connecting via UART (i.e. "0:\\.\COM1").
                                <p>
                                For TRB, the serial number of the usb2trb converter e.g.
                                "123456" may be used. For USBDBG, the port identifier of the
                                corresponding USB Hub Filter (e.g. "100") may be used.
                                Alternatively, a sequence number ranging from 1 to the number
                                of connected devices may be used for TRB and USBDBG. For
                                further details of TRB and USBDBG device identifiers, refer
                                to CS-00410202-UG.

                            dataRate -
                                Defines the baud rate to be used (for UART connections only).

                            retryTimeOut -
                                Defines how long the function will retry, in ms, when trying
                                to establish communication with the device. Care should be
                                taken when selecting an appropriate retry timeout. BlueCore1
                                and BlueCore2 running early firmware versions require a longer
                                timeout. 5000ms should be enough to pick up these early
                                devices but this value will make openTestEngine unresponsive.
                                It would be better to set this parameter to 1000ms and call
                                openTestEngine up to 5 times or until it passes.

                            usbTimeout -
                                Where transport = USB or USBDBG, this parameter will define how
                                long the function will retry, in ms, when trying to detect if
                                the specified USB device has enumerated. It has been found that
                                some PC's take a longer time than expected to enumerate a USB
                                device and, in some cases, the PC's internal USB hub may have
                                been reset which can cause a further delay in enumeration.
                                This parameter can be set to accommodate the extra time taken
                                to reset USB devices. If USB is not used then this value can
                                be set to 0.

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin.
                            <p>
                            This function opens a connection using a host transport protocol
                            running over USB or a UART, or debug transport running over TRB or
                            USBDBG. To open a debug connection with a device which is not
                            transport-locked, use openTestEngineDebug or
                            openTestEngineDebugTrans. To open a debug connection with a device
                            which is transport-locked, use openTestEngineDebugUnlock or
                            openTestEngineDebugUnlockTrans.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.openTestEngine.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngine.argtypes = [ct.c_int32, ct.c_char_p, ct.c_uint32, ct.c_int32, ct.c_int32]
        local_transportDevice = None if transportDevice is None else ct.create_string_buffer(bytes(transportDevice, encoding="UTF-8"))
        retval = self.TestEngineDLL.openTestEngine(transport, local_transportDevice, dataRate, retryTimeOut, usbTimeOut)
        
        return retval
    # end of openTestEngine


    def openTestEngineUnlock(self, transport: int, transportDevice: str, retryTimeOut: int, usbTimeOut: int, unlockKey: str) -> int:
        r"""Function TestEngine::openTestEngineUnlock() wrapper for openTestEngineUnlock in TestEngine DLL.

        Python API:
            openTestEngineUnlock(transport: int, transportDevice: str, retryTimeOut: int, usbTimeOut: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngineUnlock(transport=0, transportDevice='abc', retryTimeOut=0, usbTimeOut=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngineUnlock(int32 transport,
                                                        const char* transportDevice,
                                                        int32 retryTimeOut,
                                                        int32 usbTimeOut,
                                                        const char* unlockKey)

            Parameters :    transport -
                                Defines the protocol to be used when setting up the
                                communication with the device, where:
                                <table>
                                    <tr><td>TRB = 128
                                    <tr><td>USBDBG = 256
                                </table>

                            transportDevice -
                                Defines the physical port to use. For TRB, the serial number
                                of the usb2trb converter e.g. "123456" may be used. For
                                USBDBG, the port identifier of the corresponding USB Hub
                                Filter (e.g. "100") may be used. Alternatively, a sequence
                                number ranging from 1 to the number of connected devices
                                may be used. For further details of these device
                                identifiers, refer to CS-00410202-UG.

                            retryTimeOut -
                                Defines how long the function will retry, in ms, when trying
                                to establish communication with the device. Care should be
                                taken when selecting an appropriate retry timeout.

                            usbTimeout -
                                Where transport = USBDBG, this parameter will define how long
                                the function will retry, in ms, when trying to detect if the
                                specified USB device has enumerated. It has been found that
                                some PC's take a longer time than expected to enumerate a USB
                                device and, in some cases, the PC's internal USB hub may have
                                been reset which can cause a further delay in enumeration.
                                This parameter can be set to accommodate the extra time taken
                                to reset USB devices. If USB is not used then this value can
                                be set to 0.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin.
                            <p>
                            This function opens a connection to a transport-locked device
                            using TRB or USBDBG.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                int32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngineUnlock(USBDBG, "1", 1000, 1000,
                                                    "FB459F10828E85FCC0EB1EB3D2186F58");
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.openTestEngineUnlock.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngineUnlock.argtypes = [ct.c_int32, ct.c_char_p, ct.c_int32, ct.c_int32, ct.c_char_p]
        local_transportDevice = None if transportDevice is None else ct.create_string_buffer(bytes(transportDevice, encoding="UTF-8"))
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestEngineDLL.openTestEngineUnlock(transport, local_transportDevice, retryTimeOut, usbTimeOut, local_unlockKey)
        
        return retval
    # end of openTestEngineUnlock


    def openTestEngineDebug(self, port: int, multi: int, transport: int) -> int:
        r"""Function TestEngine::openTestEngineDebug() wrapper for openTestEngineDebug in TestEngine DLL.

        Python API:
            openTestEngineDebug(port: int, multi: int, transport: int) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngineDebug(port=0, multi=0, transport=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngineDebug(int32 port, int32 multi,
                                                       int32 transport)

            Parameters :    port -
                                Defines the physical port to use. Port enumeration numbers
                                start from 0 for the USBSPI transport and from 1 for all other
                                transports. For transports other than LPTSPI, the serial
                                number (or, in the case of USBDBG, the port identifier of the
                                corresponding USB Hub Filter) may be used as an alternative to
                                the port enumeration number. For further details of TRB and
                                USBDBG device identifiers, refer to CS-00410202-UG.
                                <p>
                                Set to -1 to use the default (first available port found).
                                NOTE: Default may be overridden by the "SPIPORT" environment
                                variable.

                            multi -
                                A gate on a multi-SPI interface. Set to zero for TRB and
                                USBDBG transports, and when communicating with a single device
                                attached to a standard LPTSPI or USBSPI port. When using the
                                gang programmer hardware, set to 0 - 15 to select the device
                                to connect to (the transport parameter must be DEBUG_LPTSPI in
                                this case).

                            transport -
                                Defines the debug transport to be used, where:
                                <table>
                                    <tr><td>DEBUG_LPTSPI = 1
                                    <tr><td>DEBUG_USBSPI = 2
                                    <tr><td>DEBUG_USBTRB = 3
                                    <tr><td>DEBUG_USBDBG = 4
                                </table>
                                Set to -1 to use the default (from SPITRANS environment
                                variable if present), otherwise DEBUG_LPTSPI.

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin.
                            <p>
                            This function, and openTestEngineDebugTrans opens a debug
                            connection for devices which are not transport-locked. To open a
                            debug connection with transport-locked devices, use
                            openTestEngineDebugUnlock. To open a host transport connection,
                            use openTestEngine.
                            <p>
                            Note that over a SPI transport the function set is limited to
                            bccmd*, radiotest*, and hq* functions. HQ functions (and radiotest
                            functions that generate HQ traffic) are only supported if the
                            BlueCore firmware supports HQ over SPI. Commands which are not
                            supported will return TE_UNSUPPORTED_FUNCTION.

            Example :

                uint32 teHandle = openTestEngineDebug(1, 0, DEBUG_LPTSPI);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.openTestEngineDebug.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngineDebug.argtypes = [ct.c_int32, ct.c_int32, ct.c_int32]
        
        retval = self.TestEngineDLL.openTestEngineDebug(port, multi, transport)
        
        return retval
    # end of openTestEngineDebug


    def openTestEngineDebugUnlock(self, port: int, multi: int, transport: int, unlockKey: str) -> int:
        r"""Function TestEngine::openTestEngineDebugUnlock() wrapper for openTestEngineDebugUnlock in TestEngine DLL.

        Python API:
            openTestEngineDebugUnlock(port: int, multi: int, transport: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngineDebugUnlock(port=0, multi=0, transport=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngineDebugUnlock(int32 port, int32 multi,
                                                             int32 transport,
                                                             const char* unlockKey)

            Parameters :    port -
                                Defines the physical port to use. Port enumeration numbers
                                start from 0 for the USBSPI transport and from 1 for all other
                                transports. For transports other than LPTSPI, the serial
                                number (or, in the case of USBDBG, the port identifier of the
                                corresponding USB Hub Filter) may be used as an alternative to
                                the port enumeration number. For further details of TRB and
                                USBDBG device identifiers, refer to CS-00410202-UG.
                                <p>
                                Set to -1 to use the default (first available port found).
                                NOTE: Default may be overridden by the "SPIPORT" environment
                                variable.

                            multi -
                                A gate on a multi-SPI interface. Set to zero for TRB and
                                USBDBG transports, and when communicating with a single device
                                attached to a standard LPTSPI or USBSPI port. When using the
                                gang programmer hardware, set to 0 - 15 to select the device
                                to connect to (the transport parameter must be DEBUG_LPTSPI in
                                this case).

                            transport -
                                Defines the debug transport to be used, where:
                                <table>
                                    <tr><td>DEBUG_LPTSPI = 1
                                    <tr><td>DEBUG_USBSPI = 2
                                    <tr><td>DEBUG_USBTRB = 3
                                    <tr><td>DEBUG_USBDBG = 4
                                </table>
                                Set to -1 to use the default (from SPITRANS environment
                                variable if present), otherwise DEBUG_LPTSPI.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin. Function
                            openTestEngineDebugUnlockTrans can be used instead.
                            <p>
                            To be used (only) to open a debug connection to a transport-locked
                            chip. If openTestEngineDebugUnlock is used to open the test
                            connection, then the functions bccmdSetWarmReset and
                            bccmdSetColdReset (for BlueCore ICs), and teChipReset (for CDA
                            ICs) will automatically use the same unlock code as
                            openTestEngineDebugUnlock when re-establishing connection with the
                            chip.
                            <p>
                            openTestEngineDebug or openTestEngineDebugTrans should be used to open
                            a debug connection with a device which is not transport-locked. To
                            open a host transport connection, use openTestEngine.
                            <p>
                            Note that over a SPI transport the function set is limited to
                            bccmd*, radiotest*, and hq* functions. HQ functions (and radiotest
                            functions that generate HQ traffic) are only supported if the
                            BlueCore firmware supports HQ over SPI. Commands which are not
                            supported will return TE_UNSUPPORTED_FUNCTION.

            Example :

                uint32 teHandle = openTestEngineDebugUnlock(1, 0, DEBUG_LPTSPI, "123456789");

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.openTestEngineDebugUnlock.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngineDebugUnlock.argtypes = [ct.c_int32, ct.c_int32, ct.c_int32, ct.c_char_p]
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestEngineDLL.openTestEngineDebugUnlock(port, multi, transport, local_unlockKey)
        
        return retval
    # end of openTestEngineDebugUnlock


    def openTestEngineDebugTrans(self, trans: str, multi: int) -> int:
        r"""Function TestEngine::openTestEngineDebugTrans() wrapper for openTestEngineDebugTrans in TestEngine DLL.

        Python API:
            openTestEngineDebugTrans(trans: str, multi: int) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngineDebugTrans(trans='abc', multi=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngineDebugTrans(const char* trans, int32 multi)

            Parameters :    trans -
                                String of space separated transport options that define the
                                transport to use. Commonly used options include:
                                <table>
                                    <tr><td>SPITRANS (The physical transport to use, e.g. LPT,
                                                      USB, TRB, USBDBG)
                                    <tr><td>SPIPORT (The port number)
                                </table>
                                E.g. for LPT1, trans would be "SPITRANS=LPT SPIPORT=1".
                                <p>
                                SPIPORT enumeration numbers start from 0 for the USBSPI
                                transport and from 1 for all other transports. For transports
                                other than LPTSPI, the serial number (or, in the case of
                                USBDBG, the port identifier of the corresponding USB Hub
                                Filter) may be used as an alternative to the SPIPORT
                                enumeration number. For further details of TRB and USBDBG
                                device identifiers, refer to CS-00410202-UG.
                                <p>
                                These options override any environment variables of the same
                                names. The transport string may be one of those returned by
                                teGetAvailableDebugPorts, which returns transport strings for
                                all available debug ports.

                            multi -
                                A gate on a multi-SPI interface. Set to zero for TRB and
                                USBDBG transports, and when communicating with a single device
                                attached to a standard LPTSPI or USBSPI port. When using the
                                gang programmer hardware, set to 0 - 15 to select the device
                                to connect to (the transport parameter must be DEBUG_LPTSPI in
                                this case).

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin.
                            <p>
                            This function, and openTestEngineDebug opens a debug connection
                            for devices which are not transport-locked. To open a debug
                            connection with transport-locked devices, use
                            openTestEngineDebugUnlock. To open a host transport connection,
                            use openTestEngine.
                            <p>
                            The trans string may be one of those returned by
                            teGetAvailableDebugPorts, which returns transport strings for all
                            available debug ports.
                            <p>
                            Note that over a SPI transport the function set is limited to
                            bccmd*, radiotest*, and hq* functions. HQ functions (and radiotest
                            functions that generate HQ traffic) are only supported if the
                            BlueCore firmware supports HQ over SPI. Commands which are not
                            supported will return TE_UNSUPPORTED_FUNCTION.

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* pPortsStr = new char[maxLen];
                char* pTransStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USB TRB (151134)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=TRB SPIPORT=1")

                int32 status = teGetAvailableDebugPorts(&maxLen, pPortsStr, pTransStr, &count);
                if (status != TE_OK && maxLen != 0)
                {
                    // Not enough space - resize the storage
                    delete[] pPortsStr;
                    pPortsStr = new char[maxLen];
                    delete[] pTransStr;
                    pTransStr = new char[maxLen];
                    status = teGetAvailableDebugPorts(&maxLen, pPortsStr, pTransStr, &count);
                }
                if (status != TE_OK || count == 0)
                {
                    cout << "Error getting debug ports, or none found" << endl;
                    delete[] pPortsStr;
                    delete[] pTransStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, pPortsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, pTransStr, ','); // Use these to open a transport

                // Open the debug port using the trans string
                // For the purposes of this example, we're just using the first in the list
                uint32 teHandle = openTestEngineDebugTrans(trans.at(0).c_str(), 0);
                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

                delete[] pPortsStr;
                delete[] pTransStr;

        """
        self.TestEngineDLL.openTestEngineDebugTrans.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngineDebugTrans.argtypes = [ct.c_char_p, ct.c_int32]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        retval = self.TestEngineDLL.openTestEngineDebugTrans(local_trans, multi)
        
        return retval
    # end of openTestEngineDebugTrans


    def openTestEngineDebugUnlockTrans(self, trans: str, multi: int, unlockKey: str) -> int:
        r"""Function TestEngine::openTestEngineDebugUnlockTrans() wrapper for openTestEngineDebugUnlockTrans in TestEngine DLL.

        Python API:
            openTestEngineDebugUnlockTrans(trans: str, multi: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.openTestEngineDebugUnlockTrans(trans='abc', multi=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 openTestEngineDebugUnlockTrans(const char* trans,
                                                                  int32 multi,
                                                                  const char* unlockKey)

            Parameters :    trans -
                                String of space separated transport options that define the
                                transport to use. Commonly used options include:
                                <table>
                                    <tr><td>SPITRANS (The physical transport to use, e.g. LPT,
                                                      USB, TRB, USBDBG)
                                    <tr><td>SPIPORT (The port number)
                                </table>
                                E.g. for LPT1, trans would be "SPITRANS=LPT SPIPORT=1".
                                <p>
                                SPIPORT enumeration numbers start from 0 for the USBSPI
                                transport and from 1 for all other transports. For transports
                                other than LPTSPI, the serial number (or, in the case of
                                USBDBG, the port identifier of the corresponding USB Hub
                                Filter) may be used as an alternative to the SPIPORT
                                enumeration number. For further details of TRB and USBDBG
                                device identifiers, refer to CS-00410202-UG.
                                <p>
                                These options override any environment variables of the same
                                names. The transport string may be one of those returned by
                                teGetAvailableDebugPorts, which returns transport strings for
                                all available debug ports.

                            multi -
                                A gate on a multi-SPI interface. Set to zero for TRB and
                                USBDBG transports, and when communicating with a single device
                                attached to a standard LPTSPI or USBSPI port. When using the
                                gang programmer hardware, set to 0 - 15 to select the device
                                to connect to (the transport parameter must be DEBUG_LPTSPI in
                                this case).

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".

            Returns :       This function will return TE_INVALID_HANDLE_VALUE on failure or an
                            unsigned integer which defines the handle used as a parameter for
                            all other function calls.

            Description :   One of the openTestEngine* set of functions has to be called
                            before any communication with the device can begin. Function
                            openTestEngineDebugUnlock can be used instead.
                            <p>
                            To be used (only) to open a debug connection to a transport-locked
                            chip. If openTestEngineDebugUnlockTrans is used to open the test
                            connection, then the functions bccmdSetWarmReset and
                            bccmdSetColdReset (for BlueCore ICs), and teChipReset (for CDA
                            ICs) will automatically use the same unlock code as
                            openTestEngineDebugUnlockTrans when re-establishing connection
                            with the chip.
                            <p>
                            openTestEngineDebug or openTestEngineDebugTrans should be used to
                            open a debug connection with a device which is not transport
                            locked. To open a host transport connection, use openTestEngine.
                            <p>
                            The trans string may be one of those returned by
                            teGetAvailableDebugPorts, which returns transport strings for all
                            available debug ports.
                            <p>
                            Note that over a SPI transport the function set is limited to
                            bccmd*, radiotest*, and hq* functions. HQ functions (and radiotest
                            functions that generate HQ traffic) are only supported if the
                            BlueCore firmware supports HQ over SPI. Commands which are not
                            supported will return TE_UNSUPPORTED_FUNCTION.

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* pPortsStr = new char[maxLen];
                char* pTransStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USB TRB (151134)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=TRB SPIPORT=1")

                int32 status = teGetAvailableDebugPorts(&maxLen, pPortsStr, pTransStr, &count);
                if (status != TE_OK && maxLen != 0)
                {
                    // Not enough space - resize the storage
                    delete[] pPortsStr;
                    pPortsStr = new char[maxLen];
                    delete[] pTransStr;
                    pTransStr = new char[maxLen];
                    status = teGetAvailableDebugPorts(&maxLen, pPortsStr, pTransStr, &count);
                }
                if (status != TE_OK || count == 0)
                {
                    cout << "Error getting debug ports, or none found" << endl;
                    delete[] pPortsStr;
                    delete[] pTransStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, pPortsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, pTransStr, ','); // Use these to open a transport

                // Open the debug port using the trans string
                // For the purposes of this example, we're just using the first in the list
                uint32 teHandle = openTestEngineDebugUnlockTrans(trans.at(0).c_str(), 0,
                                                                 "01234567890123456789012345678901");

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

                delete[] pPortsStr;
                delete[] pTransStr;

        """
        self.TestEngineDLL.openTestEngineDebugUnlockTrans.restype = ct.c_uint32
        self.TestEngineDLL.openTestEngineDebugUnlockTrans.argtypes = [ct.c_char_p, ct.c_int32, ct.c_char_p]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestEngineDLL.openTestEngineDebugUnlockTrans(local_trans, multi, local_unlockKey)
        
        return retval
    # end of openTestEngineDebugUnlockTrans


    def closeTestEngine(self, handle: int) -> int:
        r"""Function TestEngine::closeTestEngine() wrapper for closeTestEngine in TestEngine DLL.

        Python API:
            closeTestEngine(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.closeTestEngine(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 closeTestEngine(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function, or closeTestEngineEx, should always be called when
                            terminating communications with the device. On the TRB or USBDBG
                            transports this function will reset the device, relocking
                            the transport if applicable.
                            For other transports this function will NOT issue a reset.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.closeTestEngine.restype = ct.c_int32
        self.TestEngineDLL.closeTestEngine.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.closeTestEngine(handle)
        
        return retval
    # end of closeTestEngine


    def closeTestEngineEx(self, handle: int, options: int) -> int:
        r"""Function TestEngine::closeTestEngineEx() wrapper for closeTestEngineEx in TestEngine DLL.

        Python API:
            closeTestEngineEx(handle: int, options: int) -> int

        Python Example Call Syntax:
            retval = myDll.closeTestEngineEx(handle=0, options=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 closeTestEngineEx(uint32 handle, uint16 options)

            Parameters :    handle -
                                Handle to the device.

                            options -
                                Option for close, where supported values are:
                                <table>
                                    <tr><td>TE_CLOSE_EX_RESET_RELOCK_NO_WAIT
                                    <tr><td>TE_CLOSE_EX_RESET_RELOCK_WAIT
                                    <tr><td>TE_CLOSE_EX_NO_RESET_NO_RELOCK
                                </table>
                                <p>
                                TE_CLOSE_EX_RESET_RELOCK_NO_WAIT causes the same behaviour as
                                closeTestEngine, resetting and relocking the transport if
                                applicable, and is recommended for most circumstances.
                                <p>
                                TE_CLOSE_EX_RESET_RELOCK_WAIT causes reset and relock of the
                                transport if applicable, with the function waiting before
                                returning for the estimated time taken for the device to come
                                out of reset and re-enumerate (in the case of USBDBG). No
                                check is made on the state of the device after the wait
                                period. This option is recommended if the device is to be
                                connected to again after closing with this or another
                                API/tool, and reset is required before subsequent operations.
                                <p>
                                TE_CLOSE_EX_NO_RESET_NO_RELOCK skips reset and relock, and can
                                be used if the device is to be connected to again after
                                closing with this or another API/tool, and reset is not
                                required before subsequent operations.
                                <p>
                                NOTE: Reset is only performed for devices connected over TRB
                                or USBDBG (for other transports only a transport relock is
                                performed if applicable for TE_CLOSE_EX_RESET_RELOCK_NO_WAIT
                                and TE_CLOSE_EX_RESET_RELOCK_WAIT).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function, or closeTestEngine, should always be called when
                            terminating communications with the device.
                            <p>
                            NOTES: Skipping reset and relock can leave the transports
                            unlocked until the device is disconnected and/or power cycled
                            (which may never happen for a battery powered device).
                            Some TestEngine functions can put the device into a state where a
                            reset is required before normal operations can resume, e.g. 
                            teAppDisable. In addition, if device configuration settings are
                            updated, a reset is usually required for these to take effect.

            Example :

                uint32 dutHandle = openTestEngineDebugUnlock(1, 0, DEBUG_USBDBG,
                    "00000000000000000000000000000000");
                if (dutHandle == TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Failed to connect to device under test" << endl;
                    return;
                }

                cout << "Connected!" << endl;

                // Perform all your testing here

                closeTestEngineEx(dutHandle, TE_CLOSE_EX_RESET_RELOCK_NO_WAIT);

        """
        self.TestEngineDLL.closeTestEngineEx.restype = ct.c_int32
        self.TestEngineDLL.closeTestEngineEx.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.closeTestEngineEx(handle, options)
        
        return retval
    # end of closeTestEngineEx


    def teGetLastError(self, handle: int) -> int:
        r"""Function TestEngine::teGetLastError() wrapper for teGetLastError in TestEngine DLL.

        Python API:
            teGetLastError(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.teGetLastError(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 teGetLastError(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       Last reported error code. If this value is zero then no error was
                            reported. A non-zero value signifies an error and the value is
                            decoded as follows:
                            <table>
                                <tr><td>Byte 1 (0x000000ff) = BCCMD error
                                <tr><td>Byte 2 (0x0000ff00) = Reserved
                                <tr><td>Byte 3 (0x00ff0000) = HCI / DM error
                                <tr><td>Byte 4 (0xff000000) = Reserved
                            </table>
                            <p>
                            BCCMD errors are defined as:
                            <table>
                                <tr><td>0 = No error
                                <tr><td>1 = BCCMD command ID not supported
                                <tr><td>2 = Data exceeded
                                <tr><td>3 = Variable has no value
                                <tr><td>4 = Get or set command held an error
                                <tr><td>5 = Value inaccessible
                                <tr><td>6 = Unwriteable
                                <tr><td>7 = Unreadable
                                <tr><td>8 = Other error
                                <tr><td>9 = Request not allowed
                            </table>
                            <p>
                            HCI / DM errors are defined in the Bluetooth specification.

            Description :   This function can be called to obtain a more detailed error
                            description when a TestEngine function fails.
                            <p>
                            The return value of this function should not be relied upon unless
                            the preceding TestEngine function call returned 0 (for failure).
                            <p>
                            Error codes in the format returned by this function are defined at
                            the top of TestEngine.h.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    int32 teRet = bccmdChargerPsuTrim(teHandle, 15);

                    if (teRet == TE_INVALID_HANDLE)
                    {
                        cout << "Invalid teHandle" << endl;
                    }
                    else if (teRet == TE_UNSUPPORTED_FUNCTION)
                    {
                        cout << "Unsupported function" << endl;
                    }
                    else if (teRet == TE_ERROR)
                    {
                        uint32 teError = teGetLastError(teHandle);
                        // Handle teError
                    }
                    else
                    {
                        cout << "Command teRet" << endl;
                        // Perform all your testing here
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teGetLastError.restype = ct.c_uint32
        self.TestEngineDLL.teGetLastError.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.teGetLastError(handle)
        
        return retval
    # end of teGetLastError


    def bccmdSetColdReset(self, handle: int, usbTimeout: int) -> int:
        r"""Function TestEngine::bccmdSetColdReset() wrapper for bccmdSetColdReset in TestEngine DLL.

        Python API:
            bccmdSetColdReset(handle: int, usbTimeout: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetColdReset(handle=0, usbTimeout=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetColdReset(uint32 handle, int32 usbTimeout)

            Parameters :    handle -
                                Handle to the device.

                            usbTimeout -
                                Where transport = USB, this parameter will define the timeout
                                to allow the USB device to enumerate if it has not already
                                enumerated. It has been found that some PC's take a longer
                                time than expected to enumerate a USB device and, in some
                                cases, the PC's internal USB hub may have been reset which can
                                cause a further delay in enumeration. This parameter can be
                                set to accommodate the extra time taken to reset USB devices.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command forces a hardware reset of BlueCore ICs, deliberately
                            discarding all of its current state - the command emulates removing
                            power from the chip, then restoring it. It will attempt to
                            reinitialise communication using the same transport settings as
                            declared in openTestEngine*. If the reset or the
                            re-establishment fails the objects associated with the
                            communication stack will be deleted.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types teChipReset should be used.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    do
                    {
                        cout << "Connected!" << endl;

                        int32 teRet = psWriteVmDisable(teHandle, 1);
                        if (teRet != TE_OK)
                        {
                            cout << "psWriteVmDisable error" << endl;
                            break;
                        }

                        teRet = bccmdSetColdReset(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdSetColdReset error" << endl;
                            break;
                        }

                        teRet = hciSlave(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "hciSlave error" << endl;
                            if (teRet == TE_UNSUPPORTED_FUNCTION)
                            {
                                cout << "Unsupported command - if using RFCOMM build use dmSlave instead"
                                     << endl;
                            }
                            break;
                        }

                        teRet = hciEnableDeviceUnderTestMode(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "hciEnableDeviceUnderTestMode error" << endl;
                            if (teRet == TE_UNSUPPORTED_FUNCTION)
                            {
                                cout << "Unsupported command - if using RFCOMM build use dmEnableDeviceUnderTestMode instead"
                                     << endl;
                            }
                            break;
                        }

                        // PERFORM TESTING HERE.....
                        cout << "TESTING.........." << endl;

                        teRet = psWriteVmDisable(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "psWriteVmDisable error" << endl;
                            break;
                        }

                        teRet = bccmdSetColdReset(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdSetColdReset error" << endl;
                            break;
                        }

                    } while(0);

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdSetColdReset.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetColdReset.argtypes = [ct.c_uint32, ct.c_int32]
        
        retval = self.TestEngineDLL.bccmdSetColdReset(handle, usbTimeout)
        
        return retval
    # end of bccmdSetColdReset


    def bccmdSetWarmReset(self, handle: int, usbTimeout: int) -> int:
        r"""Function TestEngine::bccmdSetWarmReset() wrapper for bccmdSetWarmReset in TestEngine DLL.

        Python API:
            bccmdSetWarmReset(handle: int, usbTimeout: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetWarmReset(handle=0, usbTimeout=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetWarmReset(uint32 handle, int32 usbTimeout)

            Parameters :    handle -
                                Handle to the device.

                            usbTimeout -
                                Where transport = USB, this parameter will define the timeout
                                to allow the USB device to enumerate if it has not already
                                enumerated. It has been found that some PC's take a longer
                                time than expected to enumerate a USB device and, in some
                                cases, the PC's internal USB hub may have been reset which can
                                cause a further delay in enumeration. This parameter can be
                                set to accommodate the extra time taken to reset USB devices.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This forces a hardware reset of the BlueCore ICs, arranging that
                            some elements of the chip's current state may be available when
                            the chip is restarted, assuming the chip remains powered through
                            the reset. It will then attempt to reinitialise communication
                            using the same transport settings as declared in openTestEngine*.
                            If the reset or the re-establishment fails the objects associated
                            with the communication stack will be deleted.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types teChipReset should be used.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    do
                    {
                        cout << "Connected!" << endl;

                        int32 teRet = psWriteVmDisable(teHandle, 1);
                        if (teRet != TE_OK)
                        {
                            cout << "psWriteVmDisable error" << endl;
                            break;
                        }

                        teRet = bccmdSetWarmReset(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdSetWarmReset error" << endl;
                            break;
                        }

                        teRet = hciSlave(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "hciSlave error" << endl;
                            if (teRet == TE_UNSUPPORTED_FUNCTION)
                            {
                                cout << "Unsupported command - if using RFCOMM build use dmSlave instead"
                                     << endl;
                            }
                            break;
                        }

                        teRet = hciEnableDeviceUnderTestMode(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "hciEnableDeviceUnderTestMode error" << endl;
                            if (teRet == TE_UNSUPPORTED_FUNCTION)
                            {
                                cout << "Unsupported command - if using RFCOMM build use dmEnableDeviceUnderTestMode instead"
                                     << endl;
                            }
                            break;
                        }

                        // PERFORM TESTING HERE.....
                        cout << "TESTING.........." << endl;

                        teRet = psWriteVmDisable(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "psWriteVmDisable error" << endl;
                            break;
                        }

                        teRet = bccmdSetWarmReset(teHandle, 0);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdSetWarmReset error" << endl;
                            break;
                        }

                    } while(0);

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdSetWarmReset.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetWarmReset.argtypes = [ct.c_uint32, ct.c_int32]
        
        retval = self.TestEngineDLL.bccmdSetWarmReset(handle, usbTimeout)
        
        return retval
    # end of bccmdSetWarmReset


    def radiotestPause(self, handle: int) -> int:
        r"""Function TestEngine::radiotestPause() wrapper for radiotestPause in TestEngine DLL.

        Python API:
            radiotestPause(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPause(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPause(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will cause any radiotests running to terminate.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestPause.restype = ct.c_int32
        self.TestEngineDLL.radiotestPause.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestPause(handle)
        
        return retval
    # end of radiotestPause


    def radiotestDeepSleep(self, handle: int) -> int:
        r"""Function TestEngine::radiotestDeepSleep() wrapper for radiotestDeepSleep in TestEngine DLL.

        Python API:
            radiotestDeepSleep(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestDeepSleep(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestDeepSleep(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will cause the DUT to enter deep sleep.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestDeepSleep.restype = ct.c_int32
        self.TestEngineDLL.radiotestDeepSleep.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestDeepSleep(handle)
        
        return retval
    # end of radiotestDeepSleep


    def radiotestPcmExtLb(self, handle: int, pcmMode: int) -> int:
        r"""Function TestEngine::radiotestPcmExtLb() wrapper for radiotestPcmExtLb in TestEngine DLL.

        Python API:
            radiotestPcmExtLb(handle: int, pcmMode: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmExtLb(handle=0, pcmMode=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmExtLb(uint32 handle, uint16 pcmMode)

            Parameters :    handle -
                                Handle to the device.

                            pcmMode -
                                Can be:
                                <table>
                                    <tr><td>0  Slave in normal 4-wire configuration
                                    <tr><td>1  Master in normal 4-wire configuration
                                    <tr><td>2  Master in Alcatel-specific 2-wire configuration
                                </table>
                                <p>
                                For a "normal" loopback configuration pcmMode should be 1.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command enables PCM external loopback test mode in which a
                            block of random data is written to the PCM output port and is read
                            back again on the PCM input port. A check is made that the data
                            matches. External wiring must be provided between the
                            corresponding pins.
                            <p>
                            This function is supported for BlueCore ICs only. For CSRC9xxx
                            ICs and BlueCore ICs with multiple PCM ports use
                            radiotestPcmExtLbIf.

        """
        self.TestEngineDLL.radiotestPcmExtLb.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmExtLb.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmExtLb(handle, pcmMode)
        
        return retval
    # end of radiotestPcmExtLb


    def radiotestPcmExtLbIf(self, handle: int, pcmMode: int, pcmIf: int) -> int:
        r"""Function TestEngine::radiotestPcmExtLbIf() wrapper for radiotestPcmExtLbIf in TestEngine DLL.

        Python API:
            radiotestPcmExtLbIf(handle: int, pcmMode: int, pcmIf: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmExtLbIf(handle=0, pcmMode=0, pcmIf=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmExtLbIf(uint32 handle, uint16 pcmMode,
                                                      uint16 pcmIf)

            Parameters :    handle -
                                Handle to the device.

                            pcmMode -
                                Can be:
                                <table>
                                    <tr><td>0  Slave in normal 4-wire configuration
                                    <tr><td>1  Master in normal 4-wire configuration
                                    <tr><td>2  Master in Alcatel-specific 2-wire configuration
                                </table>
                                <p>
                                For a "normal" loopback configuration pcmMode should be 1.
                                <p>
                                This parameter is ignored for CSRC9xxx ICs.

                            pcmIf -
                                Selects the PCM interface:
                                <table>
                                    <tr><td>0  PCM1
                                    <tr><td>1  PCM2
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command enables PCM external loopback test mode in which a
                            block of random data is written to the PCM output port and is read
                            back again on the PCM input port. A check is made that the data
                            matches. External wiring must be provided between the
                            corresponding pins.
                            <p>
                            This function is supported for BlueCore and CSRC9xxx ICs only.
                            <p>
                            For BlueCore ICs, this function should be supported in firmware
                            from version 25a onwards. Use radiotestPcmExtLb if the firmware is
                            older.

        """
        self.TestEngineDLL.radiotestPcmExtLbIf.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmExtLbIf.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmExtLbIf(handle, pcmMode, pcmIf)
        
        return retval
    # end of radiotestPcmExtLbIf


    def radiotestPcmLb(self, handle: int, pcmMode: int) -> int:
        r"""Function TestEngine::radiotestPcmLb() wrapper for radiotestPcmLb in TestEngine DLL.

        Python API:
            radiotestPcmLb(handle: int, pcmMode: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmLb(handle=0, pcmMode=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmLb(uint32 handle, uint16 pcmMode)

            Parameters :    handle -
                                Handle to the device.

                            pcmMode -
                                Can be:
                                <table>
                                    <tr><td>0  Slave in normal 4-wire configuration
                                    <tr><td>1  Master in normal 4-wire configuration
                                    <tr><td>2  Master in Alcatel-specific 2-wire configuration
                                </table>
                                <p>
                                For a "normal" loopback configuration pcmMode should be 1.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command enables PCM LOOPBACK test mode in which data read
                            from the PCM input port is written back out again via the pulse
                            code modulation (PCM) output port after a delay.
                            <p>
                            This function is supported for BlueCore ICs only. For CSRC9xxx
                            ICs and BlueCore ICs with multiple PCM ports use radiotestPcmLbIf.

        """
        self.TestEngineDLL.radiotestPcmLb.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmLb.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmLb(handle, pcmMode)
        
        return retval
    # end of radiotestPcmLb


    def radiotestPcmLbIf(self, handle: int, pcmMode: int, pcmIf: int) -> int:
        r"""Function TestEngine::radiotestPcmLbIf() wrapper for radiotestPcmLbIf in TestEngine DLL.

        Python API:
            radiotestPcmLbIf(handle: int, pcmMode: int, pcmIf: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmLbIf(handle=0, pcmMode=0, pcmIf=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmLbIf(uint32 handle, uint16 pcmMode,
                                                   uint16 pcmIf)

            Parameters :    handle -
                                Handle to the device.

                            pcmMode -
                                Can be:
                                <table>
                                    <tr><td>0  Slave in normal 4-wire configuration
                                    <tr><td>1  Master in normal 4-wire configuration
                                    <tr><td>2  Master in Alcatel-specific 2-wire configuration
                                </table>
                                <p>
                                For a "normal" loopback configuration pcmMode should be 1.
                                <p>
                                This parameter is ignored for CSRC9xxx ICs.

                            pcmIf -
                                Selects the PCM interface:
                                <table>
                                    <tr><td>0  PCM1
                                    <tr><td>1  PCM2
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command enables PCM LOOPBACK test mode in which data read
                            from the PCM input port is written back out again via the pulse
                            code modulation (PCM) output port after a delay.
                            <p>
                            This function is supported for BlueCore and CSRC9xxx ICs only.
                            <p>
                            For BlueCore ICs, this function should be supported in firmware
                            from version 25a onwards. Use radiotestPcmLb if the firmware is
                            older.

        """
        self.TestEngineDLL.radiotestPcmLbIf.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmLbIf.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmLbIf(handle, pcmMode, pcmIf)
        
        return retval
    # end of radiotestPcmLbIf


    def radiotestPcmTimingIn(self, handle: int, pioOut: int, pcmIn: int) -> int:
        r"""Function TestEngine::radiotestPcmTimingIn() wrapper for radiotestPcmTimingIn in TestEngine DLL.

        Python API:
            radiotestPcmTimingIn(handle: int, pioOut: int, pcmIn: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmTimingIn(handle=0, pioOut=0, pcmIn=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmTimingIn(uint32 handle, uint16 pioOut,
                                                       uint16 pcmIn)

            Parameters :    handle -
                                Handle to the device.

                            pioOut -
                                0 to 7, PIO pin used for writing.

                            pcmIn -
                                PCM pin used for reading where:
                                <table>
                                    <tr><td>0  PCM_SYNC
                                    <tr><td>1  PCM_CLK
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command is similar to PCM_EXT_LB: this makes a series of
                            writes to a PIO pin and tests that the result is readable on one
                            of the PCM pins used for timing in slave mode, PCM_SYNC and
                            PCM_CLK.
                            A check is made that the data matches. External wiring must be
                            provided between the corresponding pins.
                            <p>
                            This function is supported for BlueCore ICs only. For BlueCore ICs
                            with multiple PCM ports use radiotestPcmTimingInIf.

        """
        self.TestEngineDLL.radiotestPcmTimingIn.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmTimingIn.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmTimingIn(handle, pioOut, pcmIn)
        
        return retval
    # end of radiotestPcmTimingIn


    def radiotestPcmTimingInIf(self, handle: int, pioOut: int, pcmIn: int, pcmIf: int) -> int:
        r"""Function TestEngine::radiotestPcmTimingInIf() wrapper for radiotestPcmTimingInIf in TestEngine DLL.

        Python API:
            radiotestPcmTimingInIf(handle: int, pioOut: int, pcmIn: int, pcmIf: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmTimingInIf(handle=0, pioOut=0, pcmIn=0, pcmIf=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmTimingInIf(uint32 handle, uint16 pioOut,
                                                         uint16 pcmIn, uint16 pcmIf)

            Parameters :    handle -
                                Handle to the device.

                            pioOut -
                                0 to 7, PIO pin used for writing.

                            pcmIn -
                                PCM pin used for reading where:
                                <table>
                                    <tr><td>0  PCM_SYNC
                                    <tr><td>1  PCM_CLK
                                </table>

                            pcmIf -
                                Selects the PCM interface:
                                <table>
                                    <tr><td>0  PCM1
                                    <tr><td>1  PCM2
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command is similar to PCM_EXT_LB_IF: this makes a series of
                            writes to a PIO pin and tests that the result is readable on one
                            of the PCM pins used for timing in slave mode, PCM_SYNC and
                            PCM_CLK.
                            A check is made that the data matches. External wiring must be
                            provided between the corresponding pins.
                            <p>
                            This function is supported for BlueCore ICs only.
                            <p>
                            This function should be supported in BlueCore firmware from
                            version 25a onwards. Use radiotestPcmTimingIn if the firmware is
                            older.

        """
        self.TestEngineDLL.radiotestPcmTimingInIf.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmTimingInIf.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmTimingInIf(handle, pioOut, pcmIn, pcmIf)
        
        return retval
    # end of radiotestPcmTimingInIf


    def radiotestPcmTone(self, handle: int, freq: int, ampl: int, dc: int) -> int:
        r"""Function TestEngine::radiotestPcmTone() wrapper for radiotestPcmTone in TestEngine DLL.

        Python API:
            radiotestPcmTone(handle: int, freq: int, ampl: int, dc: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmTone(handle=0, freq=0, ampl=0, dc=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmTone(uint32 handle, uint16 freq, uint16 ampl,
                                                   uint16 dc)

            Parameters :    handle -
                                Handle to the device.

                            freq -
                                Controls the frequency of the sine wave. The value 0
                                corresponds to 250Hz; each increment of 1 doubles the
                                frequency. Hence, 1 corresponds to 500Hz, 2 to 1kHz and so on.
                                No bounds checking is performed on the parameter, but large
                                values will not be useful owing to hardware limitations.

                            ampl -
                                Controls the amplitude of the sine wave. 8 is full volume;
                                Each decrement of 1 reduces the amplitude by a factor of 2.
                                0 is valid and causes the hardware to be activated with
                                constant audio data.

                            dc -
                                Constant offset to be added to the audio data.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command outputs a sine wave to the PCM port. For chips with
                            stereo codecs, use radiotestPcmToneStereo instead.
                            <p>
                            PSKEY_HOSTIO_MAP_SCO_CODEC must be set to 1 for this function to
                            successfully generate audio through the codec.
                            <p>
                            This function is supported for BlueCore ICs only. For CSRC9xxx
                            ICs and BlueCore ICs with multiple PCM ports use
                            radiotestPcmToneIf. For other IC types the teAudio* functions
                            should be used.

        """
        self.TestEngineDLL.radiotestPcmTone.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmTone.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmTone(handle, freq, ampl, dc)
        
        return retval
    # end of radiotestPcmTone


    def radiotestPcmToneIf(self, handle: int, freq: int, ampl: int, dc: int, pcmIf: int) -> int:
        r"""Function TestEngine::radiotestPcmToneIf() wrapper for radiotestPcmToneIf in TestEngine DLL.

        Python API:
            radiotestPcmToneIf(handle: int, freq: int, ampl: int, dc: int, pcmIf: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmToneIf(handle=0, freq=0, ampl=0, dc=0, pcmIf=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmToneIf(uint32 handle, uint16 freq, uint16 ampl,
                                                     uint16 dc, uint16 pcmIf)

            Parameters :    handle -
                                Handle to the device.

                            freq -
                                Controls the frequency of the sine wave. The value 0
                                corresponds to 250Hz; each increment of 1 doubles the
                                frequency. Hence, 1 corresponds to 500Hz, 2 to 1kHz and so on.
                                No bounds checking is performed on the parameter, but large
                                values will not be useful owing to hardware limitations.

                            ampl -
                                Controls the amplitude of the sine wave. 8 is full volume;
                                Each decrement of 1 reduces the amplitude by a factor of 2.
                                0 is valid and causes the hardware to be activated with
                                constant audio data.

                            dc -
                                Constant offset to be added to the audio data.
                                <p>
                                This parameter is ignored for CSRC9xxx ICs.

                            pcmIf -
                                Selects the PCM interface:
                                <table>
                                    <tr><td>0  PCM1
                                    <tr><td>1  PCM2
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command outputs a sine wave to the PCM port. For chips with
                            stereo codecs, use radiotestPcmToneStereo instead.
                            <p>
                            PSKEY_HOSTIO_MAP_SCO_CODEC must be set to 1 for this function to
                            successfully generate audio through the codec.
                            <p>
                            This function is supported for BlueCore and CSRC9xxx ICs only.
                            For other IC types the teAudio* functions should be used.
                            <p>
                            For BlueCore ICs, this function should be supported in firmware
                            from version 25a onwards. Use radiotestPcmTone if the firmware is
                            older.

        """
        self.TestEngineDLL.radiotestPcmToneIf.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmToneIf.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmToneIf(handle, freq, ampl, dc, pcmIf)
        
        return retval
    # end of radiotestPcmToneIf


    def radiotestPcmToneStereo(self, handle: int, freq: int, ampl: int, dc: int, channel: int) -> int:
        r"""Function TestEngine::radiotestPcmToneStereo() wrapper for radiotestPcmToneStereo in TestEngine DLL.

        Python API:
            radiotestPcmToneStereo(handle: int, freq: int, ampl: int, dc: int, channel: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestPcmToneStereo(handle=0, freq=0, ampl=0, dc=0, channel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestPcmToneStereo(uint32 handle, uint16 freq,
                                                         uint16 ampl, uint16 dc,
                                                         uint16 channel)

            Parameters :    handle -
                                Handle to the device.

                            freq -
                                Controls the frequency of the sine wave. The value 0
                                corresponds to 250Hz; each increment of 1 doubles the
                                frequency. Hence, 1 corresponds to 500Hz, 2 to 1kHz and so on.
                                No bounds checking is performed on the parameter, but large
                                values will not be useful owing to hardware limitations.

                            ampl -
                                Controls the amplitude of the sine wave. 8 is full volume;
                                Each decrement of 1 reduces the amplitude by a factor of 2.
                                0 is valid and causes the hardware to be activated with
                                constant audio data.

                            dc -
                                Constant offset to be added to the audio data.

                            channel -
                                Controls the channel(s) on which the sine wave is output,
                                where:
                                <table>
                                    <tr><td>0 = Both (L & R)
                                    <tr><td>1 = Left only
                                    <tr><td>2 = Right only
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command outputs a sine wave to the PCM port on either one, or
                            both stereo channels. Requires a BlueCore chip with a stereo
                            codec. For mono chips, use radiotestPcmTone.
                            <p>
                            PSKEY_HOSTIO_MAP_SCO_CODEC must be set to 1 for this function to
                            successfully generate audio through the codec.
                            <p>
                            This function is supported for BlueCore and CSRC9xxx ICs only.
                            For other IC types the teAudio* functions should be used.

        """
        self.TestEngineDLL.radiotestPcmToneStereo.restype = ct.c_int32
        self.TestEngineDLL.radiotestPcmToneStereo.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestPcmToneStereo(handle, freq, ampl, dc, channel)
        
        return retval
    # end of radiotestPcmToneStereo


    def radiotestCtsRtsLb(self, handle: int) -> int:
        r"""Function TestEngine::radiotestCtsRtsLb() wrapper for radiotestCtsRtsLb in TestEngine DLL.

        Python API:
            radiotestCtsRtsLb(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCtsRtsLb(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCtsRtsLb(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command performs a series of writes to the UART CTS (clear to
                            send) line and attempts to read back the value written on the UART
                            RTS (ready to send) line. External wiring must be provided between
                            the corresponding pins.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCtsRtsLb.restype = ct.c_int32
        self.TestEngineDLL.radiotestCtsRtsLb.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestCtsRtsLb(handle)
        
        return retval
    # end of radiotestCtsRtsLb


    def radiotestRadioStatus(self, handle: int) -> int:
        r"""Function TestEngine::radiotestRadioStatus() wrapper for radiotestRadioStatus in TestEngine DLL.

        Python API:
            radiotestRadioStatus(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRadioStatus(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRadioStatus(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will request the current Bluetooth radio status
                            information. Once the command is issued the DUT needs to be polled
                            for the status using the hqGetRadioStatus function.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is deprecated. Use radiotestRadioStatusArray
                            instead.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.radiotestRadioStatus.restype = ct.c_int32
        self.TestEngineDLL.radiotestRadioStatus.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestRadioStatus(handle)
        
        return retval
    # end of radiotestRadioStatus


    def hqGetRadioStatus(self, handle: int, status: list, timeout: int) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetRadioStatus() wrapper for hqGetRadioStatus in TestEngine DLL.

        Python API:
            hqGetRadioStatus(handle: int, status: list, timeout: int) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, status = myDll.hqGetRadioStatus(handle=0, status=[0,1], timeout=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 hqGetRadioStatus(uint32 handle, uint16* status,
                                                   int32 timeout)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to an array of 7 unsigned 16-bit integers. These will
                                be used to store the radio status array as follows:
                                <table>
                                    <tr><td>Index Parameter<td>Type of Status Report
                                    <tr><td>0   <td>Internal transmission level
                                    <tr><td>1   <td>External transmission level
                                    <tr><td>2   <td>Reception level
                                    <tr><td>3   <td>Receiver's attenuation
                                    <tr><td>4   <td>Local oscillator level
                                    <tr><td>5   <td>IQ trim
                                    <tr><td>6   <td>Signal to image ratio in dB
                                </table>

                            timeout -
                                Used to specify a timeout, in ms, which the software will wait
                                for the HQ radio status packet to be returned from the DUT.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will wait for a time period specified by "timeout"
                            for the HQ radio status packet.
                            <p>
                            This function is deprecated. Use hqGetRadioStatusArray instead.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.hqGetRadioStatus.restype = ct.c_int32
        self.TestEngineDLL.hqGetRadioStatus.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_int32]
        if status == None:
            status = []
        local_status = (ct.c_uint16 * len(status))(*status)
        retval = self.TestEngineDLL.hqGetRadioStatus(handle, local_status, timeout)
        status = local_status[:]
        return retval, status
    # end of hqGetRadioStatus


    def radiotestRadioStatusArray(self, handle: int) -> int:
        r"""Function TestEngine::radiotestRadioStatusArray() wrapper for radiotestRadioStatusArray in TestEngine DLL.

        Python API:
            radiotestRadioStatusArray(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRadioStatusArray(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRadioStatusArray(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will request the current Bluetooth radio status
                            information. Once the command is issued the DUT needs to be polled
                            for the status using the hqGetRadioStatusArray function.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    uint16 status[10];

                    cout << "Connected!" << endl;

                    int32 teRet = radiotestRadioStatusArray(teHandle);
                    if (teRet == TE_OK)
                    {
                        timeoutMs = 1000;
                        do
                        {
                            teRet = hqGetRadioStatusArray(teHandle, status, 100);
                            timeoutMs -= 100;
                        } while (teRet == TE_ERROR && timeoutMs > 0);
                    }

                    if (teRet == TE_OK)
                    {
                        cout << "Internal transmission level = " << status[0] << endl;
                        cout << "External transmission level = " << status[1] << endl;
                        cout << "Reception level             = " << status[2] << endl;
                        cout << "Local oscillator level      = " << status[3] << endl;
                        cout << "IQ trim                     = " << status[4] << endl;
                        cout << "Signal to image ratio in dB = " << status[5] << endl;
                        cout << "Receiver's attenuation      = " << status[6] << endl;
                        cout << "Local oscillator amplitude  = " << status[7] << endl;
                        cout << "Frequency error             = " << status[8] << endl;
                        cout << "Receive frequency error     = " << status[9] << endl;
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.radiotestRadioStatusArray.restype = ct.c_int32
        self.TestEngineDLL.radiotestRadioStatusArray.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestRadioStatusArray(handle)
        
        return retval
    # end of radiotestRadioStatusArray


    def hqGetRadioStatusArray(self, handle: int, status: list, timeout: int) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetRadioStatusArray() wrapper for hqGetRadioStatusArray in TestEngine DLL.

        Python API:
            hqGetRadioStatusArray(handle: int, status: list, timeout: int) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, status = myDll.hqGetRadioStatusArray(handle=0, status=[0,1], timeout=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 hqGetRadioStatusArray(uint32 handle, uint16* status,
                                                        int32 timeout)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to an array of 10 unsigned 16-bit integers. These will
                                be used to store the radio status array as follows:
                                <table>
                                    <tr><td>Index Parameter<td>Type of Status Report
                                    <tr><td>0   <td>Internal transmission level
                                    <tr><td>1   <td>External transmission level
                                    <tr><td>2   <td>Reception level
                                    <tr><td>3   <td>Local oscillator level
                                    <tr><td>4   <td>IQ trim
                                    <tr><td>5   <td>Signal to image ratio in dB
                                    <tr><td>6   <td>Receiver's attenuation
                                    <tr><td>7   <td>Local oscillator amplitude
                                    <tr><td>8   <td>Frequency error
                                    <tr><td>9   <td>Receive frequency error
                                </table>

                            timeout -
                                Used to specify a timeout, in ms, which the software will wait
                                for the HQ radio status packets to be returned from the DUT.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will wait for a time period specified by "timeout"
                            for all of the HQ radio status array packets.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example code for radiotestRadioStatusArray.

        """
        self.TestEngineDLL.hqGetRadioStatusArray.restype = ct.c_int32
        self.TestEngineDLL.hqGetRadioStatusArray.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_int32]
        if status == None:
            status = []
        local_status = (ct.c_uint16 * len(status))(*status)
        retval = self.TestEngineDLL.hqGetRadioStatusArray(handle, local_status, timeout)
        status = local_status[:]
        return retval, status
    # end of hqGetRadioStatusArray


    def bccmdMemoryGet(self, handle: int, baseAddr: int, dataLength: int, data: list) -> Tuple[int, list]:
        r"""Function TestEngine::bccmdMemoryGet() wrapper for bccmdMemoryGet in TestEngine DLL.

        Python API:
            bccmdMemoryGet(handle: int, baseAddr: int, dataLength: int, data: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, data = myDll.bccmdMemoryGet(handle=0, baseAddr=0, dataLength=0, data=[0,1])
            print(retval, data)

        Detail From Wrapped C API:
            Function :      int32 bccmdMemoryGet(uint32 handle, uint16 baseAddr,
                                                 uint16 dataLength, uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            baseAddr -
                                Address to read data from.

                            dataLength -
                                Length (in words) of the array pointed to by data. The
                                function can retrieve a maximum of 48 words.

                            data -
                                Pointer to an array of words to retrieve contents of memory.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to read the contents of memory.
                            <p>
                            Note that the data is specified in terms of 16-bit words and not
                            bytes.
                            <p>
                            <b>See also</b> bccmdMemorySet.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs. For earlier CDA ICs, this function can read memory in the
                            Bluetooth subsystem only.

        """
        self.TestEngineDLL.bccmdMemoryGet.restype = ct.c_int32
        self.TestEngineDLL.bccmdMemoryGet.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * max(dataLength, len(data)))(*data)
        retval = self.TestEngineDLL.bccmdMemoryGet(handle, baseAddr, dataLength, local_data)
        data = local_data[:]
        return retval, data
    # end of bccmdMemoryGet


    def bccmdMemorySet(self, handle: int, baseAddr: int, dataLength: int, data: list) -> int:
        r"""Function TestEngine::bccmdMemorySet() wrapper for bccmdMemorySet in TestEngine DLL.

        Python API:
            bccmdMemorySet(handle: int, baseAddr: int, dataLength: int, data: list) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdMemorySet(handle=0, baseAddr=0, dataLength=0, data=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdMemorySet(uint32 handle, uint16 baseAddr,
                                                 uint16 dataLength, const uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            baseAddr -
                                Address to write data to.

                            dataLength -
                                Length (in words) of the array pointed to by data. The
                                function can write a maximum of 48 words.

                            data -
                                Pointer to an array of words to write into memory.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to write the contents of memory. It
                            should be used with caution as writing to certain memory locations
                            may have unpleasant side effects.
                            <p>
                            Note that the data is specified in terms of 16-bit words and not
                            bytes.
                            <p>
                            <b>See also</b> bccmdMemoryGet.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs. For earlier CDA ICs, this function can write memory in the
                            Bluetooth subsystem only.

        """
        self.TestEngineDLL.bccmdMemorySet.restype = ct.c_int32
        self.TestEngineDLL.bccmdMemorySet.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.bccmdMemorySet(handle, baseAddr, dataLength, local_data)
        
        return retval
    # end of bccmdMemorySet


    def bccmdGetBuildId(self, handle: int, buildId: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetBuildId() wrapper for bccmdGetBuildId in TestEngine DLL.

        Python API:
            bccmdGetBuildId(handle: int, buildId: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, buildId = myDll.bccmdGetBuildId(handle=0)
            print(retval, buildId)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetBuildId(uint32 handle, uint16* buildId)

            Parameters :    handle -
                                Handle to the device.

                            buildId -
                                Pointer to a variable to hold the returned firmware build ID.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the Bluetooth firmware build ID.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs. For these ICs, or to retrieve the firmware build ID for other
                            subsystems, use teGetBuildId.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    uint16 val = 0;
                    cout << "Connected!" << endl;

                    int32 teRet = bccmdGetBuildId(teHandle, &val);
                    if (teRet == TE_OK)
                    {
                        cout << "Build id = " << val << endl;
                    }

                    teRet = bccmdGetChipVersion(teHandle, &val);
                    if (teRet == TE_OK)
                    {
                        cout << "Chip version = " << val << endl;
                    }

                    teRet = bccmdGetChipRevision(teHandle, &val);
                    if (teRet == TE_OK)
                    {
                        cout << "Chip revision = " << val << endl;
                    }

                    char name[MAX_LENGTH];
                    teRet = bccmdBuildName(teHandle, name, MAX_LENGTH, &val);
                    if (teRet == TE_OK)
                    {
                        cout << "Build name = " << name << endl;
                    }

                    // Perform other testing if necessary

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdGetBuildId.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetBuildId.argtypes = [ct.c_uint32, ct.c_void_p]
        local_buildId = ct.c_uint16(buildId)
        retval = self.TestEngineDLL.bccmdGetBuildId(handle, ct.byref(local_buildId))
        buildId = local_buildId.value
        return retval, buildId
    # end of bccmdGetBuildId


    def bccmdBuildName(self, handle: int, name: str='', maxLen: int=0, length: int=0) -> Tuple[int, str, int]:
        r"""Function TestEngine::bccmdBuildName() wrapper for bccmdBuildName in TestEngine DLL.

        Python API:
            bccmdBuildName(handle: int, name: str='', maxLen: int=0, length: int=0) -> Tuple[int, str, int]

        Python Example Call Syntax:
            retval, name, length = myDll.bccmdBuildName(handle=0, maxLen=0)
            print(retval, name, length)

        Detail From Wrapped C API:
            Function :      int32 bccmdBuildName(uint32 handle, char* name, uint16 maxLen,
                                                 uint16* length)

            Parameters :    handle -
                                Handle to the device.

                            name -
                                Pointer to an array to hold the returned firmware build ID. A
                                terminating null character will be added. If the array is not
                                large enough then the string will be truncated.

                            maxLen -
                                Length of the "name" array.

                            length -
                                Total length of the build name not including any NULL
                                character and assuming the string will not have been truncated.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the Bluetooth firmware build name.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for bccmdGetBuildId.

        """
        self.TestEngineDLL.bccmdBuildName.restype = ct.c_int32
        self.TestEngineDLL.bccmdBuildName.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_uint16, ct.c_void_p]
        local_name = None if name is None else ct.create_string_buffer(bytes(name, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_length = ct.c_uint16(length)
        retval = self.TestEngineDLL.bccmdBuildName(handle, local_name, maxLen, ct.byref(local_length))
        name = local_name.value.decode()
        length = local_length.value
        return retval, name, length
    # end of bccmdBuildName


    def bccmdGetChipVersion(self, handle: int, chipVer: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetChipVersion() wrapper for bccmdGetChipVersion in TestEngine DLL.

        Python API:
            bccmdGetChipVersion(handle: int, chipVer: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, chipVer = myDll.bccmdGetChipVersion(handle=0)
            print(retval, chipVer)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetChipVersion(uint32 handle, uint16* chipVer)

            Parameters :    handle -
                                Handle to the device.

                            chipVer -
                                Pointer to a variable to hold the returned chip version.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the chip major version number.
                            <p>
                            This function is deprecated, with the returned chipVer being valid
                            only for BlueCore ICs up to BC7. teGetChipId should be used to
                            identify the chip.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for bccmdGetBuildId.

            Deprecated :

        """
        self.TestEngineDLL.bccmdGetChipVersion.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetChipVersion.argtypes = [ct.c_uint32, ct.c_void_p]
        local_chipVer = ct.c_uint16(chipVer)
        retval = self.TestEngineDLL.bccmdGetChipVersion(handle, ct.byref(local_chipVer))
        chipVer = local_chipVer.value
        return retval, chipVer
    # end of bccmdGetChipVersion


    def bccmdGetChipRevision(self, handle: int, chipRev: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetChipRevision() wrapper for bccmdGetChipRevision in TestEngine DLL.

        Python API:
            bccmdGetChipRevision(handle: int, chipRev: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, chipRev = myDll.bccmdGetChipRevision(handle=0)
            print(retval, chipRev)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetChipRevision(uint32 handle, uint16* chipRev)

            Parameters :    handle -
                                Handle to the device.

                            chipRev -
                                Pointer to a variable to hold the returned chip revision,
                                as follows:
                                <table>
                                    <tr><td>0x43 = BC3-MM
                                    <tr><td>0x15 = BC3-ROM
                                    <tr><td>0xE2 = BC3-Flash
                                    <tr><td>0x26 = BC4-EXT
                                    <tr><td>0x30 = BC4-ROM
                                    <tr><td>0xE1 = BC5-MM
                                    <tr><td>0x41 = BC5-FM
                                    <tr><td>0x11 = BC6-ROM
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the chip revision number.
                            <p>
                            This function is deprecated. teGetChipId should be used to
                            identify the chip.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for bccmdGetBuildId.

            Deprecated :

        """
        self.TestEngineDLL.bccmdGetChipRevision.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetChipRevision.argtypes = [ct.c_uint32, ct.c_void_p]
        local_chipRev = ct.c_uint16(chipRev)
        retval = self.TestEngineDLL.bccmdGetChipRevision(handle, ct.byref(local_chipRev))
        chipRev = local_chipRev.value
        return retval, chipRev
    # end of bccmdGetChipRevision


    def bccmdGetChipAnaVer(self, handle: int, major: int=0, minor: int=0, vari: int=0) -> Tuple[int, int, int, int]:
        r"""Function TestEngine::bccmdGetChipAnaVer() wrapper for bccmdGetChipAnaVer in TestEngine DLL.

        Python API:
            bccmdGetChipAnaVer(handle: int, major: int=0, minor: int=0, vari: int=0) -> Tuple[int, int, int, int]

        Python Example Call Syntax:
            retval, major, minor, vari = myDll.bccmdGetChipAnaVer(handle=0)
            print(retval, major, minor, vari)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetChipAnaVer(uint32 handle, uint8* major,
                                                     uint8* minor, uint8* vari)

            Parameters :    handle -
                                Handle to the device.

                            major -
                                Pointer to a variable to hold the returned major version value,
                                for example (not a complete list):
                                <table>
                                    <tr><td>0x08 = BC3-MM
                                    <tr><td>0x09 = BC3-ROM
                                    <tr><td>0x0A = BC3-Flash
                                    <tr><td>0x0B = BC4-EXT
                                    <tr><td>0x0C = BC4-ROM
                                    <tr><td>0x0E = BC4-Audio-ROM
                                    <tr><td>0x11 = BC5-MM
                                    <tr><td>0x12 = BC5-FM
                                    <tr><td>0x13 = BC4-Audio-Flash
                                    <tr><td>0x17 = BC6-ROM
                                    <tr><td>0x21 = BC7-FM
                                    <tr><td>0x28 = BC7-MM
                                    <tr><td>0x32 = BC7-ROM
                                </table>

                            minor -
                                Pointer to a variable to hold the returned incremental minor
                                version value.

                            vari -
                                Pointer to a variable to hold the returned variant value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the version information for the chips
                            Bluetooth analogue components. The major version number identifies
                            the chip type.
                            <p>
                            This function is deprecated. teGetChipId should be used to
                            identify the chip.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.bccmdGetChipAnaVer.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetChipAnaVer.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_major = ct.c_uint8(major)
        local_minor = ct.c_uint8(minor)
        local_vari = ct.c_uint8(vari)
        retval = self.TestEngineDLL.bccmdGetChipAnaVer(handle, ct.byref(local_major), ct.byref(local_minor), ct.byref(local_vari))
        major = local_major.value
        minor = local_minor.value
        vari = local_vari.value
        return retval, major, minor, vari
    # end of bccmdGetChipAnaVer


    def bccmdRouteClock(self, handle: int) -> int:
        r"""Function TestEngine::bccmdRouteClock() wrapper for bccmdRouteClock in TestEngine DLL.

        Python API:
            bccmdRouteClock(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdRouteClock(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdRouteClock(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to issue a BCCMDVARID_ROUTE_CLOCK to the
                            connected BlueCore device.
                            <p>
                            On supported firmware this will route the clock to AIO1.
                            <p>
                            The device must be reset with the bccmdSetColdReset function to
                            stop the clock signal being routed to the AIO pin.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdRouteClock.restype = ct.c_int32
        self.TestEngineDLL.bccmdRouteClock.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdRouteClock(handle)
        
        return retval
    # end of bccmdRouteClock


    def bccmdRssiAcl(self, handle: int, connectionHandle: int, rssi: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdRssiAcl() wrapper for bccmdRssiAcl in TestEngine DLL.

        Python API:
            bccmdRssiAcl(handle: int, connectionHandle: int, rssi: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, rssi = myDll.bccmdRssiAcl(handle=0, connectionHandle=0)
            print(retval, rssi)

        Detail From Wrapped C API:
            Function :      int32 bccmdRssiAcl(uint32 handle, uint16 connectionHandle,
                                               int16* rssi)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

                            rssi -
                                RSSI of a received signal in dBm.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Retrieves the received signal strength indication (RSSI) for a
                            given ACL connection handle. The RSSI value is interpreted as a
                            signed integer with units of dBm.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdRssiAcl.restype = ct.c_int32
        self.TestEngineDLL.bccmdRssiAcl.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_rssi = ct.c_int16(rssi)
        retval = self.TestEngineDLL.bccmdRssiAcl(handle, connectionHandle, ct.byref(local_rssi))
        rssi = local_rssi.value
        return retval, rssi
    # end of bccmdRssiAcl


    def bccmdSetPio(self, handle: int, mask: int, port: int) -> int:
        r"""Function TestEngine::bccmdSetPio() wrapper for bccmdSetPio in TestEngine DLL.

        Python API:
            bccmdSetPio(handle: int, mask: int, port: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetPio(handle=0, mask=0, port=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetPio(uint32 handle, uint16 mask, uint16 port)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                Read / write bit mask of PIO port.

                            port -
                                Bit settings of PIO port.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will set the direction mask of the PIO and the
                            state of the PIO port.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the tePio* functions should be used.

        """
        self.TestEngineDLL.bccmdSetPio.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetPio.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdSetPio(handle, mask, port)
        
        return retval
    # end of bccmdSetPio


    def bccmdGetPio(self, handle: int, mask: int=0, port: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdGetPio() wrapper for bccmdGetPio in TestEngine DLL.

        Python API:
            bccmdGetPio(handle: int, mask: int=0, port: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, mask, port = myDll.bccmdGetPio(handle=0)
            print(retval, mask, port)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetPio(uint32 handle, uint16* mask, uint16* port)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                Direction mask of PIO port.

                            port -
                                Bit settings of PIO port.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the direction mask of the PIO and the
                            state of the PIO port.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the tePio* functions should be used.

        """
        self.TestEngineDLL.bccmdGetPio.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetPio.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        local_mask = ct.c_uint16(mask)
        local_port = ct.c_uint16(port)
        retval = self.TestEngineDLL.bccmdGetPio(handle, ct.byref(local_mask), ct.byref(local_port))
        mask = local_mask.value
        port = local_port.value
        return retval, mask, port
    # end of bccmdGetPio


    def bccmdMapPio32(self, handle: int, mask: int, pios: int, errLines: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdMapPio32() wrapper for bccmdMapPio32 in TestEngine DLL.

        Python API:
            bccmdMapPio32(handle: int, mask: int, pios: int, errLines: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, errLines = myDll.bccmdMapPio32(handle=0, mask=0, pios=0)
            print(retval, errLines)

        Detail From Wrapped C API:
            Function :      int32 bccmdMapPio32(uint32 handle, uint32 mask, uint32 pios,
                                                uint32* errLines)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                Bit mask of the mappable pins.

                            pios -
                                Bit field, where a bit being set (1) means that that pin should
                                be configured as a PIO. A bit being cleared (0) means that the
                                pin will be configured for its alternative use.

                            errLines -
                                Pointer to a uint32 bit field indicating which of the specified
                                pins could not be mapped as PIOs.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will map the pins specified in the mask according to
                            the usage specified in the pios parameter. Reports any pins which
                            could not be mapped.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the tePio* functions should be used.

        """
        self.TestEngineDLL.bccmdMapPio32.restype = ct.c_int32
        self.TestEngineDLL.bccmdMapPio32.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint32, ct.c_void_p]
        local_errLines = ct.c_uint32(errLines)
        retval = self.TestEngineDLL.bccmdMapPio32(handle, mask, pios, ct.byref(local_errLines))
        errLines = local_errLines.value
        return retval, errLines
    # end of bccmdMapPio32


    def bccmdSetPio32(self, handle: int, mask: int, direction: int, value: int, errLines: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdSetPio32() wrapper for bccmdSetPio32 in TestEngine DLL.

        Python API:
            bccmdSetPio32(handle: int, mask: int, direction: int, value: int, errLines: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, errLines = myDll.bccmdSetPio32(handle=0, mask=0, direction=0, value=0)
            print(retval, errLines)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetPio32(uint32 handle, uint32 mask, uint32 direction,
                                                uint32 value, uint32* errLines)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                Bit mask of the PIOs to be set.

                            direction -
                                Bit field which sets the PIOs as input (0) or output (1).

                            value -
                                Bit field which sets the values for the PIOs.

                            errLines -
                                Pointer to a uint32 bit field indicating which of the specified
                                pins could not be set.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will set the direction and values for the specified
                            PIOs. The value does not apply to PIOs specified as inputs.
                            <p>
                            If the PIOs to be used include lines which default to alternative
                            uses, it is necessary to call bccmdMapPio32 first to map the lines
                            as PIOs.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the tePio* functions should be used.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;
                uint32 mapMask = 0x0FFF0000;      // The lines we can map as PIOs
                uint32 pioMask = 0x0FFFFFFF;      // The lines we want to set (dedicated PIOs plus those we mapped)
                uint32 direction = 0x0F0F0F0F;    // Direction - (0) as input (1) as output
                uint32 value = 0x05050505;        // State of the lines to set (applies to output lines only)
                uint32 errLines;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < 5000);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Map lines that have other alternate functions as PIOs
                    int32 teRet = bccmdMapPio32(teHandle, mapMask, 0xFFFFFFFF, &errLines);

                    if (teRet != TE_OK)
                    {
                        // Checks if any lines could not be mapped as PIOs
                        if (errLines != 0)
                        {
                            cout << "ERROR: Lines that could not be mapped as PIOs = " << errLines << endl;
                        }
                    }
                    else
                    {
                        // Set the direction and value of the PIO lines.
                        teRet = bccmdSetPio32(teHandle, pioMask, direction, value, &errLines);

                        // Checks if any lines could not be mapped as PIOs
                        if (teRet != TE_OK)
                        {
                            // Checks which PIO lines could not be set as input or output
                            if (errLines != 0)
                            {
                                cout << "ERROR: Lines that could not be set = " << errLines << endl;
                            }
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdSetPio32.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetPio32.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint32, ct.c_uint32, ct.c_void_p]
        local_errLines = ct.c_uint32(errLines)
        retval = self.TestEngineDLL.bccmdSetPio32(handle, mask, direction, value, ct.byref(local_errLines))
        errLines = local_errLines.value
        return retval, errLines
    # end of bccmdSetPio32


    def bccmdGetPio32(self, handle: int, direction: int=0, value: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdGetPio32() wrapper for bccmdGetPio32 in TestEngine DLL.

        Python API:
            bccmdGetPio32(handle: int, direction: int=0, value: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, direction, value = myDll.bccmdGetPio32(handle=0)
            print(retval, direction, value)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetPio32(uint32 handle, uint32* direction,
                                                uint32* value)

            Parameters :    handle -
                                Handle to the device.

                            direction -
                                Pointer to uint32 value which stores the direction of the
                                PIO port lines as a bit field, where a 1 indicates that the
                                PIO is an output, and a 0 means that the PIO is an input.

                            value -
                                Pointer to uint32 value which stores the values of the PIO lines
                                as a bit field.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets the direction and state of the PIO lines.
                            If the PIOs to be read include lines which default to alternative
                            uses, it is necessary to call bccmdMapPio32 first to map the lines
                            as PIOs.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the tePio* functions should be used.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;
                uint32 direction;
                uint32 value;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < 5000);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Get the direction and value of the PIO lines.
                    int32 teRet = bccmdGetPio32(teHandle, &direction, &value);
                    if (teRet == TE_OK)
                    {
                        cout << "Direction = " << direction << endl;
                        cout << "Value = " << value << endl;
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdGetPio32.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetPio32.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        local_direction = ct.c_uint32(direction)
        local_value = ct.c_uint32(value)
        retval = self.TestEngineDLL.bccmdGetPio32(handle, ct.byref(local_direction), ct.byref(local_value))
        direction = local_direction.value
        value = local_value.value
        return retval, direction, value
    # end of bccmdGetPio32


    def bccmdGetAdc(self, handle: int, adc: int, result: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetAdc() wrapper for bccmdGetAdc in TestEngine DLL.

        Python API:
            bccmdGetAdc(handle: int, adc: int, result: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, result = myDll.bccmdGetAdc(handle=0, adc=0)
            print(retval, result)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetAdc(uint32 handle, uint16 adc, uint16* result)

            Parameters :    handle -
                                Handle to the device.

                            adc -
                                ADC which will be read. The ADCs which can be read are IC
                                dependent.

                            result -
                                Holds the result of the ADC reading. While the ADCs are
                                10-bit, the result is scaled according to any internal
                                potential divider network. Therefore the result can be
                                greater than the 10-bit maximum (1023).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will perform an ADC reading on the specified
                            Bluetooth ADC. It is only supported in BlueCore firmware from v24.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs, for which teAdcGet can be used.

        """
        self.TestEngineDLL.bccmdGetAdc.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetAdc.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_result = ct.c_uint16(result)
        retval = self.TestEngineDLL.bccmdGetAdc(handle, adc, ct.byref(local_result))
        result = local_result.value
        return retval, result
    # end of bccmdGetAdc


    def bccmdGetAio(self, handle: int, aio: int, result: int=0, numBits: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdGetAio() wrapper for bccmdGetAio in TestEngine DLL.

        Python API:
            bccmdGetAio(handle: int, aio: int, result: int=0, numBits: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, result, numBits = myDll.bccmdGetAio(handle=0, aio=0)
            print(retval, result, numBits)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetAio(uint32 handle, uint16 aio, uint16* result,
                                              uint8* numBits)

            Parameters :    handle -
                                Handle to the device.

                            aio -
                                AIO pin which will be read, 0 to 3.

                            result -
                                Holds the result of the ADC reading. This value is from 0 to
                                ADC_MAX, where ADC_MAX = 255 or 1023 for 8 and 10 bit results
                                respectively (the numBits parameter indicates 8 or 10 bit
                                result).
                                <p>
                                0 = 0V and ADC_MAX = VDD, therefore:
                                <p>
                                voltage = (result/ADC_MAX) * VDD
                                <p>
                                VDD can be calculated using a vref ADC reading and the vref
                                constant. See the help for bccmdGetVrefAdc for details.

                            numBits -
                                Holds the number of bits used for the result. In BlueCore
                                firmware from v24, the ADC readings have been changed to return
                                a 10 bit result (8 previously). This output parameter indicates
                                how many bits in the result are valid, 8 or 10, removing the
                                need to check the firmware version when using this function.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will perform an ADC reading on the specified AIO
                            pin. This function supports both the old ADC reading method (8
                            bit results) and the new (10 bit results). BlueCore devices prior
                            to BC5 have 8 bit ADCs. With these devices, and where the
                            firmware used uses the new method (returns 10 bit results), the
                            readings are shifted up by 2 bits.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs, for which teAdcGet can be used.

        """
        self.TestEngineDLL.bccmdGetAio.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetAio.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        local_result = ct.c_uint16(result)
        local_numBits = ct.c_uint8(numBits)
        retval = self.TestEngineDLL.bccmdGetAio(handle, aio, ct.byref(local_result), ct.byref(local_numBits))
        result = local_result.value
        numBits = local_numBits.value
        return retval, result, numBits
    # end of bccmdGetAio


    def bccmdBC5MMGetBatteryVoltage(self, handle: int, voltage: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdBC5MMGetBatteryVoltage() wrapper for bccmdBC5MMGetBatteryVoltage in TestEngine DLL.

        Python API:
            bccmdBC5MMGetBatteryVoltage(handle: int, voltage: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, voltage = myDll.bccmdBC5MMGetBatteryVoltage(handle=0)
            print(retval, voltage)

        Detail From Wrapped C API:
            Function :      int32 bccmdBC5MMGetBatteryVoltage(uint32 handle, uint16* voltage)

            Parameters :    handle -
                                Handle to the device.

                            voltage -
                                Pointer to 16 bit unsigned int, holds the voltage in
                                millivolts, calculated from the battery voltage ADC reading.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the value of the internal battery voltage
                            monitoring ADC and convert it to a voltage. It can be used with
                            BC5MM chips running firmware version 22d and newer.
                            <p>
                            Using this function with chips other than BC5MM is not supported,
                            and the results are undefined. The same goes for firmware
                            versions older than 22d.
                            <p>
                            Note that the accuracy of this function is limited by the ADC
                            accuracy, resolution and stability. An ADC step of 1 will result
                            in a voltage change of approximately 16-24mV. Testing has shown
                            that the voltage returned is generally within +/-50mV of the
                            voltage measured using a DVM.
                            <p>
                            This function will fail if a radiotest mode is running on the chip
                            (e.g. radiotestTxdata1 was called previously). If this is the
                            case, use a warm reset before calling this function.

        """
        self.TestEngineDLL.bccmdBC5MMGetBatteryVoltage.restype = ct.c_int32
        self.TestEngineDLL.bccmdBC5MMGetBatteryVoltage.argtypes = [ct.c_uint32, ct.c_void_p]
        local_voltage = ct.c_uint16(voltage)
        retval = self.TestEngineDLL.bccmdBC5MMGetBatteryVoltage(handle, ct.byref(local_voltage))
        voltage = local_voltage.value
        return retval, voltage
    # end of bccmdBC5MMGetBatteryVoltage


    def bccmdGetFirmwareCheckMask(self, handle: int, mask: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetFirmwareCheckMask() wrapper for bccmdGetFirmwareCheckMask in TestEngine DLL.

        Python API:
            bccmdGetFirmwareCheckMask(handle: int, mask: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, mask = myDll.bccmdGetFirmwareCheckMask(handle=0)
            print(retval, mask)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetFirmwareCheckMask(uint32 handle, uint16* mask)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                Pointer to mask which states which firmware component is
                                present AND if that component contains a pre-calculated
                                checksum.
                                <table>
                                    <tr><td>Bit  <td>Component
                                    <tr><td>0    <td>Stack
                                    <tr><td>1    <td>Loader
                                    <tr><td>2    <td>VM Application
                                    <tr><td>3    <td>File System
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will check if each firmware component is present and
                            that it contains a valid checksum. This function should be called
                            before bccmdGetFirmwareCheck.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdGetFirmwareCheckMask.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetFirmwareCheckMask.argtypes = [ct.c_uint32, ct.c_void_p]
        local_mask = ct.c_uint16(mask)
        retval = self.TestEngineDLL.bccmdGetFirmwareCheckMask(handle, ct.byref(local_mask))
        mask = local_mask.value
        return retval, mask
    # end of bccmdGetFirmwareCheckMask


    def bccmdGetFirmwareCheck(self, handle: int, check: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetFirmwareCheck() wrapper for bccmdGetFirmwareCheck in TestEngine DLL.

        Python API:
            bccmdGetFirmwareCheck(handle: int, check: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, check = myDll.bccmdGetFirmwareCheck(handle=0)
            print(retval, check)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetFirmwareCheck(uint32 handle, uint16* check)

            Parameters :    handle -
                                Handle to the device.

                            check -
                                Pointer to a mask which states which firmware component is
                                present AND if that component contains the correct checksum.
                                <table>
                                    <tr><td>Bit  <td>Component
                                    <tr><td>0    <td>Stack
                                    <tr><td>1    <td>Loader
                                    <tr><td>2    <td>VM Application
                                    <tr><td>3    <td>File System
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will check if each firmware component checksum is
                            correct.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdGetFirmwareCheck.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetFirmwareCheck.argtypes = [ct.c_uint32, ct.c_void_p]
        local_check = ct.c_uint16(check)
        retval = self.TestEngineDLL.bccmdGetFirmwareCheck(handle, ct.byref(local_check))
        check = local_check.value
        return retval, check
    # end of bccmdGetFirmwareCheck


    def bccmdGetExternalClockPeriod(self, handle: int, period: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetExternalClockPeriod() wrapper for bccmdGetExternalClockPeriod in TestEngine DLL.

        Python API:
            bccmdGetExternalClockPeriod(handle: int, period: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, period = myDll.bccmdGetExternalClockPeriod(handle=0)
            print(retval, period)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetExternalClockPeriod(uint32 handle, uint16* period)

            Parameters :    handle -
                                Handle to the device.

                            period -
                                Pointer to a value in units of 0.25us. Measures the 32kHz
                                clock once it's been divided down to 1kHz. The expected value
                                is therefore about 4000 (or 0xFA0).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the external clock period over the last
                            1kHz cycle from the appropriate pin.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdGetExternalClockPeriod.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetExternalClockPeriod.argtypes = [ct.c_uint32, ct.c_void_p]
        local_period = ct.c_uint16(period)
        retval = self.TestEngineDLL.bccmdGetExternalClockPeriod(handle, ct.byref(local_period))
        period = local_period.value
        return retval, period
    # end of bccmdGetExternalClockPeriod


    def bccmdEnableDeviceConnect(self, handle: int) -> int:
        r"""Function TestEngine::bccmdEnableDeviceConnect() wrapper for bccmdEnableDeviceConnect in TestEngine DLL.

        Python API:
            bccmdEnableDeviceConnect(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdEnableDeviceConnect(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdEnableDeviceConnect(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to be discoverable and connectable. This
                            command is effectively the BCCMD equivalent of hciSlave / dmSlave.
                            It will enable the user to set the device into test mode via a
                            host or debug interface (a call to bccmdEnableDeviceUnderTestMode
                            following this command is required).
                            <p>
                            For BlueCore ICs, firmware from 23g releases should support this
                            command. It is unsupported in older firmware.
                            <p>
                            Success is determined by:
                            <ol>
                            <li> Valid handle
                            <li> Command complete within timeout
                            </ol>
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs (hciSlave can be used instead).

        """
        self.TestEngineDLL.bccmdEnableDeviceConnect.restype = ct.c_int32
        self.TestEngineDLL.bccmdEnableDeviceConnect.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdEnableDeviceConnect(handle)
        
        return retval
    # end of bccmdEnableDeviceConnect


    def bccmdEnableDeviceUnderTestMode(self, handle: int) -> int:
        r"""Function TestEngine::bccmdEnableDeviceUnderTestMode() wrapper for bccmdEnableDeviceUnderTestMode in TestEngine DLL.

        Python API:
            bccmdEnableDeviceUnderTestMode(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdEnableDeviceUnderTestMode(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdEnableDeviceUnderTestMode(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to set the enable device under test mode flag
                            using a BCCMD instead of an HCI or DM command. This will enable
                            the user to set the device into test mode via a debug interface as
                            well as via a host interface.
                            This command will <b>NOT</b> make the device discoverable or
                            connectable. To do this, use bccmdEnableDeviceConnect if
                            supported by the BlueCore firmware (if not, a VM app can be used
                            to do this, or use a host connection and hciSlave / dmSlave).
                            <p>
                            Success is determined by:
                            <ol>
                            <li> Valid handle
                            <li> Command complete within timeout
                            </ol>
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs (hciEnableDeviceUnderTestMode can be used instead).

            Example :

                uint32 teHandle = openTestEngineDebug(1, 0, DEBUG_LPTSPI);

                if(teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    int32 teRet;

                    do
                    {
                        // Make connectable
                        teRet = bccmdEnableDeviceConnect(teHandle);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Enable DUT mode
                        teRet = bccmdEnableDeviceUnderTestMode(teHandle);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Run tests on BT tester

                    } while(0);

                    if (teRet != TE_OK)
                    {
                        cout << "TestEngine error" << endl;
                    }
                }

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdEnableDeviceUnderTestMode.restype = ct.c_int32
        self.TestEngineDLL.bccmdEnableDeviceUnderTestMode.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdEnableDeviceUnderTestMode(handle)
        
        return retval
    # end of bccmdEnableDeviceUnderTestMode


    def bccmdCheckSqifImageValidationStatus(self, handle: int, status: int=0, timeout: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdCheckSqifImageValidationStatus() wrapper for bccmdCheckSqifImageValidationStatus in TestEngine DLL.

        Python API:
            bccmdCheckSqifImageValidationStatus(handle: int, status: int=0, timeout: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, status = myDll.bccmdCheckSqifImageValidationStatus(handle=0, timeout=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 bccmdCheckSqifImageValidationStatus(uint32 handle,
                                                                      uint16* status,
                                                                      uint16 timeout)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to a value where the SQIF Image Validation
                                status of the chip will be stored. The following status
                                values may be returned:
                                <table>
                                    <tr><td>0 = Error: validation did not complete
                                    <tr><td>1 = Validation passed: an image
                                                is present.
                                    <tr><td>2 = Validation passed: no image
                                                is present.
                                </table>

                            timeout -
                                Specified in milliseconds. See Description for details.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td> 0 = Error
                                <tr><td> 1 = Success
                                <tr><td> 2 = Unsupported function
                            </table>

            Description :   This function will check the device's SQIF image validation
                            status. If validation fails to complete within the specified
                            timeout, the function will return success and an error will be
                            indicated via the status parameter.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdCheckSqifImageValidationStatus.restype = ct.c_int32
        self.TestEngineDLL.bccmdCheckSqifImageValidationStatus.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        local_status = ct.c_uint16(status)
        retval = self.TestEngineDLL.bccmdCheckSqifImageValidationStatus(handle, ct.byref(local_status), timeout)
        status = local_status.value
        return retval, status
    # end of bccmdCheckSqifImageValidationStatus


    def radiotestStereoCodecLB(self, handle: int, sampleRate: int, reroute: int) -> int:
        r"""Function TestEngine::radiotestStereoCodecLB() wrapper for radiotestStereoCodecLB in TestEngine DLL.

        Python API:
            radiotestStereoCodecLB(handle: int, sampleRate: int, reroute: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestStereoCodecLB(handle=0, sampleRate=0, reroute=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestStereoCodecLB(uint32 handle, uint16 sampleRate,
                                                         uint16 reroute)

            Parameters :    handle -
                                Handle to the device.

                            sampleRate -
                                Sample rate in Hz, which can be one of the following values:
                                <table>
                                    <tr><td>8000
                                    <tr><td>11025
                                    <tr><td>16000
                                    <tr><td>22050
                                    <tr><td>24000
                                    <tr><td>32000
                                    <tr><td>44100
                                </table>

                            reroute -
                                Controls how signal is routed from mic to speaker.
                                <table>
                                    <tr><td>0 - <td>MicL to SpkL, MicR to SpkR
                                    <tr><td>1 - <td>MicR to SpkL and SpkR
                                    <tr><td>2 - <td>MicL to SpkL and SpkR
                                    <tr><td>3 - <td>MicL to SpkR, MicR to SpkL
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to turn on the codec hardware for stereo
                            loopback.
                            <p>
                            This function is supported for BlueCore ICs only. For CDA ICs the
                            teAudio* functions should be used.

        """
        self.TestEngineDLL.radiotestStereoCodecLB.restype = ct.c_int32
        self.TestEngineDLL.radiotestStereoCodecLB.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestStereoCodecLB(handle, sampleRate, reroute)
        
        return retval
    # end of radiotestStereoCodecLB


    def radiotestTxstart(self, handle: int, frequency: int, power1: int, power2: int, modulation: int) -> int:
        r"""Function TestEngine::radiotestTxstart() wrapper for radiotestTxstart in TestEngine DLL.

        Python API:
            radiotestTxstart(handle: int, frequency: int, power1: int, power2: int, modulation: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestTxstart(handle=0, frequency=0, power1=0, power2=0, modulation=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestTxstart(uint32 handle, uint16 frequency,
                                                   uint16 power1, uint16 power2,
                                                   int16 modulation)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, the LSB (bits 0-7) is used as
                                the LSB of the magnitude value.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 are used as bits 8-11
                                of the magnitude value.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            modulation -
                                Modulation offset - 4096 = 1MHz.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates TXSTART (Carrier Wave transmission).
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs. Use teRadTxCwStart instead.

        """
        self.TestEngineDLL.radiotestTxstart.restype = ct.c_int32
        self.TestEngineDLL.radiotestTxstart.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_int16]
        
        retval = self.TestEngineDLL.radiotestTxstart(handle, frequency, power1, power2, modulation)
        
        return retval
    # end of radiotestTxstart


    def radiotestTxdata1(self, handle: int, frequency: int, power1: int, power2: int) -> int:
        r"""Function TestEngine::radiotestTxdata1() wrapper for radiotestTxdata1 in TestEngine DLL.

        Python API:
            radiotestTxdata1(handle: int, frequency: int, power1: int, power2: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestTxdata1(handle=0, frequency=0, power1=0, power2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestTxdata1(uint32 handle, uint16 frequency,
                                                   uint16 power1, uint16 power2)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates TXDATA1 packet transmission.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :

                uint32 rxHandle = TE_INVALID_HANDLE_VALUE;
                uint32 txHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying rxHandle..." << endl;
                    rxHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (rxHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                timeoutMs = 0;
                do
                {
                    cout << "Trying txHandle..." << endl;
                    txHandle = openTestEngine(USB, "\\\\.\\csr0", 0, 1000, 500);
                    timeoutMs += 1000;
                } while (txHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (txHandle != TE_INVALID_HANDLE_VALUE && rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    int32 teRet;

                    do
                    {
                        uint16 buildId;
                        teRet = bccmdGetBuildId(rxHandle, &buildId);
                        if (teRet == TE_OK)
                        {
                            cout << "DUT firmware = " << buildId << endl;
                        }
                        else
                        {
                            break;
                        }

                        teRet = bccmdGetBuildId(txHandle, &buildId);
                        if (teRet == TE_OK)
                        {
                            cout << "REF firmware = " << buildId << endl;
                        }
                        else
                        {
                            break;
                        }

                        // 1. configure the packet types
                        teRet = radiotestCfgPkt(rxHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestCfgPkt(txHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // 2. Set the TX/RX interval
                        teRet = radiotestCfgFreq(rxHandle, 37500, 9375, 1);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestCfgFreq(txHandle, 37500, 9375, 1);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        const uint16 FREQ_MHZ = 2441;
                        const uint16 INT_PA = 50;
                        const uint16 EXT_PA = 0;
                        const uint8 HI_SIDE = 0;
                        const uint16 RX_ATT = 0;
                        const uint16 SAMPLE_SIZE = 10000;

                        // 3. Start the transmitter and receiver
                        teRet = radiotestTxdata1(txHandle, FREQ_MHZ, INT_PA, EXT_PA);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestBer1(rxHandle, FREQ_MHZ, HI_SIDE, RX_ATT,
                                              SAMPLE_SIZE);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // 4. Gather the BER information
                        size_t count = 0;
                        uint32 ber[9];

                        do
                        {
                            ++count;
                            teRet = hqGetBer(rxHandle, 1000, ber);
                        } while (teRet == TE_ERROR && count < 10);

                        if (teRet == TE_OK)
                        {
                            cout << "Bit count = " << ber[0] << endl;
                            cout << "Bit errors = " << ber[1] << endl;
                            cout << "Received packets = " << ber[3] << endl;
                            cout << "Expected packets = " << ber[4] << endl;
                            cout << "Header errors = " << ber[5] << endl;
                            cout << "CRC errors = " << ber[6] << endl;
                            cout << "Uncorrected errors = " << ber[7] << endl;
                            cout << "Sync errors = " << ber[8] << endl;
                        }
                        else
                        {
                            cout << "****FAIL****" << endl;
                        }

                    } while(0);

                    if (teRet != TE_OK)
                    {
                        cout << "TestEngine error" << endl;
                    }
                }

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(txHandle);
                }
                if (rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(rxHandle);
                }

        """
        self.TestEngineDLL.radiotestTxdata1.restype = ct.c_int32
        self.TestEngineDLL.radiotestTxdata1.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestTxdata1(handle, frequency, power1, power2)
        
        return retval
    # end of radiotestTxdata1


    def radiotestTxdata2(self, handle: int, countryCode: int, power1: int, power2: int) -> int:
        r"""Function TestEngine::radiotestTxdata2() wrapper for radiotestTxdata2 in TestEngine DLL.

        Python API:
            radiotestTxdata2(handle: int, countryCode: int, power1: int, power2: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestTxdata2(handle=0, countryCode=0, power1=0, power2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestTxdata2(uint32 handle, uint16 countryCode,
                                                   uint16 power1, uint16 power2)

            Parameters :    handle -
                                Handle to the device.

                            countryCode -
                                Must be 0. Setting the countryCode to anything other than
                                zero is deprecated.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates TXDATA2 packet transmission.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestTxdata1 (substitute with
                            radiotestTxdata2).

        """
        self.TestEngineDLL.radiotestTxdata2.restype = ct.c_int32
        self.TestEngineDLL.radiotestTxdata2.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestTxdata2(handle, countryCode, power1, power2)
        
        return retval
    # end of radiotestTxdata2


    def radiotestTxdata3(self, handle: int, frequency: int, power1: int, power2: int) -> int:
        r"""Function TestEngine::radiotestTxdata3() wrapper for radiotestTxdata3 in TestEngine DLL.

        Python API:
            radiotestTxdata3(handle: int, frequency: int, power1: int, power2: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestTxdata3(handle=0, frequency=0, power1=0, power2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestTxdata3(uint32 handle, uint16 frequency,
                                                   uint16 power1, uint16 power2)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates TXDATA3 packet transmission.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestTxdata1 (substitute with
                            radiotestTxdata3).

        """
        self.TestEngineDLL.radiotestTxdata3.restype = ct.c_int32
        self.TestEngineDLL.radiotestTxdata3.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestTxdata3(handle, frequency, power1, power2)
        
        return retval
    # end of radiotestTxdata3


    def radiotestTxdata4(self, handle: int, frequency: int, power1: int, power2: int) -> int:
        r"""Function TestEngine::radiotestTxdata4() wrapper for radiotestTxdata4 in TestEngine DLL.

        Python API:
            radiotestTxdata4(handle: int, frequency: int, power1: int, power2: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestTxdata4(handle=0, frequency=0, power1=0, power2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestTxdata4(uint32 handle, uint16 frequency,
                                                   uint16 power1, uint16 power2)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates TXDATA4 packet transmission.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestTxdata1 (substitute with
                            radiotestTxdata4).

        """
        self.TestEngineDLL.radiotestTxdata4.restype = ct.c_int32
        self.TestEngineDLL.radiotestTxdata4.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestTxdata4(handle, frequency, power1, power2)
        
        return retval
    # end of radiotestTxdata4


    def radiotestCfgTxPower(self, handle: int, power: int) -> int:
        r"""Function TestEngine::radiotestCfgTxPower() wrapper for radiotestCfgTxPower in TestEngine DLL.

        Python API:
            radiotestCfgTxPower(handle: int, power: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgTxPower(handle=0, power=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgTxPower(uint32 handle, int16 power)

            Parameters :    handle -
                                Handle to the device.

                            power -
                                Requested power in dBm. This value is used to select the
                                power table entry to use.
                                <p>
                                The power table entry with the closest output power equal to
                                or less than this value is selected.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function utilises the CFG_TXPOWER radiotest function. It is
                            used to specify the output power for subsequent radiotests, e.g.
                            radiotestTxstart. Subsequent radiotests will ignore power
                            parameters and use the power table values instead.
                            <p>
                            The closest power table entry with output power equal to or less
                            than the power parameter value is selected. Therefore, the actual
                            output power may be less than what is specified. The difference
                            is dependent on the power table configuration for the device.
                            <p>
                            Setting the power value to the int16 representation of 0xdeaf
                            (-8529) switches off the use of the power table for subsequent
                            radiotest operations. After this value is set, power parameters
                            for subsequent radiotests are used instead of the power table
                            values.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgTxPower.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgTxPower.argtypes = [ct.c_uint32, ct.c_int16]
        
        retval = self.TestEngineDLL.radiotestCfgTxPower(handle, power)
        
        return retval
    # end of radiotestCfgTxPower


    def radiotestRxstart1(self, handle: int, frequency: int, hiSide: int, rxAttenuation: int) -> int:
        r"""Function TestEngine::radiotestRxstart1() wrapper for radiotestRxstart1 in TestEngine DLL.

        Python API:
            radiotestRxstart1(handle: int, frequency: int, hiSide: int, rxAttenuation: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRxstart1(handle=0, frequency=0, hiSide=0, rxAttenuation=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRxstart1(uint32 handle, uint16 frequency,
                                                    uint8 hiSide, uint16 rxAttenuation)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency in MHz. Should be in the range
                                2402 to 2480.

                            hiSide -
                                Set to 0 for low side modulation and 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. For ICs other than BC5, this value
                                should be in the range 0 to 15.
                                <p>
                                For BC5 ICs, this value also controls the RX mixer attenuation
                                and I2I level, where the bits are used as follows:
                                <table>
                                    <tr><td>0-3: Attenuation setting
                                    <tr><td>4-5: Mixer attenuation
                                    <tr><td>6-7: Unused
                                    <tr><td>8-9: I2I level
                                </table>
                                Therefore the maximum value for BC5 is 1023.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates RXSTART1.
                            <p>
                            Enables the receiver in continuous reception at a designated
                            frequency with a choice of low or high side modulation and with
                            a designated attenuation setting.
                            <p>
                            Requires a second unit to be running TXSTART.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestRxstart1.restype = ct.c_int32
        self.TestEngineDLL.radiotestRxstart1.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestRxstart1(handle, frequency, hiSide, rxAttenuation)
        
        return retval
    # end of radiotestRxstart1


    def radiotestRxstart2(self, handle: int, frequency: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int:
        r"""Function TestEngine::radiotestRxstart2() wrapper for radiotestRxstart2 in TestEngine DLL.

        Python API:
            radiotestRxstart2(handle: int, frequency: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRxstart2(handle=0, frequency=0, hiSide=0, rxAttenuation=0, sampleSize=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRxstart2(uint32 handle, uint16 frequency,
                                                    uint8 hiSide, uint16 rxAttenuation,
                                                    uint16 sampleSize)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency in MHz. Should be in the range
                                2402 to 2480.

                            hiSide -
                                Set to 0 for low side modulation and 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. For ICs other than BC5, this value
                                should be in the range 0 to 15.
                                <p>
                                For BC5 ICs, this value also controls the RX mixer attenuation
                                and I2I level, where the bits are used as follows:
                                <table>
                                    <tr><td>0-3: Attenuation setting
                                    <tr><td>4-5: Mixer attenuation
                                    <tr><td>6-7: Unused
                                    <tr><td>8-9: I2I level
                                </table>
                                Therefore the maximum value for BC5 is 1023.

                            sampleSize -
                                Number of RSSI reports to capture (for averaging purposes), up
                                to a maximum value of 100. Values greater than 100 will result
                                in the function returning Error.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates RXSTART2.
                            <p>
                            Enables the receiver in continuous reception at a designated
                            frequency with a choice of low or high side modulation and with
                            a designated attenuation setting.
                            <p>
                            Requires a second unit to be running TXSTART (see
                            radiotestTxstart).
                            <p>
                            RSSI results can be obtained by calling hqGetRssi. When
                            sampleSize results have been obtained, further results are
                            ignored until either the set has been collected with hqGetRssi,
                            or until radiotestRxstart2 is called again.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestRxstart2.restype = ct.c_int32
        self.TestEngineDLL.radiotestRxstart2.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestRxstart2(handle, frequency, hiSide, rxAttenuation, sampleSize)
        
        return retval
    # end of radiotestRxstart2


    def hqGetRssi(self, handle: int, timeout: int, maxSize: int, rssiSamples: list) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetRssi() wrapper for hqGetRssi in TestEngine DLL.

        Python API:
            hqGetRssi(handle: int, timeout: int, maxSize: int, rssiSamples: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, rssiSamples = myDll.hqGetRssi(handle=0, timeout=0, maxSize=0, rssiSamples=[0,1])
            print(retval, rssiSamples)

        Detail From Wrapped C API:
            Function :      int32 hqGetRssi(uint32 handle, int32 timeout, uint16 maxSize,
                                            uint16* rssiSamples)

            Parameters :    handle -
                                Handle to the device.

                            timeout -
                                Time, in ms, which the function will wait for valid results.
                                If set to zero the function will just check for completion.

                            maxSize -
                                Size of the array allocated to hold the RSSI samples.

                            rssiSamples -
                                Array to contain the RSSI samples.

            Returns :        <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function obtains a set of RSSI results from the DUT,
                            obtained as a result of calling radiotestRxstart2. The number of
                            results that will be written is dependent on the sampleSize
                            parameter for radiotestRxstart2.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.hqGetRssi.restype = ct.c_int32
        self.TestEngineDLL.hqGetRssi.argtypes = [ct.c_uint32, ct.c_int32, ct.c_uint16, ct.c_void_p]
        if rssiSamples == None:
            rssiSamples = []
        local_rssiSamples = (ct.c_uint16 * max(maxSize, len(rssiSamples)))(*rssiSamples)
        retval = self.TestEngineDLL.hqGetRssi(handle, timeout, maxSize, local_rssiSamples)
        rssiSamples = local_rssiSamples[:]
        return retval, rssiSamples
    # end of hqGetRssi


    def radiotestBer1(self, handle: int, frequency: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int:
        r"""Function TestEngine::radiotestBer1() wrapper for radiotestBer1 in TestEngine DLL.

        Python API:
            radiotestBer1(handle: int, frequency: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestBer1(handle=0, frequency=0, hiSide=0, rxAttenuation=0, sampleSize=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestBer1(uint32 handle, uint16 frequency, uint8 hiSide,
                                                uint16 rxAttenuation, uint32 sampleSize)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency in MHz. Should be in the range
                                2402 to 2480.

                            hiSide -
                                Set to 0 for low side modulation and 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. Should be in the range 0 to 15.

                            sampleSize -
                                Number of bits to be sampled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates BER1.
                            <p>
                            Enables the receiver at a designated frequency with a choice of
                            low or high side modulation and with a designated attenuation
                            setting.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestBer1.restype = ct.c_int32
        self.TestEngineDLL.radiotestBer1.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestBer1(handle, frequency, hiSide, rxAttenuation, sampleSize)
        
        return retval
    # end of radiotestBer1


    def radiotestBer2(self, handle: int, countryCode: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int:
        r"""Function TestEngine::radiotestBer2() wrapper for radiotestBer2 in TestEngine DLL.

        Python API:
            radiotestBer2(handle: int, countryCode: int, hiSide: int, rxAttenuation: int, sampleSize: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestBer2(handle=0, countryCode=0, hiSide=0, rxAttenuation=0, sampleSize=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestBer2(uint32 handle, uint16 countryCode,
                                                uint8 hiSide, uint16 rxAttenuation,
                                                uint32 sampleSize)

            Parameters :    handle -
                                Handle to the device.

                            countryCode -
                                Must be 0. Setting the countryCode to anything other than
                                zero is deprecated.

                            hiSide -
                                Set to 0 for low side modulation and 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. Should be in the range 0 to 15.

                            sampleSize -
                                Number of bits to be sampled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates BER2.
                            <p>
                            Enables the receiver with hopping, with a choice of low or
                            high side modulation, and with a designated attenuation setting
                            as for radiotestRxdata2.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestBer2.restype = ct.c_int32
        self.TestEngineDLL.radiotestBer2.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestBer2(handle, countryCode, hiSide, rxAttenuation, sampleSize)
        
        return retval
    # end of radiotestBer2


    def radiotestBerLoopback(self, handle: int, frequency: int, power1: int, power2: int, sampleSize: int) -> int:
        r"""Function TestEngine::radiotestBerLoopback() wrapper for radiotestBerLoopback in TestEngine DLL.

        Python API:
            radiotestBerLoopback(handle: int, frequency: int, power1: int, power2: int, sampleSize: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestBerLoopback(handle=0, frequency=0, power1=0, power2=0, sampleSize=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestBerLoopback(uint32 handle, uint16 frequency,
                                                       uint16 power1, uint16 power2,
                                                       uint32 sampleSize);

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            sampleSize -
                                Number of bits to be sampled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates BER_LOOPBACK TX/RX test mode, which is
                            used with another device running radiotestLoopback as shown in
                            the example code.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :

                uint32 rxHandle = TE_INVALID_HANDLE_VALUE;
                uint32 txHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying rxHandle..." << endl;
                    rxHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (rxHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                timeoutMs = 0;

                do
                {
                    cout << "Trying txHandle..." << endl;
                    txHandle = openTestEngine(USB, "\\\\.\\csr0", 0, 1000, 500);
                    timeoutMs += 1000;
                } while (txHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (txHandle != TE_INVALID_HANDLE_VALUE && rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    int32 teRet;

                    do
                    {
                        uint16 buildId;
                        teRet = bccmdGetBuildId(rxHandle, &buildId);
                        if (teRet == TE_OK)
                        {
                            cout << "DUT firmware = " << buildId << endl;
                        }
                        else
                        {
                            break;
                        }

                        teRet = bccmdGetBuildId(txHandle, &buildId);
                        if (teRet == TE_OK)
                        {
                            cout << "REF firmware = " << buildId << endl;
                        }
                        else
                        {
                            break;
                        }

                        // 1. configure the packet types
                        teRet = radiotestCfgPkt(rxHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestCfgPkt(txHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // 2. Set the TX/RX interval
                        teRet = radiotestCfgFreq(rxHandle, 37500, 9375, 1);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestCfgFreq(txHandle, 37500, 9375, 1);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        const uint16 FREQ_MHZ = 2441;
                        const uint16 INT_PA = 50;
                        const uint16 EXT_PA = 0;
                        const uint16 SAMPLE_SIZE = 10000;

                        // 3. Start the transmitter and receiver
                        teRet = radiotestBerLoopback(txHandle, FREQ_MHZ, INT_PA, EXT_PA,
                                                     SAMPLE_SIZE);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestLoopback(rxHandle, FREQ_MHZ, INT_PA, EXT_PA);
                        if (teRet != TE_OK)
                        {
                            break;
                        }


                        // 4. Gather the BER information
                        size_t count = 0;
                        uint32 ber[9];

                        do
                        {
                            ++count;
                            teRet = hqGetBer(txHandle, 1000, ber);
                        } while (teRet == TE_ERROR && count < 10);

                        if (teRet == TE_OK)
                        {
                            cout << "Bit count = " << ber[0] << endl;
                            cout << "Bit errors = " << ber[1] << endl;
                            cout << "Received packets = " << ber[3] << endl;
                            cout << "Expected packets = " << ber[4] << endl;
                            cout << "Header errors = " << ber[5] << endl;
                            cout << "CRC errors = " << ber[6] << endl;
                            cout << "Uncorrected errors = " << ber[7] << endl;
                            cout << "Sync errors = " << ber[8] << endl;
                        }
                        else
                        {
                            cout << "****FAIL****" << endl;
                        }

                    } while(0);

                    if (teRet != TE_OK)
                    {
                        cout << "TestEngine error" << endl;
                    }
                }

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(txHandle);
                }
                if (rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(rxHandle);
                }

        """
        self.TestEngineDLL.radiotestBerLoopback.restype = ct.c_int32
        self.TestEngineDLL.radiotestBerLoopback.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestBerLoopback(handle, frequency, power1, power2, sampleSize)
        
        return retval
    # end of radiotestBerLoopback


    def radiotestRxLoopback(self, handle: int, frequency: int, intPA: int, extPA: int) -> int:
        r"""Function TestEngine::radiotestRxLoopback() wrapper for radiotestRxLoopback in TestEngine DLL.

        Python API:
            radiotestRxLoopback(handle: int, frequency: int, intPA: int, extPA: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRxLoopback(handle=0, frequency=0, intPA=0, extPA=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRxLoopback(uint32 handle, uint16 frequency,
                                                      uint16 intPA, uint16 extPA)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            intPA -
                                Drive level for internal PA. 0 to 63 for basic rate packets,
                                0 to 127 for EDR packets. Typical values are 50 for basic
                                rate and 105 for EDR packet types.

                            extPA -
                                Drive level for external PA.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates RX_LOOPBACK.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.radiotestRxLoopback.restype = ct.c_int32
        self.TestEngineDLL.radiotestRxLoopback.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestRxLoopback(handle, frequency, intPA, extPA)
        
        return retval
    # end of radiotestRxLoopback


    def radiotestLoopback(self, handle: int, frequency: int, power1: int, power2: int) -> int:
        r"""Function TestEngine::radiotestLoopback() wrapper for radiotestLoopback in TestEngine DLL.

        Python API:
            radiotestLoopback(handle: int, frequency: int, power1: int, power2: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestLoopback(handle=0, frequency=0, power1=0, power2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestLoopback(uint32 handle, uint16 frequency,
                                                    uint16 power1, uint16 power2)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator frequency.

                            power1 -
                                For BlueCore ICs this sets the drive level for internal PA.
                                0 to 63 for basic rate packets, 0 to 127 for EDR packets.
                                Typical values are 50 for basic rate and 105 for EDR packet
                                types.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 4-5 specify the exponent
                                power control setting. Bits 0-3 and 6-7 are reserved and
                                should be set to zero. Refer to document CS-00408534-TC for
                                full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

                            power2 -
                                For BlueCore ICs this sets the drive level for external PA.
                                <p>
                                For QCC302x/3x and QCC512x ICs, bits 0-3 specify the magnitude
                                power control setting, and bits 4-7 specify the attenuation
                                setting. The magnitude value is a signed value in the range
                                -8 to 7 (2's complement representation). Refer to document
                                CS-00408534-TC for full details.
                                <p>
                                In all cases the MSB (upper 8 bits) are ignored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates LOOPBACK RX/TX test mode, which is used
                            with another device running radiotestLoopback as shown in the
                            example code.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestBerLoopback.

        """
        self.TestEngineDLL.radiotestLoopback.restype = ct.c_int32
        self.TestEngineDLL.radiotestLoopback.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestLoopback(handle, frequency, power1, power2)
        
        return retval
    # end of radiotestLoopback


    def hqGetBer(self, handle: int, timeout: int, berReport: list) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetBer() wrapper for hqGetBer in TestEngine DLL.

        Python API:
            hqGetBer(handle: int, timeout: int, berReport: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, berReport = myDll.hqGetBer(handle=0, timeout=0, berReport=[0,1])
            print(retval, berReport)

        Detail From Wrapped C API:
            Function :      int32 hqGetBer(uint32 handle, int32 timeout, uint32* berReport)

            Parameters :    handle -
                                Handle to the device.

                            timeout -
                                Time, in ms, which the function will wait for valid results.
                                If set to zero the function will just check for completion.

                            berReport -
                                Array to contain cumulative BER report. Defined as follows:
                                <table>
                                    <tr><td>r[0] = cumulative bit count
                                    <tr><td>r[1] = cumulative bit errors
                                    <tr><td>r[2] = NOT USED
                                    <tr><td>r[3] = cumulative received packets
                                    <tr><td>r[4] = cumulative expected packets
                                    <tr><td>r[5] = cumulative header errors
                                    <tr><td>r[6] = cumulative CRC errors
                                    <tr><td>r[7] = cumulative uncorrected errors
                                    <tr><td>r[8] = cumulative sync errors
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function obtains the last complete BER results sample from
                            the DUT.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestBerLoopback.

        """
        self.TestEngineDLL.hqGetBer.restype = ct.c_int32
        self.TestEngineDLL.hqGetBer.argtypes = [ct.c_uint32, ct.c_int32, ct.c_void_p]
        if berReport == None:
            berReport = []
        local_berReport = (ct.c_uint32 * len(berReport))(*berReport)
        retval = self.TestEngineDLL.hqGetBer(handle, timeout, local_berReport)
        berReport = local_berReport[:]
        return retval, berReport
    # end of hqGetBer


    def radiotestRxdata1(self, handle: int, frequency: int, hiSide: int, rxAttenuation: int) -> int:
        r"""Function TestEngine::radiotestRxdata1() wrapper for radiotestRxdata1 in TestEngine DLL.

        Python API:
            radiotestRxdata1(handle: int, frequency: int, hiSide: int, rxAttenuation: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRxdata1(handle=0, frequency=0, hiSide=0, rxAttenuation=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRxdata1(uint32 handle, uint16 frequency,
                                                   uint8 hiSide, uint16 rxAttenuation)

            Parameters :    handle -
                                Handle to the device.

                            frequency -
                                Local Oscillator (LO) frequency in MHz. Should be in the range
                                2402 to 2480.

                            hiSide -
                                Set to 0 for low side modulation or 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. Should be in the range 0 to 15.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Enables the receiver, at a designated frequency with a choice
                            of low or high side modulation, and with a designated attenuation
                            setting. The software counts the number of received packets and
                            the number of payloads with correctable errors.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestRxdata1.restype = ct.c_int32
        self.TestEngineDLL.radiotestRxdata1.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestRxdata1(handle, frequency, hiSide, rxAttenuation)
        
        return retval
    # end of radiotestRxdata1


    def radiotestRxdata2(self, handle: int, countryCode: int, hiSide: int, rxAttenuation: int) -> int:
        r"""Function TestEngine::radiotestRxdata2() wrapper for radiotestRxdata2 in TestEngine DLL.

        Python API:
            radiotestRxdata2(handle: int, countryCode: int, hiSide: int, rxAttenuation: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestRxdata2(handle=0, countryCode=0, hiSide=0, rxAttenuation=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestRxdata2(uint32 handle, uint16 countryCode,
                                                   uint8 hiSide, uint16 rxAttenuation)

            Parameters :    handle -
                                Handle to the device.

                            countryCode -
                                Must be 0. Setting the countryCode to anything other than
                                zero is deprecated.

                            hiSide -
                                Set to 0 for low side modulation or 1 for high side
                                modulation.

                            rxAttenuation -
                                Attenuation setting. Should be in the range 0 to 15.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Enables the receiver with hopping, with a choice of low or high
                            side modulation and with a designated attenuation setting. The
                            software counts the number of received packets and the number of
                            payloads with correctable errors.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestRxdata2.restype = ct.c_int32
        self.TestEngineDLL.radiotestRxdata2.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestRxdata2(handle, countryCode, hiSide, rxAttenuation)
        
        return retval
    # end of radiotestRxdata2


    def hqGetRxdata(self, handle: int, timeout: int, rxData: list) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetRxdata() wrapper for hqGetRxdata in TestEngine DLL.

        Python API:
            hqGetRxdata(handle: int, timeout: int, rxData: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, rxData = myDll.hqGetRxdata(handle=0, timeout=0, rxData=[0,1])
            print(retval, rxData)

        Detail From Wrapped C API:
            Function :      int32 hqGetRxdata(uint32 handle, int32 timeout, uint16* rxData)

            Parameters :    handle -
                                Handle to the device.

                            timeout -
                                Time, in ms, which the function will wait for valid results.
                                If set to zero the function will just check for completion.

                            rxData -
                                Pointer to an array which will receive the following:
                                <table>
                                    <tr><td> r[0] = Number of packets received
                                    <tr><td> r[1] = Number of good packets
                                    <tr><td> r[2] = Number of corrected packets
                                    <tr><td> r[3] = RSSI value
                                    <tr><td> r[4] = Boolean flag showing if RSSI value is valid
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will return the last packet generated by either
                            RXDATA1 or RXDATA2. Once the packet has been read it cannot be
                            read again until the next packet is generated.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.hqGetRxdata.restype = ct.c_int32
        self.TestEngineDLL.hqGetRxdata.argtypes = [ct.c_uint32, ct.c_int32, ct.c_void_p]
        if rxData == None:
            rxData = []
        local_rxData = (ct.c_uint16 * len(rxData))(*rxData)
        retval = self.TestEngineDLL.hqGetRxdata(handle, timeout, local_rxData)
        rxData = local_rxData[:]
        return retval, rxData
    # end of hqGetRxdata


    def radiotestCfgFreq(self, handle: int, txRxInterval: int, loopback: int, report: int) -> int:
        r"""Function TestEngine::radiotestCfgFreq() wrapper for radiotestCfgFreq in TestEngine DLL.

        Python API:
            radiotestCfgFreq(handle: int, txRxInterval: int, loopback: int, report: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgFreq(handle=0, txRxInterval=0, loopback=0, report=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgFreq(uint32 handle, uint16 txRxInterval,
                                                   uint16 loopback, uint16 report)

            Parameters :    handle -
                                Handle to the device.

                            txRxInterval -
                                Sets the period in microseconds between TX and RX events in
                                RXDATA, TXDATA, BIT ERR and LOOP BACK test modes. Default is
                                1250 (20 slots), maximum 65536. If passed as 0, current value
                                unchanged.

                            loopback -
                                Sets the offset in microseconds between a reception event and
                                retransmission of the data in loopback. Default is 1875 (two
                                slots later), must be less than txRxInterval. If passed as
                                zero current value unchanged.

                            report -
                                Sets the time in seconds between reports to host sent by
                                RXDATA and BIT ERR functions. The default is 1s. If passed 0,
                                the current value is unchanged. The maximum value is 65.
                                Passing a value greater than 65 results in error.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets three values used in deciding timing details of tests. This
                            command has been superseded by radiotestCfgFreqMs, which allows
                            finer control of the reporting interval (in milliseconds).
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestBerLoopback.

        """
        self.TestEngineDLL.radiotestCfgFreq.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgFreq.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgFreq(handle, txRxInterval, loopback, report)
        
        return retval
    # end of radiotestCfgFreq


    def radiotestCfgFreqMs(self, handle: int, txRxInterval: int, loopback: int, report: int) -> int:
        r"""Function TestEngine::radiotestCfgFreqMs() wrapper for radiotestCfgFreqMs in TestEngine DLL.

        Python API:
            radiotestCfgFreqMs(handle: int, txRxInterval: int, loopback: int, report: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgFreqMs(handle=0, txRxInterval=0, loopback=0, report=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgFreqMs(uint32 handle, uint16 txRxInterval,
                                                     uint16 loopback, uint16 report)

            Parameters :    handle -
                                Handle to the device.

                            txRxInterval -
                                Sets the period in microseconds between TX and RX events in
                                RXDATA, TXDATA, BIT ERR and LOOP BACK test modes. Default is
                                1250 (20 slots), maximum 65536. If passed as 0, current value
                                unchanged.

                            loopback -
                                Sets the offset in microseconds between a reception event and
                                retransmission of the data in loopback. Default is 1875 (two
                                slots later), must be less than txRxInterval. If passed as
                                zero current value unchanged.

                            report -
                                Sets the time in milliseconds between reports to host sent
                                by RXDATA and BIT ERR functions. The default is 1000mS. If
                                passed 0, the current value is unchanged. The absolute minimum
                                value for this parameter is 100mS. Attempting to set a value
                                greater than 0 and less than 100mS results in error. However,
                                depending on the speed of the transport used, a higher minimum
                                value may be required. It is recommended that for LPT SPI
                                connections, a minimum value of 800mS is used. For all other
                                transports, a 200mS minimum value is recommended. Using values
                                less than the recommended minimum may result in failures to
                                read HQ data, due to the transport not being able to read the
                                data from the chip quickly enough between reports.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets three values used in deciding timing details of tests, with
                            the report interval being set in milliseconds (whereas
                            radiotestCfgFreq sets the interval in seconds). If the firmware
                            version being used does not support this function, it will
                            return error. In this case, use radiotestCfgFreq instead.
                            <p>
                            For BIT ERR functions, reducing the reporting time from the
                            default 1000mS may improve test time for small sample sizes
                            tested with big packet sizes (i.e. if you are getting far more
                            bits in each report than are required for your sample size).
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :

                uint32 rxHandle = TE_INVALID_HANDLE_VALUE;
                uint32 txHandle = TE_INVALID_HANDLE_VALUE;

                cout << "Trying rxHandle..." << endl;
                rxHandle = openTestEngine(BCSP, "COM1", 115200, 5000, 0);

                cout << "Trying txHandle..." << endl;
                txHandle = openTestEngine(USB, "\\\\.\\csr0", 0, 5000, 100);

                if(txHandle != TE_INVALID_HANDLE_VALUE && rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    int32 teRet;

                    do
                    {
                        // Configure the packet types
                        teRet = radiotestCfgPkt(rxHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }
                        teRet = radiotestCfgPkt(txHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Set the TX/RX interval
                        teRet = radiotestCfgFreqMs(rxHandle, 37500, 9375, 200);
                        if (teRet != TE_OK)
                        {
                            break;
                        }
                        teRet = radiotestCfgFreqMs(txHandle, 37500, 9375, 200);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        const uint16 FREQ_MHZ = 2441;
                        const uint16 INT_PA = 50;
                        const uint16 EXT_PA = 0;
                        const uint16 SAMPLE_SIZE = 10000;

                        // Start the transmitter and receiver
                        teRet = radiotestBerLoopback(txHandle, FREQ_MHZ, INT_PA, EXT_PA,
                                                     SAMPLE_SIZE);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        teRet = radiotestLoopback(rxHandle, FREQ_MHZ, INT_PA, EXT_PA);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Gather the BER information
                        int32 count = 0;
                        uint32 ber[9];

                        do
                        {
                            ++count;
                            teRet = hqGetBer(txHandle, 1000, ber);
                        } while (teRet == TE_ERROR && count < 10);

                        if (teRet == TE_OK)
                        {
                            cout << "Bit count = " << ber[0] << endl;
                            cout << "Bit errors = " << ber[1] << endl;
                            cout << "Received packets = " << ber[3] << endl;
                            cout << "Expected packets = " << ber[4] << endl;
                            cout << "Header errors = " << ber[5] << endl;
                            cout << "CRC errors = " << ber[6] << endl;
                            cout << "Uncorrected errors = " << ber[7] << endl;
                            cout << "Sync errors = " << ber[8] << endl;
                        }
                        else
                        {
                            cout << "****FAIL****" << endl;
                        }

                    } while(0);

                    if (teRet != TE_OK)
                    {
                        cout << "TestEngine error" << endl;
                    }
                }

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(txHandle);
                }
                if (rxHandle != TE_INVALID_HANDLE_VALUE)
                {
                    closeTestEngine(rxHandle);
                }

        """
        self.TestEngineDLL.radiotestCfgFreqMs.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgFreqMs.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgFreqMs(handle, txRxInterval, loopback, report)
        
        return retval
    # end of radiotestCfgFreqMs


    def radiotestCfgPkt(self, handle: int, type: int, size: int) -> int:
        r"""Function TestEngine::radiotestCfgPkt() wrapper for radiotestCfgPkt in TestEngine DLL.

        Python API:
            radiotestCfgPkt(handle: int, type: int, size: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgPkt(handle=0, type=0, size=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgPkt(uint32 handle, uint16 type, uint16 size)

            Parameters :    handle -
                                Handle to the device.

                            type -
                                A standard Bluetooth packet type from the following table:
                                    <table>
                                        <tr><td>DM1 = 3
                                        <tr><td>DH1 = 4
                                        <tr><td>HV1 = 5
                                        <tr><td>HV2 = 6
                                        <tr><td>HV3 = 7
                                        <tr><td>DV = 8
                                        <tr><td>AUX1 = 9
                                        <tr><td>DM3 = 10
                                        <tr><td>DH3 = 11
                                        <tr><td>EV4 = 12
                                        <tr><td>EV5 = 13
                                        <tr><td>DM5 = 14
                                        <tr><td>DH5 = 15
                                        <tr><td>2-DH1 = 20
                                        <tr><td>2-EV3 = 22
                                        <tr><td>3-EV3 = 23
                                        <tr><td>3-DH1 = 24
                                        <tr><td>2-DH3 = 26
                                        <tr><td>3-DH3 = 27
                                        <tr><td>2-EV5 = 28
                                        <tr><td>3-EV5 = 29
                                        <tr><td>2-DH5 = 30
                                        <tr><td>3-DH5 = 31
                                    </table>
                                <p>
                                Any other number sets the default, which is DH1. In this case
                                the size is also set to the maximum for a DH1 packet.

                            size -
                                The size of the data payload in each packet, from 0 to the
                                maximum for the type. See teRadGetMaxPayloadLen for the
                                maximum sizes for each packet type.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets packet type and size for transmitter tests. An invalid
                            packet type or size exceeding the maximum for the specified
                            type will result in an error.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :       See example for radiotestBerLoopback.

        """
        self.TestEngineDLL.radiotestCfgPkt.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgPkt.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgPkt(handle, type, size)
        
        return retval
    # end of radiotestCfgPkt


    def radiotestCfgBitError(self, handle: int, sampleSize: int, reset: int) -> int:
        r"""Function TestEngine::radiotestCfgBitError() wrapper for radiotestCfgBitError in TestEngine DLL.

        Python API:
            radiotestCfgBitError(handle: int, sampleSize: int, reset: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgBitError(handle=0, sampleSize=0, reset=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgBitError(uint32 handle, uint32 sampleSize,
                                                       uint8 reset)

            Parameters :    handle -
                                Handle to the device.

                            sampleSize -
                                If non-zero, the target for total counters is set to this and
                                total count resets at this value. If passed as 0 the current
                                value is unchanged.

                            reset -
                                Boolean value (0 = False, anything else = True). If True, and
                                if Ber1, Ber2, or BerLoopback is active, immediately resets
                                the counters for the total statistics, but not over the last
                                report period.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Can be used to set the sample size used in bit error measurements,
                            and reset the counters if required.
                            <p>
                            Note that the radiotestBer1, radiotestBer2, and
                            radiotestBerLoopback functions also take a sampleSize parameter
                            and set the value before running the test. Therefore there is
                            normally no need to call this function, unless a reset of the
                            counters is required.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgBitError.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgBitError.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.radiotestCfgBitError(handle, sampleSize, reset)
        
        return retval
    # end of radiotestCfgBitError


    def radiotestCfgTxPaAtten(self, handle: int, atten: int) -> int:
        r"""Function TestEngine::radiotestCfgTxPaAtten() wrapper for radiotestCfgTxPaAtten in TestEngine DLL.

        Python API:
            radiotestCfgTxPaAtten(handle: int, atten: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgTxPaAtten(handle=0, atten=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgTxPaAtten(uint32 handle, uint16 atten)

            Parameters :    handle -
                                Handle to the device.

                            atten -
                                Attenuation value to set.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the TX PA attenuation value used during transmission.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgTxPaAtten.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgTxPaAtten.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgTxPaAtten(handle, atten)
        
        return retval
    # end of radiotestCfgTxPaAtten


    def radiotestCfgXtalFtrim(self, handle: int, fTrim: int) -> int:
        r"""Function TestEngine::radiotestCfgXtalFtrim() wrapper for radiotestCfgXtalFtrim in TestEngine DLL.

        Python API:
            radiotestCfgXtalFtrim(handle: int, fTrim: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgXtalFtrim(handle=0, fTrim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgXtalFtrim(uint32 handle, uint16 fTrim)

            Parameters :    handle -
                                Handle to the device.

                            fTrim -
                                A number between 0 and 63 inclusive. This is not a permanent
                                change.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Timing for BlueCore is controlled by a crystal. This requires
                            trimming for new hardware. This command can be used to set a new
                            trim value either before a radiotest command is started or while
                            a test is already in operation; the change takes effect
                            immediately.
                            <p>
                            This is supported for BlueCore ICs only - for other ICs use
                            teMcSetXtalFreqTrim.

        """
        self.TestEngineDLL.radiotestCfgXtalFtrim.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgXtalFtrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgXtalFtrim(handle, fTrim)
        
        return retval
    # end of radiotestCfgXtalFtrim


    def radiotestCalcXtalOffset(self, nominalFreqMhz: float, actualFreqMhz: float, offset: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::radiotestCalcXtalOffset() wrapper for radiotestCalcXtalOffset in TestEngine DLL.

        Python API:
            radiotestCalcXtalOffset(nominalFreqMhz: float, actualFreqMhz: float, offset: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, offset = myDll.radiotestCalcXtalOffset(nominalFreqMhz=0.0, actualFreqMhz=0.0)
            print(retval, offset)

        Detail From Wrapped C API:
            Function :      int32 radiotestCalcXtalOffset(float64 nominalFreqMhz,
                                                          float64 actualFreqMhz,
                                                          int16* offset)

            Parameters :    nominalFreqMhz -
                                The nominal frequency in MHz.

                            actualFreqMhz -
                                The measured frequency in MHz.

                            offset -
                                Location where the resulting offset value will be stored.

            Returns :       <table>
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function will calculate the frequency offset value from the
                            given parameters. The resulting value can be written to the
                            persistent store using psWriteXtalOffset.
                            <p>
                            The value of the PSKEY is an int16 value in parts per 2^20.
                            The calculation used is:
                            <p>
                            ((actualFreqKhz/nominalFreqKhz) - 1) * 2^20 = offset
                            <p>
                            The resulting offset value is then rounded to the nearest
                            integer value. This value must be between -300 and 300, otherwise
                            an error is returned (the frequency offset is too large to be
                            compensated for). An error is also returned if either frequency
                            parameter is zero.
                            <p>
                            The frequency measurement is usually taken after starting CW
                            transmission with radiotestTxstart. It is important that the
                            chip booted with an offset value of 0 (default) when taking the
                            frequency measurement for offset calibration, otherwise the
                            resulting value will be incorrect. The current offset value can
                            be read using psReadXtalOffset, and set using psWriteXtalOffset
                            (after which a reset is required for the value to take effect).
                            <p>
                            This function can be used as part of per-device crystal
                            calibration for some BC7 and later BlueCore ICs, which use a
                            frequency offset value rather than a crystal trim value. It is
                            not supported for other IC types.

        """
        self.TestEngineDLL.radiotestCalcXtalOffset.restype = ct.c_int32
        self.TestEngineDLL.radiotestCalcXtalOffset.argtypes = [ct.c_double, ct.c_double, ct.c_void_p]
        local_offset = ct.c_int16(offset)
        retval = self.TestEngineDLL.radiotestCalcXtalOffset(nominalFreqMhz, actualFreqMhz, ct.byref(local_offset))
        offset = local_offset.value
        return retval, offset
    # end of radiotestCalcXtalOffset


    def radiotestCfgUapLap(self, handle: int, uap: int, lap: int) -> int:
        r"""Function TestEngine::radiotestCfgUapLap() wrapper for radiotestCfgUapLap in TestEngine DLL.

        Python API:
            radiotestCfgUapLap(handle: int, uap: int, lap: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgUapLap(handle=0, uap=0, lap=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgUapLap(uint32 handle, uint16 uap, uint32 lap)

            Parameters :    handle -
                                Handle to the device.

                            uap -
                                UAP portion of the device address (0 to 0xff).

                            lap -
                                LAP portion of the device address (0 to 0xffffff).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the UAP and LAP to be used in radio tests. The DUT usually
                            uses its own Bluetooth Device address to determine the access sync
                            code, as if it is master of a piconet.
                            The UAP and LAP are the only parts used.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgUapLap.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgUapLap.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.radiotestCfgUapLap(handle, uap, lap)
        
        return retval
    # end of radiotestCfgUapLap


    def radiotestCfgIqTrim(self, handle: int, trim: int) -> int:
        r"""Function TestEngine::radiotestCfgIqTrim() wrapper for radiotestCfgIqTrim in TestEngine DLL.

        Python API:
            radiotestCfgIqTrim(handle: int, trim: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgIqTrim(handle=0, trim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgIqTrim(uint32 handle, uint16 trim)

            Parameters :    handle -
                                Handle to the device.

                            trim -
                                Value to be written to the register, ANA_IQ_TRIM.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   The IQ block may be trimmed by setting a register, ANA_IQ_TRIM.
                            This allows the variable to be set for the test modes. The value
                            "trim", 0 to 511 inclusive, takes effect immediately, is not
                            saved, and must be reset on each test, as the IQ is calibrated at
                            the start.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgIqTrim.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgIqTrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgIqTrim(handle, trim)
        
        return retval
    # end of radiotestCfgIqTrim


    def radiotestCfgTxIf(self, handle: int, offset: int) -> int:
        r"""Function TestEngine::radiotestCfgTxIf() wrapper for radiotestCfgTxIf in TestEngine DLL.

        Python API:
            radiotestCfgTxIf(handle: int, offset: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgTxIf(handle=0, offset=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgTxIf(uint32 handle, int16 offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                Value to be written to the register, ANA_IQ_TRIM.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   The BC01 transmitter uses an additional offset in the IF part of
                            the transmitter, which needs to be configured for optimum
                            performance. The target is to be able to set this to zero.
                            However, the stack currently uses an offset of 1MHz 1.5MHz.
                            "offset_half_mhz" sets the value of this in units of 0.5MHz for
                            the radiotests. The default is the value used in standard
                            operation, currently 3 units, i.e. 1.5MHz offset.  Note this is a
                            signed integer. The range is -5 to +5. This must be set before
                            the start of a radio transmitter test.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgTxIf.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgTxIf.argtypes = [ct.c_uint32, ct.c_int16]
        
        retval = self.TestEngineDLL.radiotestCfgTxIf(handle, offset)
        
        return retval
    # end of radiotestCfgTxIf


    def radiotestCfgTxTrim(self, handle: int, amAddr: int) -> int:
        r"""Function TestEngine::radiotestCfgTxTrim() wrapper for radiotestCfgTxTrim in TestEngine DLL.

        Python API:
            radiotestCfgTxTrim(handle: int, amAddr: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgTxTrim(handle=0, amAddr=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgTxTrim(uint32 handle, uint16 amAddr)

            Parameters :    handle -
                                Handle to the device.

                            amAddr -
                                Active member address.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the AM_ADDR used in the header of test transmissions, and
                            expected in receiving test transmissions. It is a number between
                            0 and 7, inclusive. The default value is 7. This takes effect
                            immediately and lasts until a new test is restarted, at which
                            point a default read from persistent store is used. The defaults
                            are: PSKEY_RADIOTEST_TX_TRIM1 for PRBS data (which is assumed
                            for all reception routines), PSKEY_RADIOTEST_TX_TRIM2 for alternating
                            bits (1010...), PSKEY_RADIOTEST_TX_TRIM3 for alternating nibbles
                            (11110000).
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgTxTrim.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgTxTrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgTxTrim(handle, amAddr)
        
        return retval
    # end of radiotestCfgTxTrim


    def radiotestCfgLoLvl(self, handle: int, loLvl: int) -> int:
        r"""Function TestEngine::radiotestCfgLoLvl() wrapper for radiotestCfgLoLvl in TestEngine DLL.

        Python API:
            radiotestCfgLoLvl(handle: int, loLvl: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestCfgLoLvl(handle=0, loLvl=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgLoLvl(uint32 handle, uint16 loLvl)

            Parameters :    handle -
                                Handle to the device.

                            loLvl -
                                Analogue LO output level.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command sets the value of the Analogue Local Oscillator
                            output level to loLvl, over-riding the value calculated by the
                            internal calibration algorithm.
                            <p>
                            Important Note:
                                Use of this command is unnecessary for all normal users.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.radiotestCfgLoLvl.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgLoLvl.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestCfgLoLvl(handle, loLvl)
        
        return retval
    # end of radiotestCfgLoLvl


    def radiotestCfgHoppingSeq(self, handle: int, channels: list) -> Tuple[int, list]:
        r"""Function TestEngine::radiotestCfgHoppingSeq() wrapper for radiotestCfgHoppingSeq in TestEngine DLL.

        Python API:
            radiotestCfgHoppingSeq(handle: int, channels: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, channels = myDll.radiotestCfgHoppingSeq(handle=0, channels=[0,1])
            print(retval, channels)

        Detail From Wrapped C API:
            Function :      int32 radiotestCfgHoppingSeq(uint32 handle, uint16* channels)

            Parameters :    handle -
                                Handle to the device.

                            channels -
                                Pointer to an array of 5 uint16 values. The 5 values are bit
                                fields used to enable / disable each of the 79 channels. If a
                                bit = 1, the channel is used, otherwise it is not used. The
                                array elements map to channels as follows:
                                <table>
                                    <tr><td>0 = Channels 0-15
                                    <tr><td>1 = Channels 16-31
                                    <tr><td>2 = Channels 32-47
                                    <tr><td>3 = Channels 48-63
                                    <tr><td>4 = Channels 64-78 (bit 15 unused)
                                </table>
                                For each uint16 element, bit 0 (LSB) is for the lowest channel
                                number in the range, i.e. bit 0 of the first uint16 is for
                                channel 0.
                                <p>
                                At least 1 channel must be enabled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Configures the set of hop frequencies to be used with
                            radiotestRxdata2, radiotestTxdata2 and radiotestBer2. The
                            functionality is analogous to the hciSetAfhHostChannelClass
                            function. The adjusted hopping sequence allows use of these
                            radiotest modes while simulating a reduced hop set.
                            <p>
                            The hopping algorithm is the same as that used when all
                            frequencies are in use, but only on the selected frequencies.
                            This guarantees that the radio spends equal amounts of time on
                            each selected frequency.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Attempting to open connection..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    int32 teRet;

                    do
                    {
                        // Configure the packet type
                        teRet = radiotestCfgPkt(teHandle, 15, 339);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Set the TX/RX interval
                        teRet = radiotestCfgFreq(teHandle, 37500, 9375, 1);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Use lowest 20 channels only
                        uint16 channels[5] = { 0xffff, 0x000f, 0x0000, 0x0000, 0x0000 };
                        teRet = radiotestCfgHoppingSeq(teHandle, channels);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Start transmission
                        teRet = radiotestTxdata2(teHandle, 0, 50, 0);
                        if (teRet != TE_OK)
                        {
                            break;
                        }

                        // Perform tests

                    } while(0);

                    if (teRet != TE_OK)
                    {
                        cout << "TestEngine error" << endl;
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.radiotestCfgHoppingSeq.restype = ct.c_int32
        self.TestEngineDLL.radiotestCfgHoppingSeq.argtypes = [ct.c_uint32, ct.c_void_p]
        if channels == None:
            channels = []
        local_channels = (ct.c_uint16 * len(channels))(*channels)
        retval = self.TestEngineDLL.radiotestCfgHoppingSeq(handle, local_channels)
        channels = local_channels[:]
        return retval, channels
    # end of radiotestCfgHoppingSeq


    def radiotestSettle(self, handle: int, start: int, end: int) -> int:
        r"""Function TestEngine::radiotestSettle() wrapper for radiotestSettle in TestEngine DLL.

        Python API:
            radiotestSettle(handle: int, start: int, end: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestSettle(handle=0, start=0, end=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestSettle(uint32 handle, uint16 start, uint16 end)

            Parameters :    handle -
                                Handle to the device.

                            start -
                                Channel to start stepping from. 0 to 78.

                            end -
                                Channel to finish stepping at. 0 to 78.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Builds the radio's channel LO_TRIM frequency lookup table (LUT),
                            then does a step from the start channel to the end channel, while
                            the synthesiser is running. It digitises the synthesiser (LO_TUNE)
                            error voltage at intervals of 10 | 20us over the next 200us.
                            <p>
                            The results can be retrieved using hqGetSettle.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.radiotestSettle.restype = ct.c_int32
        self.TestEngineDLL.radiotestSettle.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.radiotestSettle(handle, start, end)
        
        return retval
    # end of radiotestSettle


    def hqGetSettle(self, handle: int, results: list) -> Tuple[int, list]:
        r"""Function TestEngine::hqGetSettle() wrapper for hqGetSettle in TestEngine DLL.

        Python API:
            hqGetSettle(handle: int, results: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, results = myDll.hqGetSettle(handle=0, results=[0,1])
            print(retval, results)

        Detail From Wrapped C API:
            Function :      int32 hqGetSettle(uint32 handle, uint16* results)

            Parameters :    handle -
                                Handle to the device.

                            results -
                                Pointer to a pre-allocated 9 element array to receive the
                                results.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to retrieve the results made from a call to
                            radiotestSettle.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

            Deprecated :

        """
        self.TestEngineDLL.hqGetSettle.restype = ct.c_int32
        self.TestEngineDLL.hqGetSettle.argtypes = [ct.c_uint32, ct.c_void_p]
        if results == None:
            results = []
        local_results = (ct.c_uint16 * len(results))(*results)
        retval = self.TestEngineDLL.hqGetSettle(handle, local_results)
        results = local_results[:]
        return retval, results
    # end of hqGetSettle


    def get_freq_offset(self, handle: int, offset: float=0.0, sampleSize: int=0) -> Tuple[int, float]:
        r"""Function TestEngine::get_freq_offset() wrapper for get_freq_offset in TestEngine DLL.

        Python API:
            get_freq_offset(handle: int, offset: float=0.0, sampleSize: int=0) -> Tuple[int, float]

        Python Example Call Syntax:
            retval, offset = myDll.get_freq_offset(handle=0, sampleSize=0)
            print(retval, offset)

        Detail From Wrapped C API:
            Function :      int32 get_freq_offset(uint32 handle, float64* offset,
                                                  int32 sampleSize)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                Pointer to the offset. Measured in parts per million (PPM),
                                this value is an average of sampleSize readings from the
                                BlueCore receiver.

                            sampleSize -
                                Determines how many readings of offset are averaged. The
                                software will only accept values in the range of 20 to 200,
                                any values outside this range will be forced up to 20 or 200.
                                The choice of value will determine the accuracy and speed.
                                The lower the value the quicker but less accurate the results,
                                the higher the value the more accurate but slower the function.
                                The optimal value is 60 to 100.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command will read the frequency offset of a received signal.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.get_freq_offset.restype = ct.c_int32
        self.TestEngineDLL.get_freq_offset.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_int32]
        local_offset = ct.c_double(offset)
        retval = self.TestEngineDLL.get_freq_offset(handle, ct.byref(local_offset), sampleSize)
        offset = local_offset.value
        return retval, offset
    # end of get_freq_offset


    def bccmdSetEeprom(self, handle: int, log2bytes: int, addrMask: int) -> int:
        r"""Function TestEngine::bccmdSetEeprom() wrapper for bccmdSetEeprom in TestEngine DLL.

        Python API:
            bccmdSetEeprom(handle: int, log2bytes: int, addrMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetEeprom(handle=0, log2bytes=0, addrMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetEeprom(uint32 handle, uint16 log2bytes,
                                                 uint16 addrMask)

            Parameters :    handle -
                                Handle to the device.

                            log2bytes -
                                Specifies the size of the EEPROM (log2 bytes). That is the
                                number of bits required to address any byte of the memory
                                array.

                            addrMask -
                                A bitmap specifying which, if any, of the slave address bits
                                are used to specify high-order bits of the array address.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes the header to the I2C EEPROM to allow the device to be used
                            to store PS values and VM applications.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdSetEeprom.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetEeprom.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdSetEeprom(handle, log2bytes, addrMask)
        
        return retval
    # end of bccmdSetEeprom


    def psReadBdAddr(self, handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]:
        r"""Function TestEngine::psReadBdAddr() wrapper for psReadBdAddr in TestEngine DLL.

        Python API:
            psReadBdAddr(handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]

        Python Example Call Syntax:
            retval, lap, uap, nap = myDll.psReadBdAddr(handle=0)
            print(retval, lap, uap, nap)

        Detail From Wrapped C API:
            Function :      int32 psReadBdAddr(uint32 handle, uint32* lap, uint8* uap,
                                               uint16* nap)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                Pointer to a uint32 to hold the LAP portion of the BD_ADDR

                            uap -
                                Pointer to a uint8 to hold the UAP portion of the BD_ADDR

                            nap -
                                Pointer to a uint16 to hold the NAP portion of the BD_ADDR

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Function to read the BD_ADDR (Bluetooth address) from the device.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadBdAddr.restype = ct.c_int32
        self.TestEngineDLL.psReadBdAddr.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_lap = ct.c_uint32(lap)
        local_uap = ct.c_uint8(uap)
        local_nap = ct.c_uint16(nap)
        retval = self.TestEngineDLL.psReadBdAddr(handle, ct.byref(local_lap), ct.byref(local_uap), ct.byref(local_nap))
        lap = local_lap.value
        uap = local_uap.value
        nap = local_nap.value
        return retval, lap, uap, nap
    # end of psReadBdAddr


    def psRead(self, handle: int, psKey: int, store: int, arrayLen: int, data: list, keyLen: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::psRead() wrapper for psRead in TestEngine DLL.

        Python API:
            psRead(handle: int, psKey: int, store: int, arrayLen: int, data: list, keyLen: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, data, keyLen = myDll.psRead(handle=0, psKey=0, store=0, arrayLen=0, data=[0,1])
            print(retval, data, keyLen)

        Detail From Wrapped C API:
            Function :      int32 psRead(uint32 handle, uint16 psKey, uint16 store,
                                         uint16 arrayLen, uint16* data, uint16* keyLen)

            Parameters :    handle -
                                Handle to the device.

                            psKey -
                                PS key ID of the value to be read.

                            store -
                                Bit mask to identify the PS store layer to write to. See
                                comments above under PS_STORES.

                            arrayLen -
                                Size of the array allocated to hold the PS value.

                            data -
                                Array of 16-bit words of size "arraylen" to hold the PS value.

                            keyLen -
                                Pointer to a 16-bit word to hold to length of the PS key value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to read the value of the PS key specified.
                            <p>
                            If the given arrayLen parameter value is less than the length
                            of the PS key value, the "Error" value will be returned, and the
                            keyLen parameter will be set to the required length.
                            <p>
                            For ICs other than BlueCore IC types the teConfigCache* and/or
                            tePs* functions should be used.

        """
        self.TestEngineDLL.psRead.restype = ct.c_int32
        self.TestEngineDLL.psRead.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * max(arrayLen, len(data)))(*data)
        local_keyLen = ct.c_uint16(keyLen)
        retval = self.TestEngineDLL.psRead(handle, psKey, store, arrayLen, local_data, ct.byref(local_keyLen))
        data = local_data[:]
        keyLen = local_keyLen.value
        return retval, data, keyLen
    # end of psRead


    def psClear(self, handle: int, psKey: int, store: int) -> int:
        r"""Function TestEngine::psClear() wrapper for psClear in TestEngine DLL.

        Python API:
            psClear(handle: int, psKey: int, store: int) -> int

        Python Example Call Syntax:
            retval = myDll.psClear(handle=0, psKey=0, store=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psClear(uint32 handle, uint16 psKey, uint16 store)

            Parameters :    handle -
                                Handle to the device.

                            psKey -
                                PS key value of the entry to be removed.

                            store -
                                Bit mask to identify the PS store layer(s) from which the PS
                                entry will be erased.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function removes from the PS the value stored in the layer
                            specified by the stores parameter. Clearing values from the PS
                            can have subtle effects. The description of the Layered Model of
                            the PS stores above shows how clearing a value from the
                            PS_STORES_I layer can (re)expose a value in the PS_STORES_F or
                            PS_STORES_R layer.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* and/or tePs* functions should be used.

        """
        self.TestEngineDLL.psClear.restype = ct.c_int32
        self.TestEngineDLL.psClear.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.psClear(handle, psKey, store)
        
        return retval
    # end of psClear


    def psClearAll(self, handle: int, store: int) -> int:
        r"""Function TestEngine::psClearAll() wrapper for psClearAll in TestEngine DLL.

        Python API:
            psClearAll(handle: int, store: int) -> int

        Python Example Call Syntax:
            retval = myDll.psClearAll(handle=0, store=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psClearAll(uint32 handle, uint16 store)

            Parameters :    handle -
                                Handle to the device.

                            store -
                                Bit mask to identify the PS store layer(s) from which the PS
                                entries will be erased.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This removes all values from the stores specified; only values in
                            the PSROM layer remain. This command should be used with caution.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* and/or tePs* functions should be used.

        """
        self.TestEngineDLL.psClearAll.restype = ct.c_int32
        self.TestEngineDLL.psClearAll.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psClearAll(handle, store)
        
        return retval
    # end of psClearAll


    def psFactorySet(self, handle: int) -> int:
        r"""Function TestEngine::psFactorySet() wrapper for psFactorySet in TestEngine DLL.

        Python API:
            psFactorySet(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.psFactorySet(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psFactorySet(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This moves all values in the PS_STORES_I layer to the PS_STORES_F
                            layer.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psFactorySet.restype = ct.c_int32
        self.TestEngineDLL.psFactorySet.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.psFactorySet(handle)
        
        return retval
    # end of psFactorySet


    def psFactoryRestoreAll(self, handle: int) -> int:
        r"""Function TestEngine::psFactoryRestoreAll() wrapper for psFactoryRestoreAll in TestEngine DLL.

        Python API:
            psFactoryRestoreAll(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.psFactoryRestoreAll(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psFactoryRestoreAll(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command removes all values from the PS_STORES_I store, so
                            restoring the chip\x92s PS to the state it was in when the
                            PS_FACTORY_SET command was invoked.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psFactoryRestoreAll.restype = ct.c_int32
        self.TestEngineDLL.psFactoryRestoreAll.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.psFactoryRestoreAll(handle)
        
        return retval
    # end of psFactoryRestoreAll


    def psFactoryRestore(self, handle: int) -> int:
        r"""Function TestEngine::psFactoryRestore() wrapper for psFactoryRestore in TestEngine DLL.

        Python API:
            psFactoryRestore(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.psFactoryRestore(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psFactoryRestore(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This is identical to PS_FACTORY_RESTORE_ALL except that values in
                            the PS_STORES_I layer that do not obscure values in the
                            PS_STORES_F and/or PS_STORES_R layers are left in place.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psFactoryRestore.restype = ct.c_int32
        self.TestEngineDLL.psFactoryRestore.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.psFactoryRestore(handle)
        
        return retval
    # end of psFactoryRestore


    def psSize(self, handle: int, psKey: int, store: int, size: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psSize() wrapper for psSize in TestEngine DLL.

        Python API:
            psSize(handle: int, psKey: int, store: int, size: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, size = myDll.psSize(handle=0, psKey=0, store=0)
            print(retval, size)

        Detail From Wrapped C API:
            Function :      int32 psSize(uint32 handle, uint16 psKey, uint16 store,
                                         uint16* size)

            Parameters :    handle -
                                Handle to the device.

                            psKey -
                                PS entry to return the size of.

                            store -
                                PS store to access.

                            size -
                                Pointer to a 16-bit word to hold to length of the PS key value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Returns the internal amount of data, in uint16's, held by a
                            particular PS entry. Failure may indicate that the store mask
                            selected does not contain a valid PS entry.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psSize.restype = ct.c_int32
        self.TestEngineDLL.psSize.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_size = ct.c_uint16(size)
        retval = self.TestEngineDLL.psSize(handle, psKey, store, ct.byref(local_size))
        size = local_size.value
        return retval, size
    # end of psSize


    def psWrite(self, handle: int, psKey: int, store: int, length: int, data: list) -> int:
        r"""Function TestEngine::psWrite() wrapper for psWrite in TestEngine DLL.

        Python API:
            psWrite(handle: int, psKey: int, store: int, length: int, data: list) -> int

        Python Example Call Syntax:
            retval = myDll.psWrite(handle=0, psKey=0, store=0, length=0, data=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWrite(uint32 handle, uint16 psKey, uint16 store,
                                          uint16 length, const uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            psKey -
                                PS key value of the entry to be written.

                            store -
                                PS store to access.

                            length -
                                Length of the data to be written.

                            data -
                                Pointer to an array to hold the key contents.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes the PS setting "psKey" array "data" of length "length"
                            to the persistent store layer identified by "store".
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* and/or tePs* functions should be used.

        """
        self.TestEngineDLL.psWrite.restype = ct.c_int32
        self.TestEngineDLL.psWrite.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.psWrite(handle, psKey, store, length, local_data)
        
        return retval
    # end of psWrite


    def psWriteVerify(self, handle: int, psKey: int, store: int, length: int, data: list) -> int:
        r"""Function TestEngine::psWriteVerify() wrapper for psWriteVerify in TestEngine DLL.

        Python API:
            psWriteVerify(handle: int, psKey: int, store: int, length: int, data: list) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteVerify(handle=0, psKey=0, store=0, length=0, data=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteVerify(uint32 handle, uint16 psKey, uint16 store,
                                                uint16 length, const uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            psKey -
                                PS key value of the entry to be written.

                            store -
                                PS store to access.

                            length -
                                Length of the data to be written.

                            data -
                                Pointer to an array to hold the key contents.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes the PS setting "psKey" array "data" of length "length"
                            to the persistent store layer PS_STORES_I or PS_STORES_F if one
                            those values are identified by "store". The function will then
                            perform a PS read and verify that the PS key has been written
                            correctly.
                            <p>
                            This function will fail if a store mask does not contain
                            PS_STORES_I or PS_STORES_F.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* and/or tePs* functions should be used.

        """
        self.TestEngineDLL.psWriteVerify.restype = ct.c_int32
        self.TestEngineDLL.psWriteVerify.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.psWriteVerify(handle, psKey, store, length, local_data)
        
        return retval
    # end of psWriteVerify


    def psWriteBdAddr(self, handle: int, lap: int, uap: int, nap: int) -> int:
        r"""Function TestEngine::psWriteBdAddr() wrapper for psWriteBdAddr in TestEngine DLL.

        Python API:
            psWriteBdAddr(handle: int, lap: int, uap: int, nap: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteBdAddr(handle=0, lap=0, uap=0, nap=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteBdAddr(uint32 handle, uint32 lap, uint32 uap,
                                                uint32 nap)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                LAP portion of the address to write to the persistent store.

                            uap -
                                UAP portion of the address to write to the persistent store.

                            nap -
                                NAP portion of the address to write to the persistent store.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Function to write the BD_ADDR (Bluetooth address) to the device.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteBdAddr.restype = ct.c_int32
        self.TestEngineDLL.psWriteBdAddr.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.psWriteBdAddr(handle, lap, uap, nap)
        
        return retval
    # end of psWriteBdAddr


    def psReadModuleId(self, handle: int, moduleId: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadModuleId() wrapper for psReadModuleId in TestEngine DLL.

        Python API:
            psReadModuleId(handle: int, moduleId: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, moduleId = myDll.psReadModuleId(handle=0)
            print(retval, moduleId)

        Detail From Wrapped C API:
            Function :      int32 psReadModuleId(uint32 handle, uint32* moduleId)

            Parameters :    handle -
                                Handle to the device.

                            moduleId -
                                Pointer to a variable that will hold the returned module ID.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will attempt to read the module ID stored in
                            BlueCore. The default for this value is 0 (zero).
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadModuleId.restype = ct.c_int32
        self.TestEngineDLL.psReadModuleId.argtypes = [ct.c_uint32, ct.c_void_p]
        local_moduleId = ct.c_uint32(moduleId)
        retval = self.TestEngineDLL.psReadModuleId(handle, ct.byref(local_moduleId))
        moduleId = local_moduleId.value
        return retval, moduleId
    # end of psReadModuleId


    def psReadXtalFtrim(self, handle: int, fTrim: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadXtalFtrim() wrapper for psReadXtalFtrim in TestEngine DLL.

        Python API:
            psReadXtalFtrim(handle: int, fTrim: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, fTrim = myDll.psReadXtalFtrim(handle=0)
            print(retval, fTrim)

        Detail From Wrapped C API:
            Function :      int32 psReadXtalFtrim(uint32 handle, uint16* fTrim)

            Parameters :    handle -
                                Handle to the device.

                            fTrim -
                                Pointer to a variable that will hold the returned xtal fTrim.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will attempt to read the xtal fTrim from the
                            persistent store.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For BC7 and later BlueCore ICs, use psReadXtalOffset to read the
                            frequency offset value instead.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadXtalFtrim.restype = ct.c_int32
        self.TestEngineDLL.psReadXtalFtrim.argtypes = [ct.c_uint32, ct.c_void_p]
        local_fTrim = ct.c_uint16(fTrim)
        retval = self.TestEngineDLL.psReadXtalFtrim(handle, ct.byref(local_fTrim))
        fTrim = local_fTrim.value
        return retval, fTrim
    # end of psReadXtalFtrim


    def psWriteXtalFtrim(self, handle: int, fTrim: int) -> int:
        r"""Function TestEngine::psWriteXtalFtrim() wrapper for psWriteXtalFtrim in TestEngine DLL.

        Python API:
            psWriteXtalFtrim(handle: int, fTrim: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteXtalFtrim(handle=0, fTrim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteXtalFtrim(uint32 handle, uint16 fTrim)

            Parameters :    handle -
                                Handle to the device.

                            fTrim -
                                Crystal frequency trim.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write the crystal trim value to the persistent
                            store.
                            <p>
                            For BC7 and later BlueCore ICs, use psWriteXtalOffset to write a
                            frequency offset value rather than a crystal trim value.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteXtalFtrim.restype = ct.c_int32
        self.TestEngineDLL.psWriteXtalFtrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteXtalFtrim(handle, fTrim)
        
        return retval
    # end of psWriteXtalFtrim


    def psReadXtalOffset(self, handle: int, offset: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadXtalOffset() wrapper for psReadXtalOffset in TestEngine DLL.

        Python API:
            psReadXtalOffset(handle: int, offset: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, offset = myDll.psReadXtalOffset(handle=0)
            print(retval, offset)

        Detail From Wrapped C API:
            Function :      int32 psReadXtalOffset(uint32 handle, int16* offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                Pointer to a variable that will hold the returned xtal
                                offset value. The value is in parts per 2^20.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will attempt to read the crystal offset from the
                            persistent store.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            This function is for use with some BC7 and later BlueCore ICs
                            which use a frequency offset value for crystal trimming. For
                            earlier ICs, use psReadXtalFtrim to read the crystal trim value
                            instead.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadXtalOffset.restype = ct.c_int32
        self.TestEngineDLL.psReadXtalOffset.argtypes = [ct.c_uint32, ct.c_void_p]
        local_offset = ct.c_int16(offset)
        retval = self.TestEngineDLL.psReadXtalOffset(handle, ct.byref(local_offset))
        offset = local_offset.value
        return retval, offset
    # end of psReadXtalOffset


    def psWriteXtalOffset(self, handle: int, offset: int) -> int:
        r"""Function TestEngine::psWriteXtalOffset() wrapper for psWriteXtalOffset in TestEngine DLL.

        Python API:
            psWriteXtalOffset(handle: int, offset: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteXtalOffset(handle=0, offset=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteXtalOffset(uint32 handle, int16 offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                The offset value to write (can be calculated using
                                radiotestCalcXtalOffset).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write the crystal frequency offset value to
                            the persistent store.
                            <p>
                            The value of the PSKEY is an int16 value in parts per 2^20, and
                            can be calculated using radiotestCalcXtalOffset. See the
                            documentation for radiotestCalcXtalOffset for details of the
                            calculation used and value range.
                            <p>
                            This function is for use with some BC7 and later BlueCore ICs
                            which use a frequency offset value for crystal trimming. For
                            earlier ICs, use psWriteXtalFtrim to write a crystal trim value
                            instead.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteXtalOffset.restype = ct.c_int32
        self.TestEngineDLL.psWriteXtalOffset.argtypes = [ct.c_uint32, ct.c_int16]
        
        retval = self.TestEngineDLL.psWriteXtalOffset(handle, offset)
        
        return retval
    # end of psWriteXtalOffset


    def psWriteModuleSecurityCode(self, handle: int, code: list) -> int:
        r"""Function TestEngine::psWriteModuleSecurityCode() wrapper for psWriteModuleSecurityCode in TestEngine DLL.

        Python API:
            psWriteModuleSecurityCode(handle: int, code: list) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteModuleSecurityCode(handle=0, code=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteModuleSecurityCode(uint32 handle, const uint16* code)

            Parameters :    handle -
                                Handle to the device.

                            code -
                                Pointer to 8 member unsigned 16 bit integer array holding the
                                128 bit module security code.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write the module security code to the
                            persistent store.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psWriteModuleSecurityCode.restype = ct.c_int32
        self.TestEngineDLL.psWriteModuleSecurityCode.argtypes = [ct.c_uint32, ct.c_void_p]
        if code == None:
            code = []
        local_code = (ct.c_uint16 * len(code))(*code)
        retval = self.TestEngineDLL.psWriteModuleSecurityCode(handle, local_code)
        
        return retval
    # end of psWriteModuleSecurityCode


    def psWriteModuleId(self, handle: int, moduleId: int) -> int:
        r"""Function TestEngine::psWriteModuleId() wrapper for psWriteModuleId in TestEngine DLL.

        Python API:
            psWriteModuleId(handle: int, moduleId: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteModuleId(handle=0, moduleId=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteModuleId(uint32 handle, uint32 moduleId)

            Parameters :    handle -
                                Handle to the device.

                            moduleId -
                                Module ID to be stored in BlueCore persistent store.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will attempt to write the module ID to BlueCore.
                            The default for this value is 0 (zero).
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteModuleId.restype = ct.c_int32
        self.TestEngineDLL.psWriteModuleId.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.psWriteModuleId(handle, moduleId)
        
        return retval
    # end of psWriteModuleId


    def psWriteBaudrate(self, handle: int, value: int) -> int:
        r"""Function TestEngine::psWriteBaudrate() wrapper for psWriteBaudrate in TestEngine DLL.

        Python API:
            psWriteBaudrate(handle: int, value: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteBaudrate(handle=0, value=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteBaudrate(uint32 handle, uint16 value)

            Parameters :    handle -
                                Handle to the device.

                            value -
                                Used determine the baudrate where:
                                    baudrate = value/0.004096

                                <p>
                                Some common values are:
                                <table>
                                    <tr><td> 38k4    baud    -   157   (0x009d)
                                    <tr><td> 57k6    baud    -   236   (0x00ec)
                                    <tr><td> 115k2   baud    -   472   (0x01d8)
                                    <tr><td> 230k4   baud    -   944   (0x03b0)
                                    <tr><td> 460k8   baud    -   1887  (0x075f)
                                    <tr><td> 921k6   baud    -   3775  (0x0ebf)
                                    <tr><td> 1382k4  baud    -   5662  (0x161e)
                                </table>
                                The maximum rated speed for the UART hardware is 1.5 Mbaud,
                                although this key can be set to a higher value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a value corresponding to the baudrate to
                            the persistent store. This function can only be used in builds
                            later than 18.x. For earlier builds the
                            PSKEY_HOSTIO_UART_PS_BLOCK should be modified.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteBaudrate.restype = ct.c_int32
        self.TestEngineDLL.psWriteBaudrate.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteBaudrate(handle, value)
        
        return retval
    # end of psWriteBaudrate


    def psWriteRadiotestFirstTrimTime(self, handle: int, time: int) -> int:
        r"""Function TestEngine::psWriteRadiotestFirstTrimTime() wrapper for psWriteRadiotestFirstTrimTime in TestEngine DLL.

        Python API:
            psWriteRadiotestFirstTrimTime(handle: int, time: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteRadiotestFirstTrimTime(handle=0, time=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteRadiotestFirstTrimTime(uint32 handle, uint32 time)

            Parameters :    handle -
                                Handle to the device.

                            time -
                                The time from the start of a test till the first IQ trim
                                auto-calibration is done.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write the time to the persistent store. A value
                            of 0 disables the automatic calibration completely during the
                            test. A calibration is still done before the test starts.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteRadiotestFirstTrimTime.restype = ct.c_int32
        self.TestEngineDLL.psWriteRadiotestFirstTrimTime.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.psWriteRadiotestFirstTrimTime(handle, time)
        
        return retval
    # end of psWriteRadiotestFirstTrimTime


    def psReadRadiotestFirstTrimTime(self, handle: int, time: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadRadiotestFirstTrimTime() wrapper for psReadRadiotestFirstTrimTime in TestEngine DLL.

        Python API:
            psReadRadiotestFirstTrimTime(handle: int, time: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, time = myDll.psReadRadiotestFirstTrimTime(handle=0)
            print(retval, time)

        Detail From Wrapped C API:
            Function :      int32 psReadRadiotestFirstTrimTime(uint32 handle, uint32* time)

            Parameters :    handle -
                                Handle to the device.

                            time -
                                The time from the start of a test till the first IQ trim
                                auto-calibration is done.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the trim time from the persistent store.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadRadiotestFirstTrimTime.restype = ct.c_int32
        self.TestEngineDLL.psReadRadiotestFirstTrimTime.argtypes = [ct.c_uint32, ct.c_void_p]
        local_time = ct.c_uint32(time)
        retval = self.TestEngineDLL.psReadRadiotestFirstTrimTime(handle, ct.byref(local_time))
        time = local_time.value
        return retval, time
    # end of psReadRadiotestFirstTrimTime


    def psWriteRadiotestLoLvlTrimEnable(self, handle: int, state: int) -> int:
        r"""Function TestEngine::psWriteRadiotestLoLvlTrimEnable() wrapper for psWriteRadiotestLoLvlTrimEnable in TestEngine DLL.

        Python API:
            psWriteRadiotestLoLvlTrimEnable(handle: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteRadiotestLoLvlTrimEnable(handle=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteRadiotestLoLvlTrimEnable(uint32 handle, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Whether IQ trim is enabled. Basically this is a boolean
                                where 1 = true and 0 = false.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function enables trimming of the value for the register
                            ANA_LO_ENABLE; otherwise, has no effect. This trimming takes place
                            before the start of each test.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteRadiotestLoLvlTrimEnable.restype = ct.c_int32
        self.TestEngineDLL.psWriteRadiotestLoLvlTrimEnable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteRadiotestLoLvlTrimEnable(handle, state)
        
        return retval
    # end of psWriteRadiotestLoLvlTrimEnable


    def psReadRadiotestLoLvlTrimEnable(self, handle: int, state: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadRadiotestLoLvlTrimEnable() wrapper for psReadRadiotestLoLvlTrimEnable in TestEngine DLL.

        Python API:
            psReadRadiotestLoLvlTrimEnable(handle: int, state: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, state = myDll.psReadRadiotestLoLvlTrimEnable(handle=0)
            print(retval, state)

        Detail From Wrapped C API:
            Function :      int32 psReadRadiotestLoLvlTrimEnable(uint32 handle, uint16* state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Whether IQ trim is enabled. Basically this is a boolean
                                where 1 = true and 0 = false.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the value of PSKEY_RADIOTEST_LO_LVL_TRIM_ENABLE.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadRadiotestLoLvlTrimEnable.restype = ct.c_int32
        self.TestEngineDLL.psReadRadiotestLoLvlTrimEnable.argtypes = [ct.c_uint32, ct.c_void_p]
        local_state = ct.c_uint16(state)
        retval = self.TestEngineDLL.psReadRadiotestLoLvlTrimEnable(handle, ct.byref(local_state))
        state = local_state.value
        return retval, state
    # end of psReadRadiotestLoLvlTrimEnable


    def psWriteRadiotestSubsequentTrimTime(self, handle: int, time: int) -> int:
        r"""Function TestEngine::psWriteRadiotestSubsequentTrimTime() wrapper for psWriteRadiotestSubsequentTrimTime in TestEngine DLL.

        Python API:
            psWriteRadiotestSubsequentTrimTime(handle: int, time: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteRadiotestSubsequentTrimTime(handle=0, time=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteRadiotestSubsequentTrimTime(uint32 handle,
                                                                     uint32 time)

            Parameters :    handle -
                                Handle to the device.

                            time -
                                The time between each IQ trim auto-calibration.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Once the first IQ trim auto calibration is done in test mode, then
                            subsequent trims are done at regular intervals with the period
                            being given by this key. If this key is 0 then only the first trim
                            is done. If PSKEY_RADIOTEST_FIRST_TRIM_TIME is 0 then no trims are
                            done during the test regardless of the setting of this key
                            (PSKEY_RADIOTEST_SUBSEQUENT_TRIM_TIME).
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteRadiotestSubsequentTrimTime.restype = ct.c_int32
        self.TestEngineDLL.psWriteRadiotestSubsequentTrimTime.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.psWriteRadiotestSubsequentTrimTime(handle, time)
        
        return retval
    # end of psWriteRadiotestSubsequentTrimTime


    def psReadRadiotestSubsequentTrimTime(self, handle: int, time: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadRadiotestSubsequentTrimTime() wrapper for psReadRadiotestSubsequentTrimTime in TestEngine DLL.

        Python API:
            psReadRadiotestSubsequentTrimTime(handle: int, time: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, time = myDll.psReadRadiotestSubsequentTrimTime(handle=0)
            print(retval, time)

        Detail From Wrapped C API:
            Function :      int32 psReadRadiotestSubsequentTrimTime(uint32 handle,
                                                                    uint32* time)

            Parameters :    handle -
                                Handle to the device.

                            time -
                                The time between each IQ trim auto-calibration.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Read the value of PSKEY_RADIOTEST_SUBSEQUENT_TRIM_TIME.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadRadiotestSubsequentTrimTime.restype = ct.c_int32
        self.TestEngineDLL.psReadRadiotestSubsequentTrimTime.argtypes = [ct.c_uint32, ct.c_void_p]
        local_time = ct.c_uint32(time)
        retval = self.TestEngineDLL.psReadRadiotestSubsequentTrimTime(handle, ct.byref(local_time))
        time = local_time.value
        return retval, time
    # end of psReadRadiotestSubsequentTrimTime


    def psWriteHostInterface(self, handle: int, transport: int) -> int:
        r"""Function TestEngine::psWriteHostInterface() wrapper for psWriteHostInterface in TestEngine DLL.

        Python API:
            psWriteHostInterface(handle: int, transport: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteHostInterface(handle=0, transport=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteHostInterface(uint32 handle, uint16 transport)

            Parameters :    handle -
                                Handle to the device.

                            transport -
                                The choice of physical bus. Valid values are:
                                <table>
                                    <tr><td> 1 : BCSP
                                    <tr><td> 2 : H2 - USB
                                    <tr><td> 3 : H4 - UART
                                    <tr><td> 4 : Raw UART (VM)
                                    <tr><td> 6 : H5
                                    <tr><td> 7 : H4DS
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Select the interface type that is to be used to pass information
                            to and from the host. Only one of these can be used at a time,
                            not least because the USB interface uses some of the same chip
                            pins as the UART. If this key specifies use of USB and the chip
                            has no USB hardware support then it reverts to using BCSP. Much
                            of the chip's support for BCSP/H5 is performed by hardware - this
                            allows interrupt routines to deal with complete BCSP/H5 packets.
                            When the chip uses its UART in a more naive fashion, e.g., for
                            H4, this support must be disabled. The UART's hardware support
                            for BCSP/H5 must be enabled via PSKEY_UART_CONFIG_BCSP/H5. The H4
                            specification requires the use of UART hardware flow control and
                            no use of parity. These must also be set via PSKEY_UART_CONFIG_H4.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteHostInterface.restype = ct.c_int32
        self.TestEngineDLL.psWriteHostInterface.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteHostInterface(handle, transport)
        
        return retval
    # end of psWriteHostInterface


    def psReadHostInterface(self, handle: int, transport: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadHostInterface() wrapper for psReadHostInterface in TestEngine DLL.

        Python API:
            psReadHostInterface(handle: int, transport: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, transport = myDll.psReadHostInterface(handle=0)
            print(retval, transport)

        Detail From Wrapped C API:
            Function :      int32 psReadHostInterface(uint32 handle, uint16* transport)

            Parameters :    handle -
                                Handle to the device.

                            transport -
                                The selected physical bus. Valid values are:
                                <table>
                                    <tr><td> 1 : BCSP
                                    <tr><td> 2 : H2 - USB
                                    <tr><td> 3 : H4 - UART
                                    <tr><td> 4 : Raw UART (VM)
                                    <tr><td> 6 : H5
                                    <tr><td> 7 : H4DS
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the Host interface PS setting.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadHostInterface.restype = ct.c_int32
        self.TestEngineDLL.psReadHostInterface.argtypes = [ct.c_uint32, ct.c_void_p]
        local_transport = ct.c_uint16(transport)
        retval = self.TestEngineDLL.psReadHostInterface(handle, ct.byref(local_transport))
        transport = local_transport.value
        return retval, transport
    # end of psReadHostInterface


    def psWriteUsbAttributes(self, handle: int, bmAttributes: int) -> int:
        r"""Function TestEngine::psWriteUsbAttributes() wrapper for psWriteUsbAttributes in TestEngine DLL.

        Python API:
            psWriteUsbAttributes(handle: int, bmAttributes: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteUsbAttributes(handle=0, bmAttributes=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteUsbAttributes(uint32 handle, uint16 bmAttributes)

            Parameters :    handle -
                                Handle to the device.

                            bmAttributes -
                                The bmAttributes of the Standard Configuration Descriptor,
                                described in Table 9.8 of USB specification, version 1.1.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Configuration characteristics
                            <table>
                                <tr><td> D7: Reserved (set to one)
                                <tr><td> D6: Self-powered
                                <tr><td> D5: Remote Wakeup
                                <tr><td> D4...0: Reserved (reset to zero)
                            </table>
                            D7 is reserved and must be set to one for historical reasons. A
                            device configuration that uses power from the bus and a local
                            source reports a non-zero value in MaxPower to indicate the
                            amount of bus power required and sets D6. The actual power
                            source at runtime may be determined using the GetStatus(DEVICE)
                            request (see Section 9.4.5 of USB specification 1.1). If a device
                            configuration supports remote wakeup, D5 is set to one.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteUsbAttributes.restype = ct.c_int32
        self.TestEngineDLL.psWriteUsbAttributes.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteUsbAttributes(handle, bmAttributes)
        
        return retval
    # end of psWriteUsbAttributes


    def psWriteDPlusPullup(self, handle: int, pioPin: int) -> int:
        r"""Function TestEngine::psWriteDPlusPullup() wrapper for psWriteDPlusPullup in TestEngine DLL.

        Python API:
            psWriteDPlusPullup(handle: int, pioPin: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteDPlusPullup(handle=0, pioPin=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteDPlusPullup(uint32 handle, uint16 pioPin)

            Parameters :    handle -
                                Handle to the device.

                            pioPin -
                                The PIO line used to control the pull-up resistor on the USB
                                D+ line.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   The absence of this key in the PS indicates that this feature is
                            not in use. This value is only used if the chip is presenting its
                            USB interface. See the description of PSKEY_HOST_INTERFACE.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteDPlusPullup.restype = ct.c_int32
        self.TestEngineDLL.psWriteDPlusPullup.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteDPlusPullup(handle, pioPin)
        
        return retval
    # end of psWriteDPlusPullup


    def psWriteUsbMaxPower(self, handle: int, maxPower: int) -> int:
        r"""Function TestEngine::psWriteUsbMaxPower() wrapper for psWriteUsbMaxPower in TestEngine DLL.

        Python API:
            psWriteUsbMaxPower(handle: int, maxPower: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteUsbMaxPower(handle=0, maxPower=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteUsbMaxPower(uint32 handle, uint16 maxPower)

            Parameters :    handle -
                                Handle to the device.

                            maxPower -
                                The MaxPower field of the local USB device, as defined in
                                Table 9.8 of version 1.1 of the USB specification. Bizarrely,
                                this value is given in units of 2mA.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Function to write PSKEY_USB_MAX_POWER to the persistent store.
                            This value is only used if the chip is presenting its USB
                            interface. See the description of PSKEY_HOST_INTERFACE.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteUsbMaxPower.restype = ct.c_int32
        self.TestEngineDLL.psWriteUsbMaxPower.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWriteUsbMaxPower(handle, maxPower)
        
        return retval
    # end of psWriteUsbMaxPower


    def psWritePioProtectMask(self, handle: int, mask: int) -> int:
        r"""Function TestEngine::psWritePioProtectMask() wrapper for psWritePioProtectMask in TestEngine DLL.

        Python API:
            psWritePioProtectMask(handle: int, mask: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWritePioProtectMask(handle=0, mask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWritePioProtectMask(uint32 handle, uint16 mask)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                PIO mask to protect PIO lines from unwanted access. If a bit
                                of the PSKEY's value is set high then application code cannot
                                change the value of the corresponding PIO port pin.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   The chip's PIO port can function as a general purpose input and
                            output port. However, various optional hardware and software
                            configurations require some PIO pins for their own needs, e.g., an
                            optional external PA/LNA block is driven using PIO pins 0 and 1.
                            This PSKEY prevents applications changing PIO pins that are
                            required for lower level functions. This blocking action applies
                            to host-based applications requesting PIO changes via BCCMD and to
                            VM applications running on the chip. Bits 0 to 7 of this uint16
                            PSKEY map to PIO0 to PIO7 respectively. If a bit of the PSKEY's
                            value is set high then application code cannot change the value of
                            the corresponding PIO port pin. The default value, 0x03, suits
                            Casira as this has an external PA/LNA.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWritePioProtectMask.restype = ct.c_int32
        self.TestEngineDLL.psWritePioProtectMask.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.psWritePioProtectMask(handle, mask)
        
        return retval
    # end of psWritePioProtectMask


    def psReadPioProtectMask(self, handle: int, mask: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadPioProtectMask() wrapper for psReadPioProtectMask in TestEngine DLL.

        Python API:
            psReadPioProtectMask(handle: int, mask: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, mask = myDll.psReadPioProtectMask(handle=0)
            print(retval, mask)

        Detail From Wrapped C API:
            Function :      int32 psReadPioProtectMask(uint32 handle, uint16* mask)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                PIO mask to protect PIO lines from unwanted access. If a bit
                                of the PSKEY's value is set high then application code cannot
                                change the value of the corresponding PIO port pin.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the PIO protect mask PS setting.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psReadPioProtectMask.restype = ct.c_int32
        self.TestEngineDLL.psReadPioProtectMask.argtypes = [ct.c_uint32, ct.c_void_p]
        local_mask = ct.c_uint16(mask)
        retval = self.TestEngineDLL.psReadPioProtectMask(handle, ct.byref(local_mask))
        mask = local_mask.value
        return retval, mask
    # end of psReadPioProtectMask


    def psWriteTxOffsetHalfMhz(self, handle: int, offset: int) -> int:
        r"""Function TestEngine::psWriteTxOffsetHalfMhz() wrapper for psWriteTxOffsetHalfMhz in TestEngine DLL.

        Python API:
            psWriteTxOffsetHalfMhz(handle: int, offset: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteTxOffsetHalfMhz(handle=0, offset=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteTxOffsetHalfMhz(uint32 handle, int16 offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                Transmit offset in units of 500kHz. For example -2 == -1MHz.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the transmit offset PS setting.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWriteTxOffsetHalfMhz.restype = ct.c_int32
        self.TestEngineDLL.psWriteTxOffsetHalfMhz.argtypes = [ct.c_uint32, ct.c_int16]
        
        retval = self.TestEngineDLL.psWriteTxOffsetHalfMhz(handle, offset)
        
        return retval
    # end of psWriteTxOffsetHalfMhz


    def psReadTxOffsetHalfMhz(self, handle: int, offset: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadTxOffsetHalfMhz() wrapper for psReadTxOffsetHalfMhz in TestEngine DLL.

        Python API:
            psReadTxOffsetHalfMhz(handle: int, offset: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, offset = myDll.psReadTxOffsetHalfMhz(handle=0)
            print(retval, offset)

        Detail From Wrapped C API:
            Function :      int32 psReadTxOffsetHalfMhz(uint32 handle, int16* offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                Transmit offset in units of 500kHz. For example -2 == -1MHz.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the transmit offset PS setting.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadTxOffsetHalfMhz.restype = ct.c_int32
        self.TestEngineDLL.psReadTxOffsetHalfMhz.argtypes = [ct.c_uint32, ct.c_void_p]
        local_offset = ct.c_int16(offset)
        retval = self.TestEngineDLL.psReadTxOffsetHalfMhz(handle, ct.byref(local_offset))
        offset = local_offset.value
        return retval, offset
    # end of psReadTxOffsetHalfMhz


    def psWriteUsrValue(self, handle: int, userNo: int, length: int, data: list) -> int:
        r"""Function TestEngine::psWriteUsrValue() wrapper for psWriteUsrValue in TestEngine DLL.

        Python API:
            psWriteUsrValue(handle: int, userNo: int, length: int, data: list) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteUsrValue(handle=0, userNo=0, length=0, data=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteUsrValue(uint32 handle, uint16 userNo, uint16 length,
                                                  const uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            userNo -
                                Value between 0 and 49 which refers to 'n' in PSKEY_USRn.

                            length -
                                Length of PS key value in uint16's.

                            data -
                                Pointer to an array containing the data to be written to the
                                PS.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes to PSKEY_USRn.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types tePsWrite should be used.

        """
        self.TestEngineDLL.psWriteUsrValue.restype = ct.c_int32
        self.TestEngineDLL.psWriteUsrValue.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.psWriteUsrValue(handle, userNo, length, local_data)
        
        return retval
    # end of psWriteUsrValue


    def psReadUsrValue(self, handle: int, userNo: int, maxLen: int, length: int=0, data: list=None) -> Tuple[int, int, list]:
        r"""Function TestEngine::psReadUsrValue() wrapper for psReadUsrValue in TestEngine DLL.

        Python API:
            psReadUsrValue(handle: int, userNo: int, maxLen: int, length: int=0, data: list=None) -> Tuple[int, int, list]

        Python Example Call Syntax:
            retval, length, data = myDll.psReadUsrValue(handle=0, userNo=0, maxLen=0, data=[0,1])
            print(retval, length, data)

        Detail From Wrapped C API:
            Function :      int32 psReadUsrValue(uint32 handle, uint16 userNo, uint16 maxLen,
                                                 uint16* length, uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            userNo -
                                Value between 0 and 49 which refers to 'n' in PSKEY_USRn.

                            maxLen -
                                Length of the array to hold the returned value.

                            length -
                                Pointer to the length of the returned PS entry.

                            data -
                                Pointer to an array to hold the returned PS value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the PSKEY_USRn. If the length of PSKEY_USRn is greater than
                            maxLen, Error is returned, with the length parameter set to the
                            length of the key's data.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types tePsRead should be used.

        """
        self.TestEngineDLL.psReadUsrValue.restype = ct.c_int32
        self.TestEngineDLL.psReadUsrValue.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        local_length = ct.c_uint16(length)
        if data == None:
            data = []
        local_data = (ct.c_uint16 * max(maxLen, len(data)))(*data)
        retval = self.TestEngineDLL.psReadUsrValue(handle, userNo, maxLen, ct.byref(local_length), local_data)
        length = local_length.value
        data = local_data[:]
        return retval, length, data
    # end of psReadUsrValue


    def psWritePowerTable(self, handle: int, numEntries: int, intPA: list, extPA: list, power: list) -> int:
        r"""Function TestEngine::psWritePowerTable() wrapper for psWritePowerTable in TestEngine DLL.

        Python API:
            psWritePowerTable(handle: int, numEntries: int, intPA: list, extPA: list, power: list) -> int

        Python Example Call Syntax:
            retval = myDll.psWritePowerTable(handle=0, numEntries=0, intPA=[0,1], extPA=[0,1], power=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWritePowerTable(uint32 handle, uint16 numEntries,
                                                    const uint8* intPA, const uint8* extPA,
                                                    const int32* power)

            Parameters :    handle -
                                Handle to the device.

                            numEntries -
                                Number of entries in the power table.

                            intPA -
                                Pointer to an array of unsigned 8 bit integers of size
                                numEntries containing the intPA entries for the power table.

                            extPA -
                                Pointer to an array of unsigned 8 bit integers of size
                                numEntries containing the extPA entries for the power table.

                            power -
                                Pointer to an array of signed integers of size numEntries
                                containing the Output power entries, in dBm, for the power
                                table.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes to PSKEY_LC_POWER_TABLE.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teConfigCache* functions should be used.

        """
        self.TestEngineDLL.psWritePowerTable.restype = ct.c_int32
        self.TestEngineDLL.psWritePowerTable.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        if intPA == None:
            intPA = []
        local_intPA = (ct.c_uint8 * len(intPA))(*intPA)
        if extPA == None:
            extPA = []
        local_extPA = (ct.c_uint8 * len(extPA))(*extPA)
        if power == None:
            power = []
        local_power = (ct.c_int32 * len(power))(*power)
        retval = self.TestEngineDLL.psWritePowerTable(handle, numEntries, local_intPA, local_extPA, local_power)
        
        return retval
    # end of psWritePowerTable


    def psReadPowerTable(self, handle: int, maxSize: int, numEntries: int=0, intPA: list=None, extPA: list=None, power: list=None) -> Tuple[int, int, list, list, list]:
        r"""Function TestEngine::psReadPowerTable() wrapper for psReadPowerTable in TestEngine DLL.

        Python API:
            psReadPowerTable(handle: int, maxSize: int, numEntries: int=0, intPA: list=None, extPA: list=None, power: list=None) -> Tuple[int, int, list, list, list]

        Python Example Call Syntax:
            retval, numEntries, intPA, extPA, power = myDll.psReadPowerTable(handle=0, maxSize=0, intPA=[0,1], extPA=[0,1], power=[0,1])
            print(retval, numEntries, intPA, extPA, power)

        Detail From Wrapped C API:
            Function :      int32 psReadPowerTable(uint32 handle, int32 maxSize,
                                                   int32* numEntries, uint8* intPA,
                                                   uint8* extPA, int32* power)

            Parameters :    handle -
                                Handle to the device.

                            maxSize -
                                Size of the arrays to hold the intPA, extPA and power.

                            numEntries -
                                Pointer to the number of entries in the power table.

                            intPA -
                                Pointer to an array of unsigned 8 bit integers of size
                                maxSize containing the intPA entries for the power table.

                            extPA -
                                Pointer to an array of unsigned 8 bit integers of size
                                maxSize containing the extPA entries for the power table.

                            power -
                                Pointer to an array of signed integers of size maxSize
                                containing the Output power entries, in dBm, for the power
                                table.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the PSKEY_LC_POWER_TABLE.
                            <p>
                            This function reads using the PS_STORES_IFR store mask, therefore
                            for BlueCore ICs without the IF layers present and for any other
                            IC types, the ROM default will be returned. The psRead function
                            can be used to read any key using a different store mask.
                            <p>
                            For IC types other than BlueCore the teConfigCache* functions
                            should be used.

        """
        self.TestEngineDLL.psReadPowerTable.restype = ct.c_int32
        self.TestEngineDLL.psReadPowerTable.argtypes = [ct.c_uint32, ct.c_int32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_numEntries = ct.c_int32(numEntries)
        if intPA == None:
            intPA = []
        local_intPA = (ct.c_uint8 * max(maxSize, len(intPA)))(*intPA)
        if extPA == None:
            extPA = []
        local_extPA = (ct.c_uint8 * max(maxSize, len(extPA)))(*extPA)
        if power == None:
            power = []
        local_power = (ct.c_int32 * max(maxSize, len(power)))(*power)
        retval = self.TestEngineDLL.psReadPowerTable(handle, maxSize, ct.byref(local_numEntries), local_intPA, local_extPA, local_power)
        numEntries = local_numEntries.value
        intPA = local_intPA[:]
        extPA = local_extPA[:]
        power = local_power[:]
        return retval, numEntries, intPA, extPA, power
    # end of psReadPowerTable


    def psWriteVmDisable(self, handle: int, vmDisable: int) -> int:
        r"""Function TestEngine::psWriteVmDisable() wrapper for psWriteVmDisable in TestEngine DLL.

        Python API:
            psWriteVmDisable(handle: int, vmDisable: int) -> int

        Python Example Call Syntax:
            retval = myDll.psWriteVmDisable(handle=0, vmDisable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psWriteVmDisable(uint32 handle, uint8 vmDisable)

            Parameters :    handle -
                                Handle to the device.

                            vmDisable -
                                Boolean value where non-zero indicates that the VM will be
                                disabled after the next reset.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes to PSKEY_VM_DISABLE.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types see teAppDisable.

        """
        self.TestEngineDLL.psWriteVmDisable.restype = ct.c_int32
        self.TestEngineDLL.psWriteVmDisable.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.psWriteVmDisable(handle, vmDisable)
        
        return retval
    # end of psWriteVmDisable


    def psReadVmDisable(self, handle: int, vmDisable: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::psReadVmDisable() wrapper for psReadVmDisable in TestEngine DLL.

        Python API:
            psReadVmDisable(handle: int, vmDisable: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, vmDisable = myDll.psReadVmDisable(handle=0)
            print(retval, vmDisable)

        Detail From Wrapped C API:
            Function :      int32 psReadVmDisable(uint32 handle, uint8* vmDisable)

            Parameters :    handle -
                                Handle to the device.

                            vmDisable -
                                Boolean value where non-zero indicates that the VM is
                                disabled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads PSKEY_VM_DISABLE.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psReadVmDisable.restype = ct.c_int32
        self.TestEngineDLL.psReadVmDisable.argtypes = [ct.c_uint32, ct.c_void_p]
        local_vmDisable = ct.c_uint8(vmDisable)
        retval = self.TestEngineDLL.psReadVmDisable(handle, ct.byref(local_vmDisable))
        vmDisable = local_vmDisable.value
        return retval, vmDisable
    # end of psReadVmDisable


    def psMergeFromFile(self, handle: int, filePath: str) -> int:
        r"""Function TestEngine::psMergeFromFile() wrapper for psMergeFromFile in TestEngine DLL.

        Python API:
            psMergeFromFile(handle: int, filePath: str) -> int

        Python Example Call Syntax:
            retval = myDll.psMergeFromFile(handle=0, filePath='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 psMergeFromFile(uint32 handle, const char* filePath)

            Parameters :    handle -
                                Handle to the device.

                            filePath -
                                Full path of the persistent store file (*.psr) to merge.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to merge a Qualcomm *.psr format
                            persistent store file into the persistent store of a BlueCore
                            chip. Patch files for ROM chips in *.psr format can be loaded
                            using this function.
                            <p>
                            If there are any format errors in the file, psMergeFromFile
                            fails. The PSTool or PSCli applications can be used to find the
                            cause of the failure by attempting to merge the file using one of
                            the tools (errors are reported to the user).
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.psMergeFromFile.restype = ct.c_int32
        self.TestEngineDLL.psMergeFromFile.argtypes = [ct.c_uint32, ct.c_char_p]
        local_filePath = None if filePath is None else ct.create_string_buffer(bytes(filePath, encoding="UTF-8"))
        retval = self.TestEngineDLL.psMergeFromFile(handle, local_filePath)
        
        return retval
    # end of psMergeFromFile


    def hciSlave(self, handle: int) -> int:
        r"""Function TestEngine::hciSlave() wrapper for hciSlave in TestEngine DLL.

        Python API:
            hciSlave(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciSlave(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSlave(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Performs four steps:
                            1. Sets the event filter to auto accept a connection request.
                            Implements the command HCI_Set_Event_Filter with the following
                            parameters:
                            <table>
                                <tr><td> 0x02 - Connection  setup filter type
                                <tr><td> 0x00 - Allow connections from all devices
                                <tr><td> 0x02 - Auto accept the connection
                            </table>

                            2. Implements the command HCI_WriteScan_Enable with the following
                            parameter:
                                0x03 - Inquiry scan enabled, Page scan enabled.

            Example :       See example for bccmdSetColdReset.

        """
        self.TestEngineDLL.hciSlave.restype = ct.c_int32
        self.TestEngineDLL.hciSlave.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciSlave(handle)
        
        return retval
    # end of hciSlave


    def hciSetAfhHostChannelClass(self, handle: int, cClass: list) -> int:
        r"""Function TestEngine::hciSetAfhHostChannelClass() wrapper for hciSetAfhHostChannelClass in TestEngine DLL.

        Python API:
            hciSetAfhHostChannelClass(handle: int, cClass: list) -> int

        Python Example Call Syntax:
            retval = myDll.hciSetAfhHostChannelClass(handle=0, cClass=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSetAfhHostChannelClass(uint32 handle,
                                                            const uint8* cClass)

            Parameters :    handle -
                                Handle to the device.

                            cClass -
                                Pointer to a 10 byte array containing channel classification
                                information. The most significant bit must be 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function allow the Bluetooth host to specify a channel
                            classification based on its local information.
                            <p>
                            When called this function will block until it receives a
                            command complete event or until a preset time has elapsed
                            (~ 3 secs).

        """
        self.TestEngineDLL.hciSetAfhHostChannelClass.restype = ct.c_int32
        self.TestEngineDLL.hciSetAfhHostChannelClass.argtypes = [ct.c_uint32, ct.c_void_p]
        if cClass == None:
            cClass = []
        local_cClass = (ct.c_uint8 * len(cClass))(*cClass)
        retval = self.TestEngineDLL.hciSetAfhHostChannelClass(handle, local_cClass)
        
        return retval
    # end of hciSetAfhHostChannelClass


    def hciReadAfhChannelMap(self, handle: int, aclHandle: int, mode: int=0, cMap: list=None) -> Tuple[int, int, list]:
        r"""Function TestEngine::hciReadAfhChannelMap() wrapper for hciReadAfhChannelMap in TestEngine DLL.

        Python API:
            hciReadAfhChannelMap(handle: int, aclHandle: int, mode: int=0, cMap: list=None) -> Tuple[int, int, list]

        Python Example Call Syntax:
            retval, mode, cMap = myDll.hciReadAfhChannelMap(handle=0, aclHandle=0, cMap=[0,1])
            print(retval, mode, cMap)

        Detail From Wrapped C API:
            Function :      int32 hciReadAfhChannelMap(uint32 handle, uint16 aclHandle,
                                                       uint8* mode, uint8* cMap)

            Parameters :    handle -
                                Handle to the device.

                            aclHandle -
                                Valid ACL connection handle.

                            mode -
                                Pointer to a single byte which the function will set to
                                define whether AFH is enabled or disabled for the given
                                connection.

                            cMap -
                                Pointer to a 10 byte array that will contain channel map
                                information for the given connection.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to indicate the state of the hop
                            sequence specified by the most recent LMP_Set_AFH message for a
                            given connection handle.
                            <p>
                            When called this function will block until it receives a
                            command complete event or until a preset time has elapsed
                            (~ 3 secs).

        """
        self.TestEngineDLL.hciReadAfhChannelMap.restype = ct.c_int32
        self.TestEngineDLL.hciReadAfhChannelMap.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        local_mode = ct.c_uint8(mode)
        if cMap == None:
            cMap = []
        local_cMap = (ct.c_uint8 * len(cMap))(*cMap)
        retval = self.TestEngineDLL.hciReadAfhChannelMap(handle, aclHandle, ct.byref(local_mode), local_cMap)
        mode = local_mode.value
        cMap = local_cMap[:]
        return retval, mode, cMap
    # end of hciReadAfhChannelMap


    def hciSetEventFilterAutoacceptConnection(self, handle: int) -> int:
        r"""Function TestEngine::hciSetEventFilterAutoacceptConnection() wrapper for hciSetEventFilterAutoacceptConnection in TestEngine DLL.

        Python API:
            hciSetEventFilterAutoacceptConnection(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciSetEventFilterAutoacceptConnection(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSetEventFilterAutoacceptConnection(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the event filter to auto accept a connection request.
                            Implements the command HCI_Set_Event_Filter with the following
                            parameters:
                            <table>
                                <tr><td> 0x02 - Connection  setup filter type
                                <tr><td> 0x00 - Allow connections from all devices
                                <tr><td> 0x02 - Auto accept the connection
                            </table>

        """
        self.TestEngineDLL.hciSetEventFilterAutoacceptConnection.restype = ct.c_int32
        self.TestEngineDLL.hciSetEventFilterAutoacceptConnection.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciSetEventFilterAutoacceptConnection(handle)
        
        return retval
    # end of hciSetEventFilterAutoacceptConnection


    def hciWriteInquiryScanActivity(self, handle: int, interval: int, window: int) -> int:
        r"""Function TestEngine::hciWriteInquiryScanActivity() wrapper for hciWriteInquiryScanActivity in TestEngine DLL.

        Python API:
            hciWriteInquiryScanActivity(handle: int, interval: int, window: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWriteInquiryScanActivity(handle=0, interval=0, window=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWriteInquiryScanActivity(uint32 handle, uint16 interval,
                                                              uint16 window)

            Parameters :    handle -
                                Handle to the device.

                            interval -
                                Defines the amount of time between consecutive inquiry scans.

                            window -
                                Defines the amount of time for the duration of the inquiry
                                scan.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command HCI_Write_Inquiryscan_activity.

        """
        self.TestEngineDLL.hciWriteInquiryScanActivity.restype = ct.c_int32
        self.TestEngineDLL.hciWriteInquiryScanActivity.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciWriteInquiryScanActivity(handle, interval, window)
        
        return retval
    # end of hciWriteInquiryScanActivity


    def hciWritePageScanActivity(self, handle: int, interval: int, window: int) -> int:
        r"""Function TestEngine::hciWritePageScanActivity() wrapper for hciWritePageScanActivity in TestEngine DLL.

        Python API:
            hciWritePageScanActivity(handle: int, interval: int, window: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWritePageScanActivity(handle=0, interval=0, window=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWritePageScanActivity(uint32 handle, uint16 interval,
                                                           uint16 window)

            Parameters :    handle -
                                Handle to the device.

                            interval -
                                Defines the amount of time between consecutive page scans.

                            window -
                                Defines the amount of time for the duration of the page scan.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command HCI_Write_Pagescan_activity.

        """
        self.TestEngineDLL.hciWritePageScanActivity.restype = ct.c_int32
        self.TestEngineDLL.hciWritePageScanActivity.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciWritePageScanActivity(handle, interval, window)
        
        return retval
    # end of hciWritePageScanActivity


    def hciWriteScanEnable(self, handle: int, scanEnable: int) -> int:
        r"""Function TestEngine::hciWriteScanEnable() wrapper for hciWriteScanEnable in TestEngine DLL.

        Python API:
            hciWriteScanEnable(handle: int, scanEnable: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWriteScanEnable(handle=0, scanEnable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWriteScanEnable(uint32 handle, uint8 scanEnable)

            Parameters :    handle -
                                Handle to the device.

                            scanEnable -
                                Controls whether or not the Bluetooth device will periodically
                                scan for page attempts and/or inquiry requests from other
                                Bluetooth devices.
                                <table>
                                    <tr><td> 0x00 = No Scans enabled.
                                    <tr><td> 0x01 = Inquiry Scan enabled. Page Scan disabled.
                                    <tr><td> 0x02 = Inquiry Scan disabled. Page Scan enabled.
                                    <tr><td> 0x03 = Inquiry Scan enabled. Page Scan enabled.
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command HCI_WriteScan_Enable.

        """
        self.TestEngineDLL.hciWriteScanEnable.restype = ct.c_int32
        self.TestEngineDLL.hciWriteScanEnable.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciWriteScanEnable(handle, scanEnable)
        
        return retval
    # end of hciWriteScanEnable


    def hciInquiry(self, handle: int, inquiryLength: int, numResponses: int, lap: int) -> int:
        r"""Function TestEngine::hciInquiry() wrapper for hciInquiry in TestEngine DLL.

        Python API:
            hciInquiry(handle: int, inquiryLength: int, numResponses: int, lap: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciInquiry(handle=0, inquiryLength=0, numResponses=0, lap=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciInquiry(uint32 handle, uint8 inquiryLength,
                                             uint8 numResponses, uint32 lap)

            Parameters :    handle -
                                Handle to the device.

                            inquiryLength -
                                Maximum amount of time before the inquiry is halted, as
                                defined by the BT spec.

                            numResponses -
                                Maximum number of responses before inquiry is halted, as
                                defined in the BT spec. 0x00 is unlimited.

                            lap -
                                The LAP from which the inquiry access code is derived, as
                                defined in the BT spec.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to enter inquiry mode.
                            This function will NOT wait for any inquiry results.

        """
        self.TestEngineDLL.hciInquiry.restype = ct.c_int32
        self.TestEngineDLL.hciInquiry.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint32]
        
        retval = self.TestEngineDLL.hciInquiry(handle, inquiryLength, numResponses, lap)
        
        return retval
    # end of hciInquiry


    def hciGetInquiryResults(self, handle: int, lap: list, uap: list, nap: list, clockOffset: list, maxLen: int, dataLen: int=0) -> Tuple[int, list, list, list, list, int]:
        r"""Function TestEngine::hciGetInquiryResults() wrapper for hciGetInquiryResults in TestEngine DLL.

        Python API:
            hciGetInquiryResults(handle: int, lap: list, uap: list, nap: list, clockOffset: list, maxLen: int, dataLen: int=0) -> Tuple[int, list, list, list, list, int]

        Python Example Call Syntax:
            retval, lap, uap, nap, clockOffset, dataLen = myDll.hciGetInquiryResults(handle=0, lap=[0,1], uap=[0,1], nap=[0,1], clockOffset=[0,1], maxLen=0)
            print(retval, lap, uap, nap, clockOffset, dataLen)

        Detail From Wrapped C API:
            Function :      int32 hciGetInquiryResults(uint32 handle, uint32* lap, uint8* uap,
                                                       uint16* nap, uint16* clockOffset,
                                                       uint32 maxLen, uint32* dataLen)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                Pointer to the array of LAP's as defined by the returned
                                value.

                            uap -
                                Pointer to the array of UAP's as defined by the returned
                                value.

                            nap -
                                Pointer to the array of NAP's as defined by the returned
                                value.

                            clockOffset -
                                Pointer to the array of clock offsets as defined by the
                                returned value.

                            maxLen -
                                Size of the arrays allocated for the LAP, UAP and NAP.

                            dataLen -
                                Pointer to a variable to hold the actual count of data
                                items that was returned in the LAP, UAP and NAP.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Retrieves the bd_addrs and clock offsets of the devices found
                            during the last completed inquiry. If an inquiry is in progress
                            then this function will wait for a time based on the
                            inquiryLength parameter passed to hciInquiry.

        """
        self.TestEngineDLL.hciGetInquiryResults.restype = ct.c_int32
        self.TestEngineDLL.hciGetInquiryResults.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_uint32, ct.c_void_p]
        if lap == None:
            lap = []
        local_lap = (ct.c_uint32 * max(maxLen, len(lap)))(*lap)
        if uap == None:
            uap = []
        local_uap = (ct.c_uint8 * max(maxLen, len(uap)))(*uap)
        if nap == None:
            nap = []
        local_nap = (ct.c_uint16 * max(maxLen, len(nap)))(*nap)
        if clockOffset == None:
            clockOffset = []
        local_clockOffset = (ct.c_uint16 * max(maxLen, len(clockOffset)))(*clockOffset)
        local_dataLen = ct.c_uint32(dataLen)
        retval = self.TestEngineDLL.hciGetInquiryResults(handle, local_lap, local_uap, local_nap, local_clockOffset, maxLen, ct.byref(local_dataLen))
        lap = local_lap[:]
        uap = local_uap[:]
        nap = local_nap[:]
        clockOffset = local_clockOffset[:]
        dataLen = local_dataLen.value
        return retval, lap, uap, nap, clockOffset, dataLen
    # end of hciGetInquiryResults


    def hciInquiryCancel(self, handle: int) -> int:
        r"""Function TestEngine::hciInquiryCancel() wrapper for hciInquiryCancel in TestEngine DLL.

        Python API:
            hciInquiryCancel(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciInquiryCancel(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciInquiryCancel(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to exit inquiry mode. The DLL will check if the
                            device is currently in inquiry before issuing this. Failure on
                            invalid handle or DM commands enabled.

        """
        self.TestEngineDLL.hciInquiryCancel.restype = ct.c_int32
        self.TestEngineDLL.hciInquiryCancel.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciInquiryCancel(handle)
        
        return retval
    # end of hciInquiryCancel


    def hciCreateConnection(self, handle: int, lap: int, uap: int, nap: int, pktType: int, connectionHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciCreateConnection() wrapper for hciCreateConnection in TestEngine DLL.

        Python API:
            hciCreateConnection(handle: int, lap: int, uap: int, nap: int, pktType: int, connectionHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, connectionHandle = myDll.hciCreateConnection(handle=0, lap=0, uap=0, nap=0, pktType=0)
            print(retval, connectionHandle)

        Detail From Wrapped C API:
            Function :      int32 hciCreateConnection(uint32 handle, uint32 lap, uint8 uap,
                                                      uint16 nap, uint16 pktType,
                                                      uint16* connectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                LAP of BD_ADDR. Must be one of the BD_ADDR's returned by
                                get_inquiry_results.

                            uap -
                                UAP of BD_ADDR. Must be one of the BD_ADDR's returned by
                                get_inquiry_results.

                            nap -
                                NAP of BD_ADDR. Must be one of the BD_ADDR's returned by
                                get_inquiry_results.

                            pktType -
                                Or-ed combination of packet types as defined in the Bluetooth
                                specification. A bit being set may indicate that a packet type
                                is allowed or disallowed, as indicated in the following table:
                                <table>
                                    <tr><td>0x0002 = 2-DH1 may not be used
                                    <tr><td>0x0004 = 3-DH1 may not be used
                                    <tr><td>0x0008 = DM1 may be used
                                    <tr><td>0x0010 = DH1 may be used
                                    <tr><td>0x0100 = 2-DH3 may not be used
                                    <tr><td>0x0200 = 3-DH3 may not be used
                                    <tr><td>0x0400 = DM3 may be used
                                    <tr><td>0x0800 = DH3 may be used
                                    <tr><td>0x1000 = 2-DH5 may not be used
                                    <tr><td>0x2000 = 3-DH5 may not be used
                                    <tr><td>0x4000 = DM5 may be used
                                    <tr><td>0x8000 = DH5 may be used
                                </table>
                                <p>
                                Normally this value is set to allow all packet types, which
                                allows the device to use its own algorithm to select the best
                                rate depending on the link quality.
                                The value which would allow all of the above packets to be
                                used is: 0xCC18 = (DM1 | DH1 | DM3 | DH3 | DM5 | DH5).

                            connectionHandle -
                                Connection handle to a Bluetooth connection.
                                NOTE: The connection handle is local to a device and not a
                                link. Therefore when you create a connection each member could
                                have a different connection handle for that link so the value
                                returned by this function should only be used for this device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to attempt to create a connection with a device
                            discovered during the inquiry phase. This function will wait for a
                            connection complete event with a 3 second time out. Success is
                            determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful connection complete event
                                <li> Invalid BD_ADDR (not part of the inquiry results list)
                            </ol>

        """
        self.TestEngineDLL.hciCreateConnection.restype = ct.c_int32
        self.TestEngineDLL.hciCreateConnection.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_connectionHandle = ct.c_uint16(connectionHandle)
        retval = self.TestEngineDLL.hciCreateConnection(handle, lap, uap, nap, pktType, ct.byref(local_connectionHandle))
        connectionHandle = local_connectionHandle.value
        return retval, connectionHandle
    # end of hciCreateConnection


    def hciCreateConnectionNoInquiry(self, handle: int, lap: int, uap: int, nap: int, pktType: int, pageScanRepMode: int, pageScanMode: int, clockOffset: int, allowRoleSwitch: int, connectionHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciCreateConnectionNoInquiry() wrapper for hciCreateConnectionNoInquiry in TestEngine DLL.

        Python API:
            hciCreateConnectionNoInquiry(handle: int, lap: int, uap: int, nap: int, pktType: int, pageScanRepMode: int, pageScanMode: int, clockOffset: int, allowRoleSwitch: int, connectionHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, connectionHandle = myDll.hciCreateConnectionNoInquiry(handle=0, lap=0, uap=0, nap=0, pktType=0, pageScanRepMode=0, pageScanMode=0, clockOffset=0, allowRoleSwitch=0)
            print(retval, connectionHandle)

        Detail From Wrapped C API:
            Function :      int32 hciCreateConnectionNoInquiry(uint32 handle, uint32 lap,
                                                               uint8 uap, uint16 nap,
                                                               uint16 pktType,
                                                               uint8 pageScanRepMode,
                                                               uint8 pageScanMode,
                                                               uint16 clockOffset,
                                                               uint8 allowRoleSwitch,
                                                               uint16* connectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                LAP of BD_ADDR.

                            uap -
                                UAP of BD_ADDR.

                            nap -
                                NAP of BD_ADDR.

                            pktType -
                                As for hciCreateConnection.

                            pageScanRepMode -
                                Page scan repetition mode supported by the slave device
                                (0 = R0, 1 = R1, 2 = R2).

                            pageScanMode -
                                BT Spec. requires this to be set to 0.

                            clockOffset -
                                The clock offset between the devices.

                            allowRoleSwitch -
                                Specifies if the local device accepts the request of a
                                master/slave role switch. 0 to not allow, 1 to allow.

                            connectionHandle -
                                Connection handle to a Bluetooth connection.
                                NOTE: The connection handle is local to a device and not a
                                link. Therefore when you create a connection each member could
                                have a different connection handle for that link so the value
                                returned by this function should only be used for this device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to attempt to create a connection with a remote
                            device. This function will wait for a connection complete event
                            with a 5 second time out. Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful connection complete event
                                <li> Invalid BD_ADDR (not part of the inquiry results list)
                            </ol>

        """
        self.TestEngineDLL.hciCreateConnectionNoInquiry.restype = ct.c_int32
        self.TestEngineDLL.hciCreateConnectionNoInquiry.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_void_p]
        local_connectionHandle = ct.c_uint16(connectionHandle)
        retval = self.TestEngineDLL.hciCreateConnectionNoInquiry(handle, lap, uap, nap, pktType, pageScanRepMode, pageScanMode, clockOffset, allowRoleSwitch, ct.byref(local_connectionHandle))
        connectionHandle = local_connectionHandle.value
        return retval, connectionHandle
    # end of hciCreateConnectionNoInquiry


    def hciCreateScoConnection(self, handle: int, aclConnectionHandle: int, pktType: int, scoConnectionHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciCreateScoConnection() wrapper for hciCreateScoConnection in TestEngine DLL.

        Python API:
            hciCreateScoConnection(handle: int, aclConnectionHandle: int, pktType: int, scoConnectionHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, scoConnectionHandle = myDll.hciCreateScoConnection(handle=0, aclConnectionHandle=0, pktType=0)
            print(retval, scoConnectionHandle)

        Detail From Wrapped C API:
            Function :      int32 hciCreateScoConnection(uint32 handle,
                                                         uint16 aclConnectionHandle,
                                                         uint16 pktType,
                                                         uint16* scoConnectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            aclConnectionHandle -
                                ACL connection handle.

                            pktType -
                                Or-ed combination of packet types as defined in the Bluetooth
                                specification for the "Add_Sco_Connection" HCI command. A bit
                                being set indicates that a packet type is allowed. The
                                following table lists the packet types which can be specified:
                                <table>
                                    <tr><td>0x0020 = HV1 may be used
                                    <tr><td>0x0040 = HV2 may be used
                                    <tr><td>0x0080 = HV3 may be used
                                </table>
                                <p>
                                Normally this value is set to allow all packet types, which
                                allows the device to use its own algorithm to select the best
                                rate depending on the link quality.
                                The value which would allow all of the above packets to be
                                used is: 0x00E0 = (HV1 | HV2 | HV3).

                            scoConnectionHandle -
                                Pointer to a variable to hold the returned SCO connection
                                handle.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command will cause the link manager to create a SCO
                            connection using the ACL connection specified by the
                            aclConnectionHandle command parameter. Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful connection complete event
                            </ol>
                            <p>
                            This function is deprecated due to the HCI_Add_Sco_Connection
                            command being deprecated in the BT spec from v1.2. Use
                            hciSetupScoConnection instead for v1.2 onwards.

            Deprecated :

        """
        self.TestEngineDLL.hciCreateScoConnection.restype = ct.c_int32
        self.TestEngineDLL.hciCreateScoConnection.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_scoConnectionHandle = ct.c_uint16(scoConnectionHandle)
        retval = self.TestEngineDLL.hciCreateScoConnection(handle, aclConnectionHandle, pktType, ct.byref(local_scoConnectionHandle))
        scoConnectionHandle = local_scoConnectionHandle.value
        return retval, scoConnectionHandle
    # end of hciCreateScoConnection


    def hciSetupScoConnection(self, handle: int, aclConnectionHandle: int, txBandwidth: int, rxBandwidth: int, maxLatency: int, voiceSetting: int, retransEffort: int, pktType: int, scoConnectionHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciSetupScoConnection() wrapper for hciSetupScoConnection in TestEngine DLL.

        Python API:
            hciSetupScoConnection(handle: int, aclConnectionHandle: int, txBandwidth: int, rxBandwidth: int, maxLatency: int, voiceSetting: int, retransEffort: int, pktType: int, scoConnectionHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, scoConnectionHandle = myDll.hciSetupScoConnection(handle=0, aclConnectionHandle=0, txBandwidth=0, rxBandwidth=0, maxLatency=0, voiceSetting=0, retransEffort=0, pktType=0)
            print(retval, scoConnectionHandle)

        Detail From Wrapped C API:
            Function :      int32 hciSetupScoConnection(uint32 handle,
                                                        uint16 aclConnectionHandle,
                                                        uint32 txBandwidth,
                                                        uint32 rxBandwidth,
                                                        uint16 maxLatency,
                                                        uint16 voiceSetting,
                                                        uint8 retransEffort,
                                                        uint16 pktType,
                                                        uint16* scoConnectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            aclConnectionHandle -
                                ACL connection handle.

                            txBandwidth -
                                The transmit bandwidth requirement in octets per second.

                            rxBandwidth -
                                The receive bandwidth requirement in octets per second.

                            maxLatency -
                                A value, in milliseconds, representing the upper limit of the
                                sum of the synchronous interval and the size of the eSCO
                                window.

                            voiceSetting -
                                Also referred to as the content format. Specifies settings for
                                voice connections. Setting this parameter to anything other than
                                the current device(s) voice setting will result in failure. Use
                                hciReadVoiceSetting to get the setting, and hciWriteVoiceSetting
                                to alter it, if required, before calling this function.

                            retransEffort -
                                Specifies the retransmission behaviour as follows:
                                <table>
                                    <tr><td>0x00 = No retransmissions
                                    <tr><td>0x01 = At least 1 retransmission, optimise for
                                                   power consumption
                                    <tr><td>0x02 = At least 1 retransmission, optimise for
                                                   link quality
                                    <tr><td>0xFF = Don't care
                                    <tr><td>0x03 -> 0xFE = Reserved
                                </table>

                            pktType -
                                Or-ed combination of packet types. A bit being set may
                                indicate that a packet type is allowed or disallowed, as
                                indicated in the following table:
                                <table>
                                    <tr><td>0x0001 = HV1 may be used
                                    <tr><td>0x0002 = HV2 may be used
                                    <tr><td>0x0004 = HV3 may be used
                                    <tr><td>0x0008 = EV3 may be used
                                    <tr><td>0x0010 = EV4 may be used
                                    <tr><td>0x0020 = EV5 may be used
                                    <tr><td>0x0040 = 2-EV3 may not be used
                                    <tr><td>0x0080 = 3-EV3 may not be used
                                    <tr><td>0x0100 = 2-EV5 may not be used
                                    <tr><td>0x0200 = 3-EV5 may not be used
                                </table>
                                <p>
                                Normally this value is set to allow all packet types, which
                                allows the device to use its own algorithm to select the best
                                rate depending on the link quality.
                                The value which would allow all of the above packets to be
                                used is: 0x003F = (HV1 | HV2 | HV3 | EV3 | EV4 | EV5).

                            scoConnectionHandle -
                                Pointer to a variable to hold the returned SCO connection
                                handle.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command will cause the link manager to setup a SCO/eSCO
                            connection using the ACL connection specified by the
                            aclConnectionHandle command parameter. Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful connection complete event
                            </ol>
                            <p>
                            For more information about the parameters and their ranges, see
                            the BlueTooth specification for the
                            "Setup_Synchronous_Connection" HCI command.
                            <p>
                            Note that this function does not support the modification of an
                            existing SCO/eSCO connection.

            Example :

                static const uint16 SETUP_SCO_ALL_PKTS = 0x003F;
                static const uint32 MAX_TIMEOUT_MS = 5000;

                uint32 masterHandle = TE_INVALID_HANDLE_VALUE;
                uint32 slaveHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect to master..." << endl;
                    masterHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (masterHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                timeoutMs = 0;

                do
                {
                    cout << "Trying to connect to slave..." << endl;
                    slaveHandle = openTestEngine(USB, "\\\\.\\csr0", 0, 1000, 500);
                    timeoutMs += 1000;
                } while (slaveHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (masterHandle != TE_INVALID_HANDLE_VALUE && slaveHandle != TE_INVALID_HANDLE_VALUE)
                {
                    // Enable the slave device to auto accept incoming connections
                    // Implement the command HCI_WriteScan_Enable with the parameter 0x03,
                    // Inquiry scan enabled, Page scan enabled.
                    hciSlave(slaveHandle);

                    // Create an ACL connection to the Slave device from the master
                    uint16 aclHandle;
                    if (hciCreateConnectionNoInquiry(masterHandle, 0xf502, 0x5b, 0x2, 0xcc18,
                                                     0, 0, 0, 1, &aclHandle) != TE_OK)
                    {
                        cout << "Failed to connect to device" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;
                    }
                    cout << "ACL Handle = " << aclHandle << endl;

                    // Check connection status
                    if (hciConnectionStatus(masterHandle, aclHandle) != TE_OK)
                    {
                        cout << "Failed connection status" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;
                    }

                    // Check link quality
                    uint8 linkQuality;
                    if (hciGetLinkQuality(masterHandle, aclHandle, &linkQuality) != TE_OK)
                    {
                        cout << "Failed link quality" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;

                    }
                    cout << "link quality = " << (uint16)linkQuality << endl;

                    // Map SCO over PCM for audio test
                    if (bccmdSetMapScoPcm(masterHandle, 1) != TE_OK ||
                        bccmdSetMapScoPcm(slaveHandle, 1) != TE_OK)
                    {
                        cout << "Failed to map SCO over PCM" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;
                    }

                    // Set the voice setting if required
                    const uint16 VOICE_SETTING = 0x0060;
                    if (hciWriteVoiceSetting(masterHandle, VOICE_SETTING) != TE_OK ||
                        hciWriteVoiceSetting(slaveHandle, VOICE_SETTING) != TE_OK)
                    {
                        cout << "Failed to set voice settings" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;
                    }

                    // Setup SCO connection
                    uint16 scoConnectionHandle;
                    if (hciSetupScoConnection(masterHandle, aclHandle, 8000, 8000, 32, VOICE_SETTING,
                                              0, SETUP_SCO_ALL_PKTS, &scoConnectionHandle) != TE_OK)
                    {
                        cout << "Failed to establish SCO link" << endl;
                        closeTestEngine(masterHandle);
                        closeTestEngine(slaveHandle);
                        return;
                    }
                    else
                    {
                        // Created SCO connection successfully

                        //...
                        // Do SCO testing here
                        //...

                        hciDisconnect(masterHandle, scoConnectionHandle);
                    }

                    // Disconnect ACL link
                    hciDisconnect(masterHandle, aclHandle);

                    // Close handles to master and slave devices
                    closeTestEngine(masterHandle);
                    closeTestEngine(slaveHandle);
                }
                else
                {
                    cout << "Failed to get handles to one or both devices" << endl;
                }

        """
        self.TestEngineDLL.hciSetupScoConnection.restype = ct.c_int32
        self.TestEngineDLL.hciSetupScoConnection.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint32, ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint8, ct.c_uint16, ct.c_void_p]
        local_scoConnectionHandle = ct.c_uint16(scoConnectionHandle)
        retval = self.TestEngineDLL.hciSetupScoConnection(handle, aclConnectionHandle, txBandwidth, rxBandwidth, maxLatency, voiceSetting, retransEffort, pktType, ct.byref(local_scoConnectionHandle))
        scoConnectionHandle = local_scoConnectionHandle.value
        return retval, scoConnectionHandle
    # end of hciSetupScoConnection


    def hciReadVoiceSetting(self, handle: int, voiceSetting: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciReadVoiceSetting() wrapper for hciReadVoiceSetting in TestEngine DLL.

        Python API:
            hciReadVoiceSetting(handle: int, voiceSetting: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, voiceSetting = myDll.hciReadVoiceSetting(handle=0)
            print(retval, voiceSetting)

        Detail From Wrapped C API:
            Function :      int32 hciReadVoiceSetting(uint32 handle, uint16* voiceSetting)

            Parameters :    handle -
                                Handle to the device.

                            voiceSetting -
                                The location where the value specifying the settings for voice
                                connections will be stored. Also referred to as the content
                                format.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command will read the Voice_Setting configuration parameter.
                            Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful command complete event
                            </ol>
                            <p>
                            For more information about the parameter, see the BlueTooth
                            specification for the "HCI_Read_Voice_Setting" HCI command.
                            <p>
                            This function can be used to get the default or current voice
                            setting to be passed as a parameter in the hciSetupScoConnection
                            function.

        """
        self.TestEngineDLL.hciReadVoiceSetting.restype = ct.c_int32
        self.TestEngineDLL.hciReadVoiceSetting.argtypes = [ct.c_uint32, ct.c_void_p]
        local_voiceSetting = ct.c_uint16(voiceSetting)
        retval = self.TestEngineDLL.hciReadVoiceSetting(handle, ct.byref(local_voiceSetting))
        voiceSetting = local_voiceSetting.value
        return retval, voiceSetting
    # end of hciReadVoiceSetting


    def hciWriteVoiceSetting(self, handle: int, voiceSetting: int) -> int:
        r"""Function TestEngine::hciWriteVoiceSetting() wrapper for hciWriteVoiceSetting in TestEngine DLL.

        Python API:
            hciWriteVoiceSetting(handle: int, voiceSetting: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWriteVoiceSetting(handle=0, voiceSetting=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWriteVoiceSetting(uint32 handle, uint16 voiceSetting)

            Parameters :    handle -
                                Handle to the device.

                            voiceSetting -
                                Also referred to as the content format. Specifies settings for
                                voice connections.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command will write the Voice_Setting configuration parameter.
                            Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Successful command complete event
                            </ol>
                            <p>
                            For more information about the parameter, see the BlueTooth
                            specification for the "HCI_Write_Voice_Setting" HCI command.
                            <p>
                            Note that hciSetupScoConnection will fail if the voice setting
                            parameter is different to that set on the devices to be connected.
                            Therefore, if a voice setting other than the default is required,
                            this function must be called to write the voice setting to the
                            devices before hciSetupScoConnection is called.

        """
        self.TestEngineDLL.hciWriteVoiceSetting.restype = ct.c_int32
        self.TestEngineDLL.hciWriteVoiceSetting.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciWriteVoiceSetting(handle, voiceSetting)
        
        return retval
    # end of hciWriteVoiceSetting


    def hciWriteLinkPolicySettings(self, handle: int, connectionHandle: int, linkPolicySettings: int) -> int:
        r"""Function TestEngine::hciWriteLinkPolicySettings() wrapper for hciWriteLinkPolicySettings in TestEngine DLL.

        Python API:
            hciWriteLinkPolicySettings(handle: int, connectionHandle: int, linkPolicySettings: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWriteLinkPolicySettings(handle=0, connectionHandle=0, linkPolicySettings=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWriteLinkPolicySettings(uint32 handle,
                                                             uint16 connectionHandle,
                                                             uint16 linkPolicySettings)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

                            linkPolicySettings -
                                Determines the behaviour of the local Link Manager when it
                                receives a request from a remote device or it determines
                                itself to change the master-slave role or to enter the hold,
                                sniff, or park mode.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to attempt to write the link policy settings.
                            Success determined by:
                            <ol>
                                <li> Valid handle
                                <li> Valid connection handle
                            </ol>

        """
        self.TestEngineDLL.hciWriteLinkPolicySettings.restype = ct.c_int32
        self.TestEngineDLL.hciWriteLinkPolicySettings.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciWriteLinkPolicySettings(handle, connectionHandle, linkPolicySettings)
        
        return retval
    # end of hciWriteLinkPolicySettings


    def hciSendAclFile(self, handle: int, connHandle: int, fileName: str) -> int:
        r"""Function TestEngine::hciSendAclFile() wrapper for hciSendAclFile in TestEngine DLL.

        Python API:
            hciSendAclFile(handle: int, connHandle: int, fileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.hciSendAclFile(handle=0, connHandle=0, fileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSendAclFile(uint32 handle, uint16 connHandle,
                                                 const char* fileName)

            Parameters :    handle -
                                Handle to the device.

                            connHandle -
                                ACL connection handle as returned by hciCreateConnection or
                                hciCreateConnectionNoInquiry.

                            fileName -
                                Name of the file whose contents will be transmitted as ACL
                                packets.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to transmit the contents of a file as ACL
                            data to another device. Before this function is called a valid
                            ACL connection must have been established with a call to either
                            hciCreateConnection or hciCreateConnectionNoInquiry.
                            <p>
                            Before transmitting data a call to hciResetAclState must be made
                            on the receiving device.
                            <p>
                            When a file is sent the receiving device must be polled using the
                            hciGetAclState function for a result of ACL_RECEIVED (3) or
                            ACL_ERROR (4) at which point the entire file should have been
                            received unless there was a problem.
                            <p>
                            The received file will be saved in the system's temporary files
                            directory regardless of where it was transmitted from. The
                            received file name may be different to the original. The
                            hciGetAclFileName function should be used to find the path that
                            the received data was saved to.
                            <p>
                            This function has been tested with file sizes up to 1 Mbyte,
                            though typically smaller file sizes should be used (< 100 Kbyte)
                            to preserve memory resources required by the software in
                            transmitting the file.

        """
        self.TestEngineDLL.hciSendAclFile.restype = ct.c_int32
        self.TestEngineDLL.hciSendAclFile.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_char_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"))
        retval = self.TestEngineDLL.hciSendAclFile(handle, connHandle, local_fileName)
        
        return retval
    # end of hciSendAclFile


    def hciSendAclData(self, handle: int, connHandle: int, data: list, length: int) -> int:
        r"""Function TestEngine::hciSendAclData() wrapper for hciSendAclData in TestEngine DLL.

        Python API:
            hciSendAclData(handle: int, connHandle: int, data: list, length: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciSendAclData(handle=0, connHandle=0, data=[0,1], length=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSendAclData(uint32 handle, uint16 connHandle,
                                                 const uint8* data, uint16 length)

            Parameters :    handle -
                                Handle to the device.

                            connHandle -
                                ACL connection handle as returned by hciCreateConnection or
                                hciCreateConnectionNoInquiry.

                            data -
                                Pointer to array of bytes to be transmitted.

                            length -
                                Length of the array (in bytes) pointed to by data. Maximum
                                length is 65535.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to transmit an array of bytes as ACL data
                            to another device. Before this function is called a valid ACL
                            connection must have been established with a call to either
                            hciCreateConnection or hciCreateConnectionNoInquiry.
                            <p>
                            Before transmitting data a call to hciResetAclState must be made
                            on the receiving device.
                            <p>
                            When data is sent the receiving device must be polled using the
                            hciGetAclState function for a result of ACL_RECEIVED (3) at which
                            point all data should have been received.
                            <p>
                            The received data can be read using the hciGetAclData function.

        """
        self.TestEngineDLL.hciSendAclData.restype = ct.c_int32
        self.TestEngineDLL.hciSendAclData.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_uint16]
        if data == None:
            data = []
        local_data = (ct.c_uint8 * len(data))(*data)
        retval = self.TestEngineDLL.hciSendAclData(handle, connHandle, local_data, length)
        
        return retval
    # end of hciSendAclData


    def hciGetAclData(self, handle: int, data: list, numBytes: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::hciGetAclData() wrapper for hciGetAclData in TestEngine DLL.

        Python API:
            hciGetAclData(handle: int, data: list, numBytes: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, data, numBytes = myDll.hciGetAclData(handle=0, data=[0,1])
            print(retval, data, numBytes)

        Detail From Wrapped C API:
            Function :      int32 hciGetAclData(uint32 handle, uint8* data, uint32* numBytes)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Pointer to a pre-allocated byte array to receive ACL data
                                packet. If set to 0 no data will be copied.

                            numBytes -
                                Pointer to a value where the number of bytes in the packet
                                will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to retrieve the contents of a received
                            ACL packet.

        """
        self.TestEngineDLL.hciGetAclData.restype = ct.c_int32
        self.TestEngineDLL.hciGetAclData.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint8 * len(data))(*data)
        local_numBytes = ct.c_uint32(numBytes)
        retval = self.TestEngineDLL.hciGetAclData(handle, local_data, ct.byref(local_numBytes))
        data = local_data[:]
        numBytes = local_numBytes.value
        return retval, data, numBytes
    # end of hciGetAclData


    def hciGetAclBytesRead(self, handle: int, numBytes: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciGetAclBytesRead() wrapper for hciGetAclBytesRead in TestEngine DLL.

        Python API:
            hciGetAclBytesRead(handle: int, numBytes: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, numBytes = myDll.hciGetAclBytesRead(handle=0)
            print(retval, numBytes)

        Detail From Wrapped C API:
            Function :      int32 hciGetAclBytesRead(uint32 handle, uint32* numBytes)

            Parameters :    handle -
                                Handle to the device.

                            numBytes -
                                Pointer to a value where the number of bytes read so far will
                                be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to retrieve the number of bytes read so
                            far by the recipient of some ACL data transferred as a result of
                            a call to hciSendAclData or hciSendAclFile.

        """
        self.TestEngineDLL.hciGetAclBytesRead.restype = ct.c_int32
        self.TestEngineDLL.hciGetAclBytesRead.argtypes = [ct.c_uint32, ct.c_void_p]
        local_numBytes = ct.c_uint32(numBytes)
        retval = self.TestEngineDLL.hciGetAclBytesRead(handle, ct.byref(local_numBytes))
        numBytes = local_numBytes.value
        return retval, numBytes
    # end of hciGetAclBytesRead


    def hciGetAclFileName(self, handle: int, fileName: str='', length: int=0) -> Tuple[int, str, int]:
        r"""Function TestEngine::hciGetAclFileName() wrapper for hciGetAclFileName in TestEngine DLL.

        Python API:
            hciGetAclFileName(handle: int, fileName: str='', length: int=0) -> Tuple[int, str, int]

        Python Example Call Syntax:
            retval, fileName, length = myDll.hciGetAclFileName(handle=0)
            print(retval, fileName, length)

        Detail From Wrapped C API:
            Function :      int32 hciGetAclFileName(uint32 handle, char* fileName,
                                                    uint32* length)

            Parameters :    handle -
                                Handle to the device.

                            fileName -
                                A pre-allocated string to receive the name (full path) of the
                                file. This parameter can be set to 0 (NULL), in which case the
                                function will just set the length parameter to the number of
                                characters (NOT including a null terminator) required to hold
                                the file name.

                            length -
                                Pointer to a value where the file name length will be stored.
                                This is an input/ouput parameter, where if the value given is
                                less than that required for the file name plus a null
                                terminator, the file name will not be copied to fileName, and
                                the value will be set to the length of the file name (NOT
                                including null terminator). If the length given is greater than
                                required, it will be set to the actual length of the file name
                                (NOT including null terminator).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   The file name of received ACL data is not necessarily the same as
                            the one transmitted, because of one of the following reasons:
                            <ol>
                                <li> File already exists
                                <li> File was not in the system temporary folder
                            </ol>
                            This function is therefore used to find the name of the file
                            containing received ACL data. The name is returned in the
                            fileName argument which should be a pointer to a pre-allocated
                            character string large enough to accept the full path for the
                            file. The required string size can be found by calling this
                            function with the fileName argument set to 0 (NULL).

        """
        self.TestEngineDLL.hciGetAclFileName.restype = ct.c_int32
        self.TestEngineDLL.hciGetAclFileName.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_void_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"), 1024 if length < 1024 else length)
        local_length = ct.c_uint32(length)
        retval = self.TestEngineDLL.hciGetAclFileName(handle, local_fileName, ct.byref(local_length))
        fileName = local_fileName.value.decode()
        length = local_length.value
        return retval, fileName, length
    # end of hciGetAclFileName


    def hciGetAclState(self, handle: int, state: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciGetAclState() wrapper for hciGetAclState in TestEngine DLL.

        Python API:
            hciGetAclState(handle: int, state: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, state = myDll.hciGetAclState(handle=0)
            print(retval, state)

        Detail From Wrapped C API:
            Function :      int32 hciGetAclState(uint32 handle, int32* state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Pointer to a value where the state will be stored. This can
                                be one of the following values:
                                <table>
                                    <tr><td> ACL_IDLE<td>0<td>No transfer taking place.
                                    <tr><td> ACL_FILENAME<td>1<td>Receiving file name packet.
                                    <tr><td> ACL_RECEIVING<td>2<td>Receiving data packets.
                                    <tr><td> ACL_RECEIVED<td>3<td>File received.
                                    <tr><td> ACL_ERROR<td>4<td>Error occurred.
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to check the state of a transmission in
                            progress. It should be called for the device that is RECEIVING
                            data.

        """
        self.TestEngineDLL.hciGetAclState.restype = ct.c_int32
        self.TestEngineDLL.hciGetAclState.argtypes = [ct.c_uint32, ct.c_void_p]
        local_state = ct.c_int32(state)
        retval = self.TestEngineDLL.hciGetAclState(handle, ct.byref(local_state))
        state = local_state.value
        return retval, state
    # end of hciGetAclState


    def hciResetAclState(self, handle: int) -> int:
        r"""Function TestEngine::hciResetAclState() wrapper for hciResetAclState in TestEngine DLL.

        Python API:
            hciResetAclState(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciResetAclState(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciResetAclState(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function should be called by the RECEIVING device before a
                            call to hclSendAclData.

        """
        self.TestEngineDLL.hciResetAclState.restype = ct.c_int32
        self.TestEngineDLL.hciResetAclState.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciResetAclState(handle)
        
        return retval
    # end of hciResetAclState


    def hciReset(self, handle: int) -> int:
        r"""Function TestEngine::hciReset() wrapper for hciReset in TestEngine DLL.

        Python API:
            hciReset(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciReset(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciReset(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function issues an HCI_Reset and waits for the appropriate
                            command complete.

        """
        self.TestEngineDLL.hciReset.restype = ct.c_int32
        self.TestEngineDLL.hciReset.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciReset(handle)
        
        return retval
    # end of hciReset


    def bccmdGetAnaXtalFtrim(self, handle: int, fTrim: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetAnaXtalFtrim() wrapper for bccmdGetAnaXtalFtrim in TestEngine DLL.

        Python API:
            bccmdGetAnaXtalFtrim(handle: int, fTrim: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, fTrim = myDll.bccmdGetAnaXtalFtrim(handle=0)
            print(retval, fTrim)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetAnaXtalFtrim(uint32 handle, uint16* fTrim)

            Parameters :    handle -
                                Handle to the device.

                            fTrim -
                                Variable to receive value of fTrim.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to retrieve the BlueCore crystal trim value.
                            It can be used to get the crystal trim value on devices where the
                            firmware does not have radiotest functionality.
                            It can only be used on firmware that supports
                            BCCMD_ANA_FTRIM_READWRITE. Some recent BlueCore ICs use a
                            frequency offset value instead of a trim value. In these cases
                            this function is not supported.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdGetAnaXtalFtrim.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetAnaXtalFtrim.argtypes = [ct.c_uint32, ct.c_void_p]
        local_fTrim = ct.c_uint16(fTrim)
        retval = self.TestEngineDLL.bccmdGetAnaXtalFtrim(handle, ct.byref(local_fTrim))
        fTrim = local_fTrim.value
        return retval, fTrim
    # end of bccmdGetAnaXtalFtrim


    def bccmdSetAnaXtalFtrim(self, handle: int, fTrim: int) -> int:
        r"""Function TestEngine::bccmdSetAnaXtalFtrim() wrapper for bccmdSetAnaXtalFtrim in TestEngine DLL.

        Python API:
            bccmdSetAnaXtalFtrim(handle: int, fTrim: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetAnaXtalFtrim(handle=0, fTrim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetAnaXtalFtrim(uint32 handle, uint16 fTrim)

            Parameters :    handle -
                                Handle to the device.

                            fTrim -
                                Value of fTrim to set.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set the BlueCore crystal trim value.
                            It is equivalent to radiotestCfgXtalFtrim but can be used to set
                            the trim value on devices where the firmware does not have
                            radiotest functionality.
                            It can only be used on firmware that supports
                            BCCMD_ANA_FTRIM_READWRITE. Some recent BlueCore ICs use a
                            frequency offset value instead of a trim value. In these cases
                            this function is not supported.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdSetAnaXtalFtrim.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetAnaXtalFtrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdSetAnaXtalFtrim(handle, fTrim)
        
        return retval
    # end of bccmdSetAnaXtalFtrim


    def hciSniffMode(self, handle: int, connectionHandle: int, sniffMaxInterval: int, sniffMinInterval: int, sniffAttempt: int, sniffTimeout: int) -> int:
        r"""Function TestEngine::hciSniffMode() wrapper for hciSniffMode in TestEngine DLL.

        Python API:
            hciSniffMode(handle: int, connectionHandle: int, sniffMaxInterval: int, sniffMinInterval: int, sniffAttempt: int, sniffTimeout: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciSniffMode(handle=0, connectionHandle=0, sniffMaxInterval=0, sniffMinInterval=0, sniffAttempt=0, sniffTimeout=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSniffMode(uint32 handle, uint16 connectionHandle,
                                               uint16 sniffMaxInterval,
                                               uint16 sniffMinInterval,
                                               uint16 sniffAttempt, uint16 sniffTimeout)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

                            sniffMaxInterval -
                                Maximum acceptable number of Baseband slots between each sniff
                                period.

                            sniffMinInterval -
                                Minimum acceptable number of Baseband slots between each sniff
                                period.

                            sniffAttempt -
                                Number of Baseband receive slots for sniff attempt.

                            sniffTimeout -
                                Number of Baseband receive slots for sniff timeout.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to attempt to enter Sniff Mode with a remote
                            device. Success determined by:
                            <ol>
                                <li> Valid handle
                                <li> Valid connection handle
                            </ol>

        """
        self.TestEngineDLL.hciSniffMode.restype = ct.c_int32
        self.TestEngineDLL.hciSniffMode.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciSniffMode(handle, connectionHandle, sniffMaxInterval, sniffMinInterval, sniffAttempt, sniffTimeout)
        
        return retval
    # end of hciSniffMode


    def hciExitSniff(self, handle: int, connectionHandle: int) -> int:
        r"""Function TestEngine::hciExitSniff() wrapper for hciExitSniff in TestEngine DLL.

        Python API:
            hciExitSniff(handle: int, connectionHandle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciExitSniff(handle=0, connectionHandle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciExitSniff(uint32 handle, uint16 connectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to attempt to exit Sniff Mode with a remote
                            device. Success determined by:
                            <ol>
                                <li> Valid handle
                                <li> Valid connection handle
                                <li> DM commands not in use
                            </ol>

        """
        self.TestEngineDLL.hciExitSniff.restype = ct.c_int32
        self.TestEngineDLL.hciExitSniff.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciExitSniff(handle, connectionHandle)
        
        return retval
    # end of hciExitSniff


    def hciDisconnect(self, handle: int, connectionHandle: int) -> int:
        r"""Function TestEngine::hciDisconnect() wrapper for hciDisconnect in TestEngine DLL.

        Python API:
            hciDisconnect(handle: int, connectionHandle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciDisconnect(handle=0, connectionHandle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciDisconnect(uint32 handle, uint16 connectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to request a disconnect from a remote Bluetooth.
                            The DLL will wait, with a 5 second timeout, for the disconnect
                            event to be returned. The memory for all disconnected devices will
                            be freed for this handle. If the remote device is also connected
                            via TestEngine it is important to run
                            hciPollDisconnectComplete to confirm the correct operation and to
                            free any memory on that handle. Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Valid active connection_handle
                                <li> Successful completion of disconnect.
                            </ol>

        """
        self.TestEngineDLL.hciDisconnect.restype = ct.c_int32
        self.TestEngineDLL.hciDisconnect.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciDisconnect(handle, connectionHandle)
        
        return retval
    # end of hciDisconnect


    def hciGetConnectionHandle(self, handle: int, lap: int, uap: int, nap: int, connectionHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciGetConnectionHandle() wrapper for hciGetConnectionHandle in TestEngine DLL.

        Python API:
            hciGetConnectionHandle(handle: int, lap: int, uap: int, nap: int, connectionHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, connectionHandle = myDll.hciGetConnectionHandle(handle=0, lap=0, uap=0, nap=0)
            print(retval, connectionHandle)

        Detail From Wrapped C API:
            Function :      int32 hciGetConnectionHandle(uint32 handle, uint32 lap, uint8 uap,
                                                         uint16 nap, uint16* connectionHandle)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                LAP of BD_ADDR.

                            uap -
                                UAP of BD_ADDR.

                            nap -
                                NAP of BD_ADDR.

                            connectionHandle -
                                Pointer to a variable which will hold the returned connection
                                handle.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Returns the connection handle, if existing, between the device
                            identified by the "handle" parameter and the device identified by
                            the Bluetooth address. Failure on invalid handle and DM commands
                            enabled.

        """
        self.TestEngineDLL.hciGetConnectionHandle.restype = ct.c_int32
        self.TestEngineDLL.hciGetConnectionHandle.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_void_p]
        local_connectionHandle = ct.c_uint16(connectionHandle)
        retval = self.TestEngineDLL.hciGetConnectionHandle(handle, lap, uap, nap, ct.byref(local_connectionHandle))
        connectionHandle = local_connectionHandle.value
        return retval, connectionHandle
    # end of hciGetConnectionHandle


    def hciConnectionStatus(self, handle: int, connectionHandle: int) -> int:
        r"""Function TestEngine::hciConnectionStatus() wrapper for hciConnectionStatus in TestEngine DLL.

        Python API:
            hciConnectionStatus(handle: int, connectionHandle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciConnectionStatus(handle=0, connectionHandle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciConnectionStatus(uint32 handle, uint16 connectionHandle)


            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Checks whether the connection handle points to a valid, active
                            Bluetooth connection. Failure on invalid handle and DM commands
                            enabled.

        """
        self.TestEngineDLL.hciConnectionStatus.restype = ct.c_int32
        self.TestEngineDLL.hciConnectionStatus.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciConnectionStatus(handle, connectionHandle)
        
        return retval
    # end of hciConnectionStatus


    def hciEnableDeviceUnderTestMode(self, handle: int) -> int:
        r"""Function TestEngine::hciEnableDeviceUnderTestMode() wrapper for hciEnableDeviceUnderTestMode in TestEngine DLL.

        Python API:
            hciEnableDeviceUnderTestMode(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciEnableDeviceUnderTestMode(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciEnableDeviceUnderTestMode(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to send the enable device under test mode.
                            Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Command complete within timeout
                            </ol>

            Example :       See example for bccmdSetColdReset.

        """
        self.TestEngineDLL.hciEnableDeviceUnderTestMode.restype = ct.c_int32
        self.TestEngineDLL.hciEnableDeviceUnderTestMode.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.hciEnableDeviceUnderTestMode(handle)
        
        return retval
    # end of hciEnableDeviceUnderTestMode


    def hciGetLinkQuality(self, handle: int, connectionHandle: int, quality: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciGetLinkQuality() wrapper for hciGetLinkQuality in TestEngine DLL.

        Python API:
            hciGetLinkQuality(handle: int, connectionHandle: int, quality: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, quality = myDll.hciGetLinkQuality(handle=0, connectionHandle=0)
            print(retval, quality)

        Detail From Wrapped C API:
            Function :      int32 hciGetLinkQuality(uint32 handle, uint16 connectionHandle,
                                                    uint8* quality)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

                            quality -
                                Pointer to the link quality parameter returned by this
                                function.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the link quality.

        """
        self.TestEngineDLL.hciGetLinkQuality.restype = ct.c_int32
        self.TestEngineDLL.hciGetLinkQuality.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_quality = ct.c_uint8(quality)
        retval = self.TestEngineDLL.hciGetLinkQuality(handle, connectionHandle, ct.byref(local_quality))
        quality = local_quality.value
        return retval, quality
    # end of hciGetLinkQuality


    def hciReadBdAddr(self, handle: int, bdAddr: str='') -> Tuple[int, str]:
        r"""Function TestEngine::hciReadBdAddr() wrapper for hciReadBdAddr in TestEngine DLL.

        Python API:
            hciReadBdAddr(handle: int, bdAddr: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, bdAddr = myDll.hciReadBdAddr(handle=0)
            print(retval, bdAddr)

        Detail From Wrapped C API:
            Function :      int32 hciReadBdAddr(uint32 handle, char* bdAddr)

            Parameters :    handle -
                                Handle to the device.

                            bdAddr -
                                Pointer to a pre-allocated buffer of at least 13 bytes where
                                the Bluetooth device address will be stored as a hex string,
                                e.g. "00025b00ff01".

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the Bluetooth device address.

        """
        self.TestEngineDLL.hciReadBdAddr.restype = ct.c_int32
        self.TestEngineDLL.hciReadBdAddr.argtypes = [ct.c_uint32, ct.c_char_p]
        local_bdAddr = None if bdAddr is None else ct.create_string_buffer(bytes(bdAddr, encoding="UTF-8"), 1024)
        retval = self.TestEngineDLL.hciReadBdAddr(handle, local_bdAddr)
        bdAddr = local_bdAddr.value.decode()
        return retval, bdAddr
    # end of hciReadBdAddr


    def hciReadLocalVersionInformation(self, handle: int, versionInfo: list) -> Tuple[int, list]:
        r"""Function TestEngine::hciReadLocalVersionInformation() wrapper for hciReadLocalVersionInformation in TestEngine DLL.

        Python API:
            hciReadLocalVersionInformation(handle: int, versionInfo: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, versionInfo = myDll.hciReadLocalVersionInformation(handle=0, versionInfo=[0,1])
            print(retval, versionInfo)

        Detail From Wrapped C API:
            Function :      int32 hciReadLocalVersionInformation(uint32 handle,
                                                                 uint32* versionInfo)

            Parameters :    handle -
                                Handle to the device.

                            versionInfo -
                                A 5 member array of unsigned 32 bit integers as follows:
                                <table>
                                    <tr><td> versionInfo[0] = HCI Version
                                    <tr><td> versionInfo[1] = HCI Revision
                                    <tr><td> versionInfo[2] = LMP Version
                                    <tr><td> versionInfo[3] = Manufacturer name
                                    <tr><td> versionInfo[4] = LMP Subversion
                                </table>
                                The LMP Subversion is the firmware build ID.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the local device version information.

        """
        self.TestEngineDLL.hciReadLocalVersionInformation.restype = ct.c_int32
        self.TestEngineDLL.hciReadLocalVersionInformation.argtypes = [ct.c_uint32, ct.c_void_p]
        if versionInfo == None:
            versionInfo = []
        local_versionInfo = (ct.c_uint32 * len(versionInfo))(*versionInfo)
        retval = self.TestEngineDLL.hciReadLocalVersionInformation(handle, local_versionInfo)
        versionInfo = local_versionInfo[:]
        return retval, versionInfo
    # end of hciReadLocalVersionInformation


    def hciReadRemoteVersionInformation(self, handle: int, connectionHandle: int, versionInfo: list) -> Tuple[int, list]:
        r"""Function TestEngine::hciReadRemoteVersionInformation() wrapper for hciReadRemoteVersionInformation in TestEngine DLL.

        Python API:
            hciReadRemoteVersionInformation(handle: int, connectionHandle: int, versionInfo: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, versionInfo = myDll.hciReadRemoteVersionInformation(handle=0, connectionHandle=0, versionInfo=[0,1])
            print(retval, versionInfo)

        Detail From Wrapped C API:
            Function :      int32 hciReadRemoteVersionInformation(uint32 handle,
                                                                  uint16 connectionHandle,
                                                                  uint32* versionInfo)

            Parameters :    handle -
                                Handle to the device.

                            connectionHandle -
                                Bluetooth connection handle to remote device.

                            versionInfo -
                                A 4 member array of unsigned 32 bit integers as follows:
                                <table>
                                    <tr><td> versionInfo[0] = connectionHandle
                                    <tr><td> versionInfo[1] = LMP Version
                                    <tr><td> versionInfo[2] = Manufacturer name
                                    <tr><td> versionInfo[3] = LMP Subversion
                                </table>
                                With BlueCore and CDA ICs the LMP Subversion is the firmware
                                build ID.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the remote version information.

        """
        self.TestEngineDLL.hciReadRemoteVersionInformation.restype = ct.c_int32
        self.TestEngineDLL.hciReadRemoteVersionInformation.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        if versionInfo == None:
            versionInfo = []
        local_versionInfo = (ct.c_uint32 * len(versionInfo))(*versionInfo)
        retval = self.TestEngineDLL.hciReadRemoteVersionInformation(handle, connectionHandle, local_versionInfo)
        versionInfo = local_versionInfo[:]
        return retval, versionInfo
    # end of hciReadRemoteVersionInformation


    def hciReadRemoteNameRequest(self, handle: int, lap: int, uap: int, nap: int, pageScanRepMode: int, pageScanOffset: int, clockOffset: int, remoteName: str='') -> Tuple[int, str]:
        r"""Function TestEngine::hciReadRemoteNameRequest() wrapper for hciReadRemoteNameRequest in TestEngine DLL.

        Python API:
            hciReadRemoteNameRequest(handle: int, lap: int, uap: int, nap: int, pageScanRepMode: int, pageScanOffset: int, clockOffset: int, remoteName: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, remoteName = myDll.hciReadRemoteNameRequest(handle=0, lap=0, uap=0, nap=0, pageScanRepMode=0, pageScanOffset=0, clockOffset=0)
            print(retval, remoteName)

        Detail From Wrapped C API:
            Function :      int32 hciReadRemoteNameRequest(uint32 handle, uint32 lap,
                                                           uint8 uap, uint16 nap,
                                                           uint8 pageScanRepMode,
                                                           uint8 pageScanOffset,
                                                           uint16 clockOffset,
                                                           char* remoteName)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                LAP of BD_ADDR.

                            uap -
                                UAP of BD_ADDR.

                            nap -
                                NAP of BD_ADDR.

                            pageScanRepMode -
                                Page scan mode supported by the remote device.

                            pageScanOffset -
                                Page scan mode supported by the remote device.

                            clockOffset -
                                The clock offset between the devices.

                            remoteName -
                                Pointer to the remote name returned by the command. This
                                needs to be pre-allocated to at least 249 bytes.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the remote name.

        """
        self.TestEngineDLL.hciReadRemoteNameRequest.restype = ct.c_int32
        self.TestEngineDLL.hciReadRemoteNameRequest.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_char_p]
        local_remoteName = None if remoteName is None else ct.create_string_buffer(bytes(remoteName, encoding="UTF-8"), 1024)
        retval = self.TestEngineDLL.hciReadRemoteNameRequest(handle, lap, uap, nap, pageScanRepMode, pageScanOffset, clockOffset, local_remoteName)
        remoteName = local_remoteName.value.decode()
        return retval, remoteName
    # end of hciReadRemoteNameRequest


    def dmRegisterReq(self, handle: int) -> int:
        r"""Function TestEngine::dmRegisterReq() wrapper for dmRegisterReq in TestEngine DLL.

        Python API:
            dmRegisterReq(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmRegisterReq(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmRegisterReq(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to register the application manager queue
                            command. No other DM commands will function unless this is called.
                            Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Command complete within timeout
                                <li> non-HCI firmware
                            </ol>
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmRegisterReq.restype = ct.c_int32
        self.TestEngineDLL.dmRegisterReq.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.dmRegisterReq(handle)
        
        return retval
    # end of dmRegisterReq


    def dmSlave(self, handle: int) -> int:
        r"""Function TestEngine::dmSlave() wrapper for dmSlave in TestEngine DLL.

        Python API:
            dmSlave(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmSlave(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmSlave(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Performs two steps:
                            <ol>
                                <li>Sets the event filter to auto accept a connection request.
                                    Implements the command DM_HCI_Set_Event_Filter with the
                                    following parameters:
                                    <table>
                                        <tr><td> 0x02 - Connection setup filter type
                                        <tr><td> 0x00 - Allow connections from all devices
                                        <tr><td> 0x02 - Auto accept the connection
                                    </table>

                                <li>Implements the command DM_HCI_WriteScan_Enable with the
                                    following parameter:
                                    <p>
                                    0x03 - Inquiry scan enabled, Page scan enabled.
                            </ol>
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmSlave.restype = ct.c_int32
        self.TestEngineDLL.dmSlave.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.dmSlave(handle)
        
        return retval
    # end of dmSlave


    def dmEnableDeviceUnderTestMode(self, handle: int) -> int:
        r"""Function TestEngine::dmEnableDeviceUnderTestMode() wrapper for dmEnableDeviceUnderTestMode in TestEngine DLL.

        Python API:
            dmEnableDeviceUnderTestMode(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmEnableDeviceUnderTestMode(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmEnableDeviceUnderTestMode(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Causes the device to send the enable device under test mode.
                            Success is determined by:
                            <ol>
                                <li> Valid handle
                                <li> Command complete within timeout
                            </ol>
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmEnableDeviceUnderTestMode.restype = ct.c_int32
        self.TestEngineDLL.dmEnableDeviceUnderTestMode.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.dmEnableDeviceUnderTestMode(handle)
        
        return retval
    # end of dmEnableDeviceUnderTestMode


    def dmWritePageScanActivity(self, handle: int, interval: int, window: int) -> int:
        r"""Function TestEngine::dmWritePageScanActivity() wrapper for dmWritePageScanActivity in TestEngine DLL.

        Python API:
            dmWritePageScanActivity(handle: int, interval: int, window: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmWritePageScanActivity(handle=0, interval=0, window=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmWritePageScanActivity(uint32 handle,
                                                          uint16 interval,
                                                          uint16 window)

            Parameters :    handle -
                                Handle to the device.

                            interval -
                                Defines the amount of time between consecutive page scans.

                            window -
                                Defines the amount of time for the duration of the page scan.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command DM_HCI_Write_Pagescan_activity.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmWritePageScanActivity.restype = ct.c_int32
        self.TestEngineDLL.dmWritePageScanActivity.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.dmWritePageScanActivity(handle, interval, window)
        
        return retval
    # end of dmWritePageScanActivity


    def dmWriteInquiryScanActivity(self, handle: int, interval: int, window: int) -> int:
        r"""Function TestEngine::dmWriteInquiryScanActivity() wrapper for dmWriteInquiryScanActivity in TestEngine DLL.

        Python API:
            dmWriteInquiryScanActivity(handle: int, interval: int, window: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmWriteInquiryScanActivity(handle=0, interval=0, window=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmWriteInquiryScanActivity(uint32 handle,
                                                             uint16 interval,
                                                             uint16 window)

            Parameters :    handle -
                                Handle to the device.

                            interval -
                                Defines the amount of time between consecutive inquiry scans.

                            window -
                                Defines the amount of time for the duration of the inquiry
                                scan.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command DM_HCI_Write_Inquiryscan_activity.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmWriteInquiryScanActivity.restype = ct.c_int32
        self.TestEngineDLL.dmWriteInquiryScanActivity.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.dmWriteInquiryScanActivity(handle, interval, window)
        
        return retval
    # end of dmWriteInquiryScanActivity


    def dmWriteScanEnable(self, handle: int, scanEnable: int) -> int:
        r"""Function TestEngine::dmWriteScanEnable() wrapper for dmWriteScanEnable in TestEngine DLL.

        Python API:
            dmWriteScanEnable(handle: int, scanEnable: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmWriteScanEnable(handle=0, scanEnable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmWriteScanEnable(uint32 handle, uint8 scanEnable)

            Parameters :    handle -
                                Handle to the device.

                            scanEnable -
                                Controls whether or not the Bluetooth device will periodically
                                scan for page attempts and/or inquiry requests from other
                                Bluetooth devices.
                                <table>
                                    <tr><td> 0x00 = No Scans enabled.
                                    <tr><td> 0x01 = Inquiry Scan enabled. Page Scan disabled.
                                    <tr><td> 0x02 = Inquiry Scan disabled. Page Scan enabled.
                                    <tr><td> 0x03 = Inquiry Scan enabled. Page Scan enabled.
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Implements the command DM_HCI_WriteScan_Enable.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmWriteScanEnable.restype = ct.c_int32
        self.TestEngineDLL.dmWriteScanEnable.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.dmWriteScanEnable(handle, scanEnable)
        
        return retval
    # end of dmWriteScanEnable


    def dmSetEventFilterAutoacceptConnection(self, handle: int) -> int:
        r"""Function TestEngine::dmSetEventFilterAutoacceptConnection() wrapper for dmSetEventFilterAutoacceptConnection in TestEngine DLL.

        Python API:
            dmSetEventFilterAutoacceptConnection(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.dmSetEventFilterAutoacceptConnection(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 dmSetEventFilterAutoacceptConnection(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the event filter to auto accept a connection request.
                            Implements the command DM_HCI_Set_Event_Filter with the following
                            parameters:
                            <table>
                                <tr><td> 0x02 - Connection setup filter type
                                <tr><td> 0x00 - Allow connections from all devices
                                <tr><td> 0x02 - Auto accept the connection
                            </table>
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.dmSetEventFilterAutoacceptConnection.restype = ct.c_int32
        self.TestEngineDLL.dmSetEventFilterAutoacceptConnection.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.dmSetEventFilterAutoacceptConnection(handle)
        
        return retval
    # end of dmSetEventFilterAutoacceptConnection


    def bccmdBc3PsuTrim(self, handle: int, data: int) -> int:
        r"""Function TestEngine::bccmdBc3PsuTrim() wrapper for bccmdBc3PsuTrim in TestEngine DLL.

        Python API:
            bccmdBc3PsuTrim(handle: int, data: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdBc3PsuTrim(handle=0, data=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdBc3PsuTrim(uint32 handle, uint16 data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Data to send with the PDU.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a BCCMD with VARID of BCCMDVARID_BC3PSU
                            and a function of BCCMDPDU_BC3PSU_PSU_TRIM to the connected
                            BlueCore device.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

            Deprecated :

        """
        self.TestEngineDLL.bccmdBc3PsuTrim.restype = ct.c_int32
        self.TestEngineDLL.bccmdBc3PsuTrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdBc3PsuTrim(handle, data)
        
        return retval
    # end of bccmdBc3PsuTrim


    def bccmdChargerPsuTrim(self, handle: int, trim: int) -> int:
        r"""Function TestEngine::bccmdChargerPsuTrim() wrapper for bccmdChargerPsuTrim in TestEngine DLL.

        Python API:
            bccmdChargerPsuTrim(handle: int, trim: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdChargerPsuTrim(handle=0, trim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdChargerPsuTrim(uint32 handle, uint16 trim)

            Parameters :    handle -
                                Handle to the device.

                            trim -
                                Charger trim value to be written.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to modify the charger trim register in
                            order to alter the behaviour of BlueCore's built-in battery
                            charger.
                            <p>
                            This function is supported for applicable BlueCore ICs only. For
                            CDA ICs see teChargerSetConfig.

        """
        self.TestEngineDLL.bccmdChargerPsuTrim.restype = ct.c_int32
        self.TestEngineDLL.bccmdChargerPsuTrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdChargerPsuTrim(handle, trim)
        
        return retval
    # end of bccmdChargerPsuTrim


    def bccmdBc3BuckReg(self, handle: int, data: int) -> int:
        r"""Function TestEngine::bccmdBc3BuckReg() wrapper for bccmdBc3BuckReg in TestEngine DLL.

        Python API:
            bccmdBc3BuckReg(handle: int, data: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdBc3BuckReg(handle=0, data=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdBc3BuckReg(uint32 handle, uint16 data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Data to send with the PDU.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a BCCMD with VARID of BCCMDVARID_BC3PSU
                            and a function of BCCMDPDU_BC3PSU_BUCK_REG to the connected
                            BlueCore device.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

            Deprecated :

        """
        self.TestEngineDLL.bccmdBc3BuckReg.restype = ct.c_int32
        self.TestEngineDLL.bccmdBc3BuckReg.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdBc3BuckReg(handle, data)
        
        return retval
    # end of bccmdBc3BuckReg


    def bccmdPsuSmpsEnable(self, handle: int, reg: int) -> int:
        r"""Function TestEngine::bccmdPsuSmpsEnable() wrapper for bccmdPsuSmpsEnable in TestEngine DLL.

        Python API:
            bccmdPsuSmpsEnable(handle: int, reg: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdPsuSmpsEnable(handle=0, reg=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdPsuSmpsEnable(uint32 handle, uint16 reg)

            Parameters :    handle -
                                Handle to the device.

                            reg -
                                Value to enable (1) or disable the switch-mode regulator.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable or disable the switch-mode
                            regulator.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdPsuSmpsEnable.restype = ct.c_int32
        self.TestEngineDLL.bccmdPsuSmpsEnable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdPsuSmpsEnable(handle, reg)
        
        return retval
    # end of bccmdPsuSmpsEnable


    def bccmdBc3MicEn(self, handle: int, data: int) -> int:
        r"""Function TestEngine::bccmdBc3MicEn() wrapper for bccmdBc3MicEn in TestEngine DLL.

        Python API:
            bccmdBc3MicEn(handle: int, data: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdBc3MicEn(handle=0, data=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdBc3MicEn(uint32 handle, uint16 data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Data to send with the PDU.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a BCCMD with VARID of BCCMDVARID_BC3PSU
                            and a function of BCCMDPDU_BC3PSU_MIC_EN to the connected
                            BlueCore device.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

            Deprecated :

        """
        self.TestEngineDLL.bccmdBc3MicEn.restype = ct.c_int32
        self.TestEngineDLL.bccmdBc3MicEn.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdBc3MicEn(handle, data)
        
        return retval
    # end of bccmdBc3MicEn


    def bccmdPsuHvLinearEnable(self, handle: int, reg: int) -> int:
        r"""Function TestEngine::bccmdPsuHvLinearEnable() wrapper for bccmdPsuHvLinearEnable in TestEngine DLL.

        Python API:
            bccmdPsuHvLinearEnable(handle: int, reg: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdPsuHvLinearEnable(handle=0, reg=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdPsuHvLinearEnable(uint32 handle, uint16 reg)

            Parameters :    handle -
                                Handle to the device.

                            reg -
                                Value to enable (1) or disable the linear regulator.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable or disable the linear regulator.
                            <p>
                            For BC5 chips, use bccmdSetMicBias instead.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdPsuHvLinearEnable.restype = ct.c_int32
        self.TestEngineDLL.bccmdPsuHvLinearEnable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdPsuHvLinearEnable(handle, reg)
        
        return retval
    # end of bccmdPsuHvLinearEnable


    def bccmdBc3Led0(self, handle: int, data: int) -> int:
        r"""Function TestEngine::bccmdBc3Led0() wrapper for bccmdBc3Led0 in TestEngine DLL.

        Python API:
            bccmdBc3Led0(handle: int, data: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdBc3Led0(handle=0, data=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdBc3Led0(uint32 handle, uint16 data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Data to send with the PDU.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a BCCMD with VARID of BCCMDVARID_BC3PSU
                            and a function of BCCMDPDU_BC3PSU_LED0 to the connected BlueCore
                            device.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

            Deprecated :

        """
        self.TestEngineDLL.bccmdBc3Led0.restype = ct.c_int32
        self.TestEngineDLL.bccmdBc3Led0.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdBc3Led0(handle, data)
        
        return retval
    # end of bccmdBc3Led0


    def bccmdLedEnable(self, handle: int, led: int, state: int) -> int:
        r"""Function TestEngine::bccmdLedEnable() wrapper for bccmdLedEnable in TestEngine DLL.

        Python API:
            bccmdLedEnable(handle: int, led: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdLedEnable(handle=0, led=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdLedEnable(uint32 handle, uint16 led, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            led -
                                A zero-indexed identifier for the LED.

                            state -
                                Value to enable (1) or disable (0) the LED.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set the state of a single LED.
                            <p>
                            This function can be used with some recent BlueCore ICs, where
                            the firmware supports the LED_CONFIG BCCMD for configuring any
                            LED. For older BlueCore ICs (supporting only 2 LEDs), use
                            bccmdLed0Enable or bccmdLed1Enable. For other IC types the tePio*
                            functions can be used to drive LEDs.

        """
        self.TestEngineDLL.bccmdLedEnable.restype = ct.c_int32
        self.TestEngineDLL.bccmdLedEnable.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdLedEnable(handle, led, state)
        
        return retval
    # end of bccmdLedEnable


    def bccmdLed0Enable(self, handle: int, state: int) -> int:
        r"""Function TestEngine::bccmdLed0Enable() wrapper for bccmdLed0Enable in TestEngine DLL.

        Python API:
            bccmdLed0Enable(handle: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdLed0Enable(handle=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdLed0Enable(uint32 handle, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Value to enable (1) or disable (0) LED0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set the state of LED0.
                            <p>
                            For some recent BlueCore ICs, where the firmware supports the
                            LED_CONFIG BCCMD for configuring any LED, use bccmdLedEnable
                            instead. For other IC types the tePio* functions can be used to
                            drive LEDs.

        """
        self.TestEngineDLL.bccmdLed0Enable.restype = ct.c_int32
        self.TestEngineDLL.bccmdLed0Enable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdLed0Enable(handle, state)
        
        return retval
    # end of bccmdLed0Enable


    def bccmdBc3Led1(self, handle: int, data: int) -> int:
        r"""Function TestEngine::bccmdBc3Led1() wrapper for bccmdBc3Led1 in TestEngine DLL.

        Python API:
            bccmdBc3Led1(handle: int, data: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdBc3Led1(handle=0, data=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdBc3Led1(uint32 handle, uint16 data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                Data to send with the PDU.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write a BCCMD with VARID of BCCMDVARID_BC3PSU
                            and a function of BCCMDPDU_BC3PSU_LED1 to the connected BlueCore
                            device.
                            <p>
                            This function is supported for applicable BlueCore ICs only.

            Deprecated :

        """
        self.TestEngineDLL.bccmdBc3Led1.restype = ct.c_int32
        self.TestEngineDLL.bccmdBc3Led1.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdBc3Led1(handle, data)
        
        return retval
    # end of bccmdBc3Led1


    def bccmdLed1Enable(self, handle: int, state: int) -> int:
        r"""Function TestEngine::bccmdLed1Enable() wrapper for bccmdLed1Enable in TestEngine DLL.

        Python API:
            bccmdLed1Enable(handle: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdLed1Enable(handle=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdLed1Enable(uint32 handle, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Value to enable (1) or disable (0) LED1.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set the state of LED1.
                            <p>
                            For some recent BlueCore ICs, where the firmware supports the
                            LED_CONFIG BCCMD for configuring any LED, use bccmdLedEnable
                            instead. For other IC types the tePio* functions can be used to
                            drive LEDs.

        """
        self.TestEngineDLL.bccmdLed1Enable.restype = ct.c_int32
        self.TestEngineDLL.bccmdLed1Enable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdLed1Enable(handle, state)
        
        return retval
    # end of bccmdLed1Enable


    def bccmdChargerStatus(self, handle: int, state: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdChargerStatus() wrapper for bccmdChargerStatus in TestEngine DLL.

        Python API:
            bccmdChargerStatus(handle: int, state: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, state = myDll.bccmdChargerStatus(handle=0)
            print(retval, state)

        Detail From Wrapped C API:
            Function :      int32 bccmdChargerStatus(uint32 handle, uint16* state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Pointer to a 16-bit unsigned integer to hold the returned
                                state of the charger.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read the state of built-in battery
                            charger.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teCharger* functions should be used.

        """
        self.TestEngineDLL.bccmdChargerStatus.restype = ct.c_int32
        self.TestEngineDLL.bccmdChargerStatus.argtypes = [ct.c_uint32, ct.c_void_p]
        local_state = ct.c_uint16(state)
        retval = self.TestEngineDLL.bccmdChargerStatus(handle, ct.byref(local_state))
        state = local_state.value
        return retval, state
    # end of bccmdChargerStatus


    def bccmdChargerDisable(self, handle: int, state: int) -> int:
        r"""Function TestEngine::bccmdChargerDisable() wrapper for bccmdChargerDisable in TestEngine DLL.

        Python API:
            bccmdChargerDisable(handle: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdChargerDisable(handle=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdChargerDisable(uint32 handle, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Value to disable (1) or enable (0) the built-in battery
                                charger.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to disable or enable the built-in battery
                            charger.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teCharger* functions should be used.

        """
        self.TestEngineDLL.bccmdChargerDisable.restype = ct.c_int32
        self.TestEngineDLL.bccmdChargerDisable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdChargerDisable(handle, state)
        
        return retval
    # end of bccmdChargerDisable


    def bccmdChargerSuppressLed0(self, handle: int, state: int) -> int:
        r"""Function TestEngine::bccmdChargerSuppressLed0() wrapper for bccmdChargerSuppressLed0 in TestEngine DLL.

        Python API:
            bccmdChargerSuppressLed0(handle: int, state: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdChargerSuppressLed0(handle=0, state=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdChargerSuppressLed0(uint32 handle, uint16 state)

            Parameters :    handle -
                                Handle to the device.

                            state -
                                Value to suppress (0) or allow (1) LED0 to light when charging.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable or disable LED0 on changing.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdChargerSuppressLed0.restype = ct.c_int32
        self.TestEngineDLL.bccmdChargerSuppressLed0.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdChargerSuppressLed0(handle, state)
        
        return retval
    # end of bccmdChargerSuppressLed0


    def hciCreateConnectionNoWait(self, handle: int, lap: int, uap: int, nap: int, pktType: int, pageScanRepMode: int, pageScanMode: int, clockOffset: int, allowRoleSwitch: int) -> int:
        r"""Function TestEngine::hciCreateConnectionNoWait() wrapper for hciCreateConnectionNoWait in TestEngine DLL.

        Python API:
            hciCreateConnectionNoWait(handle: int, lap: int, uap: int, nap: int, pktType: int, pageScanRepMode: int, pageScanMode: int, clockOffset: int, allowRoleSwitch: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciCreateConnectionNoWait(handle=0, lap=0, uap=0, nap=0, pktType=0, pageScanRepMode=0, pageScanMode=0, clockOffset=0, allowRoleSwitch=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciCreateConnectionNoWait(uint32 handle, uint32 lap,
                                                            uint8 uap, uint16 nap,
                                                            uint16 pktType,
                                                            uint8 pageScanRepMode,
                                                            uint8 pageScanMode,
                                                            uint16 clockOffset,
                                                            uint8 allowRoleSwitch)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                The LAP portion of the Bluetooth address of the device to
                                request a connection with.

                            uap -
                                The UAP portion of the Bluetooth address of the device to
                                request a connection with.

                            nap -
                                The NAP portion of the Bluetooth address of the device to
                                request a connection with.

                            pktType -
                                As for hciCreateConnection.

                            pageScanRepMode -
                                The page scan repetition mode supported by the remote device
                                with the given Bluetooth address.

                            pageScanMode -
                                Indicates the page scan mode that is used for default page
                                scan.

                            clockOffset -
                                Difference between the clocks of the local device and the
                                remote device with the given Bluetooth address.

                            allowRoleSwitch -
                                Specifies whether the local device accepts or rejects the
                                request of master-slave role switch.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to request a connection with a given
                            device.
                            <p>
                            It is similar to the hciCreateConnectionNoInquiry function, the
                            difference being that this function does not wait for a
                            'Command Complete' or a 'Connection Complete' event.
                            <p>
                            This is useful for creating connections involving encryption and
                            link-key requests where other operations need to be performed
                            before these events are generated.

        """
        self.TestEngineDLL.hciCreateConnectionNoWait.restype = ct.c_int32
        self.TestEngineDLL.hciCreateConnectionNoWait.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciCreateConnectionNoWait(handle, lap, uap, nap, pktType, pageScanRepMode, pageScanMode, clockOffset, allowRoleSwitch)
        
        return retval
    # end of hciCreateConnectionNoWait


    def hciWriteAuthenticationEnable(self, handle: int, enable: int) -> int:
        r"""Function TestEngine::hciWriteAuthenticationEnable() wrapper for hciWriteAuthenticationEnable in TestEngine DLL.

        Python API:
            hciWriteAuthenticationEnable(handle: int, enable: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciWriteAuthenticationEnable(handle=0, enable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciWriteAuthenticationEnable(uint32 handle, uint8 enable)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Set to 1 when authentication required for connections,
                                otherwise 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will write the value for the Authentication_Enable
                            configuration parameter.

        """
        self.TestEngineDLL.hciWriteAuthenticationEnable.restype = ct.c_int32
        self.TestEngineDLL.hciWriteAuthenticationEnable.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciWriteAuthenticationEnable(handle, enable)
        
        return retval
    # end of hciWriteAuthenticationEnable


    def hciLinkKeyRequestNegativeReply(self, handle: int, lap: int, uap: int, nap: int) -> int:
        r"""Function TestEngine::hciLinkKeyRequestNegativeReply() wrapper for hciLinkKeyRequestNegativeReply in TestEngine DLL.

        Python API:
            hciLinkKeyRequestNegativeReply(handle: int, lap: int, uap: int, nap: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciLinkKeyRequestNegativeReply(handle=0, lap=0, uap=0, nap=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciLinkKeyRequestNegativeReply(uint32 handle, uint32 lap,
                                                                 uint8 uap, uint16 nap)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                The LAP portion of the Bluetooth address of the device that
                                there is no stored link key for.

                            uap -
                                The UAP portion of the Bluetooth address of the device that
                                there is no stored link key for.

                            nap -
                                The NAP portion of the Bluetooth address of the device that
                                there is no stored link key for.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to reply to a Link Key Request from the
                            controller if the local device does not have a stored link key
                            for the device with the given Bluetooth address.

        """
        self.TestEngineDLL.hciLinkKeyRequestNegativeReply.restype = ct.c_int32
        self.TestEngineDLL.hciLinkKeyRequestNegativeReply.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16]
        
        retval = self.TestEngineDLL.hciLinkKeyRequestNegativeReply(handle, lap, uap, nap)
        
        return retval
    # end of hciLinkKeyRequestNegativeReply


    def hciWaitForConnectionComplete(self, handle: int, connHandle: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciWaitForConnectionComplete() wrapper for hciWaitForConnectionComplete in TestEngine DLL.

        Python API:
            hciWaitForConnectionComplete(handle: int, connHandle: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, connHandle = myDll.hciWaitForConnectionComplete(handle=0)
            print(retval, connHandle)

        Detail From Wrapped C API:
            Function :      int32 hciWaitForConnectionComplete(uint32 handle,
                                                               uint16* connHandle)

            Parameters :    handle -
                                Handle to the device.

                            connHandle -
                                Pointer to connection handle of the device if successful. Set
                                to 0xffff on failure.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to wait for a 'Connection Complete'
                            event.
                            <p>
                            If the event is not triggered within 2 seconds of invocation it
                            will return failure and the value of the connHandle parameter
                            will be set to 0xffff.

        """
        self.TestEngineDLL.hciWaitForConnectionComplete.restype = ct.c_int32
        self.TestEngineDLL.hciWaitForConnectionComplete.argtypes = [ct.c_uint32, ct.c_void_p]
        local_connHandle = ct.c_uint16(connHandle)
        retval = self.TestEngineDLL.hciWaitForConnectionComplete(handle, ct.byref(local_connHandle))
        connHandle = local_connHandle.value
        return retval, connHandle
    # end of hciWaitForConnectionComplete


    def hciWaitForLinkKeyRequest(self, handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]:
        r"""Function TestEngine::hciWaitForLinkKeyRequest() wrapper for hciWaitForLinkKeyRequest in TestEngine DLL.

        Python API:
            hciWaitForLinkKeyRequest(handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]

        Python Example Call Syntax:
            retval, lap, uap, nap = myDll.hciWaitForLinkKeyRequest(handle=0)
            print(retval, lap, uap, nap)

        Detail From Wrapped C API:
            Function :      int32 hciWaitForLinkKeyRequest(uint32 handle, uint32* lap,
                                                           uint8* uap, uint16* nap)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                The LAP portion of the Bluetooth address of the device for
                                which a stored link key is being requested.

                            uap -
                                The UAP portion of the Bluetooth address of the device for
                                which a stored link key is being requested.

                            nap -
                                The NAP portion of the Bluetooth address of the device for
                                which a stored link key is being requested.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to wait for a 'Link Key Request' event.
                            A link key request event will be generated when setting up a
                            connection when authentication has been enabled (see
                            hciWriteAuthenticationEnable) prior to calling
                            hciCreateConnectionNoWait.
                            <p>
                            If the event is not triggered within 2 seconds of invocation it
                            will return failure.

        """
        self.TestEngineDLL.hciWaitForLinkKeyRequest.restype = ct.c_int32
        self.TestEngineDLL.hciWaitForLinkKeyRequest.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_lap = ct.c_uint32(lap)
        local_uap = ct.c_uint8(uap)
        local_nap = ct.c_uint16(nap)
        retval = self.TestEngineDLL.hciWaitForLinkKeyRequest(handle, ct.byref(local_lap), ct.byref(local_uap), ct.byref(local_nap))
        lap = local_lap.value
        uap = local_uap.value
        nap = local_nap.value
        return retval, lap, uap, nap
    # end of hciWaitForLinkKeyRequest


    def hciWaitForPinCodeRequest(self, handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]:
        r"""Function TestEngine::hciWaitForPinCodeRequest() wrapper for hciWaitForPinCodeRequest in TestEngine DLL.

        Python API:
            hciWaitForPinCodeRequest(handle: int, lap: int=0, uap: int=0, nap: int=0) -> Tuple[int, int, int, int]

        Python Example Call Syntax:
            retval, lap, uap, nap = myDll.hciWaitForPinCodeRequest(handle=0)
            print(retval, lap, uap, nap)

        Detail From Wrapped C API:
            Function :      int32 hciWaitForPinCodeRequest(uint32 handle, uint32* lap,
                                                           uint8* uap, uint16* nap)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                The LAP portion of the Bluetooth address of the device which
                                a new link key is being created for.

                            uap -
                                The UAP portion of the Bluetooth address of the device which
                                a new link key is being created for.

                            nap -
                                The NAP portion of the Bluetooth address of the device which
                                a new link key is being created for.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to wait for a 'PIN Code Request' event.
                            A PIN code request event will be generated when setting up a
                            connection when authentication has been enabled (see
                            hciWriteAuthenticationEnable) prior to calling
                            hciCreateConnectionNoWait.
                            <p>
                            The recipient must respond by calling hciPinCodeRequestReply.
                            <p>
                            If the event is not triggered within 2 seconds of invocation it
                            will return failure.

        """
        self.TestEngineDLL.hciWaitForPinCodeRequest.restype = ct.c_int32
        self.TestEngineDLL.hciWaitForPinCodeRequest.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_lap = ct.c_uint32(lap)
        local_uap = ct.c_uint8(uap)
        local_nap = ct.c_uint16(nap)
        retval = self.TestEngineDLL.hciWaitForPinCodeRequest(handle, ct.byref(local_lap), ct.byref(local_uap), ct.byref(local_nap))
        lap = local_lap.value
        uap = local_uap.value
        nap = local_nap.value
        return retval, lap, uap, nap
    # end of hciWaitForPinCodeRequest


    def hciWaitForEncryptionChange(self, handle: int, enable: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciWaitForEncryptionChange() wrapper for hciWaitForEncryptionChange in TestEngine DLL.

        Python API:
            hciWaitForEncryptionChange(handle: int, enable: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, enable = myDll.hciWaitForEncryptionChange(handle=0)
            print(retval, enable)

        Detail From Wrapped C API:
            Function :      int32 hciWaitForEncryptionChange(uint32 handle, uint8* enable)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Defines whether encryption is enabled/disabled.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to wait for an 'Encryption Change'
                            event. An encryption change event will be generated following a
                            call to hciSetConnectionEncryption. The event will be generated
                            for both devices on the connection.
                            <p>
                            If the event is not triggered within 2 seconds of invocation it
                            will return failure.

        """
        self.TestEngineDLL.hciWaitForEncryptionChange.restype = ct.c_int32
        self.TestEngineDLL.hciWaitForEncryptionChange.argtypes = [ct.c_uint32, ct.c_void_p]
        local_enable = ct.c_uint8(enable)
        retval = self.TestEngineDLL.hciWaitForEncryptionChange(handle, ct.byref(local_enable))
        enable = local_enable.value
        return retval, enable
    # end of hciWaitForEncryptionChange


    def hciPinCodeRequestReply(self, handle: int, lap: int, uap: int, nap: int, pinCodeLength: int, pinCode: list) -> Tuple[int, list]:
        r"""Function TestEngine::hciPinCodeRequestReply() wrapper for hciPinCodeRequestReply in TestEngine DLL.

        Python API:
            hciPinCodeRequestReply(handle: int, lap: int, uap: int, nap: int, pinCodeLength: int, pinCode: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, pinCode = myDll.hciPinCodeRequestReply(handle=0, lap=0, uap=0, nap=0, pinCodeLength=0, pinCode=[0,1])
            print(retval, pinCode)

        Detail From Wrapped C API:
            Function :      int32 hciPinCodeRequestReply(uint32 handle, uint32 lap, uint8 uap,
                                                         uint16 nap, uint8 pinCodeLength,
                                                         uint8* pinCode)

            Parameters :    handle -
                                Handle to the device.

                            lap -
                                The LAP portion of the Bluetooth address of the device for
                                which the PIN code is for.

                            uap -
                                The UAP portion of the Bluetooth address of the device for
                                which the PIN code is for.

                            nap -
                                The NAP portion of the Bluetooth address of the device for
                                which the PIN code is for.

                            pinCodeLength -
                                The length (in bytes) of the PIN code to be used. Range 1-16.

                            pinCode -
                                PIN code for the device that is to be connected. This should
                                be an array of bytes equal in length to the given
                                pinCodeLength parameter.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to respond to a 'PIN Code Request' event
                            (see hciWaitForPinCodeRequest) and specifies the PIN code to use
                            for a connection.

        """
        self.TestEngineDLL.hciPinCodeRequestReply.restype = ct.c_int32
        self.TestEngineDLL.hciPinCodeRequestReply.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_void_p]
        if pinCode == None:
            pinCode = []
        local_pinCode = (ct.c_uint8 * len(pinCode))(*pinCode)
        retval = self.TestEngineDLL.hciPinCodeRequestReply(handle, lap, uap, nap, pinCodeLength, local_pinCode)
        pinCode = local_pinCode[:]
        return retval, pinCode
    # end of hciPinCodeRequestReply


    def hciSetConnectionEncryption(self, handle: int, connHandle: int, enable: int) -> int:
        r"""Function TestEngine::hciSetConnectionEncryption() wrapper for hciSetConnectionEncryption in TestEngine DLL.

        Python API:
            hciSetConnectionEncryption(handle: int, connHandle: int, enable: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciSetConnectionEncryption(handle=0, connHandle=0, enable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciSetConnectionEncryption(uint32 handle, uint16 connHandle,
                                                             uint8 enable)

            Parameters :    handle -
                                Handle to the device.

                            connHandle -
                                Connection handle to enable/disable link layer encryption.

                            enable -
                                Set to 1 to enable link layer encryption, otherwise set to 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to enable or disable link level
                            encryption.

        """
        self.TestEngineDLL.hciSetConnectionEncryption.restype = ct.c_int32
        self.TestEngineDLL.hciSetConnectionEncryption.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciSetConnectionEncryption(handle, connHandle, enable)
        
        return retval
    # end of hciSetConnectionEncryption


    def hciLeReadLocalSupportedFeatures(self, handle: int, leFeatures: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciLeReadLocalSupportedFeatures() wrapper for hciLeReadLocalSupportedFeatures in TestEngine DLL.

        Python API:
            hciLeReadLocalSupportedFeatures(handle: int, leFeatures: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, leFeatures = myDll.hciLeReadLocalSupportedFeatures(handle=0)
            print(retval, leFeatures)

        Detail From Wrapped C API:
            Function :      int32 hciLeReadLocalSupportedFeatures(uint32 handle,
                                                                  uint64* leFeatures)

            Parameters :    handle -
                                Handle to the device.

                            leFeatures -
                                A bit mask of supported features, as specified in the
                                Bluetooth specification for the
                                HCI_LE_Read_Local_Supported_Features command.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads the local (connected device) LE supported features.

        """
        self.TestEngineDLL.hciLeReadLocalSupportedFeatures.restype = ct.c_int32
        self.TestEngineDLL.hciLeReadLocalSupportedFeatures.argtypes = [ct.c_uint32, ct.c_void_p]
        local_leFeatures = ct.c_uint64(leFeatures)
        retval = self.TestEngineDLL.hciLeReadLocalSupportedFeatures(handle, ct.byref(local_leFeatures))
        leFeatures = local_leFeatures.value
        return retval, leFeatures
    # end of hciLeReadLocalSupportedFeatures


    def hciLeTestEnd(self, handle: int, numPackets: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hciLeTestEnd() wrapper for hciLeTestEnd in TestEngine DLL.

        Python API:
            hciLeTestEnd(handle: int, numPackets: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, numPackets = myDll.hciLeTestEnd(handle=0)
            print(retval, numPackets)

        Detail From Wrapped C API:
            Function :      int32 hciLeTestEnd(uint32 handle, uint16* numPackets)

            Parameters :    handle -
                                Handle to the device.

                            numPackets -
                                Number of received packets (valid after previously running
                                hciLeEnhancedReceiverTest).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Stops a running LE transmitter or receiver test. This function
                            should be called to end running tests started with
                            hciLeEnhancedReceiverTest or hciLeEnhancedTransmitterTest (and
                            between calls to these test functions).
                            <p>
                            The numPackets value will wrap once the limit of its type (65535)
                            is reached.

            Example :

                static const uint8 LE_TEST_CHANNEL = 1;
                static const uint8 LE_TX_LENGTH = 37;
                static const uint8 LE_TX_PAYLOAD = 0; // 0 = PRBS9
                static const uint8 LE_PHY = 2; // 2 = 2M
                static const uint8 LE_RX_MOD_INDEX = 0;

                static const uint32 RX_TEST_DURATION_MS = 1000;

                uint32 dutHandle = openTestEngineDebug(1, 0, DEBUG_USBDBG);
                if (dutHandle == TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Failed to connect to device under test" << endl;
                    return;
                }

                // Test TX
                if (hciLeEnhancedTransmitterTest(dutHandle, LE_TEST_CHANNEL, LE_TX_LENGTH,
                    LE_TX_PAYLOAD, LE_PHY) != TE_OK)
                {
                    cout << "hciLeEnhancedTransmitterTest failed" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Perform TX measurements using test equipment here

                // End TX test
                uint16 pktCount = 0;
                if (hciLeTestEnd(dutHandle, &pktCount) != TE_OK)
                {
                    cout << "hciLeTestEnd failed (stopping TX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Test RX

                // Switch on test equipment transmission here

                // Start receiving packets
                if (hciLeEnhancedReceiverTest(dutHandle, LE_TEST_CHANNEL, LE_PHY,
                    LE_RX_MOD_INDEX) != TE_OK)
                {
                    cout << "hciLeEnhancedReceiverTest failed" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Wait for test duration
                Sleep(RX_TEST_DURATION_MS);

                // Stop receiving
                if (hciLeTestEnd(dutHandle, &pktCount) != TE_OK)
                {
                    cout << "hciLeTestEnd failed (stopping RX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }
                else
                {
                    cout << "Packet count = " << pktCount << endl;
                }

                closeTestEngine(dutHandle);

        """
        self.TestEngineDLL.hciLeTestEnd.restype = ct.c_int32
        self.TestEngineDLL.hciLeTestEnd.argtypes = [ct.c_uint32, ct.c_void_p]
        local_numPackets = ct.c_uint16(numPackets)
        retval = self.TestEngineDLL.hciLeTestEnd(handle, ct.byref(local_numPackets))
        numPackets = local_numPackets.value
        return retval, numPackets
    # end of hciLeTestEnd


    def hciLeEnhancedReceiverTest(self, handle: int, channel: int, phy: int, modIndex: int) -> int:
        r"""Function TestEngine::hciLeEnhancedReceiverTest() wrapper for hciLeEnhancedReceiverTest in TestEngine DLL.

        Python API:
            hciLeEnhancedReceiverTest(handle: int, channel: int, phy: int, modIndex: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciLeEnhancedReceiverTest(handle=0, channel=0, phy=0, modIndex=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciLeEnhancedReceiverTest(uint32 handle, uint8 channel,
                                                            uint8 phy, uint8 modIndex)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                The BLE channel (0 - 39).
                                <p>
                                channel = (freqMHz \x96 2402) / 2

                            phy -
                                The PHY to use, where:
                                <table>
                                    <tr><td>1 = LE 1M PHY
                                    <tr><td>2 = LE 2M PHY
                                    <tr><td>3 = LE Coded PHY
                                </table>
                                <p>
                                NOTE: The LE 2M PHY option is not supported for channels
                                0, 12 and 39 in end user scenarios, as per the BT
                                specification. Therefore, product certification testing with
                                the 2M PHY should not be performed on these channels.

                            mod -
                                The assumed transmitter modulation index, where:
                                <table>
                                    <tr><td>0 = Standard
                                    <tr><td>1 = Stable
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts Low Energy (LE) enhanced receiver test mode.
                            <p>
                            This function is not supported for BlueCore ICs - see
                            radiotestBle for testing LE with those devices.
                            <p>
                            It is necessary to end this test mode using hciLeTestEnd before
                            running another LE test mode (or changing parameters for the same
                            mode). RECEIVER or TRANSMITTER tests started with radiotestBle
                            should also be ENDed before running these test modes.

            Example :       See example code for hciLeTestEnd.

        """
        self.TestEngineDLL.hciLeEnhancedReceiverTest.restype = ct.c_int32
        self.TestEngineDLL.hciLeEnhancedReceiverTest.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciLeEnhancedReceiverTest(handle, channel, phy, modIndex)
        
        return retval
    # end of hciLeEnhancedReceiverTest


    def hciLeEnhancedTransmitterTest(self, handle: int, channel: int, dataLength: int, payloadType: int, phy: int) -> int:
        r"""Function TestEngine::hciLeEnhancedTransmitterTest() wrapper for hciLeEnhancedTransmitterTest in TestEngine DLL.

        Python API:
            hciLeEnhancedTransmitterTest(handle: int, channel: int, dataLength: int, payloadType: int, phy: int) -> int

        Python Example Call Syntax:
            retval = myDll.hciLeEnhancedTransmitterTest(handle=0, channel=0, dataLength=0, payloadType=0, phy=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 hciLeEnhancedTransmitterTest(uint32 handle, uint8 channel,
                                                               uint8 dataLength,
                                                               uint8 payloadType, uint8 phy)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                The BLE channel (0 - 39).
                                <p>
                                channel = (freqMHz \x96 2402) / 2

                            dataLength -
                                The length in bytes (0 - 255), of the payload data in each
                                packet.

                            payloadType -
                                The packet payload, where:
                                <table>
                                    <tr><td>0 = Pseudo-Random bit sequence 9
                                    <tr><td>1 = Pattern of alternating bits "11110000"
                                    <tr><td>2 = Pattern of alternating bits "10101010"
                                    <tr><td>3 = Pseudo-Random bit sequence 15
                                    <tr><td>4 = Pattern of all "1" bits
                                    <tr><td>5 = Pattern of all "0" bits
                                    <tr><td>6 = Pattern of alternating bits "00001111"
                                    <tr><td>7 = Pattern of alternating bits "01010101"
                                </table>

                            phy -
                                The PHY to use, where:
                                <table>
                                    <tr><td>1 = LE 1M PHY
                                    <tr><td>2 = LE 2M PHY
                                    <tr><td>3 = LE Coded PHY with S=8 data coding
                                    <tr><td>4 = LE Coded PHY with S=2 data coding
                                </table>
                                <p>
                                NOTE: The LE 2M PHY option is not supported for channels
                                0, 12 and 39 in end user scenarios, as per the BT
                                specification. Therefore, product certification testing with
                                the 2M PHY should not be performed on these channels.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts Low Energy (LE) enhanced transmitter test mode.
                            <p>
                            This function is not supported for BlueCore ICs - see
                            radiotestBle for testing LE with those devices.
                            <p>
                            It is necessary to end this test mode using hciLeTestEnd before
                            running another LE test mode (or changing parameters for the same
                            mode). RECEIVER or TRANSMITTER tests started with radiotestBle
                            should also be ENDed before running these test modes.

            Example :       See example code for hciLeTestEnd.

        """
        self.TestEngineDLL.hciLeEnhancedTransmitterTest.restype = ct.c_int32
        self.TestEngineDLL.hciLeEnhancedTransmitterTest.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.hciLeEnhancedTransmitterTest(handle, channel, dataLength, payloadType, phy)
        
        return retval
    # end of hciLeEnhancedTransmitterTest


    def vmWrite(self, handle: int, data: list) -> int:
        r"""Function TestEngine::vmWrite() wrapper for vmWrite in TestEngine DLL.

        Python API:
            vmWrite(handle: int, data: list) -> int

        Python Example Call Syntax:
            retval = myDll.vmWrite(handle=0, data=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 vmWrite(uint32 handle, const uint16* data)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                A pointer to an array of 16-bit unsigned integers. The first
                                element must be the length of the array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to write to a VM application running on a
                            BlueCore IC.
                            <p>
                            When using a host (HCI) transport, it uses BCSP channel 13, which
                            is tunnelled, using manufacturer specific extensions through the
                            transport.
                            <p>
                            When using a debug transport, a BCCMD is used to write the data to
                            the VM. If the firmware does not support the relevant BCCMD,
                            TE_UNSUPPORTED_FUNCTION is returned.
                            <p>
                            A successful status does NOT indicate that the packet has reached
                            BlueCore. The user should implement the appropriate hand shaking
                            both in the on-chip application and the application sitting above
                            TestEngine.
                            <p>
                            This function is supported for BlueCore ICs only - see teAppWrite
                            for other IC types.

        """
        self.TestEngineDLL.vmWrite.restype = ct.c_int32
        self.TestEngineDLL.vmWrite.argtypes = [ct.c_uint32, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.vmWrite(handle, local_data)
        
        return retval
    # end of vmWrite


    def vmRead(self, handle: int, data: list, timeout: int) -> Tuple[int, list]:
        r"""Function TestEngine::vmRead() wrapper for vmRead in TestEngine DLL.

        Python API:
            vmRead(handle: int, data: list, timeout: int) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, data = myDll.vmRead(handle=0, data=[0,1], timeout=0)
            print(retval, data)

        Detail From Wrapped C API:
            Function :      int32 vmRead(uint32 handle, uint16* data, uint16 timeout)

            Parameters :    handle -
                                Handle to the device.

                            data -
                                A pointer to an array of 16-bit unsigned integers. The first
                                element must be the length of the array.

                            timeout -
                                A timeout, in ms, of the time to wait for the packet. A value
                                of 0 means the function will just poll.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read any data returned from a VM
                            application running on a BlueCore IC. If no data has been read
                            within the timeout period, TE_ERROR will be returned and data[0]
                            will be set to zero.
                            <p>
                            When using a host (HCI) transport, it uses BCSP channel 13, which
                            is tunnelled, using manufacturer specific extensions through the
                            transport. The function will fetch VM printf messages as well
                            as other VM host messages.
                            <p>
                            When using a debug transport, a BCCMD is used to read data from
                            the VM. If the firmware does not support the relevant BCCMD,
                            TE_UNSUPPORTED_FUNCTION is returned. VM printf messages are
                            not fetched when using a debug transport.
                            <p>
                            This function is supported for BlueCore ICs only - see teAppWrite
                            for other IC types.

        """
        self.TestEngineDLL.vmRead.restype = ct.c_int32
        self.TestEngineDLL.vmRead.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.vmRead(handle, local_data, timeout)
        data = local_data[:]
        return retval, data
    # end of vmRead


    def bccmdSetSingleChan(self, handle: int, channel: int) -> int:
        r"""Function TestEngine::bccmdSetSingleChan() wrapper for bccmdSetSingleChan in TestEngine DLL.

        Python API:
            bccmdSetSingleChan(handle: int, channel: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetSingleChan(handle=0, channel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetSingleChan(uint32 handle, uint16 channel)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                The single hop channel the radio should use.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to configure the Bluetooth radio to transmit
                            and receive on a single hop channel. This disables hopping and
                            whitening.
                            <p>
                            To re-enable hopping use the bccmdSetHoppingOn function.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdSetSingleChan.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetSingleChan.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdSetSingleChan(handle, channel)
        
        return retval
    # end of bccmdSetSingleChan


    def bccmdSetHoppingOn(self, handle: int) -> int:
        r"""Function TestEngine::bccmdSetHoppingOn() wrapper for bccmdSetHoppingOn in TestEngine DLL.

        Python API:
            bccmdSetHoppingOn(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetHoppingOn(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetHoppingOn(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable hopping after previously being
                            disabled as a result of calling bccmdSetSingleChan.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdSetHoppingOn.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetHoppingOn.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdSetHoppingOn(handle)
        
        return retval
    # end of bccmdSetHoppingOn


    def bccmdFmSwitchPower(self, handle: int, powerOn: int) -> int:
        r"""Function TestEngine::bccmdFmSwitchPower() wrapper for bccmdFmSwitchPower in TestEngine DLL.

        Python API:
            bccmdFmSwitchPower(handle: int, powerOn: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmSwitchPower(handle=0, powerOn=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmSwitchPower(uint32 handle, uint8 powerOn)

            Parameters :    handle -
                                Handle to the device.

                            powerOn -
                                Power state to set. Set to 1 to power on, 0 to power off.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to switch on power to the FM radio part of
                            the chip.
                            <p>
                            If powerOn is set to 1, RDS reception is switched on after the
                            radio is powered up.
                            <p>
                            NOTE: radiotest and FM control functions should be run either side
                            of a warm reset to ensure that the firmware is in the correct
                            state in each case.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    do
                    {
                        int32 teRet = bccmdFmSwitchPower(teHandle, 1);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmSwitchPower error" << endl;
                            break;
                        }

                        uint8 status;
                        teRet = bccmdFmGetStatus(teHandle, &status);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmGetStatus error" << endl;
                            break;
                        }
                        // Check status as expected (tuner should be powered, but not tuned)
                        if ((status & 0x07) != 1)
                        {
                            cout << "bccmdFmGetStatus indicates incorrect tuner state" << endl;
                            break;
                        }

                        teRet = bccmdFmSetFreq(teHandle, 103000);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmSetFreq error" << endl;
                            break;
                        }

                        int8 rssi;
                        teRet = bccmdFmGetRssi(teHandle, &rssi);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmGetRssi error" << endl;
                            break;
                        }
                        cout << "RSSI = " << (int16)rssi << endl;

                        int16 snr;
                        teRet = bccmdFmGetSnr(teHandle, &snr);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmGetSnr error" << endl;
                            break;
                        }
                        cout << "SNR = " << snr << endl;

                        int16 offset;
                        teRet = bccmdFmGetIfOffset(teHandle, &offset);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmGetIfOffset error" << endl;
                            break;
                        }
                        cout << "IF offset = " << offset << endl;

                        teRet = bccmdFmSetupAudio(teHandle, 0, 16, 2);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmSetupAudio error" << endl;
                            break;
                        }

                        // TEST AUDIO HERE

                        // If using BC7FM or later, should disconnect audio
                        teRet = bccmdDisconnectAudio(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdDisconnectAudio error" << endl;
                            break;
                        }

                        // May need a delay to ensure the RDS PI has been received
                        Sleep(3000);
                        uint8 matched;
                        teRet = bccmdFmVerifyRDSPi(teHandle, 0xCF86, 3000, &matched);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmVerifyRDSPi error" << endl;
                            break;
                        }
                        if (matched != 0x01)
                        {
                            cout << "RDS PI did not match within the timeoutMs period" << endl;
                        }

                    } while(0);

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdFmSwitchPower.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmSwitchPower.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdFmSwitchPower(handle, powerOn)
        
        return retval
    # end of bccmdFmSwitchPower


    def bccmdFmSetFreq(self, handle: int, freqKHz: int) -> int:
        r"""Function TestEngine::bccmdFmSetFreq() wrapper for bccmdFmSetFreq in TestEngine DLL.

        Python API:
            bccmdFmSetFreq(handle: int, freqKHz: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmSetFreq(handle=0, freqKHz=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmSetFreq(uint32 handle, uint32 freqKHz)

            Parameters :    handle -
                                Handle to the device.

                            freqKHz -
                                Frequency to set in KHz.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to tune the FM radio part of the chip to
                            the desired frequency.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Valid frequency (freqKHz in range)
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmSetFreq.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmSetFreq.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdFmSetFreq(handle, freqKHz)
        
        return retval
    # end of bccmdFmSetFreq


    def bccmdFmGetRssi(self, handle: int, rssi: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdFmGetRssi() wrapper for bccmdFmGetRssi in TestEngine DLL.

        Python API:
            bccmdFmGetRssi(handle: int, rssi: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, rssi = myDll.bccmdFmGetRssi(handle=0)
            print(retval, rssi)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmGetRssi(uint32 handle, int8* rssi)

            Parameters :    handle -
                                Handle to the device.

                            rssi -
                                The measured RSSI value will be stored at this address.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets an RSSI (Received Signal Strength Indication)
                            measurement from the radio, measured in dBm.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Radio powered up and tuned to a valid frequency
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmGetRssi.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmGetRssi.argtypes = [ct.c_uint32, ct.c_void_p]
        local_rssi = ct.c_int8(rssi)
        retval = self.TestEngineDLL.bccmdFmGetRssi(handle, ct.byref(local_rssi))
        rssi = local_rssi.value
        return retval, rssi
    # end of bccmdFmGetRssi


    def bccmdFmGetSnr(self, handle: int, snr: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdFmGetSnr() wrapper for bccmdFmGetSnr in TestEngine DLL.

        Python API:
            bccmdFmGetSnr(handle: int, snr: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, snr = myDll.bccmdFmGetSnr(handle=0)
            print(retval, snr)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmGetSnr(uint32 handle, int16* snr)

            Parameters :    handle -
                                Handle to the device.

                            snr -
                                The measured SNR value will be stored at this address.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets a SNR (Signal to Noise Ratio) measurement
                            from the radio, measured in dB.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Radio powered up and tuned to a valid frequency
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmGetSnr.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmGetSnr.argtypes = [ct.c_uint32, ct.c_void_p]
        local_snr = ct.c_int16(snr)
        retval = self.TestEngineDLL.bccmdFmGetSnr(handle, ct.byref(local_snr))
        snr = local_snr.value
        return retval, snr
    # end of bccmdFmGetSnr


    def bccmdFmGetIfOffset(self, handle: int, offset: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdFmGetIfOffset() wrapper for bccmdFmGetIfOffset in TestEngine DLL.

        Python API:
            bccmdFmGetIfOffset(handle: int, offset: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, offset = myDll.bccmdFmGetIfOffset(handle=0)
            print(retval, offset)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmGetIfOffset(uint32 handle, int16* offset)

            Parameters :    handle -
                                Handle to the device.

                            offset -
                                The measured IF offset value will be stored at this address.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets an IF (Intermediate Frequency) offset
                            measurement from the radio, measured in KHz.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Radio powered up and tuned to a valid frequency
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmGetIfOffset.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmGetIfOffset.argtypes = [ct.c_uint32, ct.c_void_p]
        local_offset = ct.c_int16(offset)
        retval = self.TestEngineDLL.bccmdFmGetIfOffset(handle, ct.byref(local_offset))
        offset = local_offset.value
        return retval, offset
    # end of bccmdFmGetIfOffset


    def bccmdFmGetStatus(self, handle: int, status: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdFmGetStatus() wrapper for bccmdFmGetStatus in TestEngine DLL.

        Python API:
            bccmdFmGetStatus(handle: int, status: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, status = myDll.bccmdFmGetStatus(handle=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmGetStatus(uint32 handle, uint8* status)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                The fetched status value will be stored at this address.
                                <p>
                                The status is a bit field with the following format:
                                <ol>
                                    <li>bit[0] = TS[0] (tuner state bit 0 *)
                                    <li>bit[1] = TS[1] (tuner state bit 1 *)
                                    <li>bit[2] = TS[2] (tuner state bit 2 *)
                                    <li>bit[3] = RDA   (RDS Data Available indicator)
                                    <li>bit[4] = STR   (Stereo signal detected indicator)
                                    <li>bit[5] = IFR   (IF frequency in range indicator)
                                    <li>bit[6] = RSR   (RSSI in range indicator)
                                    <li>bit[7] = Not used
                                </ol>
                                <p>
                                Values for TS indicate:
                                <ol>
                                    <li>0 = Radio is not powered up, or has been reset
                                    <li>1 = Radio is not tuned to a valid frequency
                                    <li>2 = A tuning process is in progress
                                    <li>3 = Radio is tuned but RDS Rx. is powered down
                                    <li>4 = Radio is tuned but no RDS is present
                                    <li>5 = Radio is tuned but RDS is not synchronised
                                    <li>6 = Radio is tuned and RDS is being received
                                </ol>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function reads the status register of the FM radio.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmGetStatus.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmGetStatus.argtypes = [ct.c_uint32, ct.c_void_p]
        local_status = ct.c_uint8(status)
        retval = self.TestEngineDLL.bccmdFmGetStatus(handle, ct.byref(local_status))
        status = local_status.value
        return retval, status
    # end of bccmdFmGetStatus


    def bccmdFmSetupAudio(self, handle: int, route: int, gain: int, channel: int) -> int:
        r"""Function TestEngine::bccmdFmSetupAudio() wrapper for bccmdFmSetupAudio in TestEngine DLL.

        Python API:
            bccmdFmSetupAudio(handle: int, route: int, gain: int, channel: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmSetupAudio(handle=0, route=0, gain=0, channel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmSetupAudio(uint32 handle, uint8 route, uint8 gain,
                                                    uint8 channel)

            Parameters :    handle -
                                Handle to the device.

                            route -
                                Audio output route for FM RX, where:
                                <table>
                                    <tr><td>0 = Route audio to CODEC
                                    <tr><td>1 = Route audio to PCM port 1 (PCM Mode)
                                    <tr><td>2 = Route audio to PCM port 2 (PCM Mode)
                                    <tr><td>3 = Route audio to PCM port 1 (I2S Master Mode)
                                    <tr><td>4 = Route audio to PCM port 2 (I2S Master Mode)
                                </table>
                                <p>
                                Note: Default voice slots are used in each case.

                            gain -
                                Audio gain value to set, between 0 and maxValue, where
                                maxValue depends on the "route" parameter as follows:
                                <table>
                                    <tr><td>route = 0, maxValue = 22
                                    <tr><td>route = 1-4, maxValue = 7 (BC5FM only)
                                </table>
                                <p>
                                The gain parameter for PCM audio is ignored for chips other
                                than BC5FM.

                            channel -
                                Channel selection for CODEC routing, where:
                                <table>
                                    <tr><td>0 = Left only
                                    <tr><td>1 = Right only
                                    <tr><td>2 = Left and Right channels
                                </table>
                                <p>
                                If a single channel is selected, the other channel will be
                                muted.
                                <p>
                                Channel selection is for CODEC output only (PCM outputs always
                                use both channels).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to setup the audio routing and gain for
                            the FM RX output.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmSetupAudio.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmSetupAudio.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdFmSetupAudio(handle, route, gain, channel)
        
        return retval
    # end of bccmdFmSetupAudio


    def bccmdFmVerifyRDSPi(self, handle: int, pi: int, timeoutMs: int, matched: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdFmVerifyRDSPi() wrapper for bccmdFmVerifyRDSPi in TestEngine DLL.

        Python API:
            bccmdFmVerifyRDSPi(handle: int, pi: int, timeoutMs: int, matched: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, matched = myDll.bccmdFmVerifyRDSPi(handle=0, pi=0, timeoutMs=0)
            print(retval, matched)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmVerifyRDSPi(uint32 handle, uint16 pi,
                                                     uint16 timeoutMs, uint8* matched)

            Parameters :    handle -
                                Handle to the device.

                            pi -
                                PI (Program Identity) value to match against.

                            timeoutMs -
                                Timeout value in milliseconds. The function will poll for a
                                matching PI value for the duration of the timeout before
                                returning.

                            matched -
                                The status of the match check will be stored at this address,
                                where 0 = not matched, and 1 = matched.

  Returns :         <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to verify that an expected PI value has
                            been received and decoded by the FM radio.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Radio powered up and tuned to a valid frequency
                                    <li> RDS data being received
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM.

        """
        self.TestEngineDLL.bccmdFmVerifyRDSPi.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmVerifyRDSPi.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_matched = ct.c_uint8(matched)
        retval = self.TestEngineDLL.bccmdFmVerifyRDSPi(handle, pi, timeoutMs, ct.byref(local_matched))
        matched = local_matched.value
        return retval, matched
    # end of bccmdFmVerifyRDSPi


    def bccmdFmTxSwitchPower(self, handle: int, powerOn: int) -> int:
        r"""Function TestEngine::bccmdFmTxSwitchPower() wrapper for bccmdFmTxSwitchPower in TestEngine DLL.

        Python API:
            bccmdFmTxSwitchPower(handle: int, powerOn: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmTxSwitchPower(handle=0, powerOn=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmTxSwitchPower(uint32 handle, uint8 powerOn)

            Parameters :    handle -
                                Handle to the device.

                            powerOn -
                                Power state to set. Set to 1 to power on, 0 to power off.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to switch on power to the FM TX part of
                            the chip.
                            <p>
                            If powerOn is set to 1, FM TX with RDS is switched on.
                            <p>
                            NOTE: FM TX and RX testing cannot run in parallel.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM TX.

            Example :

                uint32 teHandle = TE_INVALID_HANDLE_VALUE;
                uint32 timeoutMs = 0;

                do
                {
                    cout << "Trying to connect..." << endl;
                    teHandle = openTestEngine(BCSP, "COM1", 115200, 1000, 0);
                    timeoutMs += 1000;
                } while (teHandle == TE_INVALID_HANDLE_VALUE && timeoutMs < MAX_TIMEOUT_MS);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    do
                    {
                        int32 teRet = bccmdFmTxSwitchPower(teHandle, 1);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmTxSwitchPower error" << endl;
                            break;
                        }

                        teRet = bccmdFmTxSetFreq(teHandle, 103000);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmTxSetFreq error" << endl;
                            break;
                        }

                        teRet = bccmdFmTxSetPowerLevel(teHandle, -1);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmTxSetPowerLevel error" << endl;
                            break;
                        }

                        teRet = bccmdFmTxSetupAudio(teHandle, 0, 10);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdFmTxSetupAudio error" << endl;
                            break;
                        }

                        // TEST AUDIO HERE

                        teRet = bccmdDisconnectAudio(teHandle);
                        if (teRet != TE_OK)
                        {
                            cout << "bccmdDisconnectAudio error" << endl;
                            break;
                        }

                    } while(0);

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.bccmdFmTxSwitchPower.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmTxSwitchPower.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdFmTxSwitchPower(handle, powerOn)
        
        return retval
    # end of bccmdFmTxSwitchPower


    def bccmdFmTxSetFreq(self, handle: int, freqKHz: int) -> int:
        r"""Function TestEngine::bccmdFmTxSetFreq() wrapper for bccmdFmTxSetFreq in TestEngine DLL.

        Python API:
            bccmdFmTxSetFreq(handle: int, freqKHz: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmTxSetFreq(handle=0, freqKHz=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmTxSetFreq(uint32 handle, uint32 freqKHz)

            Parameters :    handle -
                                Handle to the device.

                            freqKHz -
                                Frequency to set in KHz.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to tune the FM TX part of the chip to
                            the desired frequency.
                            <p>
                            Preconditions for success are:
                                <ol>
                                    <li> Valid handle
                                    <li> Valid frequency (freqKHz in range)
                                </ol>
                            <p>
                            This function is supported only for BlueCore ICs supporting FM TX.

        """
        self.TestEngineDLL.bccmdFmTxSetFreq.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmTxSetFreq.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdFmTxSetFreq(handle, freqKHz)
        
        return retval
    # end of bccmdFmTxSetFreq


    def bccmdFmTxSetPowerLevel(self, handle: int, powerLevel: int) -> int:
        r"""Function TestEngine::bccmdFmTxSetPowerLevel() wrapper for bccmdFmTxSetPowerLevel in TestEngine DLL.

        Python API:
            bccmdFmTxSetPowerLevel(handle: int, powerLevel: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmTxSetPowerLevel(handle=0, powerLevel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmTxSetPowerLevel(uint32 handle, int16 powerLevel)

            Parameters :    handle -
                                Handle to the device.

                            powerLevel -
                                FM power output value to set, between -24 and 0, where 0
                                gives the highest output power. 0 is the default value.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set the FM power level for FM TX.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM TX.

        """
        self.TestEngineDLL.bccmdFmTxSetPowerLevel.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmTxSetPowerLevel.argtypes = [ct.c_uint32, ct.c_int16]
        
        retval = self.TestEngineDLL.bccmdFmTxSetPowerLevel(handle, powerLevel)
        
        return retval
    # end of bccmdFmTxSetPowerLevel


    def bccmdFmTxSetupAudio(self, handle: int, route: int, audioGain: int) -> int:
        r"""Function TestEngine::bccmdFmTxSetupAudio() wrapper for bccmdFmTxSetupAudio in TestEngine DLL.

        Python API:
            bccmdFmTxSetupAudio(handle: int, route: int, audioGain: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdFmTxSetupAudio(handle=0, route=0, audioGain=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdFmTxSetupAudio(uint32 handle, uint8 route,
                                                      uint16 audioGain)

            Parameters :    handle -
                                Handle to the device.

                            route -
                                Audio output route for FM TX, where:
                                <table>
                                    <tr><td>0 = Route audio from CODEC
                                    <tr><td>1 = Route audio from PCM port 1 (PCM Mode)
                                    <tr><td>2 = Route audio from PCM port 2 (PCM Mode)
                                    <tr><td>3 = Route audio from PCM port 1 (I2S Master Mode)
                                    <tr><td>4 = Route audio from PCM port 2 (I2S Master Mode)
                                </table>
                                <p>
                                Note: Default voice slots are used in each case.

                            audioGain -
                                Analogue audio input gain value to set, between 0 and 22.
                                <p>
                                The following key-points are given for approximately 80%
                                full-scale on the audio input:
                                <table>
                                    <tr><td>100mV input = 12
                                    <tr><td>200mV input = 10
                                    <tr><td>300mV input = 9
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to setup the audio routing and input level
                            for FM TX.
                            <p>
                            This function is supported only for BlueCore ICs supporting FM TX.

        """
        self.TestEngineDLL.bccmdFmTxSetupAudio.restype = ct.c_int32
        self.TestEngineDLL.bccmdFmTxSetupAudio.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdFmTxSetupAudio(handle, route, audioGain)
        
        return retval
    # end of bccmdFmTxSetupAudio


    def bccmdDisconnectAudio(self, handle: int) -> int:
        r"""Function TestEngine::bccmdDisconnectAudio() wrapper for bccmdDisconnectAudio in TestEngine DLL.

        Python API:
            bccmdDisconnectAudio(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdDisconnectAudio(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdDisconnectAudio(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to disconnect any connected audio streams,
                            such as may be created when calling bccmdFmSetupAudio with BC7
                            and later chips.
                            <p>
                            Connections are disconnected, and the stream endpoints are
                            closed.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teAudio* functions should be used.

        """
        self.TestEngineDLL.bccmdDisconnectAudio.restype = ct.c_int32
        self.TestEngineDLL.bccmdDisconnectAudio.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdDisconnectAudio(handle)
        
        return retval
    # end of bccmdDisconnectAudio


    def bccmdAudioGetSource(self, handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdAudioGetSource() wrapper for bccmdAudioGetSource in TestEngine DLL.

        Python API:
            bccmdAudioGetSource(handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, sid = myDll.bccmdAudioGetSource(handle=0, device=0, iface=0, channel=0)
            print(retval, sid)

        Detail From Wrapped C API:
            Function :      int32 bccmdAudioGetSource(uint32 handle, uint16 device,
                                                      uint16 iface, uint16 channel,
                                                      uint16* sid)

            Parameters :    handle -
                                Handle to the device.

                            device -
                                The stream device identifier, where:
                                <table>
                                    <tr><td>1 = PCM
                                    <tr><td>2 = I2S
                                    <tr><td>3 = CODEC
                                    <tr><td>4 = FM
                                    <tr><td>5 = SPDIF
                                    <tr><td>6 = DIGITAL_MIC
                                </table>

                            iface -
                                The hardware interface instance, e.g. 0, 1, etc.

                            channel -
                                Channel selection for CODEC device, where:
                                <table>
                                    <tr><td>0 = Channel A
                                    <tr><td>1 = Channel B
                                    <tr><td>2 = Channels A and B
                                </table>
                                <p>
                                If a single channel is selected, the other channel will be
                                muted.

                            sid -
                                Pointer to where the source ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to get the ID for an audio stream endpoint
                            source device. This sid can be used when configuring audio
                            configuration parameters using bccmdAudioConfigure.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teAudio* functions should be used.

        """
        self.TestEngineDLL.bccmdAudioGetSource.restype = ct.c_int32
        self.TestEngineDLL.bccmdAudioGetSource.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_sid = ct.c_uint16(sid)
        retval = self.TestEngineDLL.bccmdAudioGetSource(handle, device, iface, channel, ct.byref(local_sid))
        sid = local_sid.value
        return retval, sid
    # end of bccmdAudioGetSource


    def bccmdAudioGetSink(self, handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdAudioGetSink() wrapper for bccmdAudioGetSink in TestEngine DLL.

        Python API:
            bccmdAudioGetSink(handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, sid = myDll.bccmdAudioGetSink(handle=0, device=0, iface=0, channel=0)
            print(retval, sid)

        Detail From Wrapped C API:
            Function :      int32 bccmdAudioGetSink(uint32 handle, uint16 device,
                                                    uint16 iface, uint16 channel,
                                                    uint16* sid)

            Parameters :    handle -
                                Handle to the device.

                            device -
                                The stream device identifier, where:
                                <table>
                                    <tr><td>1 = PCM
                                    <tr><td>2 = I2S
                                    <tr><td>3 = CODEC
                                    <tr><td>4 = FM
                                    <tr><td>5 = SPDIF
                                    <tr><td>6 = DIGITAL_MIC
                                </table>

                            iface -
                                The hardware interface instance, e.g. 0, 1, etc.

                            channel -
                                Channel selection for CODEC device, where:
                                <table>
                                    <tr><td>0 = Channel A
                                    <tr><td>1 = Channel B
                                    <tr><td>2 = Channels A and B
                                </table>
                                <p>
                                If a single channel is selected, the other channel will be
                                muted.

                            sid -
                                Pointer to where the sink ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to get the ID for an audio stream endpoint
                            sink device. This sid can be used when configuring audio
                            configuration parameters using bccmdAudioConfigure.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teAudio* functions should be used.

        """
        self.TestEngineDLL.bccmdAudioGetSink.restype = ct.c_int32
        self.TestEngineDLL.bccmdAudioGetSink.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_sid = ct.c_uint16(sid)
        retval = self.TestEngineDLL.bccmdAudioGetSink(handle, device, iface, channel, ct.byref(local_sid))
        sid = local_sid.value
        return retval, sid
    # end of bccmdAudioGetSink


    def bccmdAudioConfigure(self, handle: int, sid: int, key: int, value: int) -> int:
        r"""Function TestEngine::bccmdAudioConfigure() wrapper for bccmdAudioConfigure in TestEngine DLL.

        Python API:
            bccmdAudioConfigure(handle: int, sid: int, key: int, value: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdAudioConfigure(handle=0, sid=0, key=0, value=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdAudioConfigure(uint32 handle, uint16 sid, uint16 key,
                                                      uint32 value)

            Parameters :    handle -
                                Handle to the device.

                            sid -
                                Source/Sink ID to configure.

                            key -
                                Audio configuration key to set.

                            value -
                                The value to set for the audio configuration key.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set an audio configuration key value
                            for a given audio source / sink. The sid parameter can be obtained
                            using bccmdAudioGetSource / bccmdAudioGetSink.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types the teAudio* functions should be used.

        """
        self.TestEngineDLL.bccmdAudioConfigure.restype = ct.c_int32
        self.TestEngineDLL.bccmdAudioConfigure.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdAudioConfigure(handle, sid, key, value)
        
        return retval
    # end of bccmdAudioConfigure


    def bccmdDirectChargerPsuTrim(self, handle: int, trim: int) -> int:
        r"""Function TestEngine::bccmdDirectChargerPsuTrim() wrapper for bccmdDirectChargerPsuTrim in TestEngine DLL.

        Python API:
            bccmdDirectChargerPsuTrim(handle: int, trim: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdDirectChargerPsuTrim(handle=0, trim=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdDirectChargerPsuTrim(uint32 handle, uint16 trim)

            Parameters :    handle -
                                Handle to the device.

                            trim -
                                Charger trim value to be written.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to modify the charger trim register in
                            order to alter the behaviour of BlueCore's built-in battery
                            charger. The function is for use initially with BC4 and BC5
                            devices, in order to bypass routines in the firmware which cause
                            a delay in setting the register value.
                            <p>
                            This function is supported for BlueCore ICs only. For other ICs
                            see teChargerSetConfig.

        """
        self.TestEngineDLL.bccmdDirectChargerPsuTrim.restype = ct.c_int32
        self.TestEngineDLL.bccmdDirectChargerPsuTrim.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdDirectChargerPsuTrim(handle, trim)
        
        return retval
    # end of bccmdDirectChargerPsuTrim


    def teSupportsHq(self, handle: int, hqSupported: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teSupportsHq() wrapper for teSupportsHq in TestEngine DLL.

        Python API:
            teSupportsHq(handle: int, hqSupported: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, hqSupported = myDll.teSupportsHq(handle=0)
            print(retval, hqSupported)

        Detail From Wrapped C API:
            Function :      int32 teSupportsHq(uint32 handle, uint8* hqSupported)

            Parameters :    handle -
                                Handle to the device.

                            hqSupported -
                                If HQCMDs are supported by the transport used for the
                                specified handle, this value is set to 1. Otherwise the value
                                is set to 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>1 = Success
                            </table>

            Description :   This function gets the status of HQCMD support. Host transports
                            such as BCSP/H4/H4DS/H5 (UART) and USB support HQCMDs, as do the
                            TRB and USBDBG debug transports. SPI transports may support HQCMD
                            if the BlueCore firmware supports HQ over SPI.
                            <p>
                            Certain radiotests and other BCCMDs generate HQCMDs. This function
                            can be used to determine whether using such commands is
                            appropriate for the transport used.
                            <p>
                            All functions with names beginning hq* require HQCMD support. The
                            following radiotest / bccmd functions also require HQ support:
                            <table>
                                <tr><td>radiotestRxstart2
                                <tr><td>radiotestBer1
                                <tr><td>radiotestBer2
                                <tr><td>radiotestBerLoopback
                                <tr><td>radiotestRadioStatus
                                <tr><td>radiotestRadioStatusArray
                                <tr><td>radiotestRxdata1
                                <tr><td>radiotestRxdata2
                                <tr><td>radiotestRxLoopback (deprecated)
                                <tr><td>radiotestSettle (deprecated)
                                <tr><td>bccmdProvokeFault
                            </table>
                            <p>
                            See the BCCMD specification document for further information.

        """
        self.TestEngineDLL.teSupportsHq.restype = ct.c_int32
        self.TestEngineDLL.teSupportsHq.argtypes = [ct.c_uint32, ct.c_void_p]
        local_hqSupported = ct.c_uint8(hqSupported)
        retval = self.TestEngineDLL.teSupportsHq(handle, ct.byref(local_hqSupported))
        hqSupported = local_hqSupported.value
        return retval, hqSupported
    # end of teSupportsHq


    def bccmdSetAuxDac(self, handle: int, enable: int, level: int) -> int:
        r"""Function TestEngine::bccmdSetAuxDac() wrapper for bccmdSetAuxDac in TestEngine DLL.

        Python API:
            bccmdSetAuxDac(handle: int, enable: int, level: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetAuxDac(handle=0, enable=0, level=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetAuxDac(uint32 handle, uint8 enable, uint8 level)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Flag defining whether the aux DAC output should be enabled or
                                disabled. Set the value to 1 to enable, 0 to disable.

                            level -
                                Value to write to the AUX_DAC output (if enable = 1).
                                Range is 0...255.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to control the AUX_DAC line on BlueCore.
                            The line can be enabled with a given level written, or be
                            disabled.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdSetAuxDac.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetAuxDac.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdSetAuxDac(handle, enable, level)
        
        return retval
    # end of bccmdSetAuxDac


    def bccmdSetMicBiasIf(self, handle: int, instance: int, enable: int, voltage: int) -> int:
        r"""Function TestEngine::bccmdSetMicBiasIf() wrapper for bccmdSetMicBiasIf in TestEngine DLL.

        Python API:
            bccmdSetMicBiasIf(handle: int, instance: int, enable: int, voltage: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetMicBiasIf(handle=0, instance=0, enable=0, voltage=0)
            print(retval)

        Detail From Wrapped C API:
        

Function :          int32 bccmdSetMicBiasIf(uint32 handle, uint8 instance,
                                                    uint8 enable, uint8 voltage);

            Parameters :    handle -
                                Handle to the device.

                            instance -
                                Selects the mic bias line to set (zero indexed).

                            enable -
                                Value indicating whether the mic bias output should be enabled
                                or disabled. Set the value to 1 to enable, 0 to disable.

                            voltage -
                                Value which maps to an approximate output voltage for the line,
                                e.g.:
                                <table>
                                    <tr><td>0 = 1.80 V
                                    <tr><td>1 = 2.60 V
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to control MIC bias lines for some BC7
                            (those supporting multiple MIC_BIAS outputs) and later BlueCore
                            chips. Use bccmdSetMicBias for older chips.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types teAudioMicBiasConfigure should be used.

        """
        self.TestEngineDLL.bccmdSetMicBiasIf.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetMicBiasIf.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdSetMicBiasIf(handle, instance, enable, voltage)
        
        return retval
    # end of bccmdSetMicBiasIf


    def bccmdSetMicBias(self, handle: int, enable: int, voltage: int, current: int, enableLowPowerMode: int) -> int:
        r"""Function TestEngine::bccmdSetMicBias() wrapper for bccmdSetMicBias in TestEngine DLL.

        Python API:
            bccmdSetMicBias(handle: int, enable: int, voltage: int, current: int, enableLowPowerMode: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetMicBias(handle=0, enable=0, voltage=0, current=0, enableLowPowerMode=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetMicBias(uint32 handle, uint8 enable, uint8 voltage,
                                                  uint8 current, uint8 enableLowPowerMode)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Flag defining whether the mic bias output should be enabled
                                or disabled. Set the value to 1 to enable, 0 to disable.

                            voltage -
                                Value which maps to a voltage set for the line, where for
                                BC5-MM, the mapping is:
                                <table>
                                    <tr><td>0 = 1.72 V
                                    <tr><td>1 = 1.77 V
                                    <tr><td>2 = 1.83 V
                                    <tr><td>3 = 1.89 V
                                    <tr><td>4 = 1.97 V
                                    <tr><td>5 = 2.03 V
                                    <tr><td>6 = 2.12 V
                                    <tr><td>7 = 2.20 V
                                    <tr><td>8 = 2.34 V
                                    <tr><td>9 = 2.44 V
                                    <tr><td>10 = 2.58 V
                                    <tr><td>11 = 2.71 V
                                    <tr><td>12 = 2.92 V
                                    <tr><td>13 = 3.10 V
                                    <tr><td>14 = 3.34 V
                                    <tr><td>15 = 3.60 V
                                </table>

                            current -
                                Value which maps to a current set for the line, where for
                                BC5-MM, the mapping is:
                                <table>
                                    <tr><td>0 = 0.32 mA
                                    <tr><td>1 = 0.40 mA
                                    <tr><td>2 = 0.48 mA
                                    <tr><td>3 = 0.56 mA
                                    <tr><td>4 = 0.64 mA
                                    <tr><td>5 = 0.72 mA
                                    <tr><td>6 = 0.80 mA
                                    <tr><td>7 = 0.88 mA
                                    <tr><td>8 = 0.97 mA
                                    <tr><td>9 = 1.05 mA
                                    <tr><td>10 = 1.13 mA
                                    <tr><td>11 = 1.21 mA
                                    <tr><td>12 = 1.29 mA
                                    <tr><td>13 = 1.37 mA
                                    <tr><td>14 = 1.45 mA
                                    <tr><td>15 = 1.53 mA
                                </table>

                            enableLowPowerMode -
                                Flag defining whether the mic bias circuit low power mode
                                is enabled or disabled. Set the value to 1 to enable, 0 to
                                disable.
                                <p>
                                NOTE: Whilst saving power, the low power mode does result in
                                greater noise on the line. For most production test purposes,
                                this should be irrelevant.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to control the MIC_BIAS line on BlueCore.
                            The line can be enabled with specified voltage and current levels,
                            or be disabled. The built in low power mode for mic_bias can also
                            be controlled.
                            <p>
                            This function and the associated BCCMD in the firmware has been
                            implemented initially for BC5-MM.
                            <p>
                            For BC7 chips with multiple MIC_BIAS lines and later BlueCore
                            chips, use bccmdSetMicBiasIf. For other IC types
                            teAudioMicBiasConfigure should be used.

        """
        self.TestEngineDLL.bccmdSetMicBias.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetMicBias.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdSetMicBias(handle, enable, voltage, current, enableLowPowerMode)
        
        return retval
    # end of bccmdSetMicBias


    def teGetAvailableDebugPorts(self, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestEngine::teGetAvailableDebugPorts() wrapper for teGetAvailableDebugPorts in TestEngine DLL.

        Python API:
            teGetAvailableDebugPorts(maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.teGetAvailableDebugPorts()
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 teGetAvailableDebugPorts(uint16* maxLen, char* ports,
                                                           char* trans, uint16* count)

            Parameters :    maxLen -
                                Size of the arrays pointed to by the ports and trans
                                parameters. If this parameter indicates that the ports or
                                trans arrays are too small to store the complete strings,
                                then the value is set to the size required (and error is
                                returned).
                                If any other error occurs, this value is set to zero.

                            ports -
                                Pointer to an array of ASCII chars where the comma separated
                                list of available debug port names will be stored. These are
                                readable names which could be used for user selection.

                            trans -
                                Pointer to an array of ASCII chars where the comma separated
                                list of debug transport options for each of the available
                                ports will be stored. The transport options for a port can be
                                passed directly into the openTestEngineDebugTrans function to
                                open the port.

                            count -
                                This value is set to the number of available ports found.

            Returns :       <table>
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function is used to get a list of available debug ports. A
                            char array, pointed to by the ports parameter, is filled with
                            a comma separated list of port names. A further char array,
                            pointed to by the trans parameter, is filled with a comma
                            separated list of the relevant transport option strings that
                            specify each available debug port.
                            <p>
                            If the maxLen parameter indicates that either char array is not
                            large enough to contain the strings, Error is returned and the
                            maxLen parameter is set to the size required for the arrays.
                            <p>
                            If any other error occurs, the maxLen parameter is set to 0.
                            <p>
                            This function can be used by an application to get a list of
                            available debug ports with which to populate a drop down list or
                            other means of selection. The strings returned in the ports
                            parameter are in human readable format for display / selection.
                            The strings returned in the trans parameter can be passed directly
                            to the openTestEngineDebugTrans function to open the port.

            Example :       See example for openTestEngineDebugTrans.

        """
        self.TestEngineDLL.teGetAvailableDebugPorts.restype = ct.c_int32
        self.TestEngineDLL.teGetAvailableDebugPorts.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestEngineDLL.teGetAvailableDebugPorts(ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of teGetAvailableDebugPorts


    def teGetAvailableDebugPortsEx(self, criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestEngine::teGetAvailableDebugPortsEx() wrapper for teGetAvailableDebugPortsEx in TestEngine DLL.

        Python API:
            teGetAvailableDebugPortsEx(criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.teGetAvailableDebugPortsEx(criteria=0)
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 teGetAvailableDebugPortsEx(uint32 criteria, uint16* maxLen,
                                char* ports, char* trans, uint16* count)

            Parameters :    criteria -
                                Search criteria for enumerating devices. A bit pattern
                                made up one or bitwise combination of TE_TRANS_CRIT_* values.
                                For devices that have a lockable transport and are locked,
                                the trans string will contain TRANSLOCK=1 as an indicator.
                                Using TE_TRANS_CRIT_DEFAULT will return the same output as
                                teGetAvailableDebugPorts.
                                Using TE_TRANS_CRIT_ALL will output all devices.

                            maxLen -
                                Size of the arrays pointed to by the ports and trans
                                parameters. If this parameter indicates that the ports or
                                trans arrays are too small to store the complete strings,
                                then the value is set to the size required (and error is
                                returned).
                                If any other error occurs, this value is set to zero.

                            ports -
                                Pointer to an array of ASCII chars where the comma separated
                                list of available debug port names will be stored. These are
                                readable names which could be used for user selection.

                            trans -
                                Pointer to an array of ASCII chars where the comma separated
                                list of debug transport options for each of the available
                                ports will be stored. The transport options for a port can be
                                passed directly into the openTestEngineDebugTrans function to
                                open the port.

                            count -
                                This value is set to the number of available ports found.

            Returns :       <table>
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function is used to get a list of available debug ports. A
                            char array, pointed to by the ports parameter, is filled with
                            a comma separated list of port names. A further char array,
                            pointed to by the trans parameter, is filled with a comma
                            separated list of the relevant transport option strings that
                            specify each available debug port.
                            <p>
                            If the maxLen parameter indicates that either char array is not
                            large enough to contain the strings, Error is returned and the
                            maxLen parameter is set to the size required for the arrays.
                            <p>
                            If any other error occurs, the maxLen parameter is set to 0.
                            <p>
                            This function can be used by an application to get a list of
                            available debug ports with which to populate a drop down list or
                            other means of selection. The strings returned in the ports
                            parameter are in human readable format for display / selection.
                            The strings returned in the trans parameter can be passed directly
                            to the openTestEngineDebugTrans function to open the port.

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* pPortsStr = new char[maxLen];
                char* pTransStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USB TRB (151134)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=TRB SPIPORT=1")

                int32 status = teGetAvailableDebugPortsEx(TE_TRANS_CRIT_DEFAULT, &maxLen,
                    pPortsStr, pTransStr, &count);
                if (status != TE_OK && maxLen != 0)
                {
                    // Not enough space - resize the storage
                    pPortsStr = new char[maxLen];
                    pTransStr = new char[maxLen];
                    status = teGetAvailableDebugPortsEx(TE_TRANS_CRIT_DEFAULT, &maxLen,
                        pPortsStr, pTransStr, &count);
                }
                if (status != TE_OK || count == 0)
                {
                    cout << "Error getting debug ports, or none found" << endl;
                    delete[] pPortsStr;
                    delete[] pTransStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, pPortsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, pTransStr, ','); // Use these to open a transport

                // Open the debug port using the trans string
                // For the purposes of this example, we're just using the first in the list
                uint32 teHandle = openTestEngineDebugTrans(trans.at(0).c_str(), 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Perform all your testing here

                    closeTestEngine(teHandle);
                }

                delete[] pPortsStr;
                delete[] pTransStr;

        """
        self.TestEngineDLL.teGetAvailableDebugPortsEx.restype = ct.c_int32
        self.TestEngineDLL.teGetAvailableDebugPortsEx.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestEngineDLL.teGetAvailableDebugPortsEx(criteria, ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of teGetAvailableDebugPortsEx


    def bccmdProvokeFault(self, handle: int, faultCode: int) -> int:
        r"""Function TestEngine::bccmdProvokeFault() wrapper for bccmdProvokeFault in TestEngine DLL.

        Python API:
            bccmdProvokeFault(handle: int, faultCode: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdProvokeFault(handle=0, faultCode=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdProvokeFault(uint32 handle, uint16 faultCode)

            Parameters :    handle -
                                Handle to the device.

                            faultCode -
                                Fault code to provoke.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function provokes a fault within the chip. Once the command
                            is issued the device will need to be polled for the fault report
                            using the hqGetFaultReport function.
                            <p>
                            This function will clear any existing logged fault reports before
                            sending the BCCMD to provoke a fault. Therefore, it may be
                            appropriate to fetch any existing fault reports first (using
                            hqGetFaultReports).
                            <p>
                            Fault reports can be disabled by PSKEY, in which case
                            hqGetFaultReport will timeout and fail, despite the fact that
                            bccmdProvokeFault succeeded.
                            <p>
                            This function is only supported over a SPI connection if HQ over
                            SPI is supported by the device firmware.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdProvokeFault.restype = ct.c_int32
        self.TestEngineDLL.bccmdProvokeFault.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.bccmdProvokeFault(handle, faultCode)
        
        return retval
    # end of bccmdProvokeFault


    def hqGetFaultReports(self, handle: int, maxReports: int, codes: list, timestamps: list, repeats: list, numReports: int=0, timeout: int=0) -> Tuple[int, list, list, list, int]:
        r"""Function TestEngine::hqGetFaultReports() wrapper for hqGetFaultReports in TestEngine DLL.

        Python API:
            hqGetFaultReports(handle: int, maxReports: int, codes: list, timestamps: list, repeats: list, numReports: int=0, timeout: int=0) -> Tuple[int, list, list, list, int]

        Python Example Call Syntax:
            retval, codes, timestamps, repeats, numReports = myDll.hqGetFaultReports(handle=0, maxReports=0, codes=[0,1], timestamps=[0,1], repeats=[0,1], timeout=0)
            print(retval, codes, timestamps, repeats, numReports)

        Detail From Wrapped C API:
            Function :      int32 hqGetFaultReports(uint32 handle, uint16 maxReports,
                                                    uint16* codes, uint32* timestamps,
                                                    uint16* repeats, uint16* numReports,
                                                    int32 timeout)

            Parameters :    handle -
                                Handle to the device.

                            maxReports -
                                Maximum number of fault reports to fetch. The size of the
                                arrays pointed to by the codes, timeStamps and repeats
                                parameters must be >= maxReports.

                            codes -
                                Pointer to an array where the fault codes will be stored. The
                                size of the array should be >= maxReports.

                            timestamps -
                                Pointer to an array where the fault timestamps (in
                                milliseconds) will be stored. The size of the array should
                                be >= maxReports. This parameter can be set to zero if the
                                timestamps are not required.

                            repeats -
                                Pointer to an array where the fault repeat counts will be
                                stored. The repeat count specifies how many fault with the
                                same code were stored by the firmware before sending the fault
                                report. The size of the array should be >= maxReports. This
                                parameter can be set to zero if the timestamps are not
                                required.

                            numReports -
                                Pointer to a value where the actual number of fault reports
                                fetched will be stored.

                            timeout -
                                Used to specify a timeout, in ms, which the software will wait
                                for HQ fault reports to be returned from the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function returns a number of fault reports. If there are
                            existing logged faults, the function will immediately fetch the
                            fault report fields. If there are no logged fault reports, then
                            the function will wait for the specified timeout period for a
                            fault report from the device.
                            <p>
                            Fault reports can be received at any time after communications
                            are established with the device. This function can be called to
                            check for logged faults.
                            <p>
                            Faults are stored in the order in which they were received, i.e.
                            codes[0] will contain the first fault code in the list. The most
                            recent fault being codes[numReports - 1].
                            <p>
                            This function can be called following a call to bccmdProvokeFault,
                            which will clear any existing fault reports and provoke a
                            specified fault. In this case, it is possible that a fault report
                            other than that provoked is received prior to receiving the
                            provoked fault. This will cause the function to return reports
                            without the inclusion the provoked fault. In this case, calling
                            hqGetFaultReports again after a small delay should return reports
                            including the provoked fault.
                            <p>
                            Fault reports can be disabled by PSKEY, in which case
                            hqGetFaultReport will timeout and fail.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.hqGetFaultReports.restype = ct.c_int32
        self.TestEngineDLL.hqGetFaultReports.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_int32]
        if codes == None:
            codes = []
        local_codes = (ct.c_uint16 * max(maxReports, len(codes)))(*codes)
        if timestamps == None:
            timestamps = []
        local_timestamps = (ct.c_uint32 * max(maxReports, len(timestamps)))(*timestamps)
        if repeats == None:
            repeats = []
        local_repeats = (ct.c_uint16 * max(maxReports, len(repeats)))(*repeats)
        local_numReports = ct.c_uint16(numReports)
        retval = self.TestEngineDLL.hqGetFaultReports(handle, maxReports, local_codes, local_timestamps, local_repeats, ct.byref(local_numReports), timeout)
        codes = local_codes[:]
        timestamps = local_timestamps[:]
        repeats = local_repeats[:]
        numReports = local_numReports.value
        return retval, codes, timestamps, repeats, numReports
    # end of hqGetFaultReports


    def teGetFaultDesc(self, handle: int, faultCode: int, desc: str='') -> Tuple[int, str]:
        r"""Function TestEngine::teGetFaultDesc() wrapper for teGetFaultDesc in TestEngine DLL.

        Python API:
            teGetFaultDesc(handle: int, faultCode: int, desc: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, desc = myDll.teGetFaultDesc(handle=0, faultCode=0)
            print(retval, desc)

        Detail From Wrapped C API:
            Function :      int32 teGetFaultDesc(uint32 handle, uint16 faultCode, char* desc)

            Parameters :    handle -
                                Handle to the device.

                            faultCode -
                                Fault code to get the description for.

                            desc -
                                Pointer to a char array where the fault description for the
                                code will be stored. The array should be at least 128 bytes
                                long.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets a fault description string for the
                            specified fault code.
                            <p>
                            Fault reports sent from the device can be fetched using
                            hqGetFaultReports.

        """
        self.TestEngineDLL.teGetFaultDesc.restype = ct.c_int32
        self.TestEngineDLL.teGetFaultDesc.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_char_p]
        local_desc = None if desc is None else ct.create_string_buffer(bytes(desc, encoding="UTF-8"), 1024)
        retval = self.TestEngineDLL.teGetFaultDesc(handle, faultCode, local_desc)
        desc = local_desc.value.decode()
        return retval, desc
    # end of teGetFaultDesc


    def bccmdSetMapScoPcm(self, handle: int, enable: int) -> int:
        r"""Function TestEngine::bccmdSetMapScoPcm() wrapper for bccmdSetMapScoPcm in TestEngine DLL.

        Python API:
            bccmdSetMapScoPcm(handle: int, enable: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSetMapScoPcm(handle=0, enable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetMapScoPcm(uint32 handle, uint8 enable)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Value to enable (1) or disable (0) SCO over PCM.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable or disable SCO over PCM. The
                            value set with this command overrides PSKEY_MAP_SCO_PCM for the
                            next SCO connection created using hciSetupScoConnection.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdSetMapScoPcm.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetMapScoPcm.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.bccmdSetMapScoPcm(handle, enable)
        
        return retval
    # end of bccmdSetMapScoPcm


    def bccmdGetVrefConstant(self, handle: int, vref: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetVrefConstant() wrapper for bccmdGetVrefConstant in TestEngine DLL.

        Python API:
            bccmdGetVrefConstant(handle: int, vref: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, vref = myDll.bccmdGetVrefConstant(handle=0)
            print(retval, vref)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetVrefConstant(uint32 handle, uint16* vref)

            Parameters :    handle -
                                Handle to the device.

                            vref -
                                Pointer to a variable to hold the returned Vref voltage
                                (millivolts).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to get the VREF constant voltage for the
                            chip. This value can be used when calculating voltages from ADC
                            values (see the help for bccmdGetVrefAdc).
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdGetVrefConstant.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetVrefConstant.argtypes = [ct.c_uint32, ct.c_void_p]
        local_vref = ct.c_uint16(vref)
        retval = self.TestEngineDLL.bccmdGetVrefConstant(handle, ct.byref(local_vref))
        vref = local_vref.value
        return retval, vref
    # end of bccmdGetVrefConstant


    def bccmdGetVrefAdc(self, handle: int, result: int=0, numBits: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdGetVrefAdc() wrapper for bccmdGetVrefAdc in TestEngine DLL.

        Python API:
            bccmdGetVrefAdc(handle: int, result: int=0, numBits: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, result, numBits = myDll.bccmdGetVrefAdc(handle=0)
            print(retval, result, numBits)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetVrefAdc(uint32 handle, uint16* result,
                                                  uint8* numBits)

            Parameters :    handle -
                                Handle to the device.

                            result -
                                Holds the result of the ADC reading. This value is from 0 to
                                ADC_MAX, where ADC_MAX = 255 or 1023 for 8 and 10 bit results
                                respectively (the numBits parameter indicates 8 or 10 bit
                                result).

                            numBits -
                                Holds the number of bits used for the result. In BlueCore
                                firmware from v24, the ADC readings have been changed to return
                                a 10 bit result (8 previously). This output parameter indicates
                                how many bits in the result are valid, 8 or 10, removing the
                                need to check the firmware version when using this function.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the vref ADC. This function supports both
                            the old ADC reading method (8 bit results) and the new (10 bit
                            results). BlueCore devices prior to BC5 have 8 bit ADCs. With
                            these devices, and where the firmware used uses the new method
                            (returns 10 bit results), the readings are shifted up by 2 bits.
                            <p>
                            The vref ADC reading can be used to calculate VDD, which can
                            then be used when calculating voltages from other ADC readings,
                            e.g. from bccmdGetAio. Calculate VDD (in millivolts) as follows:
                            <p>
                            VDD = (vref_constant * ADC_MAX) / result
                            <p>
                            The vref_constant can be found using bccmdGetVrefConstant if
                            supported. Otherwise use the fixed value 1250mV.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs.

        """
        self.TestEngineDLL.bccmdGetVrefAdc.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetVrefAdc.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        local_result = ct.c_uint16(result)
        local_numBits = ct.c_uint8(numBits)
        retval = self.TestEngineDLL.bccmdGetVrefAdc(handle, ct.byref(local_result), ct.byref(local_numBits))
        result = local_result.value
        numBits = local_numBits.value
        return retval, result, numBits
    # end of bccmdGetVrefAdc


    def bccmdBC5FMGetI2CState(self, handle: int, sda: int=0, scl: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdBC5FMGetI2CState() wrapper for bccmdBC5FMGetI2CState in TestEngine DLL.

        Python API:
            bccmdBC5FMGetI2CState(handle: int, sda: int=0, scl: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, sda, scl = myDll.bccmdBC5FMGetI2CState(handle=0)
            print(retval, sda, scl)

        Detail From Wrapped C API:
            Function :      int32 bccmdBC5FMGetI2CState(uint32 handle, uint8* sda, uint8* scl)

            Parameters :    handle -
                                Handle to the device.

                            sda -
                                Pointer to 8 bit unsigned int, used to store the state of the
                                SDA (I2C_DATA) line. The value will be either 0 (low) or
                                1 (high).

                            scl -
                                Pointer to 8 bit unsigned int, used to store the state of the
                                SCL (I2C_CLK) line. The value will be either 0 (low) or
                                1 (high).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the status of the I2C interface lines
                            on a BC5-FM BlueCore chip. It can therefore be used to test for
                            open and short circuits on the I2C interface using appropriate
                            external hardware.
                            <p>
                            The lines are pulled up, therefore with nothing connected, the
                            values of sda and scl will be 1.
                            <p>
                            This function is for use with BC5-FM only. The results of calling
                            this function with other chip types is undefined.

        """
        self.TestEngineDLL.bccmdBC5FMGetI2CState.restype = ct.c_int32
        self.TestEngineDLL.bccmdBC5FMGetI2CState.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        local_sda = ct.c_uint8(sda)
        local_scl = ct.c_uint8(scl)
        retval = self.TestEngineDLL.bccmdBC5FMGetI2CState(handle, ct.byref(local_sda), ct.byref(local_scl))
        sda = local_sda.value
        scl = local_scl.value
        return retval, sda, scl
    # end of bccmdBC5FMGetI2CState


    def refEpGetRssiDbm(self, handle: int, freqMHz: int, rssiChip: float, rssiDbm: float=0.0) -> Tuple[int, float]:
        r"""Function TestEngine::refEpGetRssiDbm() wrapper for refEpGetRssiDbm in TestEngine DLL.

        Python API:
            refEpGetRssiDbm(handle: int, freqMHz: int, rssiChip: float, rssiDbm: float=0.0) -> Tuple[int, float]

        Python Example Call Syntax:
            retval, rssiDbm = myDll.refEpGetRssiDbm(handle=0, freqMHz=0, rssiChip=0.0)
            print(retval, rssiDbm)

        Detail From Wrapped C API:
            Function :      int32 refEpGetRssiDbm(uint32 handle, uint16 freqMHz,
                                                  float64 rssiChip, float64* rssiDbm)

            Parameters :    handle -
                                Handle to the device.

                            freqMHz -
                                The frequency in MHz for which the RSSI value is required.

                            rssiChip -
                                The rssi value, returned from the chip (using hqGetRssi) to
                                be converted into an RSSI value in dBm. The value is a
                                floating point value because the values returned from the chip
                                are usually averaged (as are the calibration values of the
                                reference endpoint).

                            rssiDbm -
                                Pointer to a value where the RSSI value in dBm will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used with reference endpoint hardware to
                            convert RSSI values obtained from the chip to a dBm value, using
                            the calibration values stored in the reference endpoint.
                            <p>
                            The reference endpoint is calibrated at the following frequencies:
                            <table>
                                <tr><td>2402 MHz
                                <tr><td>2441 MHz
                                <tr><td>2480 MHz
                            </table>
                            If the freqMHz parameter value is not equal to one of these
                            frequencies, the closest of the above frequencies will be used.
                            Frequencies outside of the BlueTooth range produce result in an
                            error being returned.
                            <p>
                            If the rssiChip parameter value is outside of the range covered by
                            the reference endpoint's calibration table, an error code will be
                            returned.
                            <p>
                            Linear interpolation is performed on the calibration data when
                            calculating the rssiDbm value.
                            <p>
                            Note that if the calibration data has not been pre-loaded using
                            refEpLoadCalDataFile, the first call to this function will take a
                            few seconds to complete. This is due to reading the calibration
                            data from the device. Subsequent calls will not incur this
                            overhead.

        """
        self.TestEngineDLL.refEpGetRssiDbm.restype = ct.c_int32
        self.TestEngineDLL.refEpGetRssiDbm.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_double, ct.c_void_p]
        local_rssiDbm = ct.c_double(rssiDbm)
        retval = self.TestEngineDLL.refEpGetRssiDbm(handle, freqMHz, rssiChip, ct.byref(local_rssiDbm))
        rssiDbm = local_rssiDbm.value
        return retval, rssiDbm
    # end of refEpGetRssiDbm


    def refEpGetPaLevel(self, handle: int, freqMHz: int, targetPowerDbm: float, intPa: int=0, powerDbm: float=0.0) -> Tuple[int, int, float]:
        r"""Function TestEngine::refEpGetPaLevel() wrapper for refEpGetPaLevel in TestEngine DLL.

        Python API:
            refEpGetPaLevel(handle: int, freqMHz: int, targetPowerDbm: float, intPa: int=0, powerDbm: float=0.0) -> Tuple[int, int, float]

        Python Example Call Syntax:
            retval, intPa, powerDbm = myDll.refEpGetPaLevel(handle=0, freqMHz=0, targetPowerDbm=0.0)
            print(retval, intPa, powerDbm)

        Detail From Wrapped C API:
            Function :      int32 refEpGetPaLevel(uint32 handle, uint16 freqMHz,
                                                  float64 targetPowerDbm, uint16* intPa,
                                                  float64* powerDbm)

            Parameters :    handle -
                                Handle to the device.

                            freqMHz -
                                The frequency in MHz for which the internal PA drive level is
                                required.

                            targetPowerDbm -
                                The power in dBm for which the internal PA drive level is
                                required.

                            intPa -
                                Pointer to a value where the internal PA drive level will be
                                stored.

                            powerDbm -
                                Pointer to a value where the actual power in dBm for the
                                internal PA drive level will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used with reference endpoint hardware to
                            convert a required output power, specified in dBm, to the
                            corresponding internal PA drive level (taken from
                            the calibration values stored in the reference endpoint). The
                            intPa value is used with radiotestTx* functions.
                            <p>
                            Some TestEngine transmit functions take both internal and external
                            PA drive levels as parameters. The external PA drive level is
                            irrelevant for the reference endpoint hardware (set to zero).
                            <p>
                            The reference endpoint is calibrated at the following frequencies:
                            <table>
                                <tr><td>2402 MHz
                                <tr><td>2441 MHz
                                <tr><td>2480 MHz
                            </table>
                            If the freqMHz parameter value is not equal to one of these
                            frequencies, the closest of the above frequencies will be used.
                            Frequencies outside of the BlueTooth range produce result in an
                            error being returned.
                            <p>
                            The internal PA gain value for the power closest to the
                            targetPowerDbm parameter value will be returned, along with the
                            actual recorded power for that gain value. If the targetPowerDbm
                            parameter value is outside of the range covered by the reference
                            endpoint's calibration table, an error code will be returned.
                            <p>
                            Note that if the calibration data has not been pre-loaded using
                            refEpLoadCalDataFile, the first call to this function will take a
                            few seconds to complete. This is due to reading the calibration
                            data from the device. Subsequent calls will not incur this
                            overhead.

        """
        self.TestEngineDLL.refEpGetPaLevel.restype = ct.c_int32
        self.TestEngineDLL.refEpGetPaLevel.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_double, ct.c_void_p, ct.c_void_p]
        local_intPa = ct.c_uint16(intPa)
        local_powerDbm = ct.c_double(powerDbm)
        retval = self.TestEngineDLL.refEpGetPaLevel(handle, freqMHz, targetPowerDbm, ct.byref(local_intPa), ct.byref(local_powerDbm))
        intPa = local_intPa.value
        powerDbm = local_powerDbm.value
        return retval, intPa, powerDbm
    # end of refEpGetPaLevel


    def refEpWriteCalDataFile(self, handle: int, filePath: str) -> int:
        r"""Function TestEngine::refEpWriteCalDataFile() wrapper for refEpWriteCalDataFile in TestEngine DLL.

        Python API:
            refEpWriteCalDataFile(handle: int, filePath: str) -> int

        Python Example Call Syntax:
            retval = myDll.refEpWriteCalDataFile(handle=0, filePath='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 refEpWriteCalDataFile(uint32 handle, const char* filePath)

            Parameters :    handle -
                                Handle to the device.

                            filePath -
                                This specifies the name of the save file.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used with reference endpoint hardware to
                            save the calibration data to a file. For subsequent tests,
                            this file can be loaded using the refEpLoadCalDataFile function
                            before refEpGetPaLevel or refEpGetRssiDbm are used. This saves
                            time due to not having to read the calibration data from the
                            reference endpoint.
                            <p>
                            If filePath is NULL, or if the file specified cannot be written,
                            an error is returned. An error is also returned if the data cannot
                            be read from the reference endpoint.
                            <p>
                            If the calibration data has already been loaded, e.g. due to a
                            call to refEpGetPaLevel or refEpGetRssiDbm, this function will
                            simply write the data to the file. If the calibration data hasn't
                            been loaded, it must be read from the reference endpoint, which
                            will take a few seconds to complete.

        """
        self.TestEngineDLL.refEpWriteCalDataFile.restype = ct.c_int32
        self.TestEngineDLL.refEpWriteCalDataFile.argtypes = [ct.c_uint32, ct.c_char_p]
        local_filePath = None if filePath is None else ct.create_string_buffer(bytes(filePath, encoding="UTF-8"))
        retval = self.TestEngineDLL.refEpWriteCalDataFile(handle, local_filePath)
        
        return retval
    # end of refEpWriteCalDataFile


    def refEpLoadCalDataFile(self, handle: int, filePath: str) -> int:
        r"""Function TestEngine::refEpLoadCalDataFile() wrapper for refEpLoadCalDataFile in TestEngine DLL.

        Python API:
            refEpLoadCalDataFile(handle: int, filePath: str) -> int

        Python Example Call Syntax:
            retval = myDll.refEpLoadCalDataFile(handle=0, filePath='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 refEpLoadCalDataFile(uint32 handle, const char* filePath)

            Parameters :    handle -
                                Handle to the device.

                            filePath -
                                This specifies the name of the file containing the calibration
                                data.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function can be used to pre-load reference endpoint
                            calibration data from a file previously created using
                            refEpWriteCalDataFile. This saves time due to not having to read
                            the calibration data from the reference endpoint when
                            refEpGetPaLevel or refEpGetRssiDbm are called.
                            <p>
                            If filePath is NULL, or if the file specified cannot be read, an
                            error is returned. An error is also returned if the file is not
                            correctly formatted (i.e. if it has been changed from what was
                            written by refEpWriteCalDataFile).
                            <p>
                            If the calibration data has already been loaded, e.g. due to a
                            call to refEpGetPaLevel or refEpGetRssiDbm, this function will
                            overwrite the calibration data.

        """
        self.TestEngineDLL.refEpLoadCalDataFile.restype = ct.c_int32
        self.TestEngineDLL.refEpLoadCalDataFile.argtypes = [ct.c_uint32, ct.c_char_p]
        local_filePath = None if filePath is None else ct.create_string_buffer(bytes(filePath, encoding="UTF-8"))
        retval = self.TestEngineDLL.refEpLoadCalDataFile(handle, local_filePath)
        
        return retval
    # end of refEpLoadCalDataFile


    def bccmdGetVmStatus(self, handle: int, status: int=0, exitCode: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::bccmdGetVmStatus() wrapper for bccmdGetVmStatus in TestEngine DLL.

        Python API:
            bccmdGetVmStatus(handle: int, status: int=0, exitCode: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, status, exitCode = myDll.bccmdGetVmStatus(handle=0)
            print(retval, status, exitCode)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetVmStatus(uint32 handle, uint16* status,
                                                   uint16* exitCode)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to a value where the VM status will be stored. The
                                following status values may be returned:
                                <table>
                                    <tr><td>0 = VM_STATUS_BOOT (Not initialised yet)
                                    <tr><td>1 = VM_STATUS_FAIL (Failed to initialise)
                                    <tr><td>2 = VM_STATUS_RUN (Running)
                                    <tr><td>3 = VM_STATUS_PANIC (A panic occurred)
                                    <tr><td>4 = VM_STATUS_EXIT (Normal termination)
                                </table>

                            exitCode -
                                Pointer to a value where the VM application exit code will
                                be stored, if the application terminates normally (status
                                is VM_STATUS_EXIT).
                                <p>
                                If the application is the CVC license checker application,
                                then the exit codes are as follows:
                                <table>
                                    <tr><td>1 = CVC_PRODTEST_PASS
                                    <tr><td>2 = CVC_PRODTEST_FAIL
                                    <tr><td>3 = CVC_PRODTEST_NO_CHECK
                                    <tr><td>4 = CVC_PRODTEST_FILE_NOT_FOUND
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will read the VM status. The exit code from a VM
                            application is returned if such an application terminated
                            normally. This function can be used to perform a CVC license check.
                            <p>
                            This function is supported for BlueCore ICs only.

            Example :

                // Perform CVC license check
                static const uint16 PSKEY_INITIAL_BOOTMODE = 973;
                static const uint16 BOOT_MODE_CVC_TEST = 4;  // boot mode for CVC license key testing
                static const uint16 BOOT_MODE_NORMAL = 1;    // normal boot mode

                uint32 dutHandle = openTestEngineDebug(1, 0, DEBUG_LPTSPI);
                if (dutHandle == TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Failed to connect to device under test" << endl;
                    return;
                }

                // Set boot mode for CVC
                uint16 bootMode = BOOT_MODE_CVC_TEST;
                if (psWrite(dutHandle, PSKEY_INITIAL_BOOTMODE, PS_STORES_I, 1, &bootMode) != TE_OK)
                {
                    cout << "Failed to set boot mode" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                if (bccmdSetColdReset(dutHandle, 0) != TE_OK)
                {
                    cout << "Cold reset failed" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // CVC license key check
                uint16 status;
                uint16 exitCode;
                static const uint16 MAX_ATTEMPTS = 100; // With loop delay 100ms, gives approx 10s timeout
                uint16 attempts(0);
                do
                {
                    if (bccmdGetVmStatus(dutHandle, &status, &exitCode) != TE_OK)
                    {
                        cout << "bccmdGetVmStatus failed" << endl;
                        closeTestEngine(dutHandle);
                        return;
                    }
                    Sleep(100);
                    ++attempts;
                } while ((status == VM_STATUS_BOOT || status == VM_STATUS_RUN) && (attempts < MAX_ATTEMPTS));

                // Check returned status and exit code
                if (status == VM_STATUS_EXIT && exitCode == CVC_PRODTEST_PASS)
                {
                    cout << "CVC Production Test PASS" << endl;
                }
                else
                {
                    cout << "CVC Production Test FAIL" << endl;
                }

                // Set boot mode back to normal
                bootMode = BOOT_MODE_NORMAL;
                if (psWrite(dutHandle, PSKEY_INITIAL_BOOTMODE, PS_STORES_I, 1, &bootMode) != TE_OK)
                {
                    cout << "Failed to set boot mode" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                closeTestEngine(dutHandle);

        """
        self.TestEngineDLL.bccmdGetVmStatus.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetVmStatus.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p]
        local_status = ct.c_uint16(status)
        local_exitCode = ct.c_uint16(exitCode)
        retval = self.TestEngineDLL.bccmdGetVmStatus(handle, ct.byref(local_status), ct.byref(local_exitCode))
        status = local_status.value
        exitCode = local_exitCode.value
        return retval, status, exitCode
    # end of bccmdGetVmStatus


    def bccmdI2CTransfer(self, handle: int, slaveAddr: int, txOctets: int, rxOctets: int, restart: int, data: list, octets: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::bccmdI2CTransfer() wrapper for bccmdI2CTransfer in TestEngine DLL.

        Python API:
            bccmdI2CTransfer(handle: int, slaveAddr: int, txOctets: int, rxOctets: int, restart: int, data: list, octets: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, data, octets = myDll.bccmdI2CTransfer(handle=0, slaveAddr=0, txOctets=0, rxOctets=0, restart=0, data=[0,1])
            print(retval, data, octets)

        Detail From Wrapped C API:
            Function :      int32 bccmdI2CTransfer(uint32 handle, uint16 slaveAddr,
                                                   uint16 txOctets, uint16 rxOctets,
                                                   uint8 restart, uint8* data, uint16* octets)

            Parameters :    handle -
                                Handle to the device.

                            slaveAddr -
                                Slave address of the I2C device.

                            txOctets -
                                Number of bytes to write to the I2C device. The data array
                                should contain this many bytes.

                            rxOctets -
                                Number of bytes to read from the I2C device. The data array
                                should be large enough to hold the number of bytes specified.

                            restart -
                                Boolean value (0 = False, anything else = True). If True,
                                inserts a repeated start condition between writes and reads.
                                This should always be '1' for devices that comply with the I2C
                                specification.

                            data -
                                Pointer to an array of bytes to write, or read from memory.
                                This parameter is an input/output parameter. In the case of a
                                write operation, data should contain the bytes to write.
                                On return, data will contain the bytes which have been written.
                                In the case of a read operation, or a composite write + read
                                operation, data should be at least as large as rxOctets.
                                On return, data will contain the bytes read from the device.

                            octets -
                                Holds the value of the number of octets transferred to or from
                                the I2C device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function performs writes to and/or reads from an I2C device.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdI2CTransfer.restype = ct.c_int32
        self.TestEngineDLL.bccmdI2CTransfer.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint8, ct.c_void_p, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint8 * max(rxOctets, len(data)))(*data)
        local_octets = ct.c_uint16(octets)
        retval = self.TestEngineDLL.bccmdI2CTransfer(handle, slaveAddr, txOctets, rxOctets, restart, local_data, ct.byref(local_octets))
        data = local_data[:]
        octets = local_octets.value
        return retval, data, octets
    # end of bccmdI2CTransfer


    def radiotestBle(self, handle: int, command: int, channel: int, txLength: int, txPayload: int) -> int:
        r"""Function TestEngine::radiotestBle() wrapper for radiotestBle in TestEngine DLL.

        Python API:
            radiotestBle(handle: int, command: int, channel: int, txLength: int, txPayload: int) -> int

        Python Example Call Syntax:
            retval = myDll.radiotestBle(handle=0, command=0, channel=0, txLength=0, txPayload=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 radiotestBle(uint32 handle, uint16 command, uint8 channel,
                                               uint8 txLength, uint8 txPayload)

            Parameters :    handle -
                                Handle to the device.

                            command -
                                The BLE radio test command, where:
                                <table>
                                    <tr><td>0 = END
                                    <tr><td>1 = RECEIVER
                                    <tr><td>2 = TRANSMITTER
                                </table>

                            channel -
                                The BLE channel (0 - 39).
                                <p>
                                channel = (freqMHz \x96 2402) / 2
                                <p>
                                This parameter is relevant to the RECEIVER and TRANSMITTER
                                test commands only.

                            txLength -
                                The length in bytes (0 - 255), of the payload data in each
                                packet. The maximum supported payload length depends on the IC
                                type. If the device supports the Data Length Extensions (DLE)
                                feature, the maximum is 255, otherwise it is 37.
                                <p>
                                This parameter is relevant to the TRANSMITTER test command
                                only.

                            txPayload -
                                The transmit packet payload, where:
                                <table>
                                    <tr><td>0 = Pseudo-Random bit sequence 9
                                    <tr><td>1 = Pattern of alternating bits "11110000"
                                    <tr><td>2 = Pattern of alternating bits "10101010"
                                    <tr><td>3 = Pseudo-Random bit sequence 15
                                    <tr><td>4 = Pattern of all "1" bits
                                    <tr><td>5 = Pattern of all "0" bits
                                    <tr><td>6 = Pattern of alternating bits "00001111"
                                    <tr><td>7 = Pattern of alternating bits "01010101"
                                </table>
                                <p>
                                This parameter is relevant to the TRANSMITTER test command
                                only.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function sends Bluetooth Low Energy (BLE) radio test
                            commands to the chip.
                            <p>
                            Only one of the RECEIVER and TRANSMITTER test modes can be running
                            at any one time - an error is returned if one of these modes is
                            specified when RECEIVER / TRANSMITTER test is running. It is
                            necessary to END each mode before running another test mode (or
                            changing parameters for the same mode). Enhanced BLE tests started
                            with hciLeEnhancedReceiverTest or hciLeEnhancedTransmitterTest
                            should also be ENDed using hciLeTestEnd before running these test
                            modes.
                            <p>
                            When the END command is sent following the RECEIVER command, an HQ
                            message is sent containing the received packet count. Use
                            hqGetBleRxPktCount to retrieve the received packet count value.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs, for which the hciLe* functions can be used.

            Example :

                static const uint16 BLE_TEST_CMD_END = 0;
                static const uint16 BLE_TEST_CMD_RX = 1;
                static const uint16 BLE_TEST_CMD_TX = 2;

                static const uint8 BLE_TEST_CHANNEL = 1;
                static const uint8 BLE_TX_LENGTH = 37;
                static const uint8 BLE_TX_PAYLOAD = 0; // 0 = PRBS9

                static const uint32 RX_TEST_DURATION_MS = 1000;

                uint32 dutHandle = openTestEngineDebug(1, 0, DEBUG_LPTSPI);
                if (dutHandle == TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Failed to connect to device under test" << endl;
                    return;
                }

                // Test TX
                if (radiotestBle(dutHandle, BLE_TEST_CMD_TX, BLE_TEST_CHANNEL, BLE_TX_LENGTH, BLE_TX_PAYLOAD) != TE_OK)
                {
                    cout << "radiotestBle failed (starting TX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Perform TX measurements using test equipment here

                // End TX test
                if (radiotestBle(dutHandle, BLE_TEST_CMD_END, 0, 0, 0) != TE_OK)
                {
                    cout << "radiotestBle failed (stopping TX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Test RX

                // Switch on test equipment transmission here

                // Start receiving packets
                if (radiotestBle(dutHandle, BLE_TEST_CMD_RX, BLE_TEST_CHANNEL, 0, 0) != TE_OK)
                {
                    cout << "radiotestBle failed (starting RX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Wait for test duration
                Sleep(RX_TEST_DURATION_MS);

                // Stop receiving
                if (radiotestBle(dutHandle, BLE_TEST_CMD_END, 0, 0, 0) != TE_OK)
                {
                    cout << "radiotestBle failed (stopping RX)" << endl;
                    closeTestEngine(dutHandle);
                    return;
                }

                // Retrieve the packet count
                uint16 pktCount = 0;
                if (hqGetBleRxPktCount(dutHandle, 1000, &pktCount) != TE_OK)
                {
                    cout << "hqGetBleRxPktCount failed" << endl;
                }
                else
                {
                    cout << "Packet count = " << pktCount << endl;
                }

                closeTestEngine(dutHandle);

        """
        self.TestEngineDLL.radiotestBle.restype = ct.c_int32
        self.TestEngineDLL.radiotestBle.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.radiotestBle(handle, command, channel, txLength, txPayload)
        
        return retval
    # end of radiotestBle


    def hqGetBleRxPktCount(self, handle: int, timeout: int, pktCount: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::hqGetBleRxPktCount() wrapper for hqGetBleRxPktCount in TestEngine DLL.

        Python API:
            hqGetBleRxPktCount(handle: int, timeout: int, pktCount: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, pktCount = myDll.hqGetBleRxPktCount(handle=0, timeout=0)
            print(retval, pktCount)

        Detail From Wrapped C API:
            Function :      int32 hqGetBleRxPktCount(uint32 handle, int32 timeout,
                                                     uint16* pktCount)

            Parameters :    handle -
                                Handle to the device.

                            timeout -
                                Time in ms, for which the function will wait for a result.
                                If set to zero the function will just check for completion.

                            pktCount -
                                Pointer to a uint16 value where the number of received packets
                                will be stored.

            Returns :        <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function obtains the number of received Bluetooth Low Energy
                            (BLE) packets received during the last BLE receiver test. The
                            radiotestBle function must be called first to start the RECEIVER
                            test mode, and again to END the receiver test after the desired
                            test duration has elapsed (see radiotestBle for more details).
                            <p>
                            The pktCount value will wrap once the limit of its type (65535)
                            is reached. This can occur if the receiver test duration is
                            greater than approximately 42 seconds.
                            <p>
                            This function is unsupported for QCC304x, QCC514x and later CDA
                            ICs, for which the hciLe* functions can be used.

        """
        self.TestEngineDLL.hqGetBleRxPktCount.restype = ct.c_int32
        self.TestEngineDLL.hqGetBleRxPktCount.argtypes = [ct.c_uint32, ct.c_int32, ct.c_void_p]
        local_pktCount = ct.c_uint16(pktCount)
        retval = self.TestEngineDLL.hqGetBleRxPktCount(handle, timeout, ct.byref(local_pktCount))
        pktCount = local_pktCount.value
        return retval, pktCount
    # end of hqGetBleRxPktCount


    def bccmdGetChargerTrims(self, handle: int, chgRefTrim: int=0, hVrefTrim: int=0, rTrim: int=0, iTrim: int=0, iExtTrim: int=0, iTermTrim: int=0, vFastTrim: int=0, hystTrim: int=0) -> Tuple[int, int, int, int, int, int, int, int, int]:
        r"""Function TestEngine::bccmdGetChargerTrims() wrapper for bccmdGetChargerTrims in TestEngine DLL.

        Python API:
            bccmdGetChargerTrims(handle: int, chgRefTrim: int=0, hVrefTrim: int=0, rTrim: int=0, iTrim: int=0, iExtTrim: int=0, iTermTrim: int=0, vFastTrim: int=0, hystTrim: int=0) -> Tuple[int, int, int, int, int, int, int, int, int]

        Python Example Call Syntax:
            retval, chgRefTrim, hVrefTrim, rTrim, iTrim, iExtTrim, iTermTrim, vFastTrim, hystTrim = myDll.bccmdGetChargerTrims(handle=0)
            print(retval, chgRefTrim, hVrefTrim, rTrim, iTrim, iExtTrim, iTermTrim, vFastTrim, hystTrim)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetChargerTrims(uint32 handle, uint16* chgRefTrim,
                                                       uint16* hVrefTrim, uint16* rTrim,
                                                       uint16* iTrim, uint16* iExtTrim,
                                                       uint16* iTermTrim, uint16* vFastTrim,
                                                       uint16* hystTrim);

            Parameters :    handle -
                                Handle to the device.

                            chgRefTrim -
                                Pointer to a uint16 value where the voltage reference trim for
                                the charger will be stored.

                            hVrefTrim -
                                Pointer to a uint16 value where the voltage reference trim for
                                high voltage parts is stored.

                            rTrim -
                                Pointer to a uint16 value where the float voltage trim is
                                stored.

                            iTrim -
                                Pointer to a uint16 value where the charger current trim for
                                the internal pass transistor is stored.

                            iExtTrim -
                                Pointer to a uint16 value where the charger current trim for
                                an external pass transistor is stored.

                            iTermTrim -
                                Pointer to a uint16 value where the trim to adjust the
                                termination current is stored.

                            vFastTrim -
                                Pointer to a uint16 value where the trickle->fast charge
                                transition voltage trim is stored.

                            hystTrim -
                                Pointer to a uint16 value where the hysteresis trim for
                                standby->fast charge transition is stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function reads charger trim values stored in the flash
                            information block in some BlueCore ICs.
                            <p>
                            This function is supported for BlueCore ICs only. For other ICs
                            see teChargerGetStatus.

        """
        self.TestEngineDLL.bccmdGetChargerTrims.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetChargerTrims.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_chgRefTrim = ct.c_uint16(chgRefTrim)
        local_hVrefTrim = ct.c_uint16(hVrefTrim)
        local_rTrim = ct.c_uint16(rTrim)
        local_iTrim = ct.c_uint16(iTrim)
        local_iExtTrim = ct.c_uint16(iExtTrim)
        local_iTermTrim = ct.c_uint16(iTermTrim)
        local_vFastTrim = ct.c_uint16(vFastTrim)
        local_hystTrim = ct.c_uint16(hystTrim)
        retval = self.TestEngineDLL.bccmdGetChargerTrims(handle, ct.byref(local_chgRefTrim), ct.byref(local_hVrefTrim), ct.byref(local_rTrim), ct.byref(local_iTrim), ct.byref(local_iExtTrim), ct.byref(local_iTermTrim), ct.byref(local_vFastTrim), ct.byref(local_hystTrim))
        chgRefTrim = local_chgRefTrim.value
        hVrefTrim = local_hVrefTrim.value
        rTrim = local_rTrim.value
        iTrim = local_iTrim.value
        iExtTrim = local_iExtTrim.value
        iTermTrim = local_iTermTrim.value
        vFastTrim = local_vFastTrim.value
        hystTrim = local_hystTrim.value
        return retval, chgRefTrim, hVrefTrim, rTrim, iTrim, iExtTrim, iTermTrim, vFastTrim, hystTrim
    # end of bccmdGetChargerTrims


    def bccmdCapacitiveSensorRead(self, handle: int, mask: int, values: list) -> Tuple[int, list]:
        r"""Function TestEngine::bccmdCapacitiveSensorRead() wrapper for bccmdCapacitiveSensorRead in TestEngine DLL.

        Python API:
            bccmdCapacitiveSensorRead(handle: int, mask: int, values: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, values = myDll.bccmdCapacitiveSensorRead(handle=0, mask=0, values=[0,1])
            print(retval, values)

        Detail From Wrapped C API:
            Function :      int32 bccmdCapacitiveSensorRead(uint32 handle, uint16 mask,
                                                            uint16* values)

            Parameters :    handle -
                                Handle to the device.

                            mask -
                                The mask specifying which pads to read, where bit 0 being
                                set means pad 0 will be read.

                            values -
                                Pointer to an array of uint16 values. These are the relative
                                values of capacitance read from the pads in units of
                                approximately 1fF.
                                There must be at least enough space in the array corresponding
                                to the highest entry in the mask. For each position in the
                                mask, the corresponding array entry is populated with the
                                current value of the capacitative sense pad.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function reads the capacitance values of the specified
                            capacitative sense pads.
                            <p>
                            The capacitive touch sensors must be calibrated before use.
                            Calibration needs to be done only once for any given product
                            design (taking into account the length and location of wires
                            etc.).
                            To initiate this calibration, set PSKEY_CAP_SENSE_CALIBRATE
                            to the mask indicating which pads are to be used.
                            During boot up, if this value is non-zero, the chip will
                            calibrate the specified pads, write the calibration constants
                            to PSKEY_CAP_SENSE_PRELOAD and reset the
                            PSKEY_CAP_SENSE_CALIBRATE value to zero.
                            The psWrite / psWriteVerify and bccmdSetWarmReset functions
                            can be used to initiate calibration.
                            If required, psReadVerify can be used to check the calibration
                            constants.
                            If the PSKEY_CAP_SENSE_PRELOAD constants are incorporated
                            into the image, it is not necessary to perform calibration on
                            each and every unit.
                            <p>
                            This function is supported for BlueCore ICs only. For other IC
                            types teCapacitiveSensorRead should be used.

        """
        self.TestEngineDLL.bccmdCapacitiveSensorRead.restype = ct.c_int32
        self.TestEngineDLL.bccmdCapacitiveSensorRead.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        if values == None:
            values = []
        local_values = (ct.c_uint16 * len(values))(*values)
        retval = self.TestEngineDLL.bccmdCapacitiveSensorRead(handle, mask, local_values)
        values = local_values[:]
        return retval, values
    # end of bccmdCapacitiveSensorRead


    def bccmdSetSpiLockCustomerKey(self, handle: int, custKey: list) -> Tuple[int, list]:
        r"""Function TestEngine::bccmdSetSpiLockCustomerKey() wrapper for bccmdSetSpiLockCustomerKey in TestEngine DLL.

        Python API:
            bccmdSetSpiLockCustomerKey(handle: int, custKey: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, custKey = myDll.bccmdSetSpiLockCustomerKey(handle=0, custKey=[0,1])
            print(retval, custKey)

        Detail From Wrapped C API:
            Function :      int32 bccmdSetSpiLockCustomerKey(uint32 handle, uint32* custKey)

            Parameters :    handle -
                                Handle to the device.

                            custKey -
                                Pointer to an array of 4 uint32 values that make up the
                                128-bit customer key.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function writes the 128 bit SPI lock customer key. The
                            customer key written using this function can be used in key string
                            form with the openTestEngineDebugUnlock* functions or with the
                            TransportUnlock (formerly spiunlock) tool to unlock the SPI port
                            if the SPI port had been previously locked (see
                            bccmdSpiLockInitiateLock). Therefore, the customer key should be
                            set before the SPI port is locked. Use bccmdGetSpiLockStatus to
                            check the SPI Lock status.
                            <p>
                            The custKey array translates to key string form as follows:
                            <table>
                                <tr><td>custKey[0] = 0x01234567
                                <tr><td>custKey[1] = 0x89ABCDEF
                                <tr><td>custKey[2] = 0xFEDCBA98
                                <tr><td>custKey[3] = 0x76543210
                            </table>
                            Key string = "0123456789ABCDEFFEDCBA9876543210".
                            <p>
                            Note that the customer key can be incorporated into the firmware
                            image loaded to flash memory. In this case, it is not necessary
                            to set the key using this function.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdSetSpiLockCustomerKey.restype = ct.c_int32
        self.TestEngineDLL.bccmdSetSpiLockCustomerKey.argtypes = [ct.c_uint32, ct.c_void_p]
        if custKey == None:
            custKey = []
        local_custKey = (ct.c_uint32 * len(custKey))(*custKey)
        retval = self.TestEngineDLL.bccmdSetSpiLockCustomerKey(handle, local_custKey)
        custKey = local_custKey[:]
        return retval, custKey
    # end of bccmdSetSpiLockCustomerKey


    def bccmdGetSpiLockStatus(self, handle: int, status: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::bccmdGetSpiLockStatus() wrapper for bccmdGetSpiLockStatus in TestEngine DLL.

        Python API:
            bccmdGetSpiLockStatus(handle: int, status: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, status = myDll.bccmdGetSpiLockStatus(handle=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 bccmdGetSpiLockStatus(uint32 handle, uint16* status)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to a value where the SPI lock status of the chip will
                                be stored. The following status values may be returned:
                                <table>
                                    <tr><td>0 = SPI unlocked, customer key not set
                                    <tr><td>1 = SPI locked, customer key not set
                                    <tr><td>2 = SPI unlocked, customer key set
                                    <tr><td>3 = SPI locked, customer key set
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function reads the SPI Lock status, i.e. whether the
                            customer key is set and the SPI port is locked. If the SPI is
                            unlocked, the customer key can be set using
                            bccmdSetSpiLockCustomerKey. If the customer key is set,
                            bccmdSpiLockInitiateLock can be used to lock the SPI port.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdGetSpiLockStatus.restype = ct.c_int32
        self.TestEngineDLL.bccmdGetSpiLockStatus.argtypes = [ct.c_uint32, ct.c_void_p]
        local_status = ct.c_uint16(status)
        retval = self.TestEngineDLL.bccmdGetSpiLockStatus(handle, ct.byref(local_status))
        status = local_status.value
        return retval, status
    # end of bccmdGetSpiLockStatus


    def bccmdSpiLockInitiateLock(self, handle: int) -> int:
        r"""Function TestEngine::bccmdSpiLockInitiateLock() wrapper for bccmdSpiLockInitiateLock in TestEngine DLL.

        Python API:
            bccmdSpiLockInitiateLock(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.bccmdSpiLockInitiateLock(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 bccmdSpiLockInitiateLock(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function initiates locking of the SPI port on devices which
                            support SPI locking.
                            <p>
                            The customer key should be set before calling this function (see
                            bccmdSetSpiLockCustomerKey). If the customer key is not set, the
                            SPI lock will not be set, and an error will be returned. If the
                            SPI lock is already set, an error will be returned. Use
                            bccmdGetSpiLockStatus to check the SPI Lock status.
                            <p>
                            Once the SPI lock is set, the SPI port will be locked out at
                            boot. The spiunlock tool must then be used to unlock the SPI port
                            if necessary, using the customer key.
                            <p>
                            This function is supported for BlueCore ICs only.

        """
        self.TestEngineDLL.bccmdSpiLockInitiateLock.restype = ct.c_int32
        self.TestEngineDLL.bccmdSpiLockInitiateLock.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.bccmdSpiLockInitiateLock(handle)
        
        return retval
    # end of bccmdSpiLockInitiateLock


    def teGetChipDisplayName(self, handle: int, maxLen: int, name: str='') -> Tuple[int, str]:
        r"""Function TestEngine::teGetChipDisplayName() wrapper for teGetChipDisplayName in TestEngine DLL.

        Python API:
            teGetChipDisplayName(handle: int, maxLen: int, name: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, name = myDll.teGetChipDisplayName(handle=0, maxLen=0)
            print(retval, name)

        Detail From Wrapped C API:
            Function :      int32 teGetChipDisplayName(uint32 handle, uint32 maxLen,
                                                       char* name)

            Parameters :    handle -
                                Handle to the device.

                            maxLen -
                                The maximum number of characters which will be copied to the
                                name location.

                            name -
                                Pointer to the location where the display name will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Obtains the display name for the connected chip. The name will be
                            truncated if it is longer than maxLen.

        """
        self.TestEngineDLL.teGetChipDisplayName.restype = ct.c_int32
        self.TestEngineDLL.teGetChipDisplayName.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_char_p]
        local_name = None if name is None else ct.create_string_buffer(bytes(name, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        retval = self.TestEngineDLL.teGetChipDisplayName(handle, maxLen, local_name)
        name = local_name.value.decode()
        return retval, name
    # end of teGetChipDisplayName


    def teGetChipFamily(self, handle: int, family: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teGetChipFamily() wrapper for teGetChipFamily in TestEngine DLL.

        Python API:
            teGetChipFamily(handle: int, family: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, family = myDll.teGetChipFamily(handle=0)
            print(retval, family)

        Detail From Wrapped C API:
            Function :      int32 teGetChipFamily(uint32 handle, uint8* family)

            Parameters :    handle -
                                Handle to the device.

                            family -
                                Pointer to the location where the chip family code will be
                                stored. Possible values are:
                                <table>
                                    <tr><td>TE_CHIP_FAMILY_UNKNOWN = Unknown
                                    <tr><td>TE_CHIP_FAMILY_BLUECORE = BlueCore chip
                                    <tr><td>TE_CHIP_FAMILY_MULTI = Multi-core (CDA) chip
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Obtains the chip family code for the connected chip.

        """
        self.TestEngineDLL.teGetChipFamily.restype = ct.c_int32
        self.TestEngineDLL.teGetChipFamily.argtypes = [ct.c_uint32, ct.c_void_p]
        local_family = ct.c_uint8(family)
        retval = self.TestEngineDLL.teGetChipFamily(handle, ct.byref(local_family))
        family = local_family.value
        return retval, family
    # end of teGetChipFamily


    def teGetChipId(self, handle: int, chipId: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teGetChipId() wrapper for teGetChipId in TestEngine DLL.

        Python API:
            teGetChipId(handle: int, chipId: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, chipId = myDll.teGetChipId(handle=0)
            print(retval, chipId)

        Detail From Wrapped C API:
            Function :      int32 teGetChipId(uint32 handle, uint32* chipId)

            Parameters :    handle -
                                Handle to the device.

                            chipId -
                                Pointer to the location where the chip ID value will be
                                stored.
                                <p>
                                The chip ID is 16bits, stored in the upper 16bits of the 32bit
                                chipId value in the case of BC7 and later ICs (the lower
                                16bits being zero), and in the lower 16bits for chips prior to
                                BC7 (the upper 16bits being zero).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Obtains the chip ID value for the connected chip.

        """
        self.TestEngineDLL.teGetChipId.restype = ct.c_int32
        self.TestEngineDLL.teGetChipId.argtypes = [ct.c_uint32, ct.c_void_p]
        local_chipId = ct.c_uint32(chipId)
        retval = self.TestEngineDLL.teGetChipId(handle, ct.byref(local_chipId))
        chipId = local_chipId.value
        return retval, chipId
    # end of teGetChipId


    def teGetPtapHifs(self, length: int=0, hifIds: str='', types: str='', names: str='', count: int=0) -> Tuple[int, int, str, str, str, int]:
        r"""Function TestEngine::teGetPtapHifs() wrapper for teGetPtapHifs in TestEngine DLL.

        Python API:
            teGetPtapHifs(length: int=0, hifIds: str='', types: str='', names: str='', count: int=0) -> Tuple[int, int, str, str, str, int]

        Python Example Call Syntax:
            retval, length, hifIds, types, names, count = myDll.teGetPtapHifs()
            print(retval, length, hifIds, types, names, count)

        Detail From Wrapped C API:
            Function :      int32 teGetPtapHifs(uint16* length, char* hifIds, char* types,
                                                char* names, uint16* count)

            Parameters :    length -
                                Size of the char arrays pointed to by each of the char*
                                parameters. If this parameter indicates that any of the char
                                arrays are too small to store the complete strings, then the
                                value is set to the size required and Error is returned. If
                                any other error occurs, this value is set to zero.

                            hifIds -
                                Pointer to an array of ASCII chars where the comma-separated
                                list of host interface ids for each of the host interfaces
                                will be stored.

                            types -
                                Pointer to an array of ASCII chars where the comma-separated
                                list of types for each of the host interfaces will be stored.

                            names -
                                Pointer to an array of ASCII chars where the comma-separated
                                list of names for each of the host interfaces will be stored.

                            count -
                                This value is set to the number of host interfaces found.

            Returns :       <table>
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   This function is used to get a list of PTAP host interfaces. The
                            char array pointed to by the hifIds parameter is filled with a
                            comma-separated list of host interface ids. The char array
                            pointed to by the types parameter is filled with a comma-
                            separated list of the corresponding types. The char array pointed
                            to by the names parameter is filled with a comma-separated list
                            of the corresponding names.
                            <p>
                            If the length parameter indicates that any char array is not
                            large enough to contain the strings, Error is returned and the
                            length parameter is set to the size required for the arrays.
                            <p>
                            If any other error occurs, the length parameter is set to zero.
                            <p>
                            This function can be used by an application to get a list of host
                            interfaces with which to populate a drop down list or other means
                            of selection.
                            <p>
                            This function is applicable to CSRC9xxx ICs only.

        """
        self.TestEngineDLL.teGetPtapHifs.restype = ct.c_int32
        self.TestEngineDLL.teGetPtapHifs.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_length = ct.c_uint16(length)
        local_hifIds = None if hifIds is None else ct.create_string_buffer(bytes(hifIds, encoding="UTF-8"), 1024)
        local_types = None if types is None else ct.create_string_buffer(bytes(types, encoding="UTF-8"), 1024)
        local_names = None if names is None else ct.create_string_buffer(bytes(names, encoding="UTF-8"), 1024)
        local_count = ct.c_uint16(count)
        retval = self.TestEngineDLL.teGetPtapHifs(ct.byref(local_length), local_hifIds, local_types, local_names, ct.byref(local_count))
        length = local_length.value
        hifIds = local_hifIds.value.decode()
        types = local_types.value.decode()
        names = local_names.value.decode()
        count = local_count.value
        return retval, length, hifIds, types, names, count
    # end of teGetPtapHifs


    def teMcSetXtalFreqTrim(self, handle: int, trimVal: int, mibVal: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teMcSetXtalFreqTrim() wrapper for teMcSetXtalFreqTrim in TestEngine DLL.

        Python API:
            teMcSetXtalFreqTrim(handle: int, trimVal: int, mibVal: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, mibVal = myDll.teMcSetXtalFreqTrim(handle=0, trimVal=0)
            print(retval, mibVal)

        Detail From Wrapped C API:
            Function :      int32 teMcSetXtalFreqTrim(uint32 handle, uint16 trimVal,
                                                      int16* mibVal)

            Parameters :    handle -
                                Handle to the device.

                            trimVal -
                                Frequency trim value to write. For CSRC9xxx ICs this value is
                                a register value. For CSRA681xx and later ICs this value is
                                effectively the XtalFreqTrim MIB value, written in 2's
                                complement form (range -16 to 15).

                            mibVal -
                                The equivalent frequency trim MIB value for the given trim
                                value (output parameter).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the active crystal frequency trim value, and returns the
                            equivalent MIB value. For CSRA681xx and later ICs, this is a fine
                            frequency trim adjustment, with teMcSetXtalLoadCapacitance
                            providing a coarse trim adjustment.
                            <p>
                            This function is not supported for BlueCore ICs - use
                            radiotestCfgXtalFtrim or radiotestCalcXtalOffset instead.

        """
        self.TestEngineDLL.teMcSetXtalFreqTrim.restype = ct.c_int32
        self.TestEngineDLL.teMcSetXtalFreqTrim.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_mibVal = ct.c_int16(mibVal)
        retval = self.TestEngineDLL.teMcSetXtalFreqTrim(handle, trimVal, ct.byref(local_mibVal))
        mibVal = local_mibVal.value
        return retval, mibVal
    # end of teMcSetXtalFreqTrim


    def teMcSetXtalLoadCapacitance(self, handle: int, value: int) -> int:
        r"""Function TestEngine::teMcSetXtalLoadCapacitance() wrapper for teMcSetXtalLoadCapacitance in TestEngine DLL.

        Python API:
            teMcSetXtalLoadCapacitance(handle: int, value: int) -> int

        Python Example Call Syntax:
            retval = myDll.teMcSetXtalLoadCapacitance(handle=0, value=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teMcSetXtalLoadCapacitance(uint32 handle, uint16 value)

            Parameters :    handle -
                                Handle to the device.

                            value -
                                Xtal load capacitance value to write (active
                                XtalLoadCapacitance MIB value).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Sets the active crystal load capacitance value. For CSRA681xx and
                            later ICs, this is effectively a coarse frequency trim adjustment,
                            with teMcSetXtalFreqTrim providing a fine trim adjustment.
                            <p>
                            This function is not supported for BlueCore and CSRC9xxx ICs.

        """
        self.TestEngineDLL.teMcSetXtalLoadCapacitance.restype = ct.c_int32
        self.TestEngineDLL.teMcSetXtalLoadCapacitance.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teMcSetXtalLoadCapacitance(handle, value)
        
        return retval
    # end of teMcSetXtalLoadCapacitance


    def teGetBuildId(self, handle: int, subsystem: int, buildId: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teGetBuildId() wrapper for teGetBuildId in TestEngine DLL.

        Python API:
            teGetBuildId(handle: int, subsystem: int, buildId: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, buildId = myDll.teGetBuildId(handle=0, subsystem=0)
            print(retval, buildId)

        Detail From Wrapped C API:
            Function :      int32 teGetBuildId(uint32 handle, uint8 subsystem,
                                               uint16* buildId)

            Parameters :    handle -
                                Handle to the device.

                            subsystem -
                                Subsystem ID, where:
                                <table>
                                    <tr><td>TE_SUBSYSTEM_BT = Bluetooth
                                    <tr><td>TE_SUBSYSTEM_AUDIO = Audio
                                    <tr><td>TE_SUBSYSTEM_APPS0 = Application 0
                                    <tr><td>TE_SUBSYSTEM_APPS1 = Application 1
                                </table>

                            buildId -
                                Pointer to a variable to hold the returned firmware build ID.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will retrieve the firmware build ID for a
                            given subsystem.
                            <p>
                            This function is not supported for BlueCore ICs, for which
                            bccmdGetBuildId should be used.

        """
        self.TestEngineDLL.teGetBuildId.restype = ct.c_int32
        self.TestEngineDLL.teGetBuildId.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_void_p]
        local_buildId = ct.c_uint32(buildId)
        retval = self.TestEngineDLL.teGetBuildId(handle, subsystem, ct.byref(local_buildId))
        buildId = local_buildId.value
        return retval, buildId
    # end of teGetBuildId


    def tePioMap(self, handle: int, bank: int, mask: int, pios: int, errLines: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::tePioMap() wrapper for tePioMap in TestEngine DLL.

        Python API:
            tePioMap(handle: int, bank: int, mask: int, pios: int, errLines: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, errLines = myDll.tePioMap(handle=0, bank=0, mask=0, pios=0)
            print(retval, errLines)

        Detail From Wrapped C API:
            Function :      int32 tePioMap(uint32 handle, uint16 bank, uint32 mask,
                                           uint32 pios, uint32* errLines)

            Parameters :    handle -
                                Handle to the device.

                            bank -
                                PIO bank.

                            mask -
                                Bit mask of the mappable pins.

                            pios -
                                Bit field, where a bit being set (1) means that that pin should
                                be configured as a PIO. A bit being cleared (0) means that the
                                pin will be configured for its alternative use.

                            errLines -
                                Pointer to a uint32 bit field indicating which of the specified
                                pins could not be mapped as PIOs.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will map the pins specified by the bank and mask
                            according to the usage specified in the pios parameter. Reports
                            any pins which could not be mapped.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            relevant bccmd* PIO functions should be used.

        """
        self.TestEngineDLL.tePioMap.restype = ct.c_int32
        self.TestEngineDLL.tePioMap.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint32, ct.c_uint32, ct.c_void_p]
        local_errLines = ct.c_uint32(errLines)
        retval = self.TestEngineDLL.tePioMap(handle, bank, mask, pios, ct.byref(local_errLines))
        errLines = local_errLines.value
        return retval, errLines
    # end of tePioMap


    def tePioSet(self, handle: int, bank: int, mask: int, direction: int, value: int, errLines: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::tePioSet() wrapper for tePioSet in TestEngine DLL.

        Python API:
            tePioSet(handle: int, bank: int, mask: int, direction: int, value: int, errLines: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, errLines = myDll.tePioSet(handle=0, bank=0, mask=0, direction=0, value=0)
            print(retval, errLines)

        Detail From Wrapped C API:
            Function :      int32 tePioSet(uint32 handle, uint16 bank, uint32 mask,
                                           uint32 direction, uint32 value, uint32* errLines)

            Parameters :    handle -
                                Handle to the device.

                            bank -
                                PIO bank.

                            mask -
                                Bit mask of the PIOs to be set.

                            direction -
                                Bit field which sets the PIOs as input (0) or output (1).

                            value -
                                Bit field, where a bit being set (1) means that that pin should
                                be set high. A bit being cleared (0) means that the pin will be
                                set low.

                            errLines -
                                Pointer to a uint32 bit field indicating which of the specified
                                pins could not be set.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will set the state for the specified PIOs.
                            <p>
                            If the PIOs to be used include lines which default to alternative
                            uses, it is necessary to call tePioMap first to map the lines as
                            PIOs.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            relevant bccmd* PIO functions should be used.

            Example :

                uint16 pioBank = 2;              // The PIO bank we want to use
                uint32 mapMask = 0x00000400;     // The line(s) we want to map as PIOs
                uint32 pioMask = 0x00000400;     // The line(s) we want to set
                uint32 direction = 0x00000400;   // Direction - (0) as input (1) as output
                uint32 value = 0x00000400;       // State of the lines to set (applies to output lines only)
                uint32 errLines;

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Map lines as PIOs
                    int32 teRet = tePioMap(teHandle, pioBank, mapMask, pioMask, &errLines);

                    if (teRet != TE_OK)
                    {
                        // Checks if any lines could not be mapped as PIOs
                        if (errLines != 0)
                        {
                            cout << "ERROR: Lines that could not be mapped as PIOs = "
                                 << hex << "0x" << errLines << endl;
                        }
                    }
                    else
                    {
                        // Set the direction and value of the PIO lines.
                        teRet = tePioSet(teHandle, pioBank, pioMask, direction, value, &errLines);

                        // Checks if any lines could not be set
                        if (teRet != TE_OK)
                        {
                            if (errLines != 0)
                            {
                                cout << "ERROR: Lines that could not be set = "
                                     << hex << "0x" << errLines << endl;
                            }
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.tePioSet.restype = ct.c_int32
        self.TestEngineDLL.tePioSet.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint32, ct.c_uint32, ct.c_uint32, ct.c_void_p]
        local_errLines = ct.c_uint32(errLines)
        retval = self.TestEngineDLL.tePioSet(handle, bank, mask, direction, value, ct.byref(local_errLines))
        errLines = local_errLines.value
        return retval, errLines
    # end of tePioSet


    def tePioGet(self, handle: int, bank: int, direction: int=0, value: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::tePioGet() wrapper for tePioGet in TestEngine DLL.

        Python API:
            tePioGet(handle: int, bank: int, direction: int=0, value: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, direction, value = myDll.tePioGet(handle=0, bank=0)
            print(retval, direction, value)

        Detail From Wrapped C API:
            Function :      int32 tePioGet(uint32 handle, uint16 bank, uint32* direction,
                                           uint32* value)

            Parameters :    handle -
                                Handle to the device.

                            bank -
                                PIO bank.

                            direction -
                                Pointer to uint32 value which stores the direction of the
                                PIO port lines as a bit field, where a 1 indicates that the
                                PIO is an output, and a 0 means that the PIO is an input.

                            value -
                                Pointer to uint32 value which stores the values of the PIO lines
                                as a bit field.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets the direction and state of the PIO lines.
                            <p>
                            If the PIOs to be read include lines which default to alternative
                            uses, it is necessary to call tePioMap first to map the lines
                            as PIOs.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            relevant bccmd* PIO functions should be used.

            Example :

                uint16 pioBank = 2; // The PIO bank we want to use

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Get the direction and value of the PIO lines.
                    uint32 direction;
                    uint32 value;
                    int32 teRet = tePioGet(teHandle, pioBank, &direction, &value);
                    if (teRet == TE_OK)
                    {
                        cout << "Direction = " << hex << "0x" << direction << endl;
                        cout << "Value = " << hex << "0x" << value << endl;
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.tePioGet.restype = ct.c_int32
        self.TestEngineDLL.tePioGet.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        local_direction = ct.c_uint32(direction)
        local_value = ct.c_uint32(value)
        retval = self.TestEngineDLL.tePioGet(handle, bank, ct.byref(local_direction), ct.byref(local_value))
        direction = local_direction.value
        value = local_value.value
        return retval, direction, value
    # end of tePioGet


    def teAudioGetSource(self, handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teAudioGetSource() wrapper for teAudioGetSource in TestEngine DLL.

        Python API:
            teAudioGetSource(handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, sid = myDll.teAudioGetSource(handle=0, device=0, iface=0, channel=0)
            print(retval, sid)

        Detail From Wrapped C API:
            Function :      int32 teAudioGetSource(uint32 handle, uint16 device,
                                                   uint16 iface, uint16 channel,
                                                   uint16* sid)

            Parameters :    handle -
                                Handle to the device.

                            device -
                                The stream device identifier, e.g.:
                                <table>
                                    <tr><td>1 = PCM
                                    <tr><td>2 = I2S
                                    <tr><td>3 = CODEC
                                    <tr><td>5 = SPDIF
                                    <tr><td>6 = DIGITAL_MIC
                                </table>
                                <p>
                                See device audio library file stream_if.h for other
                                stream_device identifiers.

                            iface -
                                The instance of the specified device, e.g. 0, 1, etc.

                            channel -
                                Channel / timeslot selection.
                                <p>
                                For CODEC and DIGITAL_MIC devices, the channel, where:
                                <table>
                                    <tr><td>0 = Channel A (Left)
                                    <tr><td>1 = Channel B (Right)
                                    <tr><td>2 = Channels A and B (Left and right)
                                </table>
                                <p>
                                If a single channel is selected, the other channel will be
                                muted.
                                <p>
                                For PCM, I2S, and SPDIF devices, the timeslot to use (0 or 1,
                                except for PCM, where 0 - 3 can be specified).

                            sid -
                                Pointer to where the source ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to get the ID for an audio stream endpoint
                            source device. This sid can be used when configuring audio
                            configuration parameters using teAudioConfigure.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported parameter values, please see the
                            Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the StreamAudioSource
                            function).

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioGetSource.restype = ct.c_int32
        self.TestEngineDLL.teAudioGetSource.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_sid = ct.c_uint16(sid)
        retval = self.TestEngineDLL.teAudioGetSource(handle, device, iface, channel, ct.byref(local_sid))
        sid = local_sid.value
        return retval, sid
    # end of teAudioGetSource


    def teAudioCloseSource(self, handle: int, sid: int) -> int:
        r"""Function TestEngine::teAudioCloseSource() wrapper for teAudioCloseSource in TestEngine DLL.

        Python API:
            teAudioCloseSource(handle: int, sid: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioCloseSource(handle=0, sid=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioCloseSource(uint32 handle, uint16 sid)

            Parameters :    handle -
                                Handle to the device.

                            sid -
                                Source ID obtained using teAudioGetSource.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to close the connection with an audio
                            stream source obtained using teAudioGetSource.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioCloseSource.restype = ct.c_int32
        self.TestEngineDLL.teAudioCloseSource.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAudioCloseSource(handle, sid)
        
        return retval
    # end of teAudioCloseSource


    def teAudioGetSink(self, handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teAudioGetSink() wrapper for teAudioGetSink in TestEngine DLL.

        Python API:
            teAudioGetSink(handle: int, device: int, iface: int, channel: int, sid: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, sid = myDll.teAudioGetSink(handle=0, device=0, iface=0, channel=0)
            print(retval, sid)

        Detail From Wrapped C API:
            Function :      int32 teAudioGetSink(uint32 handle, uint16 device, uint16 iface,
                                                 uint16 channel, uint16* sid)

            Parameters :    handle -
                                Handle to the device.

                            device -
                                The stream device identifier, e.g.:
                                <table>
                                    <tr><td>1 = PCM
                                    <tr><td>2 = I2S
                                    <tr><td>3 = CODEC
                                    <tr><td>5 = SPDIF
                                    <tr><td>6 = DIGITAL_MIC
                                </table>
                                <p>
                                See device audio library file stream_if.h for other
                                stream_device identifiers.

                            iface -
                                The hardware interface instance, e.g. 0, 1, etc.

                            channel -
                                Channel / timeslot selection.
                                <p>
                                For CODEC and DIGITAL_MIC devices, the channel, where:
                                <table>
                                    <tr><td>0 = Channel A (Left)
                                    <tr><td>1 = Channel B (Right)
                                    <tr><td>2 = Channels A and B (Left and right)
                                </table>
                                <p>
                                If a single channel is selected, the other channel will be
                                muted.
                                <p>
                                For PCM, I2S, and SPDIF devices, the timeslot to use (0 or 1,
                                except for PCM, where 0 - 3 can be specified).

                            sid -
                                Pointer to where the sink ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to get the ID for an audio stream endpoint
                            sink device. This sid can be used when configuring audio
                            configuration parameters using teAudioConfigure.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported parameter values, please see the
                            Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the StreamAudioSink
                            function).

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioGetSink.restype = ct.c_int32
        self.TestEngineDLL.teAudioGetSink.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_sid = ct.c_uint16(sid)
        retval = self.TestEngineDLL.teAudioGetSink(handle, device, iface, channel, ct.byref(local_sid))
        sid = local_sid.value
        return retval, sid
    # end of teAudioGetSink


    def teAudioCloseSink(self, handle: int, sid: int) -> int:
        r"""Function TestEngine::teAudioCloseSink() wrapper for teAudioCloseSink in TestEngine DLL.

        Python API:
            teAudioCloseSink(handle: int, sid: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioCloseSink(handle=0, sid=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioCloseSink(uint32 handle, uint16 sid)

            Parameters :    handle -
                                Handle to the device.

                            sid -
                                Sink ID obtained using teAudioGetSink.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to close the connection with an audio
                            stream sink obtained using teAudioGetSink.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioCloseSink.restype = ct.c_int32
        self.TestEngineDLL.teAudioCloseSink.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAudioCloseSink(handle, sid)
        
        return retval
    # end of teAudioCloseSink


    def teAudioConnect(self, handle: int, sourceId: int, sinkId: int, tid: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teAudioConnect() wrapper for teAudioConnect in TestEngine DLL.

        Python API:
            teAudioConnect(handle: int, sourceId: int, sinkId: int, tid: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, tid = myDll.teAudioConnect(handle=0, sourceId=0, sinkId=0)
            print(retval, tid)

        Detail From Wrapped C API:
            Function :      int32 teAudioConnect(uint32 handle, uint16 sourceId,
                                                 uint16 sinkId, uint16* tid)

            Parameters :    handle -
                                Handle to the device.

                            sourceId -
                                The source stream device identifier obtained using
                                teAudioGetSource.

                            sinkId -
                                The sink stream device identifier obtained using
                                teAudioGetSink.

                            tid -
                                Pointer to where the transform ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to connect a source audio stream device to
                            a sink device. This tid can be used to disconnect the streams
                            using teAudioDisconnect.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:

                // Example: Stereo loopback

                static const uint16 CODEC_DEVICE = 3;
                static const uint16 AUDIO_INTERFACE = 1;

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Get sources and sinks for stereo loopback operation
                    uint16 sourceId0;
                    uint16 sourceId1;
                    uint16 sinkId0;
                    uint16 sinkId1;
                    int32 teRet = teAudioGetSource(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 0, &sourceId0);
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSource(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 1, &sourceId1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSink(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 0, &sinkId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSink(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 1, &sinkId1);
                    }

                    // Enable mic bias
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioMicBiasConfigure(teHandle, 0, 0, 1);
                    }

                    // Connect the source and sink for each channel
                    uint16 transformId0;
                    uint16 transformId1;
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConnect(teHandle, sourceId0, sinkId0, &transformId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConnect(teHandle, sourceId1, sinkId1, &transformId1);
                    }

                    // Audio loopback established - perform checks / measurements here

                    // Disconnect the audio streams
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioDisconnect(teHandle, transformId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioDisconnect(teHandle, transformId1);
                    }

                    // Close the sources and sinks
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSource(teHandle, sourceId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSource(teHandle, sourceId1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSink(teHandle, sinkId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSink(teHandle, sinkId1);
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teAudioConnect.restype = ct.c_int32
        self.TestEngineDLL.teAudioConnect.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_tid = ct.c_uint16(tid)
        retval = self.TestEngineDLL.teAudioConnect(handle, sourceId, sinkId, ct.byref(local_tid))
        tid = local_tid.value
        return retval, tid
    # end of teAudioConnect


    def teAudioDisconnect(self, handle: int, tid: int) -> int:
        r"""Function TestEngine::teAudioDisconnect() wrapper for teAudioDisconnect in TestEngine DLL.

        Python API:
            teAudioDisconnect(handle: int, tid: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioDisconnect(handle=0, tid=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioDisconnect(uint32 handle, uint16 tid)

            Parameters :    handle -
                                Handle to the device.

                            tid -
                                Transform ID obtained using teAudioConnect.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to disconnect audio streams connected
                            using teAudioConnect.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioDisconnect.restype = ct.c_int32
        self.TestEngineDLL.teAudioDisconnect.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAudioDisconnect(handle, tid)
        
        return retval
    # end of teAudioDisconnect


    def teAudioConfigure(self, handle: int, sid: int, key: int, value: int) -> int:
        r"""Function TestEngine::teAudioConfigure() wrapper for teAudioConfigure in TestEngine DLL.

        Python API:
            teAudioConfigure(handle: int, sid: int, key: int, value: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioConfigure(handle=0, sid=0, key=0, value=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioConfigure(uint32 handle, uint16 sid, uint16 key,
                                                   uint32 value)

            Parameters :    handle -
                                Handle to the device.

                            sid -
                                The source or sink stream device identifier obtained using
                                teAudioGetSource or teAudioGetSink.

                            key -
                                Audio configuration key to set.

                            value -
                                The value to set for the audio configuration key.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set an audio configuration key value
                            for a given audio source / sink.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported configuration keys, please see
                            the Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the Source/SinkConfigure
                            functions).

            Example:        See example code for teAudioStartOperators.

        """
        self.TestEngineDLL.teAudioConfigure.restype = ct.c_int32
        self.TestEngineDLL.teAudioConfigure.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.teAudioConfigure(handle, sid, key, value)
        
        return retval
    # end of teAudioConfigure


    def teAudioCreateOperator(self, handle: int, capabilityId: int, operatorId: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teAudioCreateOperator() wrapper for teAudioCreateOperator in TestEngine DLL.

        Python API:
            teAudioCreateOperator(handle: int, capabilityId: int, operatorId: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, operatorId = myDll.teAudioCreateOperator(handle=0, capabilityId=0)
            print(retval, operatorId)

        Detail From Wrapped C API:
            Function :      int32 teAudioCreateOperator(uint32 handle, uint16 capabilityId,
                                                        uint16* operatorId)

            Parameters :    handle -
                                Handle to the device.

                            capabilityId -
                                The capability identifier for which to create an operator.

                            operatorId -
                                Pointer to where the operator ID will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to create an audio operator for a given
                            audio capability.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported capabilities, please see the
                            Kymera Capability Library User Guide documentation relevant to the
                            ADK used to build the IC application firmware (see Capability
                            Identifiers).

            Example:        See example code for teAudioStartOperators.

        """
        self.TestEngineDLL.teAudioCreateOperator.restype = ct.c_int32
        self.TestEngineDLL.teAudioCreateOperator.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_operatorId = ct.c_uint16(operatorId)
        retval = self.TestEngineDLL.teAudioCreateOperator(handle, capabilityId, ct.byref(local_operatorId))
        operatorId = local_operatorId.value
        return retval, operatorId
    # end of teAudioCreateOperator


    def teAudioDestroyOperators(self, handle: int, operators: list, count: int) -> int:
        r"""Function TestEngine::teAudioDestroyOperators() wrapper for teAudioDestroyOperators in TestEngine DLL.

        Python API:
            teAudioDestroyOperators(handle: int, operators: list, count: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioDestroyOperators(handle=0, operators=[0,1], count=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioDestroyOperators(uint32 handle,
                                                          const uint16* operators,
                                                          uint16 count)

            Parameters :    handle -
                                Handle to the device.

                            operators -
                                Array of operator IDs.

                            count -
                                Number of operator IDs, i.e. the size of the operators array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to destroy operators created using
                            teAudioCreateOperator.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioStartOperators.

        """
        self.TestEngineDLL.teAudioDestroyOperators.restype = ct.c_int32
        self.TestEngineDLL.teAudioDestroyOperators.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        if operators == None:
            operators = []
        local_operators = (ct.c_uint16 * len(operators))(*operators)
        retval = self.TestEngineDLL.teAudioDestroyOperators(handle, local_operators, count)
        
        return retval
    # end of teAudioDestroyOperators


    def teAudioOperatorMessage(self, handle: int, operatorId: int, message: list, messageLength: int) -> int:
        r"""Function TestEngine::teAudioOperatorMessage() wrapper for teAudioOperatorMessage in TestEngine DLL.

        Python API:
            teAudioOperatorMessage(handle: int, operatorId: int, message: list, messageLength: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioOperatorMessage(handle=0, operatorId=0, message=[0,1], messageLength=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioOperatorMessage(uint32 handle, uint16 operatorId,
                                                         const uint16* message,
                                                         uint16 messageLength)

            Parameters :    handle -
                                Handle to the device.

                            operatorId -
                                Operator ID.

                            message -
                                Array of uint16 values forming the operator message.

                            messageLength -
                                Length of the message array (number of uint16s).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to send a message to an operator created
                            using teAudioCreateOperator.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported operator messages, please see the
                            Kymera Capability Library User Guide documentation relevant to the
                            ADK used to build the IC application firmware (see Operator
                            Messages).

            Example:        See example code for teAudioStartOperators.

        """
        self.TestEngineDLL.teAudioOperatorMessage.restype = ct.c_int32
        self.TestEngineDLL.teAudioOperatorMessage.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_uint16]
        if message == None:
            message = []
        local_message = (ct.c_uint16 * len(message))(*message)
        retval = self.TestEngineDLL.teAudioOperatorMessage(handle, operatorId, local_message, messageLength)
        
        return retval
    # end of teAudioOperatorMessage


    def teAudioResetOperators(self, handle: int, operators: list, count: int) -> int:
        r"""Function TestEngine::teAudioResetOperators() wrapper for teAudioResetOperators in TestEngine DLL.

        Python API:
            teAudioResetOperators(handle: int, operators: list, count: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioResetOperators(handle=0, operators=[0,1], count=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioResetOperators(uint32 handle,
                                                        const uint16* operators,
                                                        uint16 count)

            Parameters :    handle -
                                Handle to the device.

                            operators -
                                Array of operator IDs.

                            count -
                                Number of operator IDs, i.e. the size of the operators array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to reset operators created using
                            teAudioCreateOperator.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

        """
        self.TestEngineDLL.teAudioResetOperators.restype = ct.c_int32
        self.TestEngineDLL.teAudioResetOperators.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        if operators == None:
            operators = []
        local_operators = (ct.c_uint16 * len(operators))(*operators)
        retval = self.TestEngineDLL.teAudioResetOperators(handle, local_operators, count)
        
        return retval
    # end of teAudioResetOperators


    def teAudioStartOperators(self, handle: int, operators: list, count: int) -> int:
        r"""Function TestEngine::teAudioStartOperators() wrapper for teAudioStartOperators in TestEngine DLL.

        Python API:
            teAudioStartOperators(handle: int, operators: list, count: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioStartOperators(handle=0, operators=[0,1], count=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioStartOperators(uint32 handle,
                                                        const uint16* operators,
                                                        uint16 count)

            Parameters :    handle -
                                Handle to the device.

                            operators -
                                Array of operator IDs.

                            count -
                                Number of operator IDs, i.e. the size of the operators array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to start operators created using
                            teAudioCreateOperator.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:

                // Example: Play tone through codec

                static const uint16 CODEC_DEVICE = 3;
                static const uint16 AUDIO_INTERFACE = 1;
                static const uint16 AUDIO_CHANNEL = 2; // L & R
                static const uint16 RINGTONE_GENERATOR_CAPABILITY = 0x37;
                static const uint16 STREAM_CODEC_OUTPUT_RATE_KEYID = 0x301;
                static const uint16 STREAM_CODEC_OUTPUT_RATE = 8000;
                static const uint16 TONE_DURATION_MS = 1000;

                // Message corresponds to:
                // RINGTONE_DECAY(0),
                // RINGTONE_TIMBRE(sine),
                // RINGTONE_TEMPO(0xFF),
                // RINGTONE_NOTE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_NOTE_TIE(C5, SEMIBREVE),
                // RINGTONE_END
                //
                // It gives a tone approx. 6 seconds in duration (i.e. max duration would be approx. 6 seconds)
                static const uint16 RINGTONE_MESSAGE[] = { 0x1, 0xC000, 0xB000, 0x90FF, 0x1E01, 0x5E01, 0x5E01, 0x5E01, 0x5E01, 0x5E01, 0x5E01, 0x8000 };

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Get sink (output endpoint)
                    uint16 sinkId;
                    int32 teRet = teAudioGetSink(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, AUDIO_CHANNEL, &sinkId);

                    // Configure the output sample rate
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sinkId, STREAM_CODEC_OUTPUT_RATE_KEYID, STREAM_CODEC_OUTPUT_RATE);
                    }

                    // Create an operator
                    uint16 operatorId;
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCreateOperator(teHandle, RINGTONE_GENERATOR_CAPABILITY, &operatorId);
                    }

                    // Message the operator with ringtone elements
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioOperatorMessage(teHandle, operatorId, RINGTONE_MESSAGE, (sizeof(RINGTONE_MESSAGE) / sizeof(uint16)));
                    }

                    // Connect the source to the sink
                    uint16 transformId;
                    if (teRet == TE_OK)
                    {
                        // Need to get the source ID from the operator ID:
                        //     sourceId = opId + operator_connection_number + 0x2000
                        // The ringtone generator capability only has one output connection, so operator_connection_number = 0.
                        uint16 sourceId = operatorId + 0 + 0x2000;
                        teRet = teAudioConnect(teHandle, sourceId, sinkId, &transformId);
                    }

                    // Start the operator (starts tone)
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioStartOperators(teHandle, &operatorId, 1);
                    }

                    // Tone now playing

                    // Play for intended duration
                    Sleep(TONE_DURATION_MS);

                    // Stop the operator (stops tone)
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioStopOperators(teHandle, &operatorId, 1);
                    }

                    // Disconnect the audio streams
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioDisconnect(teHandle, transformId);
                    }

                    // Destroy the operator
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioDestroyOperators(teHandle, &operatorId, 1);
                    }

                    // Close the sink
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSink(teHandle, sinkId);
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teAudioStartOperators.restype = ct.c_int32
        self.TestEngineDLL.teAudioStartOperators.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        if operators == None:
            operators = []
        local_operators = (ct.c_uint16 * len(operators))(*operators)
        retval = self.TestEngineDLL.teAudioStartOperators(handle, local_operators, count)
        
        return retval
    # end of teAudioStartOperators


    def teAudioStopOperators(self, handle: int, operators: list, count: int) -> int:
        r"""Function TestEngine::teAudioStopOperators() wrapper for teAudioStopOperators in TestEngine DLL.

        Python API:
            teAudioStopOperators(handle: int, operators: list, count: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioStopOperators(handle=0, operators=[0,1], count=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioStopOperators(uint32 handle, const uint16* operators,
                                                       uint16 count)

            Parameters :    handle -
                                Handle to the device.

                            operators -
                                Array of operator IDs.

                            count -
                                Number of operator IDs, i.e. the size of the operators array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to stop operators started using
                            teAudioStartOperators.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioStartOperators.

        """
        self.TestEngineDLL.teAudioStopOperators.restype = ct.c_int32
        self.TestEngineDLL.teAudioStopOperators.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint16]
        if operators == None:
            operators = []
        local_operators = (ct.c_uint16 * len(operators))(*operators)
        retval = self.TestEngineDLL.teAudioStopOperators(handle, local_operators, count)
        
        return retval
    # end of teAudioStopOperators


    def teAudioSetAncIirFilter(self, handle: int, ancInstance: int, pathId: int, coefficients: list, numCoeffs: int) -> int:
        r"""Function TestEngine::teAudioSetAncIirFilter() wrapper for teAudioSetAncIirFilter in TestEngine DLL.

        Python API:
            teAudioSetAncIirFilter(handle: int, ancInstance: int, pathId: int, coefficients: list, numCoeffs: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioSetAncIirFilter(handle=0, ancInstance=0, pathId=0, coefficients=[0,1], numCoeffs=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioSetAncIirFilter(uint32 handle, uint16 ancInstance,
                                                         uint16 pathId,
                                                         const uint16* coefficients,
                                                         uint16 numCoeffs)

            Parameters :    handle -
                                Handle to the device.

                            ancInstance -
                                ANC channel instance.

                            pathId -
                                ID of the ANC path (and therefore the IIR filter instance to
                                configure).

                            coefficients -
                                Array of filter coefficients.

                            numCoeffs -
                                Number of coefficients supplied.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to configure an ANC IIR filter.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported parameter values, please see the
                            Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the AudioAncFilterIirSet
                            function).

            Example:        See example code for teAudioStreamAncEnable.

        """
        self.TestEngineDLL.teAudioSetAncIirFilter.restype = ct.c_int32
        self.TestEngineDLL.teAudioSetAncIirFilter.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_void_p, ct.c_uint16]
        if coefficients == None:
            coefficients = []
        local_coefficients = (ct.c_uint16 * len(coefficients))(*coefficients)
        retval = self.TestEngineDLL.teAudioSetAncIirFilter(handle, ancInstance, pathId, local_coefficients, numCoeffs)
        
        return retval
    # end of teAudioSetAncIirFilter


    def teAudioSetAncLpfFilter(self, handle: int, ancInstance: int, pathId: int, shift1: int, shift2: int) -> int:
        r"""Function TestEngine::teAudioSetAncLpfFilter() wrapper for teAudioSetAncLpfFilter in TestEngine DLL.

        Python API:
            teAudioSetAncLpfFilter(handle: int, ancInstance: int, pathId: int, shift1: int, shift2: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioSetAncLpfFilter(handle=0, ancInstance=0, pathId=0, shift1=0, shift2=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioSetAncLpfFilter(uint32 handle, uint16 ancInstance,
                                                         uint16 pathId, uint16 shift1,
                                                         uint16 shift2)

            Parameters :    handle -
                                Handle to the device.

                            ancInstance -
                                ANC channel instance.

                            pathId -
                                ID of the ANC path (and therefore the LPF filter instance to
                                configure).

                            shift1 -
                                Used to derive the first LPF coefficient.

                            shift2 -
                                Used to derive the second LPF coefficient.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to configure an ANC LPF filter.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported parameter values, please see the
                            Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the AudioAncFilterLpfSet
                            function).

            Example:        See example code for teAudioStreamAncEnable.

        """
        self.TestEngineDLL.teAudioSetAncLpfFilter.restype = ct.c_int32
        self.TestEngineDLL.teAudioSetAncLpfFilter.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAudioSetAncLpfFilter(handle, ancInstance, pathId, shift1, shift2)
        
        return retval
    # end of teAudioSetAncLpfFilter


    def teAudioStreamAncEnable(self, handle: int, anc0: int, anc1: int) -> int:
        r"""Function TestEngine::teAudioStreamAncEnable() wrapper for teAudioStreamAncEnable in TestEngine DLL.

        Python API:
            teAudioStreamAncEnable(handle: int, anc0: int, anc1: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioStreamAncEnable(handle=0, anc0=0, anc1=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioStreamAncEnable(uint32 handle, uint16 anc0,
                                                         uint16 anc1)

            Parameters :    handle -
                                Handle to the device.

                            anc0 -
                                Bit field that enables the ANC input and output paths of the
                                ANC0 instance.

                            anc1 -
                                Bit field that enables the ANC input and output paths of the
                                ANC1 instance.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable or disable ANC.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.
                            <p>
                            For further details of supported parameter values, please see the
                            Audio API reference documentation relevant to the ADK used to
                            build the IC application firmware (see the AudioAncStreamEnable
                            function).

            Example:

                // Example: Use of ANC audio functions

                static const uint16 CODEC_DEVICE = 3;
                static const uint16 AUDIO_INTERFACE = 0;
                static const uint16 STREAM_CODEC_INPUT_RATE_KEYID = 0x300;
                static const uint16 STREAM_CODEC_OUTPUT_RATE_KEYID = 0x301;
                static const uint16 STREAM_ANC_INSTANCE_KEYID = 0x1100;
                static const uint16 STREAM_ANC_INPUT_KEYID = 0x1101;
                static const uint16 STREAM_CODEC_SAMPLE_RATE = 48000;

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Get sources and sinks
                    uint16 sourceId0;
                    uint16 sourceId1;
                    uint16 sinkId0;
                    uint16 sinkId1;
                    int32 teRet = teAudioGetSource(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 0, &sourceId0);
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSource(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 1, &sourceId1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSink(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 0, &sinkId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioGetSink(teHandle, CODEC_DEVICE, AUDIO_INTERFACE, 1, &sinkId1);
                    }

                    // Configure the sample rates
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId0, STREAM_CODEC_INPUT_RATE_KEYID, STREAM_CODEC_SAMPLE_RATE);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId1, STREAM_CODEC_INPUT_RATE_KEYID, STREAM_CODEC_SAMPLE_RATE);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sinkId0, STREAM_CODEC_OUTPUT_RATE_KEYID, STREAM_CODEC_SAMPLE_RATE);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sinkId1, STREAM_CODEC_OUTPUT_RATE_KEYID, STREAM_CODEC_SAMPLE_RATE);
                    }

                    // Set ANC instances / inputs
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId0, STREAM_ANC_INSTANCE_KEYID, 1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId1, STREAM_ANC_INSTANCE_KEYID, 2);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId0, STREAM_ANC_INPUT_KEYID, 1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sourceId1, STREAM_ANC_INPUT_KEYID, 1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sinkId0, STREAM_ANC_INSTANCE_KEYID, 1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioConfigure(teHandle, sinkId1, STREAM_ANC_INSTANCE_KEYID, 2);
                    }

                    // Set IIR filters
                    static const uint16 NUM_IIR_COEFFS = 15;
                    uint16 iirCoefficients[NUM_IIR_COEFFS] = { 0xFE4A, 0x71, 0xFF5E, 0x29, 0xFFFF, 0x1, 0xFFFF, 0x167, 0x1B2, 0xFDDB, 0xFFC0, 0x21, 0xFFA2, 0xFFFF, 0x1 };
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioSetAncIirFilter(teHandle, 1, 1, iirCoefficients, NUM_IIR_COEFFS);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioSetAncIirFilter(teHandle, 2, 1, iirCoefficients, NUM_IIR_COEFFS);
                    }

                    // Set LPF filters
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioSetAncLpfFilter(teHandle, 1, 1, 5, 5);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioSetAncLpfFilter(teHandle, 2, 1, 5, 5);
                    }

                    // Enable ANC
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioStreamAncEnable(teHandle, 9, 9);
                    }

                    // Close the sources and sinks
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSource(teHandle, sourceId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSource(teHandle, sourceId1);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSink(teHandle, sinkId0);
                    }
                    if (teRet == TE_OK)
                    {
                        teRet = teAudioCloseSink(teHandle, sinkId1);
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teAudioStreamAncEnable.restype = ct.c_int32
        self.TestEngineDLL.teAudioStreamAncEnable.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAudioStreamAncEnable(handle, anc0, anc1)
        
        return retval
    # end of teAudioStreamAncEnable


    def teAudioMicBiasConfigure(self, handle: int, id: int, key: int, value: int) -> int:
        r"""Function TestEngine::teAudioMicBiasConfigure() wrapper for teAudioMicBiasConfigure in TestEngine DLL.

        Python API:
            teAudioMicBiasConfigure(handle: int, id: int, key: int, value: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAudioMicBiasConfigure(handle=0, id=0, key=0, value=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAudioMicBiasConfigure(uint32 handle, uint16 id,
                                                          uint16 key, uint32 value)

            Parameters :    handle -
                                Handle to the device.

                            id -
                                The mic bias instance to configure, starting from 0.

                            key -
                                Mic bias configuration key to set, where:
                                <table>
                                    <tr><td>0 = MIC_BIAS_ENABLE
                                    <tr><td>1 = MIC_BIAS_VOLTAGE
                                </table>

                            value -
                                The value to set for the audio configuration key. For
                                MIC_BIAS_ENABLE the value must be either 0 or 1. For
                                MIC_BIAS_VOLTAGE, the mapping from value to voltage is IC
                                dependent, so the IC datasheet should be consulted.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to set a mic bias configuration key value for
                            a given mic bias instace.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example:        See example code for teAudioConnect.

        """
        self.TestEngineDLL.teAudioMicBiasConfigure.restype = ct.c_int32
        self.TestEngineDLL.teAudioMicBiasConfigure.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint32]
        
        retval = self.TestEngineDLL.teAudioMicBiasConfigure(handle, id, key, value)
        
        return retval
    # end of teAudioMicBiasConfigure


    def teCapacitiveSensorRead(self, handle: int, pad: int, value: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teCapacitiveSensorRead() wrapper for teCapacitiveSensorRead in TestEngine DLL.

        Python API:
            teCapacitiveSensorRead(handle: int, pad: int, value: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, value = myDll.teCapacitiveSensorRead(handle=0, pad=0)
            print(retval, value)

        Detail From Wrapped C API:
            Function :      int32 teCapacitiveSensorRead(uint32 handle, uint16 pad,
                                                         uint16* value)

            Parameters :    handle -
                                Handle to the device.

                            pad -
                                The pad to read.

                            value -
                                Absolute capacitance read from the pad in units of 1fF.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function reads the capacitance value of the specified
                            capacitative sense pad.
                            <p>
                            This function is not supported for BlueCore ICs, for which
                            bccmdCapacitiveSensorRead should be used.

        """
        self.TestEngineDLL.teCapacitiveSensorRead.restype = ct.c_int32
        self.TestEngineDLL.teCapacitiveSensorRead.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p]
        local_value = ct.c_uint32(value)
        retval = self.TestEngineDLL.teCapacitiveSensorRead(handle, pad, ct.byref(local_value))
        value = local_value.value
        return retval, value
    # end of teCapacitiveSensorRead


    def teCheckLicense(self, handle: int, featureId: int, result: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teCheckLicense() wrapper for teCheckLicense in TestEngine DLL.

        Python API:
            teCheckLicense(handle: int, featureId: int, result: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, result = myDll.teCheckLicense(handle=0, featureId=0)
            print(retval, result)

        Detail From Wrapped C API:
            Function :      int32 teCheckLicense(uint32 handle, uint8 featureId, uint8* result)

            Parameters :    handle -
                                Handle to the device.

                            featureId -
                                The ID number of the feature to check.

                            result -
                                Boolean value (0 = license check failed, 1 = license check
                                passed).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets the license status for a given feature.
                            <p>
                            This function is deprecated. Use teCheckLicenses instead (it is
                            more efficient when checking multiple features).
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Deprecated :

        """
        self.TestEngineDLL.teCheckLicense.restype = ct.c_int32
        self.TestEngineDLL.teCheckLicense.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_void_p]
        local_result = ct.c_uint8(result)
        retval = self.TestEngineDLL.teCheckLicense(handle, featureId, ct.byref(local_result))
        result = local_result.value
        return retval, result
    # end of teCheckLicense


    def teCheckLicenses(self, handle: int, numFeatureIds: int, featureIds: list, results: list) -> Tuple[int, list]:
        r"""Function TestEngine::teCheckLicenses() wrapper for teCheckLicenses in TestEngine DLL.

        Python API:
            teCheckLicenses(handle: int, numFeatureIds: int, featureIds: list, results: list) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, results = myDll.teCheckLicenses(handle=0, numFeatureIds=0, featureIds=[0,1], results=[0,1])
            print(retval, results)

        Detail From Wrapped C API:
            Function :      int32 teCheckLicenses(uint32 handle, uint16 numFeatureIds,
                                                  const uint16* featureIds, uint8* results)

            Parameters :    handle -
                                Handle to the device.

                            numFeatureIds -
                                The number of features to check.

                            featureIds -
                                Pointer to an array of length numFeatureIds, containing the ID
                                numbers of the features to check.

                            results -
                                Pointer to an array of length numFeatureIds, to contain the
                                results of the license check for the given featureIds.
                                Each array element is a boolean value (0 = feature is
                                unlicensed, 1 = feature is licensed).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function gets the license status for one or more features.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs.

            Example :

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 5000);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    static const uint16 NUM_FEATURES = 3;
                    uint16 featureIds[NUM_FEATURES] = {3, 4, 6};
                    uint8 results[NUM_FEATURES];
                    int32 teRet = teCheckLicenses(teHandle, NUM_FEATURES, featureIds, results);
                    if (teRet == TE_OK)
                    {
                        for (uint16 i = 0; i < NUM_FEATURES; ++i)
                        {
                            cout << "Feature " << featureIds[i] << " is "
                                 << (results[i] ? "licensed" : "unlicensed") << endl;
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teCheckLicenses.restype = ct.c_int32
        self.TestEngineDLL.teCheckLicenses.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        if featureIds == None:
            featureIds = []
        local_featureIds = (ct.c_uint16 * max(numFeatureIds, len(featureIds)))(*featureIds)
        if results == None:
            results = []
        local_results = (ct.c_uint8 * max(numFeatureIds, len(results)))(*results)
        retval = self.TestEngineDLL.teCheckLicenses(handle, numFeatureIds, local_featureIds, local_results)
        results = local_results[:]
        return retval, results
    # end of teCheckLicenses


    def teAppDisable(self, handle: int, reserved: int) -> int:
        r"""Function TestEngine::teAppDisable() wrapper for teAppDisable in TestEngine DLL.

        Python API:
            teAppDisable(handle: int, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAppDisable(handle=0, reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAppDisable(uint32 handle, uint16 reserved)

            Parameters :    handle -
                                Handle to the device.

                            reserved -
                                Currently unused.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   For applicable ICs, this disables any application running in apps
                            processor 1.
                            <p>This function is not supported for BlueCore or CSRC9xxx ICs -
                            see psWriteVmDisable.

        """
        self.TestEngineDLL.teAppDisable.restype = ct.c_int32
        self.TestEngineDLL.teAppDisable.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teAppDisable(handle, reserved)
        
        return retval
    # end of teAppDisable


    def teAppWrite(self, handle: int, channel: int, data: list, length: int) -> int:
        r"""Function TestEngine::teAppWrite() wrapper for teAppWrite in TestEngine DLL.

        Python API:
            teAppWrite(handle: int, channel: int, data: list, length: int) -> int

        Python Example Call Syntax:
            retval = myDll.teAppWrite(handle=0, channel=0, data=[0,1], length=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teAppWrite(uint32 handle, uint8 channel, const uint16* data,
                                             uint16 length)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                The channel number for the message (0...127).

                            data -
                                A pointer to an array of 16-bit unsigned integers containing
                                the message payload.

                            length -
                                The number of words to send. Must be between 1 and 80, and
                                no larger than the size of the data array.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to write a message to an application
                            running on CSRA681xx and later ICs.
                            <p>
                            This function is not supported for BlueCore ICs - use vmWrite
                            instead.

            Example :

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Write a message
                    static const uint16 MSG_LEN = 3;
                    uint16 txData[MSG_LEN] = { 1, 2, 3 };
                    int32 teRet = teAppWrite(teHandle, 0, txData, MSG_LEN);
                    if (teRet == TE_OK)
                    {
                        cout << "Message sent to application" << endl;

                        // Read a message (e.g. response from application to above message)
                        static const uint16 MAX_MSG_LEN = 80;
                        uint16 rxData[MAX_MSG_LEN];
                        uint8 channel;
                        uint16 readLength;
                        teRet = teAppRead(teHandle, &channel, rxData, MAX_MSG_LEN, &readLength, 1000);
                        if (teRet == TE_OK)
                        {
                            cout << "Message received from application on channel "
                                 << static_cast<uint16>(channel) << ":" << endl;
                            for (uint16 i = 0; i < readLength; ++i)
                            {
                                cout << rxData[i] << endl;
                            }
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teAppWrite.restype = ct.c_int32
        self.TestEngineDLL.teAppWrite.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_void_p, ct.c_uint16]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestEngineDLL.teAppWrite(handle, channel, local_data, length)
        
        return retval
    # end of teAppWrite


    def teAppRead(self, handle: int, channel: int=0, data: list=None, dataLength: int=0, readLength: int=0, timeoutMs: int=0) -> Tuple[int, int, list, int]:
        r"""Function TestEngine::teAppRead() wrapper for teAppRead in TestEngine DLL.

        Python API:
            teAppRead(handle: int, channel: int=0, data: list=None, dataLength: int=0, readLength: int=0, timeoutMs: int=0) -> Tuple[int, int, list, int]

        Python Example Call Syntax:
            retval, channel, data, readLength = myDll.teAppRead(handle=0, data=[0,1], dataLength=0, timeoutMs=0)
            print(retval, channel, data, readLength)

        Detail From Wrapped C API:
            Function :      int32 teAppRead(uint32 handle, uint8* channel, uint16* data,
                                            uint16 dataLength, uint16* readLength,
                                            uint16 timeoutMs)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                Location where the channel number of the message will be
                                stored.

                            data -
                                A pointer to an array of 16-bit unsigned integers where the
                                message data will be stored.

                            dataLength -
                                The length of the data array. Must be >= 1.

                            readLength -
                                Location where the length of any message read will be stored.
                                If the dataLength indicates that the data array is too small to
                                hold the message data, TE_ERROR will be returned and the value
                                will be set to the length of the message. As much data as
                                possible will be stored in the data array in this case.

                            timeoutMs -
                                A timeout, in milliseconds, of the time to wait for a message.
                                A value of 0 means the function will just poll.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read any message returned from an
                            application running on CSRA681xx and later ICs.
                            <p>
                            If a message has already been received, it will be returned
                            immediately, otherwise the function will wait for a message until
                            the timeout has expired. If no data has been read within the
                            timeout period, TE_ERROR will be returned and readLength will be
                            set to zero.
                            <p>
                            This function is not supported for BlueCore ICs - use vmRead
                            instead.

            Example:        See example code for teAppWrite.

        """
        self.TestEngineDLL.teAppRead.restype = ct.c_int32
        self.TestEngineDLL.teAppRead.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_uint16, ct.c_void_p, ct.c_uint16]
        local_channel = ct.c_uint8(channel)
        if data == None:
            data = []
        local_data = (ct.c_uint16 * max(dataLength, len(data)))(*data)
        local_readLength = ct.c_uint16(readLength)
        retval = self.TestEngineDLL.teAppRead(handle, ct.byref(local_channel), local_data, dataLength, ct.byref(local_readLength), timeoutMs)
        channel = local_channel.value
        data = local_data[:]
        readLength = local_readLength.value
        return retval, channel, data, readLength
    # end of teAppRead


    def teAdcGet(self, handle: int, adc: int, delay: int, extraFlag: int, result: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teAdcGet() wrapper for teAdcGet in TestEngine DLL.

        Python API:
            teAdcGet(handle: int, adc: int, delay: int, extraFlag: int, result: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, result = myDll.teAdcGet(handle=0, adc=0, delay=0, extraFlag=0)
            print(retval, result)

        Detail From Wrapped C API:
            Function :      int32 teAdcGet(uint32 handle, uint16 adc, uint16 delay,
                                           uint16 extraFlag, uint16* result)

            Parameters :    handle -
                                Handle to the device.

                            adc -
                                ADC which will be read. The ADCs which can be read are IC
                                dependent. See the vm_adc_source_type enum in the on-chip
                                application file adc_if.h.

                            delay -
                                Delay in milliseconds used before the read is taken.
                                <p>
                                This parameter is ignored for BlueCore ICs.

                            extraFlag -
                                The lower 8 bits of this parameter specify a value which can
                                enable a current source on the pin being measured from. Set 
                                to zero if no current source is required. See the
                                vm_adc_extra_flag enum in the on-chip application file
                                adc_if.h. The upper 8 bits are unused.
                                <p>
                                This parameter is ignored for BlueCore ICs.

                            result -
                                Holds the result of the ADC reading.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function will perform an ADC read.
                            <p>
                            For BlueCore ICs, bccmdGetAdc can be used directly.

        """
        self.TestEngineDLL.teAdcGet.restype = ct.c_int32
        self.TestEngineDLL.teAdcGet.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p]
        local_result = ct.c_uint16(result)
        retval = self.TestEngineDLL.teAdcGet(handle, adc, delay, extraFlag, ct.byref(local_result))
        result = local_result.value
        return retval, result
    # end of teAdcGet


    def teChargerSetConfig(self, handle: int, config: list) -> int:
        r"""Function TestEngine::teChargerSetConfig() wrapper for teChargerSetConfig in TestEngine DLL.

        Python API:
            teChargerSetConfig(handle: int, config: list) -> int

        Python Example Call Syntax:
            retval = myDll.teChargerSetConfig(handle=0, config=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teChargerSetConfig(uint32 handle, const uint16* config)

            Parameters :    handle -
                                Handle to the device.

                            config -
                                Pointer to an array of exactly 13 16-bit unsigned integers
                                which define the configuration parameters. Each indexed value
                                maps to a configuration setting as follows:
                                <table>
                                    <tr><td>0 = pre_external_milliohms
                                    <tr><td>1 = fast_external_milliohms
                                    <tr><td>2 = trickle_milliamps
                                    <tr><td>3 = pre_milliamps
                                    <tr><td>4 = fast_milliamps
                                    <tr><td>5 = pre_fast_threshold
                                    <tr><td>6 = float_constant_voltage
                                    <tr><td>7 = termination_current
                                    <tr><td>8 = termination_debounce
                                    <tr><td>9 = standby_fast_hysteris
                                    <tr><td>10 = charger_configure_type (unused for firmware before ADK6.1)
                                    <tr><td>11 = unused (reserved for future use)
                                    <tr><td>12 = enable
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to configure the battery charger.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            bccmdCharger* functions should be used.

            Example:

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Disable charger
                    uint16 configParams[] = {
                        0,      // pre_external_milliohms
                        0,      // fast_external_milliohms
                        30,     // trickle_milliamps
                        100,    // pre_milliamps
                        200,    // fast_milliamps
                        2,      // pre_fast_threshold
                        11,     // float_constant_voltage
                        0,      // termination_current
                        3,      // termination_debounce
                        1,      // standby_fast_hysteris
                        0,      // charger_configure_type
                        0,      // unused_expansion2
                        0       // enable
                    };

                    int32 teRet = teChargerSetConfig(teHandle, configParams);

                    // Get the charger status
                    if (teRet == TE_OK)
                    {
                        uint16 status;
                        teRet = teChargerGetStatus(teHandle, &status);
                        if (teRet == TE_OK)
                        {
                            cout << "Charger status = " << status << endl;
                        }
                    }

                    // Enable charger
                    if (teRet == TE_OK)
                    {
                        configParams[12] = 1;
                        teRet = teChargerSetConfig(teHandle, configParams);
                    }

                    // Get the charger status
                    if (teRet == TE_OK)
                    {
                        uint16 status;
                        teRet = teChargerGetStatus(teHandle, &status);
                        if (teRet == TE_OK)
                        {
                            cout << "Charger status (after enable) = " << status << endl;
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teChargerSetConfig.restype = ct.c_int32
        self.TestEngineDLL.teChargerSetConfig.argtypes = [ct.c_uint32, ct.c_void_p]
        if config == None:
            config = []
        local_config = (ct.c_uint16 * len(config))(*config)
        retval = self.TestEngineDLL.teChargerSetConfig(handle, local_config)
        
        return retval
    # end of teChargerSetConfig


    def teChargerGetStatus(self, handle: int, status: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teChargerGetStatus() wrapper for teChargerGetStatus in TestEngine DLL.

        Python API:
            teChargerGetStatus(handle: int, status: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, status = myDll.teChargerGetStatus(handle=0)
            print(retval, status)

        Detail From Wrapped C API:
            Function :      int32 teChargerGetStatus(uint32 handle, uint16* status)

            Parameters :    handle -
                                Handle to the device.

                            status -
                                Pointer to a 16-bit unsigned integer to hold the returned
                                status of the charger.
                                <p>
                                The following values can be returned (from device code
                                source file charger_if.h):
                                <table>
                                    <tr><td>0 = NO_POWER
                                    <tr><td>1 = TRICKLE_CHARGE
                                    <tr><td>2 = PRE_CHARGE
                                    <tr><td>3 = FAST_CHARGE
                                    <tr><td>4 = HEADROOM_ERROR
                                    <tr><td>5 = VBAT_OVERVOLT_ERROR
                                    <tr><td>6 = STANDBY (Battery is full)
                                    <tr><td>7 = DISABLED_ERROR
                                    <tr><td>8 = CONFIG_FAIL_UNKNOWN
                                    <tr><td>9 = CONFIG_FAIL_CHARGER_ENABLED
                                    <tr><td>10 = CONFIG_FAIL_EFUSE_CRC_INVALID
                                    <tr><td>11 = CONFIG_FAIL_EFUSE_TRIMS_ZERO
                                    <tr><td>12 = CONFIG_FAIL_CURRENTS_ZERO
                                    <tr><td>13 = CONFIG_FAIL_VALUES_OUT_OF_RANGE
                                    <tr><td>14 = ENABLE_FAIL_UNKNOWN
                                    <tr><td>15 = ENABLE_FAIL_EFUSE_CRC_INVALID
                                    <tr><td>16 = INTERNAL_CURRENT_SOURCE_CONFIG_FAIL
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read the state of the battery charger.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            bccmdCharger* functions should be used.

            Example:

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    uint16 status;
                    int32 teRet = teChargerGetStatus(teHandle, &status);
                    if (teRet == TE_OK)
                    {
                        cout << "Charger status = " << status << endl;
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teChargerGetStatus.restype = ct.c_int32
        self.TestEngineDLL.teChargerGetStatus.argtypes = [ct.c_uint32, ct.c_void_p]
        local_status = ct.c_uint16(status)
        retval = self.TestEngineDLL.teChargerGetStatus(handle, ct.byref(local_status))
        status = local_status.value
        return retval, status
    # end of teChargerGetStatus


    def teNfcConfigure(self, handle: int, enable: int) -> int:
        r"""Function TestEngine::teNfcConfigure() wrapper for teNfcConfigure in TestEngine DLL.

        Python API:
            teNfcConfigure(handle: int, enable: int) -> int

        Python Example Call Syntax:
            retval = myDll.teNfcConfigure(handle=0, enable=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teNfcConfigure(uint32 handle, uint8 enable)

            Parameters :    handle -
                                Handle to the device.

                            enable -
                                Boolean value (0 = Disable NFC, 1 = Enable NFC).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to enable / disable NFC for testing.
                            <p>
                            This function is not supported for BlueCore ICs.

        """
        self.TestEngineDLL.teNfcConfigure.restype = ct.c_int32
        self.TestEngineDLL.teNfcConfigure.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestEngineDLL.teNfcConfigure(handle, enable)
        
        return retval
    # end of teNfcConfigure


    def teConfigCacheInit(self, handle: int, configDb: str) -> int:
        r"""Function TestEngine::teConfigCacheInit() wrapper for teConfigCacheInit in TestEngine DLL.

        Python API:
            teConfigCacheInit(handle: int, configDb: str) -> int

        Python Example Call Syntax:
            retval = myDll.teConfigCacheInit(handle=0, configDb='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheInit(uint32 handle, const char* configDb)

            Parameters :    handle -
                                Handle to the device.

                            configDb -
                                Configuration database specifier in the following format:
                                "DbFilePath:SysVerLabel", e.g. "hyd.sdb:CSRA68100_CONFIG".
                                <p>
                                The MIB database file should be a *.sdb file. The system
                                version label determines the dataset within the database.
                                It can be omitted if there is only one system version label
                                in the database, i.e. "hyd.sdb" is permissible when there
                                is only one possible system version to select.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to initialise the configuration cache. It
                            must be called before any other teConfigCache* functions are used.
                            <p>
                            If the system version selected in the database is not compatible
                            with the connected device, an error will be returned.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :       See example code for teConfigCacheWrite.

        """
        self.TestEngineDLL.teConfigCacheInit.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheInit.argtypes = [ct.c_uint32, ct.c_char_p]
        local_configDb = None if configDb is None else ct.create_string_buffer(bytes(configDb, encoding="UTF-8"))
        retval = self.TestEngineDLL.teConfigCacheInit(handle, local_configDb)
        
        return retval
    # end of teConfigCacheInit


    def teConfigCacheRead(self, handle: int, file: str, reserved: int) -> int:
        r"""Function TestEngine::teConfigCacheRead() wrapper for teConfigCacheRead in TestEngine DLL.

        Python API:
            teConfigCacheRead(handle: int, file: str, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.teConfigCacheRead(handle=0, file='abc', reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheRead(uint32 handle, const char* file,
                                                    uint16 reserved)

            Parameters :    handle -
                                Handle to the device.

                            file -
                                Path of a *.htf file containing configuration data to load
                                into the cache, or NULL to specify that configuration data
                                should be read from the connected device.

                            reserved -
                                Currently unused, should be set to 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read configuration data into the cache.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :       See example code for teConfigCacheWrite.

        """
        self.TestEngineDLL.teConfigCacheRead.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheRead.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_uint16]
        local_file = None if file is None else ct.create_string_buffer(bytes(file, encoding="UTF-8"))
        retval = self.TestEngineDLL.teConfigCacheRead(handle, local_file, reserved)
        
        return retval
    # end of teConfigCacheRead


    def teConfigCacheMerge(self, handle: int, file: str) -> int:
        r"""Function TestEngine::teConfigCacheMerge() wrapper for teConfigCacheMerge in TestEngine DLL.

        Python API:
            teConfigCacheMerge(handle: int, file: str) -> int

        Python Example Call Syntax:
            retval = myDll.teConfigCacheMerge(handle=0, file='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheMerge(uint32 handle, const char* file)

            Parameters :    handle -
                                Handle to the device.

                            file -
                                Path of a *.htf file containing configuration data to merge
                                into the cache.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to merge configuration data into the cache.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :

                static const char* const CFG_DB_PARAM = "hyd.sdb:QCC514X_CONFIG";
                static const char* const CFG_MERGE_FILE = "C:\\temp\\merge.htf";

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Initialise the configuration cache
                    int32 teRet = teConfigCacheInit(teHandle, CFG_DB_PARAM);

                    // Read the configuration into the cache from the device
                    uint16 unused = 0;
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheRead(teHandle, NULL, unused);
                    }

                    // Merge configuration data from file into the cache
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheMerge(teHandle, CFG_MERGE_FILE);
                    }

                    // Write the configuration cache to the device
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheWrite(teHandle, NULL, unused);
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teConfigCacheMerge.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheMerge.argtypes = [ct.c_uint32, ct.c_char_p]
        local_file = None if file is None else ct.create_string_buffer(bytes(file, encoding="UTF-8"))
        retval = self.TestEngineDLL.teConfigCacheMerge(handle, local_file)
        
        return retval
    # end of teConfigCacheMerge


    def teConfigCacheReadItem(self, handle: int, key: str, value: str='', maxLen: int=0) -> Tuple[int, str, int]:
        r"""Function TestEngine::teConfigCacheReadItem() wrapper for teConfigCacheReadItem in TestEngine DLL.

        Python API:
            teConfigCacheReadItem(handle: int, key: str, value: str='', maxLen: int=0) -> Tuple[int, str, int]

        Python Example Call Syntax:
            retval, value, maxLen = myDll.teConfigCacheReadItem(handle=0, key='abc')
            print(retval, value, maxLen)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheReadItem(uint32 handle, const char* key,
                                                        char* value, uint32* maxLen)

            Parameters :    handle -
                                Handle to the device.

                            key -
                                Key specifier in the following format:
                                "Subsys[Layer]:Name", e.g. "curator3:XtalFreqTrim", or
                                "curator:XtalFreqTrim".

                            value -
                                Location where the key value will be stored in the same
                                format as is used when written to a file (but without
                                descriptive text, indentation and other layout formatting).

                            maxLen -
                                Input / output parameter, where the input value is the length
                                of the value array (in bytes). If the given length is
                                insufficient to store the key's value, an error is returned,
                                and the value will be set to the required length.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to read a configuration key value from the
                            cache. If the layer part of the key specifier is omitted, the key
                            value read will be that set in the highest layer.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :       See example code for teConfigCacheWrite.

        """
        self.TestEngineDLL.teConfigCacheReadItem.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheReadItem.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_key = None if key is None else ct.create_string_buffer(bytes(key, encoding="UTF-8"))
        local_value = None if value is None else ct.create_string_buffer(bytes(value, encoding="UTF-8"), 1024)
        local_maxLen = ct.c_uint32(maxLen)
        retval = self.TestEngineDLL.teConfigCacheReadItem(handle, local_key, local_value, ct.byref(local_maxLen))
        value = local_value.value.decode()
        maxLen = local_maxLen.value
        return retval, value, maxLen
    # end of teConfigCacheReadItem


    def teConfigCacheWriteItem(self, handle: int, key: str, value: str) -> int:
        r"""Function TestEngine::teConfigCacheWriteItem() wrapper for teConfigCacheWriteItem in TestEngine DLL.

        Python API:
            teConfigCacheWriteItem(handle: int, key: str, value: str) -> int

        Python Example Call Syntax:
            retval = myDll.teConfigCacheWriteItem(handle=0, key='abc', value='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheWriteItem(uint32 handle, const char* key,
                                                         const char* value)

            Parameters :    handle -
                                Handle to the device.

                            key -
                                Key specifier in the following format:
                                "SubsysLayer:Name", e.g. "curator3:XtalFreqTrim".

                            value -
                                The value to write. The format is the same as is used for
                                text (*.htf) files (but without any descriptive text,
                                indentation and other layout formatting).
                                <p>
                                To delete a value, use the value "NULL" or an empty string.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to write a configuration key value to the
                            cache.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :       See example code for teConfigCacheWrite.

        """
        self.TestEngineDLL.teConfigCacheWriteItem.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheWriteItem.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_char_p]
        local_key = None if key is None else ct.create_string_buffer(bytes(key, encoding="UTF-8"))
        local_value = None if value is None else ct.create_string_buffer(bytes(value, encoding="UTF-8"))
        retval = self.TestEngineDLL.teConfigCacheWriteItem(handle, local_key, local_value)
        
        return retval
    # end of teConfigCacheWriteItem


    def teConfigCacheWrite(self, handle: int, file: str, reserved: int) -> int:
        r"""Function TestEngine::teConfigCacheWrite() wrapper for teConfigCacheWrite in TestEngine DLL.

        Python API:
            teConfigCacheWrite(handle: int, file: str, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.teConfigCacheWrite(handle=0, file='abc', reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teConfigCacheWrite(uint32 handle, const char* file,
                                                     uint16 reserved)

            Parameters :    handle -
                                Handle to the device.

                            file -
                                Path of a *.htf file to write the configuration cache data to.
                                If NULL, the configuration cache data is written to the
                                connected device.

                            reserved -
                                Currently unused, should be set to 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function is used to write configuration data from the cache.
                            <p>
                            The teConfigCache* functions are unsupported for BlueCore and
                            CSRC9xxx ICs (for BlueCore ICs use the ps* functions).

            Example :

                static const char* const CFG_DB_PARAM = "hyd.sdb:CSRA68100_CONFIG";
                static const uint32 KEY_READ_BUFFER_LEN = 128;

                cout << "Trying to connect..." << endl;
                uint32 teHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected!" << endl;

                    // Initialise the configuration cache
                    int32 teRet = teConfigCacheInit(teHandle, CFG_DB_PARAM);

                    // Read the configuration into the cache from the device
                    uint16 unused = 0;
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheRead(teHandle, NULL, unused);
                    }

                    // Read current XTAL trim value
                    if (teRet == TE_OK)
                    {
                        char valueString[KEY_READ_BUFFER_LEN];
                        uint32 maxLen = KEY_READ_BUFFER_LEN;

                        teRet = teConfigCacheReadItem(teHandle, "curator:XtalFreqTrim", valueString, &maxLen);
                        if (teRet == TE_OK)
                        {
                            cout << "curator:XtalFreqTrim = " << valueString << endl;
                        }
                    }

                    // Write updated XTAL trim value
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheWriteItem(teHandle, "curator15:XtalFreqTrim", "3");
                    }

                    // Write Bluetooth address
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheWriteItem(teHandle, "bt15:PSKEY_BDADDR", "{0x3456,0x5B,0x02}");
                    }

                    // Write the configuration cache to the device
                    if (teRet == TE_OK)
                    {
                        teRet = teConfigCacheWrite(teHandle, NULL, unused);
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teConfigCacheWrite.restype = ct.c_int32
        self.TestEngineDLL.teConfigCacheWrite.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_uint16]
        local_file = None if file is None else ct.create_string_buffer(bytes(file, encoding="UTF-8"))
        retval = self.TestEngineDLL.teConfigCacheWrite(handle, local_file, reserved)
        
        return retval
    # end of teConfigCacheWrite


    def teChipReset(self, handle: int, mode: int) -> int:
        r"""Function TestEngine::teChipReset() wrapper for teChipReset in TestEngine DLL.

        Python API:
            teChipReset(handle: int, mode: int) -> int

        Python Example Call Syntax:
            retval = myDll.teChipReset(handle=0, mode=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teChipReset(uint32 handle, uint32 mode)

            Parameters :    handle -
                                Handle to the device.

                            mode -
                                The reset mode, where:
                                <table>
                                    <tr><td>0 = Wait for reboot / re-enumeration
                                    <tr><td>1 = Return immediately
                                </table>
                                <p>
                                If no further operations are to be performed with the
                                connected device (i.e. closeTestEngine is the next TestEngine
                                function to be called), then mode 1 can be used to avoid an
                                unnecessary delay. Otherwise mode 0 should be used so that the
                                device is ready to communicate on return.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function causes a reset of the connected device. Depending on
                            the mode setting, it will either wait for the device to reboot
                            (and in the case of USBDBG to re-enumerate), or return
                            immediately.
                            <p>
                            This function is unsupported for BlueCore ICs, for which
                            bccmdSetColdReset or bccmdSetWarmReset should be used.

        """
        self.TestEngineDLL.teChipReset.restype = ct.c_int32
        self.TestEngineDLL.teChipReset.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.teChipReset(handle, mode)
        
        return retval
    # end of teChipReset


    def teEnableSecurity(self, handle: int, options: int) -> int:
        r"""Function TestEngine::teEnableSecurity() wrapper for teEnableSecurity in TestEngine DLL.

        Python API:
            teEnableSecurity(handle: int, options: int) -> int

        Python Example Call Syntax:
            retval = myDll.teEnableSecurity(handle=0, options=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teEnableSecurity(uint32 handle, uint32 options)

            Parameters :    handle -
                                Handle to the device.

                            options -
                                A value to define what security aspects are to be enabled,
                                where each bit specifies a security aspect as follows:
                                <table>
                                    <tr><td>Bit 0 =     <td>Encryption
                                    <tr><td>Bit 1 =     <td>Debug Transport Lock
                                    <tr><td>Bit 2 =     <td>USB Debug disabled
                                    <tr><td>Bit 3..31 = <td>Reserved. Must be set to zero
                                                            unless advised otherwise by QTIL.
                                </table>
                                <p>
                                NOTE: In addition to those listed above, the USBDBG_ALLOWED
                                security function can be set with the SecureKeyCmd tool.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Enables one or more security aspects.
                            <p>
                            Security aspects enabled with this function become active after
                            the next power cycle or device reset. See teChipReset for
                            details of performing a device reset.
                            <p>
                            This function is not applicable for BlueCore or CSRC9xxx ICs.
                            <p>
                            NOTE: For CSRA681xx, QCC302x-8x, and QCC512x-8x devices, the
                            same key (written with the TestFlash API function flSetSecurityKey
                            or using the securekeycmd tool) is used for debug transport
                            locking and encryption, and the Debug Transport Lock bit has no
                            effect unless the Encryption bit is also set (or encryption has
                            been previously enabled). Once both the encryption and debug
                            transport lock security aspects are active, the correct key will
                            need to be supplied when opening a connection. See
                            openTestEngineUnlock, openTestEngineDebugUnlock or
                            openTestEngineDebugUnlockTrans for details.
                            <p>
                            NOTE: If the "USB Debug disabled" option is set, USB Debug will
                            be permanently disabled, with no means to re-enable it. It is
                            not recommended that this is done unless another debug transport
                            (such as TRB) is available.

        """
        self.TestEngineDLL.teEnableSecurity.restype = ct.c_int32
        self.TestEngineDLL.teEnableSecurity.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestEngineDLL.teEnableSecurity(handle, options)
        
        return retval
    # end of teEnableSecurity


    def teI2cTransfer(self, handle: int, pioScl: int, pioSda: int, devAddr: int, clockKhz: int, txOctets: int, rxOctets: int, data: list, rxdOctets: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::teI2cTransfer() wrapper for teI2cTransfer in TestEngine DLL.

        Python API:
            teI2cTransfer(handle: int, pioScl: int, pioSda: int, devAddr: int, clockKhz: int, txOctets: int, rxOctets: int, data: list, rxdOctets: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, data, rxdOctets = myDll.teI2cTransfer(handle=0, pioScl=0, pioSda=0, devAddr=0, clockKhz=0, txOctets=0, rxOctets=0, data=[0,1])
            print(retval, data, rxdOctets)

        Detail From Wrapped C API:
            Function :      int32 teI2cTransfer(uint32 handle, uint16 pioScl, uint16 pioSda,
                                                uint16 devAddr, uint16 clockKhz,
                                                uint16 txOctets, uint16 rxOctets,
                                                uint8* data, uint16* rxdOctets)

            Parameters :    handle -
                                Handle to the device.

                            pioScl -
                                PIO used for I2C SCL.

                            pioSda -
                                PIO used for I2C SDA.

                            devAddr -
                                Address of the I2C device.

                            clockKhz -
                                I2C clock speed in KHz.

                            txOctets -
                                Number of bytes to write to the I2C device. The data array
                                size must be at least this many bytes.
                                <p>
                                The maximum number of bytes is 32.

                            rxOctets -
                                Number of bytes to read from the I2C device. The data array
                                size must be large enough to hold at least this many bytes.
                                <p>
                                The maximum number of bytes is 32.

                            data -
                                Pointer to an array of bytes to write, or read from memory.
                                This parameter is an input/output parameter.
                                <p>
                                In the case of a write operation, data should contain the
                                bytes to write.
                                <p>
                                In the case of a read operation, or a composite write + read
                                operation, data should be at least as large as the larger of
                                txOctets and rxOctets. On return, data will contain the bytes
                                read from the device.

                            rxdOctets -
                                Number of bytes read from the I2C device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This function performs writes to and/or reads from an I2C device.
                            <p>
                            This function is not supported for BlueCore ICs, for which the
                            bccmdI2CTransfer function should be used.

        """
        self.TestEngineDLL.teI2cTransfer.restype = ct.c_int32
        self.TestEngineDLL.teI2cTransfer.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint8 * max(rxOctets, len(data)))(*data)
        local_rxdOctets = ct.c_uint16(rxdOctets)
        retval = self.TestEngineDLL.teI2cTransfer(handle, pioScl, pioSda, devAddr, clockKhz, txOctets, rxOctets, local_data, ct.byref(local_rxdOctets))
        data = local_data[:]
        rxdOctets = local_rxdOctets.value
        return retval, data, rxdOctets
    # end of teI2cTransfer


    def teNvmTagRead(self, handle: int, tagId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::teNvmTagRead() wrapper for teNvmTagRead in TestEngine DLL.

        Python API:
            teNvmTagRead(handle: int, tagId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, value, readLen = myDll.teNvmTagRead(handle=0, tagId=0, valueLen=0, value=[0,1])
            print(retval, value, readLen)

        Detail From Wrapped C API:
            Function :      int32 teNvmTagRead(uint32 handle, uint16 tagId, uint8 valueLen,
                                               uint8* value, uint8* readLen)

            Parameters :    handle -
                                Handle to the device.

                            tagId -
                                NVM tag ID to read (0 - 0xFFFF).

                            valueLen -
                                Length of the array allocated to hold the key value (0 - 0xFF).
                                Can be set to zero to get the length of the key value.

                            value -
                                Array of uint8 values of size valueLen to hold the key value.

                            readLen -
                                Pointer to an 8-bit word to hold the length of the tag's
                                value.
                                This is the length of the valid value data read for the tag
                                (may be less than the "valueLen" given if that exceeds the
                                actual length of the tag's value).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Reads an NVM tag value from device RAM.
                            <p>
                            If the valueLen value is less than the actual length of the tag's
                            value, an error will be returned, and readLen will be set to the
                            length required to hold the value.
                            <p>
                            This function reads the value of the NVM tag from device RAM - to
                            read the persisting value, the teConfigCache* functions should be
                            used.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teNvmTagWrite.

        """
        self.TestEngineDLL.teNvmTagRead.restype = ct.c_int32
        self.TestEngineDLL.teNvmTagRead.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_void_p, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint8 * max(valueLen, len(value)))(*value)
        local_readLen = ct.c_uint8(readLen)
        retval = self.TestEngineDLL.teNvmTagRead(handle, tagId, valueLen, local_value, ct.byref(local_readLen))
        value = local_value[:]
        readLen = local_readLen.value
        return retval, value, readLen
    # end of teNvmTagRead


    def teNvmTagWrite(self, handle: int, tagId: int, valueLen: int, value: list) -> int:
        r"""Function TestEngine::teNvmTagWrite() wrapper for teNvmTagWrite in TestEngine DLL.

        Python API:
            teNvmTagWrite(handle: int, tagId: int, valueLen: int, value: list) -> int

        Python Example Call Syntax:
            retval = myDll.teNvmTagWrite(handle=0, tagId=0, valueLen=0, value=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teNvmTagWrite(uint32 handle, uint16 tagId, uint8 valueLen,
                                                const uint8* value)

            Parameters :    handle -
                                Handle to the device.

                            tagId -
                                NVM tag ID to write (0 - 0xFFFF).

                            valueLen -
                                Length of the key value (0 - 0xFF).

                            value -
                                Array holding the key value (size must be at least valueLen).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Writes an NVM tag value to device RAM.
                            <p>
                            After writing an NVM tag value, hciReset should be used to ensure
                            that the device uses the updated value.
                            <p>
                            This function overwrites the value of the NVM tag in device RAM -
                            to write the value persistently, the teConfigCache* functions
                            should be used.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                cout << "Trying to connect device..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected device!" << endl;

                    // Get power table
                    const uint16 POWER_TABLE_TAG_ID = 1539;
                    const uint8 POWER_TABLE_LEN = 200;
                    uint8 value[POWER_TABLE_LEN];
                    uint8 readLen;
                    int32 teRet = teNvmTagRead(teHandle, POWER_TABLE_TAG_ID, POWER_TABLE_LEN,
                                               value, &readLen);

                    if (teRet == TE_OK)
                    {
                        // Adjust the PA attenuation for BR at power level 6
                        const size_t POWER_LEVEL_CFG_SET_SIZE = 5;
                        const size_t NUM_CFG_SETS_PER_LEVEL = 4;
                        size_t paAttenBrStartIndex = POWER_LEVEL_CFG_SET_SIZE *
                                                     NUM_CFG_SETS_PER_LEVEL * 6;
                        value[paAttenBrStartIndex] = 10;

                        teRet = teNvmTagWrite(teHandle, POWER_TABLE_TAG_ID, POWER_TABLE_LEN,
                                               value);

                        if (teRet == TE_OK)
                        {
                            // Reset BT
                            teRet = hciReset(teHandle);
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teNvmTagWrite.restype = ct.c_int32
        self.TestEngineDLL.teNvmTagWrite.argtypes = [ct.c_uint32, ct.c_uint16, ct.c_uint8, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint8 * len(value))(*value)
        retval = self.TestEngineDLL.teNvmTagWrite(handle, tagId, valueLen, local_value)
        
        return retval
    # end of teNvmTagWrite


    def tePsGetNextKeyId(self, handle: int, keyType: int, resetSearch: int, keyId: int=0, endOfStore: int=0) -> Tuple[int, int, int]:
        r"""Function TestEngine::tePsGetNextKeyId() wrapper for tePsGetNextKeyId in TestEngine DLL.

        Python API:
            tePsGetNextKeyId(handle: int, keyType: int, resetSearch: int, keyId: int=0, endOfStore: int=0) -> Tuple[int, int, int]

        Python Example Call Syntax:
            retval, keyId, endOfStore = myDll.tePsGetNextKeyId(handle=0, keyType=0, resetSearch=0)
            print(retval, keyId, endOfStore)

        Detail From Wrapped C API:
            Function :      int32 tePsGetNextKeyId(uint32 handle, uint8 keyType,
                                                   uint8 resetSearch, uint32* keyId,
                                                   uint8* endOfStore)

            Parameters :    handle -
                                Handle to the device.

                            keyType -
                                PS key type, where:
                                <table>
                                    <tr><td>0 =   <td>Apps keys
                                    <tr><td>1 =   <td>Audio keys
                                </table>
                                <p>
                                Apps keys are those read / written with tePsRead / tePsWrite.
                                Audio keys are those read / written with
                                tePsAudioRead / tePsAudioWrite.

                            resetSearch -
                                Controls the search, where:
                                <table>
                                    <tr><td>0 =   <td>Continue
                                    <tr><td>1 =   <td>Reset
                                </table>
                                <p>
                                Continue means get the next key ID found. Reset means reset
                                the search and get the first key found.

                            keyId -
                                Pointer to a 32-bit value to hold the key ID value found.

                            endOfStore -
                                Pointer to an 8-bit value to hold the value indicating whether
                                the end of the store has been reached, where:
                                <table>
                                    <tr><td>0 =   <td>Not at end of store (keyId is valid)
                                    <tr><td>1 =   <td>At end of store (keyId is not valid).
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to read the IDs of apps or audio keys that are set in
                            the persistent store.
                            <p>
                            The values of the keyIds obtained using this function can be
                            read or written using tePsRead / tePsWrite (for apps keys), and
                            tePsAudioRead / tePsAudioWrite (for audio keys).
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs (for
                            BlueCore ICs use the psRead* functions).

            Example :

                cout << "Trying to connect device..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected device!" << endl;

                    // Get all apps key IDs set in persistent store
                    const uint8 KEY_TYPE_APPS = 0;
                    uint8 resetSearch = 1;
                    uint32 keyId = 0;
                    uint8 endOfStore = 0;
                    int32 teRet;

                    do
                    {
                        teRet = tePsGetNextKeyId(teHandle, KEY_TYPE_APPS, resetSearch, &keyId, &endOfStore);
                        if (teRet == TE_OK && endOfStore == 0)
                        {
                            resetSearch = 0;
                            cout << "Found apps key ID 0x" << hex << keyId << endl;
                        }
                    } while (teRet == TE_OK && endOfStore == 0);

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.tePsGetNextKeyId.restype = ct.c_int32
        self.TestEngineDLL.tePsGetNextKeyId.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_void_p, ct.c_void_p]
        local_keyId = ct.c_uint32(keyId)
        local_endOfStore = ct.c_uint8(endOfStore)
        retval = self.TestEngineDLL.tePsGetNextKeyId(handle, keyType, resetSearch, ct.byref(local_keyId), ct.byref(local_endOfStore))
        keyId = local_keyId.value
        endOfStore = local_endOfStore.value
        return retval, keyId, endOfStore
    # end of tePsGetNextKeyId


    def tePsRead(self, handle: int, keyId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::tePsRead() wrapper for tePsRead in TestEngine DLL.

        Python API:
            tePsRead(handle: int, keyId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, value, readLen = myDll.tePsRead(handle=0, keyId=0, valueLen=0, value=[0,1])
            print(retval, value, readLen)

        Detail From Wrapped C API:
            Function :      int32 tePsRead(uint32 handle, uint32 keyId, uint16 valueLen,
                                           uint16* value, uint16* readLen)

            Parameters :    handle -
                                Handle to the device.

                            keyId -
                                PS key ID to read, from 1 to 0xFFFF.

                            valueLen -
                                Size of the array allocated to hold the key value. Must be
                                between 0 and 64, where 0 indicates that only the length of
                                the key's value is to be read.

                            value -
                                Array of 16-bit words of size "valueLen" to hold the key
                                value. Can be NULL if valueLen is 0.

                            readLen -
                                Pointer to a 16-bit word to hold the length of the key's
                                value.
                                This is the length of the valid value data read for the key
                                (may be less than the "valueLen" given if that exceeds the
                                actual length of the key's value).
                                <p>
                                If the key has not been written this value will be set to
                                zero.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to read the persistent store key specified for USR (user),
                            DSP, CONNLIB (connectivity library) and CUSTOMER PS keys (for
                            audio PS keys use tePsAudioRead).
                            <p>
                            Refer to the PS key documentation in the relevant ADK for the
                            details of supported PS keys (the ps_if.h file included in ADK
                            releases defines the PS key ID ranges for each of the supported
                            key groups).
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs (for
                            BlueCore ICs use the psRead* functions).

        """
        self.TestEngineDLL.tePsRead.restype = ct.c_int32
        self.TestEngineDLL.tePsRead.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint16 * max(valueLen, len(value)))(*value)
        local_readLen = ct.c_uint16(readLen)
        retval = self.TestEngineDLL.tePsRead(handle, keyId, valueLen, local_value, ct.byref(local_readLen))
        value = local_value[:]
        readLen = local_readLen.value
        return retval, value, readLen
    # end of tePsRead


    def tePsWrite(self, handle: int, keyId: int, valueLen: int, value: list) -> int:
        r"""Function TestEngine::tePsWrite() wrapper for tePsWrite in TestEngine DLL.

        Python API:
            tePsWrite(handle: int, keyId: int, valueLen: int, value: list) -> int

        Python Example Call Syntax:
            retval = myDll.tePsWrite(handle=0, keyId=0, valueLen=0, value=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 tePsWrite(uint32 handle, uint32 keyId, uint16 valueLen,
                                            const uint16* value)

            Parameters :    handle -
                                Handle to the device.

                            keyId -
                                PS key ID to write, from 1 to 0xFFFF.

                            valueLen -
                                Size of the array holding the key value. Must be between 0
                                and 64, where 0 effectively means that the key will be deleted.

                            value -
                                Array of 16-bit words of size "valueLen" holding the key
                                value. Can be NULL if valueLen is 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to write the persistent store key specified for USR (user),
                            DSP, CONNLIB (connectivity library) and CUSTOMER PS keys (for
                            audio PS keys use tePsAudioWrite).
                            <p>
                            Refer to the PS key documentation in the relevant ADK for the
                            details of supported PS keys (the ps_if.h file included in ADK
                            releases defines the PS key ID ranges for each of the supported
                            key groups).
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs (for
                            BlueCore ICs use the psWrite* functions).

        """
        self.TestEngineDLL.tePsWrite.restype = ct.c_int32
        self.TestEngineDLL.tePsWrite.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint16, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint16 * len(value))(*value)
        retval = self.TestEngineDLL.tePsWrite(handle, keyId, valueLen, local_value)
        
        return retval
    # end of tePsWrite


    def tePsAudioRead(self, handle: int, keyId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]:
        r"""Function TestEngine::tePsAudioRead() wrapper for tePsAudioRead in TestEngine DLL.

        Python API:
            tePsAudioRead(handle: int, keyId: int, valueLen: int, value: list, readLen: int=0) -> Tuple[int, list, int]

        Python Example Call Syntax:
            retval, value, readLen = myDll.tePsAudioRead(handle=0, keyId=0, valueLen=0, value=[0,1])
            print(retval, value, readLen)

        Detail From Wrapped C API:
            Function :      int32 tePsAudioRead(uint32 handle, uint32 keyId, uint16 valueLen,
                                                uint16* value, uint16* readLen)

            Parameters :    handle -
                                Handle to the device.

                            keyId -
                                PS key ID to read. Maximum value 0xFFFFFF.

                            valueLen -
                                Size of the data array allocated to hold the key value. A
                                valueLen of 0 indicates that only the length of the key's
                                value is to be read.

                            value -
                                Array of 16-bit words of size "valueLen" to hold the key
                                value. Can be NULL if valueLen is 0.

                            readLen -
                                Pointer to a 16-bit word to hold the length of the key's
                                value.
                                This is the length of the valid value data read for the key
                                (may be less than the "valueLen" given if that exceeds the
                                actual length of the key's value).
                                <p>
                                If the key has not been written or has a zero length value,
                                this value will be set to zero.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to read the audio persistent store key specified (for
                            other PS keys use tePsRead).
                            <p>
                            In the event of failure, if the readLen value has been set to a
                            value greater than valueLen, it means that insufficient storage
                            was provided to read the key value which has a length of readLen.
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs (for
                            BlueCore ICs use the psRead* functions).
                            <p>
                            Refer to the document CS-00304075-SP for further details regarding
                            audio PS keys.

        """
        self.TestEngineDLL.tePsAudioRead.restype = ct.c_int32
        self.TestEngineDLL.tePsAudioRead.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint16, ct.c_void_p, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint16 * max(valueLen, len(value)))(*value)
        local_readLen = ct.c_uint16(readLen)
        retval = self.TestEngineDLL.tePsAudioRead(handle, keyId, valueLen, local_value, ct.byref(local_readLen))
        value = local_value[:]
        readLen = local_readLen.value
        return retval, value, readLen
    # end of tePsAudioRead


    def tePsAudioWrite(self, handle: int, keyId: int, valueLen: int, value: list) -> int:
        r"""Function TestEngine::tePsAudioWrite() wrapper for tePsAudioWrite in TestEngine DLL.

        Python API:
            tePsAudioWrite(handle: int, keyId: int, valueLen: int, value: list) -> int

        Python Example Call Syntax:
            retval = myDll.tePsAudioWrite(handle=0, keyId=0, valueLen=0, value=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 tePsAudioWrite(uint32 handle, uint32 keyId, uint16 valueLen,
                                                 const uint16* value)

            Parameters :    handle -
                                Handle to the device.

                            keyId -
                                PS key ID to write. Maximum value 0xFFFFFF.

                            valueLen -
                                Size of the data array holding the key value. Setting this to
                                zero causes any existing value data for the key to be deleted,
                                with the key remaining present in (or being written to) the
                                store as a flag-like entry.

                            value -
                                Array of 16-bit words of size "valueLen" holding the key
                                value. Can be NULL if valueLen is 0.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Used to write the audio persistent store key specified (for
                            other PS keys use tePsWrite).
                            <p>
                            This function is unsupported for BlueCore and CSRC9xxx ICs (for
                            BlueCore ICs use the psWrite* functions).
                            <p>
                            Refer to the document CS-00304075-SP for further details regarding
                            audio PS keys.

        """
        self.TestEngineDLL.tePsAudioWrite.restype = ct.c_int32
        self.TestEngineDLL.tePsAudioWrite.argtypes = [ct.c_uint32, ct.c_uint32, ct.c_uint16, ct.c_void_p]
        if value == None:
            value = []
        local_value = (ct.c_uint16 * len(value))(*value)
        retval = self.TestEngineDLL.tePsAudioWrite(handle, keyId, valueLen, local_value)
        
        return retval
    # end of tePsAudioWrite


    def teRadGetMaxPayloadLen(self, pktType: int, maxLen: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teRadGetMaxPayloadLen() wrapper for teRadGetMaxPayloadLen in TestEngine DLL.

        Python API:
            teRadGetMaxPayloadLen(pktType: int, maxLen: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, maxLen = myDll.teRadGetMaxPayloadLen(pktType=0)
            print(retval, maxLen)

        Detail From Wrapped C API:
            Function :      int32 teRadGetMaxPayloadLen(uint8 pktType, uint16* maxLen)

            Parameters :    pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x00 =   <td>NULL packets
                                    <tr><td>0x01 =   <td>POLL packets
                                    <tr><td>0x02 =   <td>FHS packets
                                    <tr><td>0x03 =   <td>DM1 packets
                                    <tr><td>0x04 =   <td>DH1 packets
                                    <tr><td>0x05 =   <td>HV1 packets
                                    <tr><td>0x06 =   <td>HV2 packets
                                    <tr><td>0x07 =   <td>HV3 packets
                                    <tr><td>0x08 =   <td>DV packets
                                    <tr><td>0x09 =   <td>AUX1 packets
                                    <tr><td>0x0A =   <td>DM3 packets
                                    <tr><td>0x0B =   <td>DH3 packets
                                    <tr><td>0x0E =   <td>DM5 packets
                                    <tr><td>0x0F =   <td>DH5 packets
                                    <tr><td>0x17 =   <td>EV3 packets
                                    <tr><td>0x1C =   <td>EV4 packets
                                    <tr><td>0x1D =   <td>EV5 packets
                                    <tr><td>0x24 =   <td>2-DH1 packets
                                    <tr><td>0x28 =   <td>3-DH1 packets
                                    <tr><td>0x2A =   <td>2-DH3 packets
                                    <tr><td>0x2B =   <td>3-DH3 packets
                                    <tr><td>0x2E =   <td>2-DH5 packets
                                    <tr><td>0x2F =   <td>3-DH5 packets
                                    <tr><td>0x36 =   <td>2-EV3 packets
                                    <tr><td>0x37 =   <td>3-EV3 packets
                                    <tr><td>0x3C =   <td>2-EV5 packets
                                    <tr><td>0x3D =   <td>3-EV5 packets
                                    <tr><td>0x40 =   <td>LE1M packets
                                    <tr><td>0x41 =   <td>LE2M packets
                                    <tr><td>0x42 =   <td>LE Coded 125k packets
                                    <tr><td>0x43 =   <td>LE Coded 500k packets
                                    <tr><td>0x52 =   <td>QHS-P2 packets
                                    <tr><td>0x53 =   <td>QHS-P3 packets
                                    <tr><td>0x54 =   <td>QHS-P4 packets
                                    <tr><td>0x55 =   <td>QHS-P5 packets
                                    <tr><td>0x56 =   <td>QHS-P6 packets
                                </table>

                            maxLen -
                                Pointer to where the maximum payload length (in bytes) will
                                be stored. Maximum payload lengths are:
                                <table>
                                    <tr><td>NULL = 0
                                    <tr><td>POLL = 0
                                    <tr><td>FHS = 18
                                    <tr><td>DM1 = 17
                                    <tr><td>DH1 = 27
                                    <tr><td>HV1 = 10
                                    <tr><td>HV2 = 20
                                    <tr><td>HV3 = 30
                                    <tr><td>DV = 19
                                    <tr><td>AUX1 = 29
                                    <tr><td>DM3 = 121
                                    <tr><td>DH3 = 183
                                    <tr><td>DM5 = 224
                                    <tr><td>DH5 = 339
                                    <tr><td>EV3 = 30
                                    <tr><td>EV4 = 120
                                    <tr><td>EV5 = 180
                                    <tr><td>2-DH1 = 54
                                    <tr><td>3-DH1 = 83
                                    <tr><td>2-DH3 = 367
                                    <tr><td>3-DH3 = 552
                                    <tr><td>2-DH5 = 679
                                    <tr><td>3-DH5 = 1021
                                    <tr><td>2-EV3 = 60
                                    <tr><td>3-EV3 = 90
                                    <tr><td>2-EV5 = 360
                                    <tr><td>3-EV5 = 540
                                    <tr><td>LE1M = 255*
                                    <tr><td>LE2M = 255*
                                    <tr><td>LE Coded 125k = 255*
                                    <tr><td>LE Coded 500k = 255*
                                    <tr><td>QHS-P2 = 1023
                                    <tr><td>QHS-P3 = 1023
                                    <tr><td>QHS-P4 = 1023
                                    <tr><td>QHS-P5 = 1023
                                    <tr><td>QHS-P6 = 1023
                                </table>
                                <p>
                                *if data length extension is not supported by the device, the
                                maximum will be 37.

            Returns :       <table>
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                            </table>

            Description :   Gets the maximum payload length (in bytes) for a given packet
                            type. If the pktType value is unknown, or maxLen is NULL, an
                            error is returned.
                            <p>
                            A device connection is not required for this function.

        """
        self.TestEngineDLL.teRadGetMaxPayloadLen.restype = ct.c_int32
        self.TestEngineDLL.teRadGetMaxPayloadLen.argtypes = [ct.c_uint8, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        retval = self.TestEngineDLL.teRadGetMaxPayloadLen(pktType, ct.byref(local_maxLen))
        maxLen = local_maxLen.value
        return retval, maxLen
    # end of teRadGetMaxPayloadLen


    def teRadQhsStart(self, handle: int, testMode: int, channel: int, payloadLen: int, payload: int, phyRate: int, txPower: int, maxPackets: int, cteLen: int, cteType: int, slotDuration: int, numAntennae: int, antennaIds: list) -> int:
        r"""Function TestEngine::teRadQhsStart() wrapper for teRadQhsStart in TestEngine DLL.

        Python API:
            teRadQhsStart(handle: int, testMode: int, channel: int, payloadLen: int, payload: int, phyRate: int, txPower: int, maxPackets: int, cteLen: int, cteType: int, slotDuration: int, numAntennae: int, antennaIds: list) -> int

        Python Example Call Syntax:
            retval = myDll.teRadQhsStart(handle=0, testMode=0, channel=0, payloadLen=0, payload=0, phyRate=0, txPower=0, maxPackets=0, cteLen=0, cteType=0, slotDuration=0, numAntennae=0, antennaIds=[0,1])
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadQhsStart(uint32 handle, uint8 testMode,
                                                uint8 channel, uint16 payloadLen,
                                                uint8 payload, uint8 phyRate, uint8 txPower,
                                                uint16 maxPackets, uint8 cteLen,
                                                uint8 cteType, uint8 slotDuration,
                                                uint8 numAntennae, const uint8* antennaIds)

            Parameters :    handle -
                                Handle to the device.

                            testMode -
                                The test mode where:
                                <table>
                                    <tr><td>2 =   <td>TX
                                    <tr><td>3 =   <td>RX
                                </table>
                            
                            channel -
                                The channel to test (0-39), where:
                                frequencyMhz = 2402 + (channel * 2)
                                <p>
                                NOTE: QHS is not supported for channels 0, 12 and 39 in end
                                user scenarios. Therefore, product certification testing with
                                QHS should not be performed on these channels.

                            payloadLen -
                                Length of the payload in each packet (bytes), from 0 to 1023.

                            payload -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>PRBS9
                                    <tr><td>1 =   <td>Alternating nibbles 11110000
                                    <tr><td>2 =   <td>Alternating bits 10101010
                                    <tr><td>3 =   <td>PRBS15
                                    <tr><td>4 =   <td>All ones
                                    <tr><td>5 =   <td>All zeros
                                    <tr><td>6 =   <td>Alternating nibbles 00001111
                                    <tr><td>7 =   <td>Alternating bits 01010101
                                </table>

                            phyRate -
                                The PHY rate, where:
                                <table>
                                    <tr><td>0x06 =   <td>QHS2P 2 Mbps PSK modulation
                                    <tr><td>0x07 =   <td>QHS3P 3 Mbps PSK modulation
                                    <tr><td>0x08 =   <td>QHS4P 4 Mbps PSK modulation
                                    <tr><td>0x09 =   <td>QHS5P 5 Mbps PSK modulation
                                    <tr><td>0x0A =   <td>QHS6P 6 Mbps PSK modulation
                                </table>

                            txPower -
                                TX power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

                            maxPackets -
                                Maximum number of packets to transmit after TX mode is
                                initiated (0 to 0xFFFF). After this count the test mode will
                                automatically end (no need to call teRadStop). If the value is
                                set to 0 the device will transmit indefinitely, unless
                                explicitly stopped with teRadStop.

                            cteLen -
                                Constant Tone Extension length, where:
                                <table>
                                    <tr><td>0 =         <td>Do not transmit CTE
                                    <tr><td>0x2-0x14 =  <td>CTE length in 8 uS units
                                </table>
                                <p>
                                Note that CTE support is IC dependent.

                            cteType -
                                Constant Tone Extension type, where:
                                <table>
                                    <tr><td>0 =   <td>AoA (Angle of Arrival)
                                    <tr><td>1 =   <td>AoD (Angle of Departure) with 1 uS slots
                                    <tr><td>2 =   <td>AoD (Angle of Departure) with 2 uS slots
                                </table>
                                <p>
                                Only relevant if CTE is used (cteLen is non-zero). Note that
                                CTE support is IC dependent.

                            slotDuration -
                                The duration of switching and sampling slots in uS (1-2).
                                <p>
                                Only relevant if CTE is used (cteLen is non-zero). Note that
                                CTE support is IC dependent.

                            numAntennae -
                                The number of antennaIds (0-0x4B).
                                <p>
                                Only relevant if CTE is used (cteLen is non-zero). Note that
                                CTE support is IC dependent.

                            antennaIds -
                                Pointer to an array of numAntennae 8-bit antenna ID values.
                                Can by NULL if numAntennae = 0.
                                <p>
                                Only relevant if CTE is used (cteLen is non-zero). Note that
                                CTE support is IC dependent.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts QHS test modes.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                cout << "Trying to connect TX device..." << endl;
                uint32 txHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected TX device!" << endl;

                    cout << "Trying to connect RX device..." << endl;
                    uint32 rxHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                    if (rxHandle != 0)
                    {
                        cout << "Connected RX device!" << endl;

                        const uint8 TEST_MODE_TX = 2;
                        const uint8 TEST_MODE_RX = 3;
                        const uint8 TEST_CHANNEL = 19;
                        const uint16 PAYLOAD_LEN = 1023;
                        const uint8 PSBS9_PAYLOAD = 0;
                        const uint8 PHY_RATE_QHS6P = 0x0A;
                        const uint8 POWER_LEVEL = 6;

                        // Start transmitting
                        int32 teRet = teRadQhsStart(txHandle, TEST_MODE_TX, TEST_CHANNEL,
                            PAYLOAD_LEN, PSBS9_PAYLOAD, PHY_RATE_QHS6P,
                            POWER_LEVEL, 0, 0, 0, 1, 0, NULL);

                        if (teRet == TE_OK)
                        {
                            // Start receiving
                            teRet = teRadQhsStart(rxHandle, TEST_MODE_RX, TEST_CHANNEL,
                                PAYLOAD_LEN, PSBS9_PAYLOAD, PHY_RATE_QHS6P,
                                POWER_LEVEL, 0, 0, 0, 1, 0, NULL);
                        }

                        if (teRet == TE_OK)
                        {
                            // Wait a period then then get the RX'd packet stats
                            Sleep(1000);

                            uint16 pktLen;
                            const size_t NUM_STATS_CHANNELS = 5;
                            uint32 pktsRxd[NUM_STATS_CHANNELS];
                            uint32 acErrs[NUM_STATS_CHANNELS];
                            uint32 hecErrs[NUM_STATS_CHANNELS];
                            uint32 crcErrs[NUM_STATS_CHANNELS];
                            uint32 totalBitErrs[NUM_STATS_CHANNELS];
                            int16 rssi[NUM_STATS_CHANNELS];
                            uint32 unused;
                            teRet = teRadRxGetStats(rxHandle, &pktLen, pktsRxd, acErrs,
                                hecErrs, crcErrs, totalBitErrs, rssi, &unused);

                            if (teRet == TE_OK)
                            {
                                cout << "Packet stats:" << endl;
                                cout << "Packet length = " << pktLen << endl;
                                cout << "Packets received = " << pktsRxd[0] << endl;
                                cout << "Access code errors = " << acErrs[0] << endl;
                                cout << "HEC errors = " << hecErrs[0] << endl;
                                cout << "CRC errors = " << crcErrs[0] << endl;
                                cout << "Total bit errors = " << totalBitErrs[0] << endl;
                                cout << "RSSI (dBm) = " << rssi[0] << endl;
                            }
                        }

                        closeTestEngine(rxHandle);
                    }

                    closeTestEngine(txHandle);
                }
                        
        """
        self.TestEngineDLL.teRadQhsStart.restype = ct.c_int32
        self.TestEngineDLL.teRadQhsStart.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_void_p]
        if antennaIds == None:
            antennaIds = []
        local_antennaIds = (ct.c_uint8 * len(antennaIds))(*antennaIds)
        retval = self.TestEngineDLL.teRadQhsStart(handle, testMode, channel, payloadLen, payload, phyRate, txPower, maxPackets, cteLen, cteType, slotDuration, numAntennae, local_antennaIds)
        
        return retval
    # end of teRadQhsStart


    def teRadRxContStart(self, handle: int, techType: int, channel: int, swGain: int, lePhy: int) -> int:
        r"""Function TestEngine::teRadRxContStart() wrapper for teRadRxContStart in TestEngine DLL.

        Python API:
            teRadRxContStart(handle: int, techType: int, channel: int, swGain: int, lePhy: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadRxContStart(handle=0, techType=0, channel=0, swGain=0, lePhy=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadRxContStart(uint32 handle, uint8 techType,
                                                   uint8 channel, uint8 swGain, uint8 lePhy)

            Parameters :    handle -
                                Handle to the device.

                            techType -
                                The technology type, where:
                                <table>
                                    <tr><td>0 =   <td>BR/EDR
                                    <tr><td>1 =   <td>LE
                                </table>

                            channel -
                                Bluetooth RF channel:
                                <table>
                                    <tr><td>BR/EDR = <td>0 - 78
                                    <tr><td>LE = <td>0 - 39
                                </table>

                            swGain -
                                Receiver gain level, where:
                                <table>
                                    <tr><td>0 =   <td>High gain
                                    <tr><td>1 =   <td>Normal gain
                                    <tr><td>2 =   <td>Low gain
                                    <tr><td>3 =   <td>Low-Minus gain
                                    <tr><td>4 =   <td>High-Plus gain
                                </table>

                            lePhy -
                                LE PHY, where:
                                <table>
                                    <tr><td>0 =   <td>1M
                                    <tr><td>1 =   <td>2M
                                    <tr><td>2 =   <td>Coded S=8
                                    <tr><td>3 =   <td>Coded S=2
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts continuous receive.
                            <p>
                            The RSSI of an input signal can be obtained using teRadRxGetRssi.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                // NOTE: Example shows another device being used to provide the
                // input (reference) signal. An alternative source can be used, 
                // e.g., a signal generator.

                cout << "Trying to connect TX device..." << endl;
                uint32 txHandle = openTestEngine(USBDBG, "105", 0, 5000, 0);

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected TX device!" << endl;

                    cout << "Trying to connect RX device..." << endl;
                    uint32 rxHandle = openTestEngine(USBDBG, "104", 0, 5000, 0);

                    if (rxHandle != 0)
                    {
                        cout << "Connected RX device!" << endl;

                        const uint8 TECH_TYPE_BREDR = 0;
                        const uint8 CHANNEL = 39;
                        const uint8 SW_GAIN_NORMAL = 1;
                        const uint8 NUM_SAMPLES = 10;
                        const uint8 POWER_LEVEL = 6;
                        const uint8 TX_TYPE_BREDR_CW = 4;

                        // Disable running application
                        int32 teRet = teAppDisable(txHandle, 0);
                        if (teRet == TE_OK)
                        {
                            teRet = teAppDisable(rxHandle, 0);
                        }

                        if (teRet == TE_OK)
                        {
                            // Start transmitting
                            teRet = teRadTxContStart(txHandle, CHANNEL, POWER_LEVEL,
                                TX_TYPE_BREDR_CW, 0, 0);
                        }

                        if (teRet == TE_OK)
                        {
                            // Start receiving
                            teRet = teRadRxContStart(rxHandle, TECH_TYPE_BREDR, CHANNEL,
                                SW_GAIN_NORMAL, 0);
                        }

                        if (teRet == TE_OK)
                        {
                            // Get the RSSI
                            int8 rssi;
                            teRet = teRadRxGetRssi(rxHandle, TECH_TYPE_BREDR, CHANNEL,
                                NUM_SAMPLES, &rssi);
                            if (teRet == TE_OK)
                            {
                                cout << "RSSI (dBm) = " << static_cast<int16>(rssi) << endl;
                            }
                        }

                        closeTestEngine(rxHandle);
                    }

                    closeTestEngine(txHandle);
                }

        """
        self.TestEngineDLL.teRadRxContStart.restype = ct.c_int32
        self.TestEngineDLL.teRadRxContStart.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.teRadRxContStart(handle, techType, channel, swGain, lePhy)
        
        return retval
    # end of teRadRxContStart


    def teRadRxGetRssi(self, handle: int, techType: int, channel: int, numSamples: int, rssi: int=0) -> Tuple[int, int]:
        r"""Function TestEngine::teRadRxGetRssi() wrapper for teRadRxGetRssi in TestEngine DLL.

        Python API:
            teRadRxGetRssi(handle: int, techType: int, channel: int, numSamples: int, rssi: int=0) -> Tuple[int, int]

        Python Example Call Syntax:
            retval, rssi = myDll.teRadRxGetRssi(handle=0, techType=0, channel=0, numSamples=0)
            print(retval, rssi)

        Detail From Wrapped C API:
            Function :      int32 teRadRxGetRssi(uint32 handle, uint8 techType, uint8 channel,
                                                 uint8 numSamples, int8* rssi)

            Parameters :    handle -
                                Handle to the device.

                            techType -
                                The technology type, where:
                                <table>
                                    <tr><td>0 =   <td>BR/EDR
                                    <tr><td>1 =   <td>LE
                                </table>

                            channel -
                                Bluetooth RF channel:
                                <table>
                                    <tr><td>BR/EDR = <td>0 - 78
                                    <tr><td>LE = <td>0 - 39
                                </table>

                            numSamples -
                                The number of samples to use for averaging.

                            rssi -
                                Pointer to where the average RSSI in dBm will be stored.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Gets the RSSI from a device running continuous receive test mode
                            (started with teRadRxContStart).
                            <p>
                            If the device is not running continuous receive test mode, an
                            error may be returned.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadRxContStart.

        """
        self.TestEngineDLL.teRadRxGetRssi.restype = ct.c_int32
        self.TestEngineDLL.teRadRxGetRssi.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_void_p]
        local_rssi = ct.c_int8(rssi)
        retval = self.TestEngineDLL.teRadRxGetRssi(handle, techType, channel, numSamples, ct.byref(local_rssi))
        rssi = local_rssi.value
        return retval, rssi
    # end of teRadRxGetRssi


    def teRadRxGetStats(self, handle: int, pktLen: int=0, pktsRxd: list=None, acErrs: list=None, hecErrs: list=None, crcErrs: list=None, totalBitErrs: list=None, rssi: list=None, reserved: int=0) -> Tuple[int, int, list, list, list, list, list, list, int]:
        r"""Function TestEngine::teRadRxGetStats() wrapper for teRadRxGetStats in TestEngine DLL.

        Python API:
            teRadRxGetStats(handle: int, pktLen: int=0, pktsRxd: list=None, acErrs: list=None, hecErrs: list=None, crcErrs: list=None, totalBitErrs: list=None, rssi: list=None, reserved: int=0) -> Tuple[int, int, list, list, list, list, list, list, int]

        Python Example Call Syntax:
            retval, pktLen, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved = myDll.teRadRxGetStats(handle=0, pktsRxd=[0,1], acErrs=[0,1], hecErrs=[0,1], crcErrs=[0,1], totalBitErrs=[0,1], rssi=[0,1])
            print(retval, pktLen, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved)

        Detail From Wrapped C API:
            Function :      int32 teRadRxGetStats(uint32 handle, uint16* pktLen,
                                                  uint32* pktsRxd, uint32* acErrs,
                                                  uint32* hecErrs, uint32* crcErrs,
                                                  uint32* totalBitErrs, int16* rssi,
                                                  uint32* reserved)

            Parameters :    handle -
                                Handle to the device.

                            pktLen -
                                Pointer to where the expected length (in bytes) of the
                                received packets will be stored.

                            pktsRxd -
                                Pointer to an array of 5 32-bit values where the number of
                                packets received will be stored (for each of 5 channels).

                            acErrs -
                                Pointer to an array of 5 32-bit values where the number of
                                packets with access code errors (not recieved) will be stored
                                (for each of 5 channels).

                            hecErrs -
                                Pointer to an array of 5 32-bit values where the number of
                                packets with HEC errors will be stored (for each of 5
                                channels).

                            crcErrs -
                                Pointer to an array of 5 32-bit values where the number of
                                packets with CRC errors will be stored (for each of 5
                                channels).

                            totalBitErrs -
                                Pointer to an array of 5 32-bit values where the number of
                                packet bit errors will be stored (for each of 5 channels).

                            rssi -
                                Pointer to an array of 5 signed 16-bit values where the
                                average RSSI in dBm will be stored (for each of 5 channels).

                            reserved -
                                Currently unused.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Gets RX statistics from a device running in packet receive test
                            mode (started with teRadRxPktStart).
                            <p>
                            If the device is not running packet receive test mode, an error
                            will be returned.
                            <p>
                            If the hopMode set for teRadTxPktStart and teRadRxPktStart is for
                            hopping over the full range of Bluetooth channels, then packet
                            and error counts are returned as totals in the first element of
                            each array. The other elements are unused in this case.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadTxPktStart.

        """
        self.TestEngineDLL.teRadRxGetStats.restype = ct.c_int32
        self.TestEngineDLL.teRadRxGetStats.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_pktLen = ct.c_uint16(pktLen)
        if pktsRxd == None:
            pktsRxd = []
        local_pktsRxd = (ct.c_uint32 * len(pktsRxd))(*pktsRxd)
        if acErrs == None:
            acErrs = []
        local_acErrs = (ct.c_uint32 * len(acErrs))(*acErrs)
        if hecErrs == None:
            hecErrs = []
        local_hecErrs = (ct.c_uint32 * len(hecErrs))(*hecErrs)
        if crcErrs == None:
            crcErrs = []
        local_crcErrs = (ct.c_uint32 * len(crcErrs))(*crcErrs)
        if totalBitErrs == None:
            totalBitErrs = []
        local_totalBitErrs = (ct.c_uint32 * len(totalBitErrs))(*totalBitErrs)
        if rssi == None:
            rssi = []
        local_rssi = (ct.c_int16 * len(rssi))(*rssi)
        local_reserved = ct.c_uint32(reserved)
        retval = self.TestEngineDLL.teRadRxGetStats(handle, ct.byref(local_pktLen), local_pktsRxd, local_acErrs, local_hecErrs, local_crcErrs, local_totalBitErrs, local_rssi, ct.byref(local_reserved))
        pktLen = local_pktLen.value
        pktsRxd = local_pktsRxd[:]
        acErrs = local_acErrs[:]
        hecErrs = local_hecErrs[:]
        crcErrs = local_crcErrs[:]
        totalBitErrs = local_totalBitErrs[:]
        rssi = local_rssi[:]
        reserved = local_reserved.value
        return retval, pktLen, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved
    # end of teRadRxGetStats


    def teRadRxPktCfg(self, handle: int, numPkts: int) -> int:
        r"""Function TestEngine::teRadRxPktCfg() wrapper for teRadRxPktCfg in TestEngine DLL.

        Python API:
            teRadRxPktCfg(handle: int, numPkts: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadRxPktCfg(handle=0, numPkts=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadRxPktCfg(uint32 handle, uint16 numPkts)

            Parameters :    handle -
                                Handle to the device.

                            numPkts -
                                Number of expected packets (0 = continuous receive).

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Configures the number of expected packets to be received for
                            subsequent executions of teRadRxPktStart. If a fixed number of
                            packets is configured, reception stops after that number of
                            packets has been received.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadTxPktStart.

        """
        self.TestEngineDLL.teRadRxPktCfg.restype = ct.c_int32
        self.TestEngineDLL.teRadRxPktCfg.argtypes = [ct.c_uint32, ct.c_uint16]
        
        retval = self.TestEngineDLL.teRadRxPktCfg(handle, numPkts)
        
        return retval
    # end of teRadRxPktCfg


    def teRadRxPktStart(self, handle: int, channels: list, payload: int, pktType: int, bdAddr: str, hopMode: int, pktLen: int, ltAddr: int, reserved: int) -> int:
        r"""Function TestEngine::teRadRxPktStart() wrapper for teRadRxPktStart in TestEngine DLL.

        Python API:
            teRadRxPktStart(handle: int, channels: list, payload: int, pktType: int, bdAddr: str, hopMode: int, pktLen: int, ltAddr: int, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadRxPktStart(handle=0, channels=[0,1], payload=0, pktType=0, bdAddr='abc', hopMode=0, pktLen=0, ltAddr=0, reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadRxPktStart(uint32 handle, const uint8* channels,
                                                  uint8 payload, uint8 pktType,
                                                  const char* bdAddr, uint8 hopMode,
                                                  uint16 pktLen, uint8 ltAddr,
                                                  uint32 reserved)

            Parameters :    handle -
                                Handle to the device.

                            channels -
                                Pointer to an array of 5 8-bit values specifying Bluetooth RF
                                channels (0-78).

                            payload -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>All zeros
                                    <tr><td>1 =   <td>All ones
                                    <tr><td>2 =   <td>Alternating bit
                                    <tr><td>3 =   <td>Alternating nibble
                                    <tr><td>4 =   <td>Pseudo-random
                                </table>

                            pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x00 =  <td>NULL packets
                                    <tr><td>0x01 =  <td>POLL packets
                                    <tr><td>0x02 =  <td>FHS packets
                                    <tr><td>0x03 =  <td>DM1 packets
                                    <tr><td>0x04 =  <td>DH1 packets
                                    <tr><td>0x05 =  <td>HV1 packets
                                    <tr><td>0x06 =  <td>HV2 packets
                                    <tr><td>0x07 =  <td>HV3 packets
                                    <tr><td>0x08 =  <td>DV packets
                                    <tr><td>0x09 =  <td>AUX1 packets
                                    <tr><td>0x0A =  <td>DM3 packets
                                    <tr><td>0x0B =  <td>DH3 packets
                                    <tr><td>0x0E =  <td>DM5 packets
                                    <tr><td>0x0F =  <td>DH5 packets
                                    <tr><td>0x17 =  <td>EV3 packets
                                    <tr><td>0x1C =  <td>EV4 packets
                                    <tr><td>0x1D =  <td>EV5 packets
                                    <tr><td>0x24 =  <td>2-DH1 packets
                                    <tr><td>0x28 =  <td>3-DH1 packets
                                    <tr><td>0x2A =  <td>2-DH3 packets
                                    <tr><td>0x2B =  <td>3-DH3 packets
                                    <tr><td>0x2E =  <td>2-DH5 packets
                                    <tr><td>0x2F =  <td>3-DH5 packets
                                    <tr><td>0x36 =  <td>2-EV3 packets
                                    <tr><td>0x37 =  <td>3-EV3 packets
                                    <tr><td>0x3C =  <td>2-EV5 packets
                                    <tr><td>0x3D =  <td>3-EV5 packets
                                </table>

                            bdAddr -
                                This is the Central Bluetooth device address as a string of 12
                                hexadecimal values, e.g. "00025B123456".

                            hopMode -
                                Hopping mode, where:
                                <table>
                                    <tr><td>0 =   <td>Device hops over all 5 specified channels.
                                    <tr><td>1 =   <td>Device starts at channel specified in
                                                      channels[0], then hops over the full range
                                                      of Bluetooth channels.
                                </table>

                            pktLen -
                                Length of the payload in each packet (bytes), from 0 to the
                                maximum for the type. See teRadGetMaxPayloadLen for the
                                maximum sizes for each packet type.

                            ltAddr -
                                Logical transport address (0-7).

                            reserved -
                                Currently unused.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts packet receive.
                            <p>
                            Statistics can be obtained using teRadRxGetStats.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadTxPktStart.

        """
        self.TestEngineDLL.teRadRxPktStart.restype = ct.c_int32
        self.TestEngineDLL.teRadRxPktStart.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint8, ct.c_uint8, ct.c_char_p, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint32]
        if channels == None:
            channels = []
        local_channels = (ct.c_uint8 * len(channels))(*channels)
        local_bdAddr = None if bdAddr is None else ct.create_string_buffer(bytes(bdAddr, encoding="UTF-8"))
        retval = self.TestEngineDLL.teRadRxPktStart(handle, local_channels, payload, pktType, local_bdAddr, hopMode, pktLen, ltAddr, reserved)
        
        return retval
    # end of teRadRxPktStart


    def teRadStop(self, handle: int) -> int:
        r"""Function TestEngine::teRadStop() wrapper for teRadStop in TestEngine DLL.

        Python API:
            teRadStop(handle: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadStop(handle=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadStop(uint32 handle)

            Parameters :    handle -
                                Handle to the device.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Stops the current radio test mode.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadTxCwStart.

        """
        self.TestEngineDLL.teRadStop.restype = ct.c_int32
        self.TestEngineDLL.teRadStop.argtypes = [ct.c_uint32]
        
        retval = self.TestEngineDLL.teRadStop(handle)
        
        return retval
    # end of teRadStop


    def teRadTxContStart(self, handle: int, channel: int, power: int, transmitType: int, patternLen: int, bitPattern: int) -> int:
        r"""Function TestEngine::teRadTxContStart() wrapper for teRadTxContStart in TestEngine DLL.

        Python API:
            teRadTxContStart(handle: int, channel: int, power: int, transmitType: int, patternLen: int, bitPattern: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadTxContStart(handle=0, channel=0, power=0, transmitType=0, patternLen=0, bitPattern=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadTxContStart(uint32 handle, uint8 channel, uint8 power,
                                                   uint8 transmitType, uint8 patternLen,
                                                   uint32 bitPattern)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                Bluetooth RF channel:
                                <table>
                                    <tr><td>BR/EDR/QHS =  <td>0 - 78
                                    <tr><td>LE =          <td>0 - 39
                                </table>

                            power -
                                Power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

                            transmitType -
                                The transmission type where:
                                <p>
                                For BR/EDR:
                                <table>
                                    <tr><td>0x04 =  <td>Carrier (CW) only
                                    <tr><td>0x05 =  <td>1-PRBS9 (GFSK)
                                    <tr><td>0x06 =  <td>1-PRBS15 (GFSK)
                                    <tr><td>0x07 =  <td>1-Pattern (GFSK)
                                    <tr><td>0x08 =  <td>2-PRBS9 (pi/4-DQPSK)
                                    <tr><td>0x09 =  <td>2-PRBS15 (pi/4-DQPSK)
                                    <tr><td>0x0A =  <td>2-Pattern (pi/4-DQPSK)
                                    <tr><td>0x0B =  <td>3-PRBS9 (8DPSK)
                                    <tr><td>0x0C =  <td>3-PRBS15 (8DPSK)
                                    <tr><td>0x0D =  <td>3-Pattern (8DPSK)
                                </table>
                                <p>
                                For LE:
                                <table>
                                    <tr><td>0x24 =  <td>Carrier (CW) only
                                    <tr><td>0x25 =  <td>LE1M-PRBS9 (GMSK)
                                    <tr><td>0x26 =  <td>LE1M-PRBS15 (GMSK)
                                    <tr><td>0x27 =  <td>LE1M-Pattern (GMSK)
                                    <tr><td>0x28 =  <td>LE2M-PRBS9 (GMSK)
                                    <tr><td>0x29 =  <td>LE2M-PRBS15 (GMSK)
                                    <tr><td>0x2A =  <td>LE2M-Pattern (GMSK)
                                </table>
                                <p>
                                For QHS:
                                <table>
                                    <tr><td>0x2B =  <td>QHS-P2-PRBS9 (pi/4-QPSK)
                                    <tr><td>0x2C =  <td>QHS-P2-PRBS15 (pi/4-QPSK)
                                    <tr><td>0x2D =  <td>QHS-P2-Pattern (pi/4-QPSK)
                                    <tr><td>0x2E =  <td>QHS-P3-PRBS9 (pi/4-QPSK)
                                    <tr><td>0x2F =  <td>QHS-P3-PRBS15 (pi/4-QPSK)
                                    <tr><td>0x30 =  <td>QHS-P3-Pattern (pi/4-QPSK)
                                    <tr><td>0x31 =  <td>QHS-P4-PRBS9 (pi/4-DQPSK)
                                    <tr><td>0x32 =  <td>QHS-P4-PRBS15 (pi/4-DQPSK)
                                    <tr><td>0x33 =  <td>QHS-P4-Pattern (pi/4-DQPSK)
                                    <tr><td>0x34 =  <td>QHS-P5-PRBS9 (8PSK)
                                    <tr><td>0x35 =  <td>QHS-P5-PRBS15 (8PSK)
                                    <tr><td>0x36 =  <td>QHS-P5-Pattern (8PSK)
                                    <tr><td>0x37 =  <td>QHS-P6-PRBS9 (8DPSK)
                                    <tr><td>0x38 =  <td>QHS-P6-PRBS15 (8DPSK)
                                    <tr><td>0x39 =  <td>QHS-P6-Pattern (8DPSK)
                                </table>
                                <p>
                                Note that using transmitType 0x04 results in the same output
                                as teRadTxCwStart.

                            patternLen -
                                Specifies the length of the repeated pattern in bits (1 - 32).
                                <p>
                                Only used if the transmitType is one of the "Pattern" types.

                            bitPattern -
                                Bit pattern to transmit (repeatedly).
                                <p>
                                Only used if the transmitType is one of the "Pattern" types.
                                Only the least significant patternLen bits are used.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts continuous transmission.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                cout << "Trying to connect device..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected device!" << endl;

                    // Disable running application
                    int32 teRet = teAppDisable(teHandle, 0);

                    if (teRet == TE_OK)
                    {
                        // Start transmitting 1-PRBS9 on channel 39, power level 6,
                        // using repeated "10" bit pattern.
                        teRet = teRadTxContStart(teHandle, 39, 6, 0x05, 2, 0x2);

                        if (teRet == TE_OK)
                        {
                            // Measure output here

                            // Stop transmission
                            teRet = teRadStop(teHandle);
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teRadTxContStart.restype = ct.c_int32
        self.TestEngineDLL.teRadTxContStart.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_uint32]
        
        retval = self.TestEngineDLL.teRadTxContStart(handle, channel, power, transmitType, patternLen, bitPattern)
        
        return retval
    # end of teRadTxContStart


    def teRadTxCwStart(self, handle: int, channel: int, power: int) -> int:
        r"""Function TestEngine::teRadTxCwStart() wrapper for teRadTxCwStart in TestEngine DLL.

        Python API:
            teRadTxCwStart(handle: int, channel: int, power: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadTxCwStart(handle=0, channel=0, power=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadTxCwStart(uint32 handle, uint8 channel, uint8 power)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                Bluetooth RF channel (0-78).

                            power -
                                Power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts unmodulated continuous Carrier Wave transmission.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                cout << "Trying to connect device..." << endl;
                uint32 teHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (teHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected device!" << endl;

                    // Disable running application
                    int32 teRet = teAppDisable(teHandle, 0);

                    if (teRet == TE_OK)
                    {
                        // Start transmitting
                        teRet = teRadTxCwStart(teHandle, 39, 6);

                        if (teRet == TE_OK)
                        {
                            // Measure output here

                            // Stop transmission
                            teRet = teRadStop(teHandle);
                        }
                    }

                    closeTestEngine(teHandle);
                }

        """
        self.TestEngineDLL.teRadTxCwStart.restype = ct.c_int32
        self.TestEngineDLL.teRadTxCwStart.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.teRadTxCwStart(handle, channel, power)
        
        return retval
    # end of teRadTxCwStart


    def teRadTxPktStart(self, handle: int, channels: list, payload: int, pktType: int, power: int, bdAddr: str, hopMode: int, pktLen: int, ltAddr: int, reserved: int) -> int:
        r"""Function TestEngine::teRadTxPktStart() wrapper for teRadTxPktStart in TestEngine DLL.

        Python API:
            teRadTxPktStart(handle: int, channels: list, payload: int, pktType: int, power: int, bdAddr: str, hopMode: int, pktLen: int, ltAddr: int, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadTxPktStart(handle=0, channels=[0,1], payload=0, pktType=0, power=0, bdAddr='abc', hopMode=0, pktLen=0, ltAddr=0, reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadTxPktStart(uint32 handle, const uint8* channels,
                                                  uint8 payload, uint8 pktType,
                                                  uint8 power, const char* bdAddr,
                                                  uint8 hopMode, uint16 pktLen, uint8 ltAddr,
                                                  uint32 reserved)

            Parameters :    handle -
                                Handle to the device.

                            channels -
                                Pointer to an array of 5 8-bit values specifying Bluetooth RF
                                channels (0-78).

                            payload -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>All zeros
                                    <tr><td>1 =   <td>All ones
                                    <tr><td>2 =   <td>Alternating bit
                                    <tr><td>3 =   <td>Alternating nibble
                                    <tr><td>4 =   <td>Pseudo-random
                                </table>

                            pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x00 =   <td>NULL packets
                                    <tr><td>0x01 =   <td>POLL packets
                                    <tr><td>0x02 =   <td>FHS packets
                                    <tr><td>0x03 =   <td>DM1 packets
                                    <tr><td>0x04 =   <td>DH1 packets
                                    <tr><td>0x05 =   <td>HV1 packets
                                    <tr><td>0x06 =   <td>HV2 packets
                                    <tr><td>0x07 =   <td>HV3 packets
                                    <tr><td>0x08 =   <td>DV packets
                                    <tr><td>0x09 =   <td>AUX1 packets
                                    <tr><td>0x0A =   <td>DM3 packets
                                    <tr><td>0x0B =   <td>DH3 packets
                                    <tr><td>0x0E =   <td>DM5 packets
                                    <tr><td>0x0F =   <td>DH5 packets
                                    <tr><td>0x17 =   <td>EV3 packets
                                    <tr><td>0x1C =   <td>EV4 packets
                                    <tr><td>0x1D =   <td>EV5 packets
                                    <tr><td>0x24 =   <td>2-DH1 packets
                                    <tr><td>0x28 =   <td>3-DH1 packets
                                    <tr><td>0x2A =   <td>2-DH3 packets
                                    <tr><td>0x2B =   <td>3-DH3 packets
                                    <tr><td>0x2E =   <td>2-DH5 packets
                                    <tr><td>0x2F =   <td>3-DH5 packets
                                    <tr><td>0x36 =   <td>2-EV3 packets
                                    <tr><td>0x37 =   <td>3-EV3 packets
                                    <tr><td>0x3C =   <td>2-EV5 packets
                                    <tr><td>0x3D =   <td>3-EV5 packets
                                </table>

                            power -
                                Power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

                            bdAddr -
                                This is the Central Bluetooth device address as a string of 12
                                hexadecimal values, e.g. "00025B123456".

                            hopMode -
                                Hopping mode, where:
                                <table>
                                    <tr><td>0 =   <td>Device hops over all 5 specified channels.
                                    <tr><td>1 =   <td>Device starts at channel specified in
                                                      channels[0], then hops over the full range
                                                      of Bluetooth channels.
                                </table>

                            pktLen -
                                Length of the payload in each packet (bytes), from 0 to the
                                maximum for the type. See teRadGetMaxPayloadLen for the
                                maximum sizes for each packet type.

                            ltAddr -
                                Logical transport address (0-7).

                            reserved -
                                Currently unused.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts packet transmission.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :

                cout << "Trying to connect TX device..." << endl;
                uint32 txHandle = openTestEngine(TRB, "1", 0, 5000, 0);

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected TX device!" << endl;

                    cout << "Trying to connect RX device..." << endl;
                    uint32 rxHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                    if (rxHandle != 0)
                    {
                        cout << "Connected RX device!" << endl;

                        const size_t NUM_CHANNELS = 5;
                        const uint8 TEST_CHANNELS[NUM_CHANNELS] = { 0, 19, 39, 58, 78 };
                        const uint8 PSEUDO_RANDOM_PAYLOAD_PATTERN = 4;
                        const uint8 DH5_PACKET_TYPE = 0x0F;
                        const uint8 POWER_LEVEL = 6;
                        const string MASTER_BD_ADDR = "00025B03FF01";
                        const uint8 HOP_5 = 0;
                        const uint16 MAX_DH5_PACKET_BYTES = 339;
                        const uint8 LT_ADDR = 1;

                        // Set RX device to continuous receive
                        int32 teRet = teRadRxPktCfg(rxHandle, 0);

                        if (teRet == TE_OK)
                        {
                            // Start transmitting
                            teRet = teRadTxPktStart(txHandle, TEST_CHANNELS,
                                PSEUDO_RANDOM_PAYLOAD_PATTERN, DH5_PACKET_TYPE,
                                POWER_LEVEL, MASTER_BD_ADDR.c_str(), HOP_5,
                                MAX_DH5_PACKET_BYTES, LT_ADDR, 0);
                        }

                        if (teRet == TE_OK)
                        {
                            // Start receiving
                            teRet = teRadRxPktStart(rxHandle, TEST_CHANNELS,
                                PSEUDO_RANDOM_PAYLOAD_PATTERN, DH5_PACKET_TYPE,
                                MASTER_BD_ADDR.c_str(), HOP_5, MAX_DH5_PACKET_BYTES, LT_ADDR,
                                0);
                        }

                        if (teRet == TE_OK)
                        {
                            // Wait a period then then get the RX'd packet stats
                            Sleep(1000);

                            uint16 pktLen;
                            uint32 pktsRxd[NUM_CHANNELS];
                            uint32 acErrs[NUM_CHANNELS];
                            uint32 hecErrs[NUM_CHANNELS];
                            uint32 crcErrs[NUM_CHANNELS];
                            uint32 totalBitErrs[NUM_CHANNELS];
                            int16 rssi[NUM_CHANNELS];
                            uint32 unused;
                            teRet = teRadRxGetStats(rxHandle, &pktLen, pktsRxd, acErrs,
                                hecErrs, crcErrs, totalBitErrs, rssi, &unused);

                            if (teRet == TE_OK)
                            {
                                cout << "Packet stats:" << endl;
                                cout << "Packet length = " << pktLen << endl;
                                cout << "Packets received = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << pktsRxd[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                                cout << "Access code errors = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << acErrs[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                                cout << "HEC errors = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << hecErrs[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                                cout << "CRC errors = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << crcErrs[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                                cout << "Total bit errors = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << totalBitErrs[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                                cout << "RSSI (dBm) = ";
                                for (size_t i = 0; i < NUM_CHANNELS; ++i)
                                {
                                    cout << rssi[i];
                                    if (i < NUM_CHANNELS - 1) cout << ", ";
                                }
                                cout << endl;
                            }
                        }

                        closeTestEngine(rxHandle);
                    }

                    closeTestEngine(txHandle);
                }

        """
        self.TestEngineDLL.teRadTxPktStart.restype = ct.c_int32
        self.TestEngineDLL.teRadTxPktStart.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_char_p, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint32]
        if channels == None:
            channels = []
        local_channels = (ct.c_uint8 * len(channels))(*channels)
        local_bdAddr = None if bdAddr is None else ct.create_string_buffer(bytes(bdAddr, encoding="UTF-8"))
        retval = self.TestEngineDLL.teRadTxPktStart(handle, local_channels, payload, pktType, power, local_bdAddr, hopMode, pktLen, ltAddr, reserved)
        
        return retval
    # end of teRadTxPktStart


    def teRadLeTxBurst(self, handle: int, hopMode: int, payloadLen: int, payloadType: int, pktType: int, power: int) -> int:
        r"""Function TestEngine::teRadLeTxBurst() wrapper for teRadLeTxBurst in TestEngine DLL.

        Python API:
            teRadLeTxBurst(handle: int, hopMode: int, payloadLen: int, payloadType: int, pktType: int, power: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadLeTxBurst(handle=0, hopMode=0, payloadLen=0, payloadType=0, pktType=0, power=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadLeTxBurst(uint32 handle, uint8 hopMode,
                                                 uint16 payloadLen, uint8 payloadType,
                                                 uint8 pktType, uint8 power)

            Parameters :    handle -
                                Handle to the device.

                            hopMode -
                                Hopping mode, where if a valid hop offset (0x5-0x10) is
                                provided, transmission starts at channel 0 and continues
                                hopping with "offset x 2MHz" as the channel spacing between
                                hops.
                                If a value outside the valid hop offset range is provided,
                                a hop offset of 1 is used to hop over all 40 LE channels.

                            payloadLen -
                                Length of the payload in each packet (bytes), from 0 to max,
                                where max is 255 for LE packets, and 1023 for QHS packets.

                            payloadType -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>PRBS9
                                    <tr><td>1 =   <td>Alternating nibbles 11110000
                                    <tr><td>2 =   <td>Alternating bits 10101010
                                    <tr><td>3 =   <td>PRBS15
                                    <tr><td>4 =   <td>All ones
                                    <tr><td>5 =   <td>All zeros
                                    <tr><td>6 =   <td>Alternating nibbles 00001111
                                    <tr><td>7 =   <td>Alternating bits 01010101
                                </table>

                            pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x01 =   <td>LE1M
                                    <tr><td>0x02 =   <td>LE2M
                                    <tr><td>0x03 =   <td>LE Coded 125k
                                    <tr><td>0x04 =   <td>LE Coded 500k
                                    <tr><td>0x05 =   <td>LE1M and Coded Simultaneous Scan
                                    <tr><td>0x06 =   <td>QHS-P2
                                    <tr><td>0x07 =   <td>QHS-P3
                                    <tr><td>0x08 =   <td>QHS-P4
                                    <tr><td>0x09 =   <td>QHS-P5
                                    <tr><td>0x0A =   <td>QHS-P6
                                </table>

                            power -
                                Power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Starts transmission of Bluetooth LE/QHS packets while bursting.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

        """
        self.TestEngineDLL.teRadLeTxBurst.restype = ct.c_int32
        self.TestEngineDLL.teRadLeTxBurst.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestEngineDLL.teRadLeTxBurst(handle, hopMode, payloadLen, payloadType, pktType, power)
        
        return retval
    # end of teRadLeTxBurst


    def teRadTxEnhanced(self, handle: int, channel: int, pktType: int, payloadLen: int, payloadType: int, payloadPattern: int, transmitType: int, ltAddr: int, hopping: int, bdAddr: str, maxPkts: int, offSlots: int, power: int) -> int:
        r"""Function TestEngine::teRadTxEnhanced() wrapper for teRadTxEnhanced in TestEngine DLL.

        Python API:
            teRadTxEnhanced(handle: int, channel: int, pktType: int, payloadLen: int, payloadType: int, payloadPattern: int, transmitType: int, ltAddr: int, hopping: int, bdAddr: str, maxPkts: int, offSlots: int, power: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadTxEnhanced(handle=0, channel=0, pktType=0, payloadLen=0, payloadType=0, payloadPattern=0, transmitType=0, ltAddr=0, hopping=0, bdAddr='abc', maxPkts=0, offSlots=0, power=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadTxEnhanced(uint32 handle, uint8 channel,
                                                  uint8 pktType, uint16 payloadLen,
                                                  uint8 payloadType, uint32 payloadPattern,
                                                  uint8 transmitType, uint8 ltAddr,
                                                  uint8 hopping, const char* bdAddr,
                                                  uint32 maxPkts, uint8 offSlots, uint8 power)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                Bluetooth RF channel:
                                <table>
                                    <tr><td>BR/EDR = <td>0 - 78
                                    <tr><td>LE/QHS = <td>0 - 39
                                </table>

                            pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x00 =   <td>NULL packets
                                    <tr><td>0x01 =   <td>POLL packets
                                    <tr><td>0x02 =   <td>FHS packets
                                    <tr><td>0x03 =   <td>DM1 packets
                                    <tr><td>0x04 =   <td>DH1 packets
                                    <tr><td>0x05 =   <td>HV1 packets
                                    <tr><td>0x06 =   <td>HV2 packets
                                    <tr><td>0x07 =   <td>HV3 packets
                                    <tr><td>0x08 =   <td>DV packets
                                    <tr><td>0x09 =   <td>AUX1 packets
                                    <tr><td>0x0A =   <td>DM3 packets
                                    <tr><td>0x0B =   <td>DH3 packets
                                    <tr><td>0x0E =   <td>DM5 packets
                                    <tr><td>0x0F =   <td>DH5 packets
                                    <tr><td>0x17 =   <td>EV3 packets
                                    <tr><td>0x1C =   <td>EV4 packets
                                    <tr><td>0x1D =   <td>EV5 packets
                                    <tr><td>0x24 =   <td>2-DH1 packets
                                    <tr><td>0x28 =   <td>3-DH1 packets
                                    <tr><td>0x2A =   <td>2-DH3 packets
                                    <tr><td>0x2B =   <td>3-DH3 packets
                                    <tr><td>0x2E =   <td>2-DH5 packets
                                    <tr><td>0x2F =   <td>3-DH5 packets
                                    <tr><td>0x36 =   <td>2-EV3 packets
                                    <tr><td>0x37 =   <td>3-EV3 packets
                                    <tr><td>0x3C =   <td>2-EV5 packets
                                    <tr><td>0x3D =   <td>3-EV5 packets
                                    <tr><td>0x40 =   <td>LE1M packets
                                    <tr><td>0x41 =   <td>LE2M packets
                                    <tr><td>0x42 =   <td>LE Coded 125k packets
                                    <tr><td>0x43 =   <td>LE Coded 500k packets
                                    <tr><td>0x52 =   <td>QHS-P2 packets
                                    <tr><td>0x53 =   <td>QHS-P3 packets
                                    <tr><td>0x54 =   <td>QHS-P4 packets
                                    <tr><td>0x55 =   <td>QHS-P5 packets
                                    <tr><td>0x56 =   <td>QHS-P6 packets
                                </table>

                            payloadLen -
                                Length of the payload in each packet (bytes). See 
                                teRadGetMaxPayloadLen for the maximum sizes for each packet
                                type.

                            payloadType -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>PRBS9
                                    <tr><td>1 =   <td>Alternating nibbles 11110000
                                    <tr><td>2 =   <td>Alternating bits 10101010
                                    <tr><td>3 =   <td>PRBS15
                                    <tr><td>4 =   <td>All ones
                                    <tr><td>5 =   <td>All zeros
                                    <tr><td>6 =   <td>Alternating nibbles 00001111
                                    <tr><td>7 =   <td>Alternating bits 01010101
                                    <tr><td>8 =   <td>Pattern defined by payloadPattern
                                </table>

                            payloadPattern - 
                                Pattern to be used when payloadType = 8.

                            transmitType - 
                                The transmission type, where:
                                <table>
                                    <tr><td>0 =   <td>Bursting
                                    <tr><td>1 =   <td>Continuous
                                </table>
                                
                            ltAddr -
                                Logical transport address (1-7). Ignored for LE and QHS.

                            hopping -
                                Defines the hopping parameters, where:
                                <p>
                                Bits 0-3 define the hopping offset n, where:
                                next_channel = (current_channel + n) MOD max_channel.
                                Note: When n=0, the same channel is always used.
                                <p>
                                Bits 4-5 define the number of band-edge channels to remove.
                                <p>
                                Bits 6-7 define the channel usage, where:
                                <table>
                                    <tr><td>0 =   <td>Use all channels
                                    <tr><td>1 =   <td>Use only odd numbered channels
                                    <tr><td>2 =   <td>Use only even numbered channels
                                </table>

                            bdAddr -
                                Bluetooth device address as a string of 12 hexadecimal values,
                                e.g. "00025B123456".
                                For BR/EDR, it is the Central Bluetooth device address.
                                For LE it is ingored (but must be provided).
                                For QHS only the least significant 8 hexadecimal values are
                                used to define the 32-bit Access Address used to create a
                                Coded Access Address (but 12 hexadecimal values must be
                                provided).

                            maxPkts -
                                Maximum number of packets to transmit after TX mode is
                                initiated. After this count the test mode will automatically
                                end (no need to call teRadStop). If the value is set to 0 the
                                device will transmit indefinitely, unless explicitly stopped
                                with teRadStop.

                            offSlots -
                                Number of off slots between TX packets when bursting. Ignored
                                for continuous transmission (see transmitType).

                            power -
                                Power level (0-n, where 0 is the lower power).
                                <p>
                                Note that the highest usable power level is dependent on the
                                device power table configuration.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command causes the device to transmit Bluetooth BR/EDR, LE or
                            QHS packets while bursting or in a continuous transmission mode.
                            It can be used for device to device testing with an other device
                            running teRadRxEnhanced.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs). Support is also
                            dependent on the firmware version present on the device.

            Example :

                cout << "Trying to connect TX device..." << endl;
                uint32 txHandle = openTestEngine(USBDBG, "1", 0, 5000, 0);

                if (txHandle != TE_INVALID_HANDLE_VALUE)
                {
                    cout << "Connected TX device!" << endl;

                    cout << "Trying to connect RX device..." << endl;
                    uint32 rxHandle = openTestEngine(USBDBG, "2", 0, 5000, 0);

                    if (rxHandle != 0)
                    {
                        cout << "Connected RX device!" << endl;

                        const uint8 TEST_CHANNEL = 39;
                        const uint8 DH5_PACKET_TYPE = 0x0F;
                        const uint16 MAX_DH5_PACKET_BYTES = 339;
                        const uint8 PRBS9_PAYLOAD_TYPE = 0;
                        const uint32 PAYLOAD_PATTERN = 0;
                        const uint8 TRANSMIT_TYPE_BURSTING = 0;
                        const uint8 LT_ADDR = 1;
                        const uint8 HOPPING = 0;
                        const string BD_ADDR = "00025B03FF01";
                        const uint32 MAX_PACKETS = 100;
                        const uint8 OFF_SLOTS = 1;
                        const uint8 POWER_LEVEL = 6;
                        const uint8 SW_GAIN = 3;

                        // Start receiving
                        int32 teRet = teRadRxEnhanced(rxHandle, TEST_CHANNEL, DH5_PACKET_TYPE,
                            MAX_DH5_PACKET_BYTES, PRBS9_PAYLOAD_TYPE, PAYLOAD_PATTERN,
                            TRANSMIT_TYPE_BURSTING, LT_ADDR, HOPPING, BD_ADDR.c_str(),
                            MAX_PACKETS, OFF_SLOTS, SW_GAIN);

                        if (teRet == TE_OK)
                        {
                            // Start transmitting
                            teRet = teRadTxEnhanced(txHandle, TEST_CHANNEL, DH5_PACKET_TYPE,
                                MAX_DH5_PACKET_BYTES, PRBS9_PAYLOAD_TYPE, PAYLOAD_PATTERN,
                                TRANSMIT_TYPE_BURSTING, LT_ADDR, HOPPING, BD_ADDR.c_str(),
                                MAX_PACKETS, OFF_SLOTS, POWER_LEVEL);
                        }

                        if (teRet == TE_OK)
                        {
                            // Wait a period then then get the RX'd packet stats
                            Sleep(1000);

                            uint32 pktsRxd;
                            uint32 acErrs;
                            uint32 hecErrs;
                            uint32 crcErrs;
                            uint32 totalBitErrs;
                            int16 rssi;
                            uint32 unused;
                            teRet = teRadRxGetStatsEnhanced(rxHandle, &pktsRxd, &acErrs,
                                &hecErrs, &crcErrs, &totalBitErrs, &rssi, &unused);

                            if (teRet == TE_OK)
                            {
                                cout << "Packet stats:" << endl;
                                cout << "Packets received = " << pktsRxd << endl;
                                cout << "Access code errors = " << acErrs << endl;
                                cout << "HEC errors = " << hecErrs << endl;
                                cout << "CRC errors = " << crcErrs << endl;
                                cout << "Total bit errors = " << totalBitErrs << endl;
                                cout << "RSSI (dBm) = " << rssi << endl;
                            }
                        }

                        closeTestEngine(rxHandle);
                    }

                    closeTestEngine(txHandle);
                }

        """
        self.TestEngineDLL.teRadTxEnhanced.restype = ct.c_int32
        self.TestEngineDLL.teRadTxEnhanced.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_char_p, ct.c_uint32, ct.c_uint8, ct.c_uint8]
        local_bdAddr = None if bdAddr is None else ct.create_string_buffer(bytes(bdAddr, encoding="UTF-8"))
        retval = self.TestEngineDLL.teRadTxEnhanced(handle, channel, pktType, payloadLen, payloadType, payloadPattern, transmitType, ltAddr, hopping, local_bdAddr, maxPkts, offSlots, power)
        
        return retval
    # end of teRadTxEnhanced


    def teRadRxEnhanced(self, handle: int, channel: int, pktType: int, payloadLen: int, payloadType: int, payloadPattern: int, receiveType: int, ltAddr: int, hopping: int, bdAddr: str, maxPkts: int, offSlots: int, rxSwGain: int) -> int:
        r"""Function TestEngine::teRadRxEnhanced() wrapper for teRadRxEnhanced in TestEngine DLL.

        Python API:
            teRadRxEnhanced(handle: int, channel: int, pktType: int, payloadLen: int, payloadType: int, payloadPattern: int, receiveType: int, ltAddr: int, hopping: int, bdAddr: str, maxPkts: int, offSlots: int, rxSwGain: int) -> int

        Python Example Call Syntax:
            retval = myDll.teRadRxEnhanced(handle=0, channel=0, pktType=0, payloadLen=0, payloadType=0, payloadPattern=0, receiveType=0, ltAddr=0, hopping=0, bdAddr='abc', maxPkts=0, offSlots=0, rxSwGain=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 teRadRxEnhanced(uint32 handle, uint8 channel,
                                                  uint8 pktType, uint16 payloadLen,
                                                  uint8 payloadType, uint32 payloadPattern,
                                                  uint8 receiveType, uint8 ltAddr,
                                                  uint8 hopping, const char* bdAddr,
                                                  uint32 maxPkts, uint8 offSlots,
                                                  uint8 rxSwGain)

            Parameters :    handle -
                                Handle to the device.

                            channel -
                                Bluetooth RF channel:
                                <table>
                                    <tr><td>BR/EDR = <td>0 - 78
                                    <tr><td>LE/QHS = <td>0 - 39
                                </table>

                            pktType -
                                The packet type, where:
                                <table>
                                    <tr><td>0x00 =   <td>NULL packets
                                    <tr><td>0x01 =   <td>POLL packets
                                    <tr><td>0x02 =   <td>FHS packets
                                    <tr><td>0x03 =   <td>DM1 packets
                                    <tr><td>0x04 =   <td>DH1 packets
                                    <tr><td>0x05 =   <td>HV1 packets
                                    <tr><td>0x06 =   <td>HV2 packets
                                    <tr><td>0x07 =   <td>HV3 packets
                                    <tr><td>0x08 =   <td>DV packets
                                    <tr><td>0x09 =   <td>AUX1 packets
                                    <tr><td>0x0A =   <td>DM3 packets
                                    <tr><td>0x0B =   <td>DH3 packets
                                    <tr><td>0x0E =   <td>DM5 packets
                                    <tr><td>0x0F =   <td>DH5 packets
                                    <tr><td>0x17 =   <td>EV3 packets
                                    <tr><td>0x1C =   <td>EV4 packets
                                    <tr><td>0x1D =   <td>EV5 packets
                                    <tr><td>0x24 =   <td>2-DH1 packets
                                    <tr><td>0x28 =   <td>3-DH1 packets
                                    <tr><td>0x2A =   <td>2-DH3 packets
                                    <tr><td>0x2B =   <td>3-DH3 packets
                                    <tr><td>0x2E =   <td>2-DH5 packets
                                    <tr><td>0x2F =   <td>3-DH5 packets
                                    <tr><td>0x36 =   <td>2-EV3 packets
                                    <tr><td>0x37 =   <td>3-EV3 packets
                                    <tr><td>0x3C =   <td>2-EV5 packets
                                    <tr><td>0x3D =   <td>3-EV5 packets
                                    <tr><td>0x40 =   <td>LE1M packets
                                    <tr><td>0x41 =   <td>LE2M packets
                                    <tr><td>0x42 =   <td>LE Coded 125k packets
                                    <tr><td>0x43 =   <td>LE Coded 500k packets
                                    <tr><td>0x52 =   <td>QHS-P2 packets
                                    <tr><td>0x53 =   <td>QHS-P3 packets
                                    <tr><td>0x54 =   <td>QHS-P4 packets
                                    <tr><td>0x55 =   <td>QHS-P5 packets
                                    <tr><td>0x56 =   <td>QHS-P6 packets
                                </table>

                            payloadLen -
                                Length of the payload in each packet (bytes). See 
                                teRadGetMaxPayloadLen for the maximum sizes for each packet
                                type.

                            payloadType -
                                The packet payload bit pattern, where:
                                <table>
                                    <tr><td>0 =   <td>PRBS9
                                    <tr><td>1 =   <td>Alternating nibbles 11110000
                                    <tr><td>2 =   <td>Alternating bits 10101010
                                    <tr><td>3 =   <td>PRBS15
                                    <tr><td>4 =   <td>All ones
                                    <tr><td>5 =   <td>All zeros
                                    <tr><td>6 =   <td>Alternating nibbles 00001111
                                    <tr><td>7 =   <td>Alternating bits 01010101
                                    <tr><td>8 =   <td>Pattern defined by payloadPattern
                                </table>

                            payloadPattern - 
                                Pattern to be used when payloadType = 8.

                            receiveType - 
                                The reception type, where:
                                <table>
                                    <tr><td>0 =   <td>Bursting
                                    <tr><td>1 =   <td>Continuous
                                </table>
                                
                            ltAddr -
                                Logical transport address (1-7). Ignored for LE and QHS.

                            hopping -
                                Defines the hopping parameters, where:
                                <p>
                                Bits 0-3 define the hopping offset n, where:
                                next_channel = (current_channel + n) MOD max_channel.
                                Note: When n=0, the same channel is always used.
                                <p>
                                Bits 4-5 define the number of band-edge channels to remove.
                                <p>
                                Bits 6-7 define the channel usage, where:
                                <table>
                                    <tr><td>0 =   <td>Use all channels
                                    <tr><td>1 =   <td>Use only odd numbered channels
                                    <tr><td>2 =   <td>Use only even numbered channels
                                </table>

                            bdAddr -
                                Bluetooth device address as a string of 12 hexadecimal values,
                                e.g. "00025B123456".
                                For BR/EDR, it is the Central Bluetooth device address.
                                For LE it is ingored (but must be provided).
                                For QHS only the least significant 8 hexadecimal values are
                                used to define the 32-bit Access Address used to create a
                                Coded Access Address (but 12 hexadecimal values must be
                                provided).

                            maxPkts -
                                Maximum number of packets to receive after RX mode is
                                initiated. After this count the test mode will automatically
                                end (no need to call teRadStop). If the value is set to 0 the
                                device will receive indefinitely, unless explicitly stopped
                                with teRadStop.

                            offSlots -
                                Number of off slots between TX packets when bursting. Ignored
                                for continuous transmission (see transmitType).

                            rxSwGain -
                                Receiver gain level, where:
                                <table>
                                    <tr><td>0 =   <td>GS0 (Gain state 0), lowest gain
                                    <tr><td>1 =   <td>GS1
                                    <tr><td>2 =   <td>GS2
                                    <tr><td>3 =   <td>GS3
                                    <tr><td>4 =   <td>GS4
                                    <tr><td>5 =   <td>GS5 (Gain state 5), highest gain
                                </table>

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   This command causes the device to receive Bluetooth packets while
                            bursting or in a continuous reception mode. When the receiveType
                            is continuous, stats can be read from the device using
                            teRadRxGetStatsEnhanced.
                            It can be used for device to device testing with an other device
                            running teRadTxEnhanced.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs). Support is also
                            dependent on the firmware version present on the device.

            Example :       See example code for teRadTxEnhanced.

        """
        self.TestEngineDLL.teRadRxEnhanced.restype = ct.c_int32
        self.TestEngineDLL.teRadRxEnhanced.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint16, ct.c_uint8, ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8, ct.c_char_p, ct.c_uint32, ct.c_uint8, ct.c_uint8]
        local_bdAddr = None if bdAddr is None else ct.create_string_buffer(bytes(bdAddr, encoding="UTF-8"))
        retval = self.TestEngineDLL.teRadRxEnhanced(handle, channel, pktType, payloadLen, payloadType, payloadPattern, receiveType, ltAddr, hopping, local_bdAddr, maxPkts, offSlots, rxSwGain)
        
        return retval
    # end of teRadRxEnhanced


    def teRadRxGetStatsEnhanced(self, handle: int, pktsRxd: int=0, acErrs: int=0, hecErrs: int=0, crcErrs: int=0, totalBitErrs: int=0, rssi: int=0, reserved: int=0) -> Tuple[int, int, int, int, int, int, int, int]:
        r"""Function TestEngine::teRadRxGetStatsEnhanced() wrapper for teRadRxGetStatsEnhanced in TestEngine DLL.

        Python API:
            teRadRxGetStatsEnhanced(handle: int, pktsRxd: int=0, acErrs: int=0, hecErrs: int=0, crcErrs: int=0, totalBitErrs: int=0, rssi: int=0, reserved: int=0) -> Tuple[int, int, int, int, int, int, int, int]

        Python Example Call Syntax:
            retval, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved = myDll.teRadRxGetStatsEnhanced(handle=0)
            print(retval, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved)

        Detail From Wrapped C API:
            Function :      int32 teRadRxGetStatsEnhanced(uint32 handle, uint32* pktsRxd,
                                                          uint32* acErrs, uint32* hecErrs,
                                                          uint32* crcErrs,
                                                          uint32* totalBitErrs, int16* rssi,
                                                          uint32* reserved)

            Parameters :    handle -
                                Handle to the device.

                            pktsRxd -
                                Pointer to where the number of packets received will be
                                stored.

                            acErrs -
                                Pointer to where the number of packets with access code errors
                                (not recieved) will be stored.

                            hecErrs -
                                Pointer to where the number of packets with HEC errors will be
                                stored.

                            crcErrs -
                                Pointer to where the number of packets with CRC errors will be
                                stored.

                            totalBitErrs -
                                Pointer to where the number of packet bit errors will be
                                stored.

                            rssi -
                                Pointer to where the average RSSI in dBm will be stored.

                            reserved -
                                Currently unused.

            Returns :       <table>
                                <tr><td>-1 = Invalid handle
                                <tr><td>0 = Error
                                <tr><td>1 = Success
                                <tr><td>2 = Unsupported function
                            </table>

            Description :   Gets RX statistics from a device running the enhanced receive test
                            mode (started with teRadRxEnhanced), and in bursting receive mode
                            (stats cannot be reported in continuous receive mode). The
                            statistics returned are accumulated over all channels when hopping
                            is used.
                            <p>
                            This function is supported only for devices supporting QHCI
                            commands (QCC304x / QCC514x and later ICs).

            Example :       See example code for teRadTxEnhanced.

        """
        self.TestEngineDLL.teRadRxGetStatsEnhanced.restype = ct.c_int32
        self.TestEngineDLL.teRadRxGetStatsEnhanced.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_pktsRxd = ct.c_uint32(pktsRxd)
        local_acErrs = ct.c_uint32(acErrs)
        local_hecErrs = ct.c_uint32(hecErrs)
        local_crcErrs = ct.c_uint32(crcErrs)
        local_totalBitErrs = ct.c_uint32(totalBitErrs)
        local_rssi = ct.c_int16(rssi)
        local_reserved = ct.c_uint32(reserved)
        retval = self.TestEngineDLL.teRadRxGetStatsEnhanced(handle, ct.byref(local_pktsRxd), ct.byref(local_acErrs), ct.byref(local_hecErrs), ct.byref(local_crcErrs), ct.byref(local_totalBitErrs), ct.byref(local_rssi), ct.byref(local_reserved))
        pktsRxd = local_pktsRxd.value
        acErrs = local_acErrs.value
        hecErrs = local_hecErrs.value
        crcErrs = local_crcErrs.value
        totalBitErrs = local_totalBitErrs.value
        rssi = local_rssi.value
        reserved = local_reserved.value
        return retval, pktsRxd, acErrs, hecErrs, crcErrs, totalBitErrs, rssi, reserved
    # end of teRadRxGetStatsEnhanced



    #
    # DEPRECATED FUNCTIONS
    #
    bccmdPsuBuckReg = bccmdPsuSmpsEnable
    bccmdPsuMicEn = bccmdPsuHvLinearEnable
    bccmdLed0 = bccmdLed0Enable
    bccmdLed1 = bccmdLed1Enable
    bccmdChargerSupressLed0 = bccmdChargerSuppressLed0
    openTestEngineSpi = openTestEngineDebug
    openTestEngineSpiTrans = openTestEngineDebugTrans
    openTestEngineSpiUnlock = openTestEngineDebugUnlock
    openTestEngineSpiUnlockTrans = openTestEngineDebugUnlockTrans
    teGetAvailableSpiPorts = teGetAvailableDebugPorts

# endclass TestEngine

  