################################################################################
#  TestFlashAPI.py : Declares the DLL functions for Python.
#  Copyright (c) 2022 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Auto-generated Python wrapper for TestFlash DLL.
#  Created on 2022-11-18 15:14 from TestFlash.h file"
################################################################################

import os
import ctypes as ct
from typing import Tuple

class TestFlash():
    """
    A python wrapper class for TestFlash DLL.
    Usage:
        myDll = TestFlash("<DLL_PATH>" [, debug=False])    
    """
    def __init__(self, path_to_dll):
        """Load the TestFlash DLL"""
        self.TestFlashDLL = None
        try:
            full_path = os.path.realpath(path_to_dll)
            if full_path.strip().lower().endswith('.dll'):
                path_to_dll = os.path.dirname(full_path) + '\\'  # Extract directory from DLL name
                
            if not path_to_dll.endswith('\\'):
                path_to_dll += '\\'

            if not path_to_dll + ';' in os.environ['PATH']: # add this to the path if not already present
                os.environ['PATH'] = path_to_dll + ';' + os.environ['PATH']

            self.TestFlashDLL = ct.windll.LoadLibrary(path_to_dll + 'TestFlash')
        except Exception as e:
            print("Cannot load TestFlash.dll from " + path_to_dll)
            if ct.sizeof(ct.c_void_p) == 8:
                print("Check that the DLL is present and 64 bit.\n"
                      "64 bit Python can only be used with 64 bit DLL")
            else:
                print("Check that the DLL is present and 32 bit\n"
                      "32 bit Python can only be used with 32 bit DLL")
            raise e
    # end __init__

    #
    # Pre-defined constants that may be used as parameter values or returns from the TestFlash API
    #

    TFL_OK = 0
    TFL_ERROR = -1
    TFL_DEVICE_ERROR = -2
    TFL_ERROR_UNSUPPORTED = -3
    TFL_SPI_LPT = 0x1
    TFL_SPI_USB = 0x2
    TFL_TRB = 0x3
    TFL_USBDBG = 0x4
    TFL_CHIP = 0
    TFL_FILE = 1
    TFL_ERROR_OPEN_FAILED = 0x1001
    TFL_ERROR_DEVICE_OPEN = 0x1002
    TFL_ERROR_DEVICE_NOT_OPEN = 0x1003
    TFL_ERROR_DEVICE_BUSY = 0x1004
    TFL_ERROR_THREAD_ERROR = 0x1005
    TFL_ERROR_RESET_FAIL = 0x1006
    TFL_ERROR_WRONG_TRANS = 0x1008
    TFL_ERROR_SPIUNLOCK = 0x1009
    TFL_MAX_DEVICES = 32
    TFL_ALL_DEVICES = 0xFFFFFFFF
    TFL_TYPE_STANDARD = 0x0
    TFL_TYPE_SPIF = 0x1
    TFL_TYPE_SQIF = 0x2
    TFL_TYPE_MTP = 0x3
    TFL_TYPE_OTP = 0x4
    TFL_TYPE_SMEM = 0x5
    TFL_TYPE_E2 = 0x6
    TFL_TRANS_CRIT_NOLOCK = 0x00000001
    TFL_TRANS_CRIT_UNLOCKED = 0x00000002
    TFL_TRANS_CRIT_LOCKED = 0x00000004
    TFL_TRANS_CRIT_ALL = 0x00000007
    TFL_TRANS_CRIT_DEFAULT = 0x00000003

    #
    # Exported routines for the TestFlash API
    #

    def flOpen(self, port: int, xtal: int, delays: int, transport: int) -> int:
        r"""Function TestFlash::flOpen() wrapper for flOpen in TestFlash DLL.

        Python API:
            flOpen(port: int, xtal: int, delays: int, transport: int) -> int

        Python Example Call Syntax:
            retval = myDll.flOpen(port=0, xtal=0, delays=0, transport=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flOpen(int32 port, int32 xtal, int32 delays,
                                         int32 transport)

            Parameters :    port -
                                For USB or LPT transports:
                                Defines the physical port to use. An LPT port number starting
                                from 1, or the id number of a USB SPI device. Set to -1 to
                                use the default (port 1 if LPT, first USB SPI device if USB).
                                NOTE: Default may be overridden by the "SPIPORT" environment
                                variable.
                                <p>
                                For TRB or USBDBG transports:
                                For TRB, the serial number of the usb2trb converter e.g.
                                "123456" may be used. For USBDBG, the port identifier of the
                                corresponding USB Hub Filter (e.g. "100") may be used.
                                Alternatively, a sequence number ranging from 1 to the number
                                of connected devices may be used for TRB and USBDBG. For
                                further details of TRB and USBDBG device identifiers, refer
                                to CS-00410202-UG.

                            xtal -
                                Specifies module's crystal frequency. Acceptable values are
                                10, 16, 26, 32. Higher values make code run slower, lower
                                values may cause instability. (Casiras use 16Mhz).
                                <p>
                                This parameter is only applicable to BlueCore ICs.

                            delays -
                                For transports types TFL_SPI_LPT or TFL_SPI_USB, this
                                represents the delay used in driving the SPI port.
                                1 = fastest SPI speed, but may give unreliability.
                                2 = reasonable value, higher values may be better if chip is
                                in deep sleep.
                                <p>
                                For other transport types this value is unused.

                            transport -
                                Defines the transport to be used, where:
                                    <table>
                                        <tr><td>TFL_SPI_LPT <td>1
                                        <tr><td>TFL_SPI_USB <td>2
                                        <tr><td>TFL_TRB     <td>3
                                        <tr><td>TFL_USBDBG  <td>4
                                    </table>
                                Set to -1 to use the default (from SPITRANS environment
                                variable if present), otherwise LPT.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is one of the flOpen* set of functions used to
                            create the appropriate host side objects to enable NVM
                            programming via a single debug or gang programming interface.
                            <p>
                            To be used (only) with devices which are not transport locked.
                            flOpenTrans can also be used to do this.
                            <p>
                            flOpenUnlock or flOpenUnlockTrans should be used with transport
                            locked devices.
                            <p>
                            This is an entry point to the single connection version of
                            TestFlash. This can be used when programming a single device, and
                            must be used when using a parallel port gang programmer with
                            devices which are not transport locked.
                            <p>
                            In the case of a gang programmer being used, this function does
                            not verify whether the chips can be communicated with.

        """
        self.TestFlashDLL.flOpen.restype = ct.c_int32
        self.TestFlashDLL.flOpen.argtypes = [ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32]
        
        retval = self.TestFlashDLL.flOpen(port, xtal, delays, transport)
        
        return retval
    # end of flOpen


    def flOpenUnlock(self, port: int, xtal: int, delays: int, transport: int, unlockKey: str) -> int:
        r"""Function TestFlash::flOpenUnlock() wrapper for flOpenUnlock in TestFlash DLL.

        Python API:
            flOpenUnlock(port: int, xtal: int, delays: int, transport: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.flOpenUnlock(port=0, xtal=0, delays=0, transport=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flOpenUnlock(int32 port, int32 xtal, int32 delays,
                                               int32 transport, const char* unlockKey)

            Parameters :    port -
                                For USB or LPT transports:
                                Defines the physical port to use. An LPT port number starting
                                from 1, or the id number of a USB SPI device. Set to -1 to
                                use the default (port 1 if LPT, first USB SPI device if USB).
                                NOTE: Default may be overridden by the "SPIPORT" environment
                                variable.
                                <p>
                                For TRB or USBDBG transports:
                                For TRB, the serial number of the usb2trb converter e.g.
                                "123456" may be used. For USBDBG, the port identifier of the
                                corresponding USB Hub Filter (e.g. "100") may be used.
                                Alternatively, a sequence number ranging from 1 to the number
                                of connected devices may be used for TRB and USBDBG. For
                                further details of TRB and USBDBG device identifiers, refer
                                to CS-00410202-UG.

                            xtal -
                                Specifies module's crystal frequency. Acceptable values are
                                10, 16, 26, 32. Higher values make code run slower, lower
                                values may cause instability. (Casiras use 16Mhz).
                                <p>
                                This parameter is only applicable to BlueCore ICs.

                            delays -
                                For transports types TFL_SPI_LPT or TFL_SPI_USB, this
                                represents the delay used in driving the SPI port.
                                1 = fastest SPI speed, but may give unreliability.
                                2 = reasonable value, higher values may be better if chip is
                                in deep sleep.
                                <p>
                                Where transport = TFL_USBDBG, this parameter will define how
                                long the function will retry, in ms, when trying to detect if
                                the specified USBDBG device has enumerated. It has been found
                                that some PC's take a longer time than expected to enumerate a
                                USB device and, in some cases, the PC's internal USB hub may
                                have been reset which can cause a further delay in enumeration.
                                This parameter can be set to accommodate the extra time taken
                                to reset USB devices.
                                <p>
                                For other transport types this value is unused.

                            transport -
                                Defines the transport to be used, where:
                                    <table>
                                        <tr><td>TFL_SPI_LPT <td>1
                                        <tr><td>TFL_SPI_USB <td>2
                                        <tr><td>TFL_TRB     <td>3
                                        <tr><td>TFL_USBDBG  <td>4
                                        </table>
                                Set to -1 to use the default (from SPITRANS environment
                                variable if present), otherwise LPT.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".
                                <p>
                                Can be NULL if unlocking is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is one of the flOpen* set of functions used to
                            create the appropriate host side objects to enable NVM
                            programming via a single debug or gang programming interface.
                            <p>
                            To be used (only) with transport locked devices.
                            flOpenUnlockTrans can also be used to do this.
                            <p>
                            flOpen or flOpenTrans should be used with devices which are not
                            transport locked.
                            <p>
                            This is an entry point to the single connection version of
                            TestFlash. This can be used when programming a single device, and
                            must be used when using a parallel port gang programmer with
                            transport locked devices.
                            <p>
                            In the case of a gang programmer being used, this function does
                            not verify whether the chips can be communicated with.

        """
        self.TestFlashDLL.flOpenUnlock.restype = ct.c_int32
        self.TestFlashDLL.flOpenUnlock.argtypes = [ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32, ct.c_char_p]
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestFlashDLL.flOpenUnlock(port, xtal, delays, transport, local_unlockKey)
        
        return retval
    # end of flOpenUnlock


    def flmOpen(self, deviceMask: int, xtal: int, transport: int) -> int:
        r"""Function TestFlash::flmOpen() wrapper for flmOpen in TestFlash DLL.

        Python API:
            flmOpen(deviceMask: int, xtal: int, transport: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmOpen(deviceMask=0, xtal=0, transport=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmOpen(uint32 deviceMask, int32 xtal, int32 transport);

            Parameters :    deviceMask -
                                A bit mask of the devices to be opened. For example, to open
                                devices 2 and 4 using USB-SPI, TRB or USBDBG connections, a
                                device mask of 0x0A would be used.
                                <p>
                                NOTE: Devices are opened according to their port number, i.e.
                                in the case of USB-SPI, the order of enumeration, where bit 0
                                being set means that port 0 will be opened. For LPT-SPI, port
                                numbers start at 1, therefore bit 0 is unused, and bit 1 must
                                be set to open LPT1. For TRB and USBDBG transports, the bit
                                positions refer to the order of the adapter serial numbers
                                (for USBDBG, the port identifiers of the corresponding USB Hub
                                Filters), with bit 0 being the first device (port 1, lowest
                                adapter serial number / USB Hub Filter port identifier). For
                                further details of TRB and USBDBG device identifiers, refer
                                to CS-00410202-UG.

                            xtal -
                                See flOpen.

                            transport -
                                See flOpen.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>


            Description:    This is the multiple connection version of flOpen. See flOpen for
                            more details.
                            <p>
                            To be used (only) with devices which are not transport locked.
                            flmOpenTrans can be used as an alternative to flmOpen.
                            <p>
                            flmOpenUnlock or flmOpenUnlockTrans should be used with transport
                            locked devices.
                            <p>
                            This function will fail if the chip(s) cannot be communicated
                            with. If the return value is TFL_DEVICE_ERROR, use
                            flmGetBitErrorField to determine which devices failed or succeeded.
                            <p>
                            This is an entry point for the multiple connection version of
                            TestFlash. This must be used when programming multiple devices
                            which are not transport locked, but not when using a parallel
                            port gang programmer.
                            <p>
                            flmOpen can either be called with a mask specifying all devices to
                            open, or it can be called multiple times to open multiple devices
                            (the devices in the mask must be different for each call). In the
                            case of multiple calls to flmOpen, the transport type must be the
                            same for each call.

        """
        self.TestFlashDLL.flmOpen.restype = ct.c_int32
        self.TestFlashDLL.flmOpen.argtypes = [ct.c_uint32, ct.c_int32, ct.c_int32]
        
        retval = self.TestFlashDLL.flmOpen(deviceMask, xtal, transport)
        
        return retval
    # end of flmOpen


    def flmOpenUnlock(self, deviceMask: int, xtal: int, transport: int, unlockKey: str) -> int:
        r"""Function TestFlash::flmOpenUnlock() wrapper for flmOpenUnlock in TestFlash DLL.

        Python API:
            flmOpenUnlock(deviceMask: int, xtal: int, transport: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.flmOpenUnlock(deviceMask=0, xtal=0, transport=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmOpenUnlock(uint32 deviceMask, int32 xtal,
                                                int32 transport, const char* unlockKey);

            Parameters :    deviceMask -
                                A bit mask of the devices to be opened. For example, to open
                                devices 2 and 4 using USB-SPI connections, a device mask of
                                0x0A would be used.
                                <p>
                                NOTE: Devices are opened according to their port number, i.e.
                                in the case of USB-SPI, the order of enumeration, where bit 0
                                being set means that port 0 will be opened. For LPT-SPI, port
                                numbers start at 1, therefore bit 0 is unused, and bit 1 must
                                be set to open LPT1. For TRB and USBDBG transports, the bit
                                positions refer to the order of the adapter serial numbers
                                (for USBDBG, the port identifiers of the corresponding USB Hub
                                Filters), with bit 0 being the first device (port 1, lowest
                                adapter serial number / USB Hub Filter port identifier). For
                                further details of TRB and USBDBG device identifiers, refer
                                to CS-00410202-UG.

                            xtal -
                                See flOpen.

                            transport -
                                See flOpen.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".
                                <p>
                                Can be NULL if unlocking is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>


            Description:    This is the multiple connection version of flOpenUnlock. See
                            flOpenUnlock for more details.
                            <p>
                            To be used (only) with transport locked devices.
                            flmOpenUnlockTrans can be used as an alternative to flmOpenUnlock.
                            <p>
                            flmOpen or flmOpenTrans should be used with devices which are not
                            transport locked.
                            <p>
                            This function will fail if the chip(s) cannot be communicated
                            with. If the return value is TFL_DEVICE_ERROR, use
                            flmGetBitErrorField to determine which devices failed or succeeded.
                            <p>
                            This is an entry point for the multiple connection version of
                            TestFlash. This must be used when programming multiple transport
                            locked devices, but not when using a parallel port gang programmer
                            to do so.
                            <p>
                            flmOpenUnlock can either be called with a mask specifying all
                            devices to open, or it can be called multiple times to open
                            multiple devices (the devices in the mask must be different for
                            each call). In the case of multiple calls to flmOpen, the
                            transport type must be the same for each call.

        """
        self.TestFlashDLL.flmOpenUnlock.restype = ct.c_int32
        self.TestFlashDLL.flmOpenUnlock.argtypes = [ct.c_uint32, ct.c_int32, ct.c_int32, ct.c_char_p]
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmOpenUnlock(deviceMask, xtal, transport, local_unlockKey)
        
        return retval
    # end of flmOpenUnlock


    def flOpenTrans(self, trans: str, xtal: int, delays: int) -> int:
        r"""Function TestFlash::flOpenTrans() wrapper for flOpenTrans in TestFlash DLL.

        Python API:
            flOpenTrans(trans: str, xtal: int, delays: int) -> int

        Python Example Call Syntax:
            retval = myDll.flOpenTrans(trans='abc', xtal=0, delays=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flOpenTrans(const char* trans, int32 xtal, int32 delays)

            Parameters :    trans -
                                String of space separated transport options that define the
                                transport to use. Commonly used options include:
                                    SPITRANS (The physical transport to use, e.g. LPT, USB,
                                              TRB, USBDBG)
                                    SPIPORT (The port number)
                                E.g. for LPT1, trans would be "SPITRANS=LPT SPIPORT=1".
                                These options override any environment variables of the same
                                names.
                                The transport string may be one of those returned by
                                flGetAvailablePorts, which returns transport strings for
                                all available ports.

                            xtal -
                                Specifies module's crystal frequency. Acceptable values are
                                10, 16, 26, 32. Higher values make code run slower, lower
                                values may cause instability. (Casiras use 16Mhz).
                                <p>
                                This parameter is only applicable to BlueCore ICs.

                            delays -
                                For transports types TFL_SPI_LPT or TFL_SPI_USB, this
                                represents the delay used in driving the SPI port.
                                1 = fastest SPI speed, but may give unreliability.
                                2 = reasonable value, higher values may be better if chip is
                                in deep sleep.
                                <p>
                                For other transport types this value is unused.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is one of the flOpen* set of functions used to
                            create the appropriate host side objects to enable NVM
                            programming via a debug or gang programming interface.
                            <p>
                            To be used (only) with devices which are not transport locked.
                            flOpen can also be used to do this.
                            <p>
                            flOpenUnlock or flOpenUnlockTrans should be used with transport
                            locked devices.
                            <p>
                            The trans string may be one of those returned by
                            flGetAvailableports, which returns transport strings for all
                            available ports.
                            <p>
                            In the case of a gang programmer being used, this function does
                            not verify whether the chips can be communicated with.

        """
        self.TestFlashDLL.flOpenTrans.restype = ct.c_int32
        self.TestFlashDLL.flOpenTrans.argtypes = [ct.c_char_p, ct.c_int32, ct.c_int32]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        retval = self.TestFlashDLL.flOpenTrans(local_trans, xtal, delays)
        
        return retval
    # end of flOpenTrans


    def flOpenUnlockTrans(self, trans: str, xtal: int, delays: int, unlockKey: str) -> int:
        r"""Function TestFlash::flOpenUnlockTrans() wrapper for flOpenUnlockTrans in TestFlash DLL.

        Python API:
            flOpenUnlockTrans(trans: str, xtal: int, delays: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.flOpenUnlockTrans(trans='abc', xtal=0, delays=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flOpenUnlockTrans(const char* trans, int32 xtal,
                                                    int32 delays, const char* unlockKey)

            Parameters :    trans -
                                String of space separated transport options that define the
                                transport to use. Commonly used options include:
                                    SPITRANS (The physical transport to use, e.g. LPT, USB,
                                              TRB, USBDBG)
                                    SPIPORT (The port number)
                                E.g. for LPT1, trans would be "SPITRANS=LPT SPIPORT=1".
                                These options override any environment variables of the same
                                names.
                                The transport string may be one of those returned by
                                flGetAvailablePorts, which returns transport strings for
                                all available ports.

                            xtal -
                                Specifies module's crystal frequency. Acceptable values are
                                10, 16, 26, 32. Higher values make code run slower, lower
                                values may cause instability. (Casiras use 16Mhz).
                                <p>
                                This parameter is only applicable to BlueCore ICs.

                            delays -
                                For transports types TFL_SPI_LPT or TFL_SPI_USB, this
                                represents the delay used in driving the SPI port.
                                1 = fastest SPI speed, but may give unreliability.
                                2 = reasonable value, higher values may be better if chip is
                                in deep sleep.
                                <p>
                                Where transport = TFL_USBDBG, this parameter will define how
                                long the function will retry, in ms, when trying to detect if
                                the specified USBDBG device has enumerated. It has been found
                                that some PC's take a longer time than expected to enumerate a
                                USB device and, in some cases, the PC's internal USB hub may
                                have been reset which can cause a further delay in enumeration.
                                This parameter can be set to accommodate the extra time taken
                                to reset USB devices. If USB is not used then this value can
                                be set to 0.
                                <p>
                                For other transport types this value is unused.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".
                                <p>
                                Can be NULL if unlocking is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is one of the flOpen* set of functions used to
                            create the appropriate host side objects to enable NVM
                            programming via a debug or gang programming interface.
                            <p>
                            To be used (only) with devices which are transport locked.
                            flOpenUnlock can also be used to do this.
                            <p>
                            flOpen or flOpenTrans should be used with devices which are not
                            transport locked.
                            <p>
                            The trans string may be one of those returned by
                            flGetAvailablePorts, which returns transport strings for all
                            available ports.
                            <p>
                            In the case of a gang programmer being used, this function does
                            not verify whether the chips can be communicated with.

        """
        self.TestFlashDLL.flOpenUnlockTrans.restype = ct.c_int32
        self.TestFlashDLL.flOpenUnlockTrans.argtypes = [ct.c_char_p, ct.c_int32, ct.c_int32, ct.c_char_p]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestFlashDLL.flOpenUnlockTrans(local_trans, xtal, delays, local_unlockKey)
        
        return retval
    # end of flOpenUnlockTrans


    def flmOpenTrans(self, deviceMask: int, trans: str, xtal: int) -> int:
        r"""Function TestFlash::flmOpenTrans() wrapper for flmOpenTrans in TestFlash DLL.

        Python API:
            flmOpenTrans(deviceMask: int, trans: str, xtal: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmOpenTrans(deviceMask=0, trans='abc', xtal=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmOpenTrans(uint32 deviceMask, const char* trans,
                                               int32 xtal);

            Parameters :    deviceMask -
                                See flmOpen for the details of this parameter.

                            trans -
                                See flOpenTrans. The transport string given to flmOpenTrans
                                cannot contain a SPIPORT specifier (see
                                flmGetAvailablePorts and flmConvertPort).

                            xtal -
                                See flOpenTrans.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This is the multiple connection version of flOpenTrans. See
                            flOpenTrans for more details. flmOpen can also be used as an
                            alternative to flmOpenTrans.
                            <p>
                            To be used (only) with devices which are not transport locked.
                            <p>
                            flmOpenUnlock or flmOpenUnlockTrans should be used with transport
                            locked devices.
                            <p>
                            This function will fail if the chip(s) cannot be communicated
                            with. If the return value is TFL_DEVICE_ERROR, use
                            flmGetBitErrorField to determine which devices failed / succeeded.
                            <p>
                            This is the entry point for the multiple connection version of
                            TestFlash. This must be used when programming multiple devices,
                            but not when using a parallel port gang programmer to do so.
                            <p>
                            flmOpenTrans can either be called with a mask specifying all
                            devices to open, or it can be called multiple times to open
                            multiple devices (the devices in the mask must be different for
                            each call). In the case of multiple calls to flmOpen, the
                            transport type must be the same for each call.

        """
        self.TestFlashDLL.flmOpenTrans.restype = ct.c_int32
        self.TestFlashDLL.flmOpenTrans.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_int32]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmOpenTrans(deviceMask, local_trans, xtal)
        
        return retval
    # end of flmOpenTrans


    def flmOpenUnlockTrans(self, deviceMask: int, trans: str, xtal: int, unlockKey: str) -> int:
        r"""Function TestFlash::flmOpenUnlockTrans() wrapper for flmOpenUnlockTrans in TestFlash DLL.

        Python API:
            flmOpenUnlockTrans(deviceMask: int, trans: str, xtal: int, unlockKey: str) -> int

        Python Example Call Syntax:
            retval = myDll.flmOpenUnlockTrans(deviceMask=0, trans='abc', xtal=0, unlockKey='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmOpenUnlockTrans(uint32 deviceMask, const char* trans,
                                                     int32 xtal, const char* unlockKey);

            Parameters :    deviceMask -
                                See flmOpen for the details of this parameter.

                            trans -
                                See flOpenTrans. The transport string given to flmOpenTrans
                                cannot contain a SPIPORT specifier (see
                                flmGetAvailablePorts and flmConvertPort).

                            xtal -
                                See flOpenTrans.

                            unlockKey -
                                Defines the unlock key. By default, the unlock key should be
                                supplied unencrypted. For USBDBG only, the user can override
                                the default and supply an encrypted key - this must be
                                prefaced with 'ENC', for example,
                                "ENCdc0ed85df9611abb7249cdd168c5467e".
                                <p>
                                Can be NULL if unlocking is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This is the multiple connection version of flOpenUnlockTrans. See
                            flOpenUnlockTrans for more details.
                            flmOpenUnlock can also be used as an alternative to
                            flmOpenUnlockTrans.
                            <p>
                            To be used (only) with transport locked devices.
                            <p>
                            flmOpen or flmOpenTrans should be used with devices which are not
                            transport locked.
                            <p>
                            This function will fail if the chip(s) cannot be communicated
                            with. If the return value is TFL_DEVICE_ERROR, use
                            flmGetBitErrorField to determine which devices failed / succeeded.
                            <p>
                            This is the entry point for the multiple connection version of
                            TestFlash. This must be used when programming multiple devices,
                            but not when using a parallel port gang programmer to do so.
                            <p>
                            flmOpenTrans can either be called with a mask specifying all
                            devices to open, or it can be called multiple times to open
                            multiple devices (the devices in the mask must be different for
                            each call). In the case of multiple calls to flmOpen, the
                            transport type must be the same for each call.

 *************************************************************************************/
        """
        self.TestFlashDLL.flmOpenUnlockTrans.restype = ct.c_int32
        self.TestFlashDLL.flmOpenUnlockTrans.argtypes = [ct.c_uint32, ct.c_char_p, ct.c_int32, ct.c_char_p]
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"))
        local_unlockKey = None if unlockKey is None else ct.create_string_buffer(bytes(unlockKey, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmOpenUnlockTrans(deviceMask, local_trans, xtal, local_unlockKey)
        
        return retval
    # end of flmOpenUnlockTrans


    def flReadProgramFiles(self, fileName: str) -> int:
        r"""Function TestFlash::flReadProgramFiles() wrapper for flReadProgramFiles in TestFlash DLL.

        Python API:
            flReadProgramFiles(fileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flReadProgramFiles(fileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flReadProgramFiles(const char* fileName)

            Parameters :    fileName -
                                String containing the image file path, where the supported
                                file types (identified by their extension) are:
                                <ol>
                                    <li>XUV
                                    <li>HEX or IHEX
                                    <li>XPV/XDV pair of files
                                    <li>IMG
                                </ol>
                                If the given file extension is XPV or XDV, both XPV and XDV
                                extension files will be read.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is used to load image files into memory.

        """
        self.TestFlashDLL.flReadProgramFiles.restype = ct.c_int32
        self.TestFlashDLL.flReadProgramFiles.argtypes = [ct.c_char_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flReadProgramFiles(local_fileName)
        
        return retval
    # end of flReadProgramFiles


    def flmReadProgramFiles(self, fileName: str) -> int:
        r"""Function TestFlash::flmReadProgramFiles() wrapper for flmReadProgramFiles in TestFlash DLL.

        Python API:
            flmReadProgramFiles(fileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flmReadProgramFiles(fileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmReadProgramFiles(const char* fileName)

            Parameters :    fileName -
                                See flReadProgramFiles. If this parameter is a zero-length
                                string then the current image is cleared and TFL_OK is
                                returned.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This is the multiple connection version of flReadProgramFiles.
                            See flReadProgramFiles for more information. flmReadProgramFiles
                            can be called before flmOpen and flmOpenTrans.

        """
        self.TestFlashDLL.flmReadProgramFiles.restype = ct.c_int32
        self.TestFlashDLL.flmReadProgramFiles.argtypes = [ct.c_char_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmReadProgramFiles(local_fileName)
        
        return retval
    # end of flmReadProgramFiles


    def flProgramBlock(self) -> int:
        r"""Function TestFlash::flProgramBlock() wrapper for flProgramBlock in TestFlash DLL.

        Python API:
            flProgramBlock() -> int

        Python Example Call Syntax:
            retval = myDll.flProgramBlock()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flProgramBlock(void)

            Parameters :    None

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as defined for flGetLastError.

            Description :   This function is used to program a device. The function will
                            block until the process has completed successfully or an error
                            occurs.

        """
        self.TestFlashDLL.flProgramBlock.restype = ct.c_int32
        self.TestFlashDLL.flProgramBlock.argtypes = []
        
        retval = self.TestFlashDLL.flProgramBlock()
        
        return retval
    # end of flProgramBlock


    def flmProgramBlock(self, deviceMask: int, eraseFirst: int, verifyAfter: int, restartAfter: int) -> int:
        r"""Function TestFlash::flmProgramBlock() wrapper for flmProgramBlock in TestFlash DLL.

        Python API:
            flmProgramBlock(deviceMask: int, eraseFirst: int, verifyAfter: int, restartAfter: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmProgramBlock(deviceMask=0, eraseFirst=0, verifyAfter=0, restartAfter=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmProgramBlock(uint32 deviceMask, uint8 eraseFirst,
                                                  uint8 verifyAfter, uint8 restartAfter)

            Parameters :    deviceMask -
                                Specifies which devices will be programmed. See flmOpen for
                                the details of this parameter.

                            eraseFirst -
                                Set to 1 to erase the entire NVM of all devices before
                                programming. Set to 0 if erase is not required.

                            verifyAfter -
                                Set to 1 to verify the NVM contents of devices after
                                completion of the programming process. Set to 0 if verify is
                                not required.

                            restartAfter -
                                Set to 1 to restart the device after completion of the
                                programming process. Set to 0 if restart is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This function is used to program up to 32 devices over multiple
                            ports. This function will block execution until all devices have
                            been programmed successfully or have failed.
                            <p>
                            If this function returns TFL_DEVICE_ERROR, use flmGetBitErrorField
                            to determine which devices failed.

        """
        self.TestFlashDLL.flmProgramBlock.restype = ct.c_int32
        self.TestFlashDLL.flmProgramBlock.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmProgramBlock(deviceMask, eraseFirst, verifyAfter, restartAfter)
        
        return retval
    # end of flmProgramBlock


    def flErase(self) -> int:
        r"""Function TestFlash::flErase() wrapper for flErase in TestFlash DLL.

        Python API:
            flErase() -> int

        Python Example Call Syntax:
            retval = myDll.flErase()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flErase(void)

            Parameters :    None

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as defined for flGetLastError.

            Description :   This function is used to erase the NVM.

        """
        self.TestFlashDLL.flErase.restype = ct.c_int32
        self.TestFlashDLL.flErase.argtypes = []
        
        retval = self.TestFlashDLL.flErase()
        
        return retval
    # end of flErase


    def flmEraseBlock(self, deviceMask: int) -> int:
        r"""Function TestFlash::flmEraseBlock() wrapper for flmEraseBlock in TestFlash DLL.

        Python API:
            flmEraseBlock(deviceMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmEraseBlock(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmEraseBlock(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be erased. See flmOpen for the
                                details of this parameter.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This function is used to erase the NVM of to up to 32 devices
                            over multiple ports. This function will block execution until all
                            devices have been erased successfully or an error occurs.
                            <p>
                            If this function returns TFL_DEVICE_ERROR, use flmGetBitErrorField
                            to determine which devices failed.

        """
        self.TestFlashDLL.flmEraseBlock.restype = ct.c_int32
        self.TestFlashDLL.flmEraseBlock.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmEraseBlock(deviceMask)
        
        return retval
    # end of flmEraseBlock


    def flmEraseSpawn(self, deviceMask: int) -> int:
        r"""Function TestFlash::flmEraseSpawn() wrapper for flmEraseSpawn in TestFlash DLL.

        Python API:
            flmEraseSpawn(deviceMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmEraseSpawn(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmEraseSpawn(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be erased. See flmOpen for the
                                details of this parameter.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is used to erase the NVM of to up to 32 devices
                            over multiple ports. This function will spawn the threads which
                            perform the erase.
                            <p>
                            NOTE: The return value indicates only whether the erase threads
                            started successfully or not. When the erase completes,
                            flmGetDeviceError should be called to get the final status.
                            flmGetDeviceProgress should be used to check for completion.

        """
        self.TestFlashDLL.flmEraseSpawn.restype = ct.c_int32
        self.TestFlashDLL.flmEraseSpawn.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmEraseSpawn(deviceMask)
        
        return retval
    # end of flmEraseSpawn


    def flGangProgramBlock(self, deviceMask: int, eraseFirst: int, restartAfter: int, skipUnused: int) -> int:
        r"""Function TestFlash::flGangProgramBlock() wrapper for flGangProgramBlock in TestFlash DLL.

        Python API:
            flGangProgramBlock(deviceMask: int, eraseFirst: int, restartAfter: int, skipUnused: int) -> int

        Python Example Call Syntax:
            retval = myDll.flGangProgramBlock(deviceMask=0, eraseFirst=0, restartAfter=0, skipUnused=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flGangProgramBlock(uint16 deviceMask, uint8 eraseFirst,
                                                     uint8 restartAfter, uint8 skipUnused)

            Parameters :    deviceMask -
                                Specifies which devices will be programmed. Uses a bit-field
                                so 5 = 0000000000000101 = devices 0 and 2. A value of 0 (zero)
                                will auto-detect and program all devices present.

                            eraseFirst -
                                Set to 1 to erase the entire NVM of all devices before
                                programming. Set to 0 if erase is not required.

                            restartAfter -
                                Set to 1 to restart all devices after completion of the
                                programming process. Set to 0 if restart is not required.

                            skipUnused -
                                Set to 1 to skip attempts to stop and restart devices at
                                unused positions. Set to zero to attempt to stop and restart
                                all positions regardless of deviceMask value (this takes some
                                time).
                                <p>
                                NOTE: skipUnused has no effect when deviceMask = 0
                                (auto-detect).

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as defined for flGetLastError.

                            If all the specified devices were programmed correctly the function
                            will return FLASH_ERROR_NONE, if there were 1 or more programming
                            failures then the function will return
                            FLASH_ERROR_COULD_NOT_DOWNLOAD_PROG. All other error returns denote
                            a gross failure.

            Description :   This function is used to program one or more devices connected
                            to the gang programmer hardware. This function will block
                            execution until the process completes successfully or an error
                            occurs.
                            <p>
                            On completion with an error return of either FLASH_ERROR_NONE or
                            FLASH_ERROR_COULD_NOT_DOWNLOAD_PROG the programmer should call
                            flGetBitErrorField to determine which device(s) failed to program.

        """
        self.TestFlashDLL.flGangProgramBlock.restype = ct.c_int32
        self.TestFlashDLL.flGangProgramBlock.argtypes = [ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flGangProgramBlock(deviceMask, eraseFirst, restartAfter, skipUnused)
        
        return retval
    # end of flGangProgramBlock


    def flGetDetectedDevices(self) -> int:
        r"""Function TestFlash::flGetDetectedDevices() wrapper for flGetDetectedDevices in TestFlash DLL.

        Python API:
            flGetDetectedDevices() -> int

        Python Example Call Syntax:
            retval = myDll.flGetDetectedDevices()
            print(retval)

        Detail From Wrapped C API:
            Function :      uint16 flGetDetectedDevices(void)

            Parameters :    None

            Returns :       Bitfield indicating which devices were detected when using
                            auto-detect mode with gang programmer hardware. A value of 0 means
                            that no devices were detected. A value of 5 indicates that devices
                            0 and 2 were detected.

            Description :   This function can be used after gang programming operations in
                            auto-detect mode to determine which devices were detected. It can
                            be used with flGetBitErrorField to determine which devices were
                            successfully programmed (those devices which were detected and
                            didn't fail).
                            <p>
                            auto-detect mode is used when the device_mask parameter given to
                            flGangProgramBlock or flGangProgramSpawn is 0.

        """
        self.TestFlashDLL.flGetDetectedDevices.restype = ct.c_uint16
        self.TestFlashDLL.flGetDetectedDevices.argtypes = []
        
        retval = self.TestFlashDLL.flGetDetectedDevices()
        
        return retval
    # end of flGetDetectedDevices


    def flGetBitErrorField(self) -> int:
        r"""Function TestFlash::flGetBitErrorField() wrapper for flGetBitErrorField in TestFlash DLL.

        Python API:
            flGetBitErrorField() -> int

        Python Example Call Syntax:
            retval = myDll.flGetBitErrorField()
            print(retval)

        Detail From Wrapped C API:
            Function :      uint16 flGetBitErrorField(void)

            Parameters :    None

            Returns :       Bitfield referring to the devices present on the gang programmer
                            and those that have failed. Will return
                            (failed_devices & deviceMask).
                            Therefore a return of zero (0) means all devices have been
                            programmed successfully. A return value of five (5) denotes that
                            devices 0 and 2 have failed and the remainder have successfully
                            been programmed.
                            <p>
                            If the last broadcast operation was performed in Auto-detect mode
                            and no devices were detected, then flGetBitErrorField will return
                            the value 0xFFFF.

            Description :   This function is used to determine which devices have failed to be
                            programmed during the gang programming process.

        """
        self.TestFlashDLL.flGetBitErrorField.restype = ct.c_uint16
        self.TestFlashDLL.flGetBitErrorField.argtypes = []
        
        retval = self.TestFlashDLL.flGetBitErrorField()
        
        return retval
    # end of flGetBitErrorField


    def flmGetBitErrorField(self) -> int:
        r"""Function TestFlash::flmGetBitErrorField() wrapper for flmGetBitErrorField in TestFlash DLL.

        Python API:
            flmGetBitErrorField() -> int

        Python Example Call Syntax:
            retval = myDll.flmGetBitErrorField()
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 flmGetBitErrorField(void)

            Parameters :    None

            Returns :       Bitfield indicating which devices have failed. A return value of
                            0 means that the previous operation completed successfully on all
                            devices. A return value of 5 denotes that devices 0 and 2 have
                            failed and any other devices completed without errors.
                            <p>
                            The returned value should be masked by the device mask used, i.e.
                            perform a bitwise AND operation with the returned value and
                            device mask to get a bitfield indicating which of the specified
                            devices failed.

            Description :   This function is used to determine which devices failed during the
                            last multiple connection operation. flmGetBitErrorField is valid
                            after a function returns TFL_DEVICE_ERROR or after a spawned
                            process indicates completion (flmGetDeviceProgress returns 100
                            for all devices).

        """
        self.TestFlashDLL.flmGetBitErrorField.restype = ct.c_uint32
        self.TestFlashDLL.flmGetBitErrorField.argtypes = []
        
        retval = self.TestFlashDLL.flmGetBitErrorField()
        
        return retval
    # end of flmGetBitErrorField


    def flProgramSpawn(self) -> int:
        r"""Function TestFlash::flProgramSpawn() wrapper for flProgramSpawn in TestFlash DLL.

        Python API:
            flProgramSpawn() -> int

        Python Example Call Syntax:
            retval = myDll.flProgramSpawn()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flProgramSpawn(void)

            Parameters :    None

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as follows:
                                <table>
                                    <tr><td>FLASH_ERROR_NONE                        <td> 0
                                    <tr><td>FLASH_ERROR_NO_IMAGE                    <td> 14
                                    <tr><td>FLASH_ERROR_BUSY                        <td> 15
                                </table>

            Description :   This function is used to program a device. The function will
                            spawn the thread which performs the NVM programming.
                            <p>
                            NOTE: The return value indicates only whether the programming
                            thread started successfully or not. When programming completes,
                            flGetLastError should be called to get the final status.
                            flGetProgress should be used to check for completion.

        """
        self.TestFlashDLL.flProgramSpawn.restype = ct.c_int32
        self.TestFlashDLL.flProgramSpawn.argtypes = []
        
        retval = self.TestFlashDLL.flProgramSpawn()
        
        return retval
    # end of flProgramSpawn


    def flmProgramSpawn(self, deviceMask: int, eraseFirst: int, verifyAfter: int, restartAfter: int) -> int:
        r"""Function TestFlash::flmProgramSpawn() wrapper for flmProgramSpawn in TestFlash DLL.

        Python API:
            flmProgramSpawn(deviceMask: int, eraseFirst: int, verifyAfter: int, restartAfter: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmProgramSpawn(deviceMask=0, eraseFirst=0, verifyAfter=0, restartAfter=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmProgramSpawn(uint32 deviceMask, uint8 eraseFirst,
                                                  uint8 verifyAfter, uint8 restartAfter)

            Parameters :    deviceMask -
                                Specifies which devices will be programmed. See flmOpen for
                                the details of this parameter.

                            eraseFirst -
                                Set to 1 to erase the entire NVM of all devices before
                                programming. Set to 0 if erase is not required.

                            verifyAfter -
                                Set to 1 to verify the NVM contents of devices after
                                completion of the programming process. Set to 0 if verify is
                                not required.

                            restartAfter -
                                Set to 1 to restart all devices after completion of the
                                programming process. Set to 0 if restart is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is used to program up to 32 devices over multiple
                            connections. This function will spawn the threads which perform
                            the NVM programming.
                            <p>
                            NOTE: The return value indicates only whether the programming
                            threads started successfully or not. When programming completes,
                            flmGetDeviceError should be called to get the final status.
                            flmGetDeviceProgress should be used to check for completion.

        """
        self.TestFlashDLL.flmProgramSpawn.restype = ct.c_int32
        self.TestFlashDLL.flmProgramSpawn.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmProgramSpawn(deviceMask, eraseFirst, verifyAfter, restartAfter)
        
        return retval
    # end of flmProgramSpawn


    def flGangProgramSpawn(self, deviceMask: int, eraseFirst: int, restartAfter: int, skipUnused: int) -> int:
        r"""Function TestFlash::flGangProgramSpawn() wrapper for flGangProgramSpawn in TestFlash DLL.

        Python API:
            flGangProgramSpawn(deviceMask: int, eraseFirst: int, restartAfter: int, skipUnused: int) -> int

        Python Example Call Syntax:
            retval = myDll.flGangProgramSpawn(deviceMask=0, eraseFirst=0, restartAfter=0, skipUnused=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flGangProgramSpawn(uint16 deviceMask, uint8 eraseFirst,
                                                     uint8 restartAfter, uint8 skipUnused)


            Parameters :    deviceMask -
                                Specifies which devices will be programmed. Uses a bit-field
                                so 5 = 0000000000000101 = devices 0 and 2. A value of 0 (zero)
                                will auto-detect and program all devices present.

                            eraseFirst -
                                Set to 1 to erase the entire NVM of all devices before
                                programming. Set to 0 if erase is not required.

                            restartAfter -
                                Set to 1 to restart the XAP processors of all devices after
                                completion of the programming process. Set to 0 if restart is
                                not required.

                            skipUnused -
                                Set to 1 to skip attempts to stop and restart devices at
                                unused positions. Set to zero to attempt to stop and restart
                                all positions regardless of deviceMask value (this takes
                                some time).
                                <p>
                                NOTE: skipUnused has no effect when deviceMask = 0
                                (auto-detect).

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as follows:
                                <table>
                                    <tr><td>FLASH_ERROR_NONE                        <td> 0
                                    <tr><td>FLASH_ERROR_NO_IMAGE                    <td> 14
                                    <tr><td>FLASH_ERROR_BUSY                        <td> 15
                                </table>

            Description :   This function is used to program one or more devices connected
                            to the gang programmer hardware. The function will spawn the
                            thread which performs the NVM programming.
                            <p>
                            NOTE: The return value indicates only whether the programming
                            thread started successfully or not. When programming completes,
                            flGetLastError should be called to get the final status.
                            flGetBitErrorField should then be called to determine which, if
                            any, of the devices failed. flGetProgress can be used to check
                            for completion.

        """
        self.TestFlashDLL.flGangProgramSpawn.restype = ct.c_int32
        self.TestFlashDLL.flGangProgramSpawn.argtypes = [ct.c_uint16, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flGangProgramSpawn(deviceMask, eraseFirst, restartAfter, skipUnused)
        
        return retval
    # end of flGangProgramSpawn


    def flGetProgress(self) -> int:
        r"""Function TestFlash::flGetProgress() wrapper for flGetProgress in TestFlash DLL.

        Python API:
            flGetProgress() -> int

        Python Example Call Syntax:
            retval = myDll.flGetProgress()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flGetProgress(void)

            Parameters :    None

            Returns :       Progress as a percentage (0 to 100). 100 indicates that the
                            spawned programming thread has returned with or without an error.

            Description :   This function is used to check the progress of the programming
                            thread spawned by flProgramSpawn or flGangProgramSpawn.

        """
        self.TestFlashDLL.flGetProgress.restype = ct.c_int32
        self.TestFlashDLL.flGetProgress.argtypes = []
        
        retval = self.TestFlashDLL.flGetProgress()
        
        return retval
    # end of flGetProgress


    def flmGetDeviceProgress(self, device: int) -> int:
        r"""Function TestFlash::flmGetDeviceProgress() wrapper for flmGetDeviceProgress in TestFlash DLL.

        Python API:
            flmGetDeviceProgress(device: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmGetDeviceProgress(device=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmGetDeviceProgress(uint32 device)

            Parameters :    device -
                                The index of the device for which to retrieve the progress.
                                E.g. to retrieve the progress of the 3rd device, the parameter
                                is 2. For LPT-SPI transports only, device indices start at 1,
                                so the parameter value for the 3rd device would be 3 in this
                                case.

            Returns :       Progress as a percentage (0 to 100). 100 indicates that the
                            spawned programming thread has returned with or without an error.

            Description :   This function is used to check the progress of an operation
                            spawned by flmProgramSpawn, flmEraseSpawn and flmVerifySpawn.

        """
        self.TestFlashDLL.flmGetDeviceProgress.restype = ct.c_int32
        self.TestFlashDLL.flmGetDeviceProgress.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmGetDeviceProgress(device)
        
        return retval
    # end of flmGetDeviceProgress


    def flGetLastError(self) -> int:
        r"""Function TestFlash::flGetLastError() wrapper for flGetLastError in TestFlash DLL.

        Python API:
            flGetLastError() -> int

        Python Example Call Syntax:
            retval = myDll.flGetLastError()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flGetLastError(void)

            Parameters :    None

            Returns :       One of the codes as follows:
                            <table>
                                <tr><td>FLASH_ERROR_NONE                        <td> 0
                                <tr><td>FLASH_ERROR_DOWNLOAD_FAILED             <td> 1
                                <tr><td>FLASH_ERROR_VERIFY_FAILED               <td> 2
                                <tr><td>FLASH_ERROR_TIMED_OUT                   <td> 3
                                <tr><td>FLASH_ERROR_CRC_FAILED                  <td> 4
                                <tr><td>FLASH_ERROR_READBACK_FAILED             <td> 5
                                <tr><td>FLASH_ERROR_COULD_NOT_DOWNLOAD_PROG     <td> 6
                                <tr><td>FLASH_ERROR_COULD_NOT_STOP_XAP          <td> 7
                                <tr><td>FLASH_ERROR_BOOT_PROG_HALTED            <td> 8
                                <tr><td>FLASH_ERROR_ERASE_FAILED                <td> 9
                                <tr><td>FLASH_ERROR_XAP_ERROR                   <td> 10
                                <tr><td>FLASH_ERROR_UNKNOWN_CHIP_TYPE           <td> 11
                                <tr><td>FLASH_ERROR_BROADCAST_MIXED_CHIP_TYPES  <td> 12
                                <tr><td>FLASH_ERROR_OPEN_FILE                   <td> 13
                                <tr><td>FLASH_ERROR_NO_IMAGE                    <td> 14
                                <tr><td>FLASH_ERROR_BUSY                        <td> 15
                                <tr><td>FLASH_ERROR_NO_FLASH                    <td> 16
                                <tr><td>FLASH_ERROR_OOM (out of memory)         <td> 17
                                <tr><td>FLASH_ERROR_UNSUPPORTED_FLASH           <td> 18
                                <tr><td>FLASH_ERROR_DUMP_FAILED                 <td> 19
                                <tr><td>FLASH_ERROR_WRONG_PARAMS                <td> 20
                                <tr><td>FLASH_ERROR_UCI_OPERATION_FAIL          <td> 21
                                <tr><td>FLASH_ERROR_UCI_COMMAND_STATUS          <td> 22
                                <tr><td>FLASH_ERROR_GENERAL                     <td> 23
                                <tr><td>TFL_ERROR_OPEN_FAILED                   <td> 4097
                                <tr><td>TFL_ERROR_DEVICE_OPEN                   <td> 4098
                                <tr><td>TFL_ERROR_DEVICE_NOT_OPEN               <td> 4099
                                <tr><td>TFL_ERROR_DEVICE_BUSY                   <td> 4100
                                <tr><td>TFL_ERROR_THREAD_ERROR                  <td> 4101
                                <tr><td>TFL_ERROR_RESET_FAIL                    <td> 4102
                                <tr><td>TFL_ERROR_XTAL_INVALID                  <td> 4103
                            </table>

            Description :   This function will return the last error generated by the NVM
                            programming stack. If called after flGetProgress returns 100 it
                            can be used to check for programming errors after spawned
                            operations.

        """
        self.TestFlashDLL.flGetLastError.restype = ct.c_int32
        self.TestFlashDLL.flGetLastError.argtypes = []
        
        retval = self.TestFlashDLL.flGetLastError()
        
        return retval
    # end of flGetLastError


    def flmGetLastError(self) -> int:
        r"""Function TestFlash::flmGetLastError() wrapper for flmGetLastError in TestFlash DLL.

        Python API:
            flmGetLastError() -> int

        Python Example Call Syntax:
            retval = myDll.flmGetLastError()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmGetLastError(void)

            Parameters :    None

            Returns :       See flGetLastError.

            Description :   This returns the error that caused the last multiple connection
                            function called to return TFL_ERROR. This function does not
                            return errors encountered by specific devices, such as when a
                            function returns TFL_DEVICE_ERROR; Use flmGetDeviceError to
                            retrieve those errors.

        """
        self.TestFlashDLL.flmGetLastError.restype = ct.c_int32
        self.TestFlashDLL.flmGetLastError.argtypes = []
        
        retval = self.TestFlashDLL.flmGetLastError()
        
        return retval
    # end of flmGetLastError


    def flmGetDeviceError(self, device: int) -> int:
        r"""Function TestFlash::flmGetDeviceError() wrapper for flmGetDeviceError in TestFlash DLL.

        Python API:
            flmGetDeviceError(device: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmGetDeviceError(device=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmGetDeviceError(uint32 device)

            Parameters :    device -
                                The index of the device for which to retrieve the error code.
                                E.g. to retrieve the error code for the 3rd device, the
                                parameter is 2. For LPT-SPI transports only, device indices
                                start at 1, so the parameter value for the 3rd device would be
                                3 in this case.

            Returns :       See flGetLastError.

            Description :   This function returns the error status for a specific device.
                            This function should be used after flmOpen, flmEraseBlock,
                            flmProgramBlock or flmVerifyBlock returns TFL_DEVICE_ERROR, or
                            when a spawned operation completes and flmGetBitErrorField shows
                            an error for a device.

        """
        self.TestFlashDLL.flmGetDeviceError.restype = ct.c_int32
        self.TestFlashDLL.flmGetDeviceError.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmGetDeviceError(device)
        
        return retval
    # end of flmGetDeviceError


    def flResetAndStart(self) -> int:
        r"""Function TestFlash::flResetAndStart() wrapper for flResetAndStart in TestFlash DLL.

        Python API:
            flResetAndStart() -> int

        Python Example Call Syntax:
            retval = myDll.flResetAndStart()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flResetAndStart(void)

            Parameters :    None

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function can be used to reset and start the device.
                            <p>
                            The current connection to the device is considered to be invalid
                            after this call, and it must be closed (see flClose
                            / flCloseRet). To open a new connection to the device use
                            flOpenTrans (or flOpenUnlockTrans if the Debug Lock is enabled).

        """
        self.TestFlashDLL.flResetAndStart.restype = ct.c_int32
        self.TestFlashDLL.flResetAndStart.argtypes = []
        
        retval = self.TestFlashDLL.flResetAndStart()
        
        return retval
    # end of flResetAndStart


    def flmResetAndStart(self, deviceMask: int) -> int:
        r"""Function TestFlash::flmResetAndStart() wrapper for flmResetAndStart in TestFlash DLL.

        Python API:
            flmResetAndStart(deviceMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmResetAndStart(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmResetAndStart(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be reset and started. See flmOpen
                                for the details of this parameter.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This is the multiple connection version of flResetAndStart. If
                            this function returns TFL_DEVICE_ERROR, use flmGetBitErrorField
                            to determine which devices failed.
                            <p>
                            The current connection to the device is considered to be invalid
                            after this call, and it must be closed (see flmClose
                            / flmCloseRet). To open a new connection to the device use
                            flmOpenTrans (or flmOpenUnlockTrans if the Debug Lock is enabled).

        """
        self.TestFlashDLL.flmResetAndStart.restype = ct.c_int32
        self.TestFlashDLL.flmResetAndStart.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmResetAndStart(deviceMask)
        
        return retval
    # end of flmResetAndStart


    def flClose(self):
        r"""Function TestFlash::flClose() wrapper for flClose in TestFlash DLL.

        Python API:
            flClose()

        Python Example Call Syntax:
            retval = myDll.flClose()
            print(retval)

        Detail From Wrapped C API:
            Function :      void flClose(void)

            Parameters :    None

            Returns :       None

            Description :   Performs shut-down activities (such as relocking the transport, if
                            applicable) for any device connection, before disconnecting the
                            device connection and freeing any memory used by TestFlash.
                            Transport relocking is only supported on certain devices.
                            <p>
                            Note that if the connection was opened using flOpenUnlock, it is
                            recommended to close the connection using flCloseRet, as
                            flCloseRet will indicate by its return code if relocking the
                            transport failed.

        """
        self.TestFlashDLL.flClose.restype = None
        self.TestFlashDLL.flClose.argtypes = []
        
        retval = self.TestFlashDLL.flClose()
        
        return retval
    # end of flClose


    def flCloseRet(self) -> int:
        r"""Function TestFlash::flCloseRet() wrapper for flCloseRet in TestFlash DLL.

        Python API:
            flCloseRet() -> int

        Python Example Call Syntax:
            retval = myDll.flCloseRet()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flCloseRet(void)

            Parameters :    None

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Performs shut-down activities (such as relocking the transport, if
                            applicable) for any device connection, before disconnecting the
                            device connection and freeing any memory used by TestFlash.
                            Transport relocking is only supported on certain devices.
                            <p>
                            A return code of TFL_ERROR indicates a problem in the shut-down
                            activities, e.g. relocking the transport failed (in a scenario
                            where flOpenUnlock was used to open the connection).

        """
        self.TestFlashDLL.flCloseRet.restype = ct.c_int32
        self.TestFlashDLL.flCloseRet.argtypes = []
        
        retval = self.TestFlashDLL.flCloseRet()
        
        return retval
    # end of flCloseRet


    def flmClose(self, deviceMask: int):
        r"""Function TestFlash::flmClose() wrapper for flmClose in TestFlash DLL.

        Python API:
            flmClose(deviceMask: int)

        Python Example Call Syntax:
            retval = myDll.flmClose(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      void flmClose(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be closed. See flmOpen for the
                                details of this parameter.

            Returns :       None

            Description :   This is the multiple connection version of flClose. Refer to
                            flClose for more details.

        """
        self.TestFlashDLL.flmClose.restype = None
        self.TestFlashDLL.flmClose.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmClose(deviceMask)
        
        return retval
    # end of flmClose


    def flmCloseRet(self, deviceMask: int) -> int:
        r"""Function TestFlash::flmCloseRet() wrapper for flmCloseRet in TestFlash DLL.

        Python API:
            flmCloseRet(deviceMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmCloseRet(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmCloseRet(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be closed. See flmOpen for the
                                details of this parameter.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This is the multiple connection version of flCloseRet. Refer to
                            flCloseRet for more details.

        """
        self.TestFlashDLL.flmCloseRet.restype = ct.c_int32
        self.TestFlashDLL.flmCloseRet.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmCloseRet(deviceMask)
        
        return retval
    # end of flmCloseRet


    def flGetVersion(self, versionStr: str='') -> Tuple[int, str]:
        r"""Function TestFlash::flGetVersion() wrapper for flGetVersion in TestFlash DLL.

        Python API:
            flGetVersion(versionStr: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, versionStr = myDll.flGetVersion()
            print(retval, versionStr)

        Detail From Wrapped C API:
            Function :      int32 flGetVersion(char* versionStr)

            Parameters :    versionStr -
                                Pre-allocated string for receiving the version number.

            Returns :       Always returns TFL_OK (0).

            Description :   Gets the version string for this DLL.

        """
        self.TestFlashDLL.flGetVersion.restype = ct.c_int32
        self.TestFlashDLL.flGetVersion.argtypes = [ct.c_char_p]
        local_versionStr = None if versionStr is None else ct.create_string_buffer(bytes(versionStr, encoding="UTF-8"), 1024)
        retval = self.TestFlashDLL.flGetVersion(local_versionStr)
        versionStr = local_versionStr.value.decode()
        return retval, versionStr
    # end of flGetVersion


    def flmGetVersion(self, versionStr: str='') -> Tuple[int, str]:
        r"""Function TestFlash::flmGetVersion() wrapper for flmGetVersion in TestFlash DLL.

        Python API:
            flmGetVersion(versionStr: str='') -> Tuple[int, str]

        Python Example Call Syntax:
            retval, versionStr = myDll.flmGetVersion()
            print(retval, versionStr)

        Detail From Wrapped C API:
            Function :      int32 flmGetVersion(char* versionStr)

            Parameters :    versionStr -
                                See flGetVersion.

            Returns :       See flGetVersion.

            Description :   This is a synonym for flGetVersion.

        """
        self.TestFlashDLL.flmGetVersion.restype = ct.c_int32
        self.TestFlashDLL.flmGetVersion.argtypes = [ct.c_char_p]
        local_versionStr = None if versionStr is None else ct.create_string_buffer(bytes(versionStr, encoding="UTF-8"), 1024)
        retval = self.TestFlashDLL.flmGetVersion(local_versionStr)
        versionStr = local_versionStr.value.decode()
        return retval, versionStr
    # end of flmGetVersion


    def flStopProcessor(self) -> int:
        r"""Function TestFlash::flStopProcessor() wrapper for flStopProcessor in TestFlash DLL.

        Python API:
            flStopProcessor() -> int

        Python Example Call Syntax:
            retval = myDll.flStopProcessor()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flStopProcessor(void)

            Parameters :    None

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function will stop the processor of the connected device.
                            <p>
                            A SPI connection has to be made for this function to complete
                            successfully.
                            <p>
                            This function is only applicable for BlueCore and Bluetooth low
                            energy ICs.

        """
        self.TestFlashDLL.flStopProcessor.restype = ct.c_int32
        self.TestFlashDLL.flStopProcessor.argtypes = []
        
        retval = self.TestFlashDLL.flStopProcessor()
        
        return retval
    # end of flStopProcessor


    def flmStopProcessor(self, deviceMask: int) -> int:
        r"""Function TestFlash::flmStopProcessor() wrapper for flmStopProcessor in TestFlash DLL.

        Python API:
            flmStopProcessor(deviceMask: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmStopProcessor(deviceMask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmStopProcessor(uint32 deviceMask)

            Parameters :    deviceMask -
                                Specifies which devices will be stopped. See flmOpen for the
                                details of this parameter.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This is the multiple connection version of flStopProcessor. Refer
                            to flStopProcessor for more details. If this function returns
                            TFL_DEVICE_ERROR, use flmGetBitErrorField to determine which
                            devices failed.
                            <p>
                            This function is only applicable for BlueCore and Bluetooth low
                            energy ICs.

        """
        self.TestFlashDLL.flmStopProcessor.restype = ct.c_int32
        self.TestFlashDLL.flmStopProcessor.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmStopProcessor(deviceMask)
        
        return retval
    # end of flmStopProcessor


    def flGetDownloadTime(self) -> int:
        r"""Function TestFlash::flGetDownloadTime() wrapper for flGetDownloadTime in TestFlash DLL.

        Python API:
            flGetDownloadTime() -> int

        Python Example Call Syntax:
            retval = myDll.flGetDownloadTime()
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 flGetDownloadTime(void)

            Parameters :    None

            Returns :       The time taken in milliseconds for the last download. Returns 0
                            if an error occurred or if download has not completed.

            Description :   Fetches the last download time.

        """
        self.TestFlashDLL.flGetDownloadTime.restype = ct.c_uint32
        self.TestFlashDLL.flGetDownloadTime.argtypes = []
        
        retval = self.TestFlashDLL.flGetDownloadTime()
        
        return retval
    # end of flGetDownloadTime


    def flmGetDeviceDownloadTime(self, device: int) -> int:
        r"""Function TestFlash::flmGetDeviceDownloadTime() wrapper for flmGetDeviceDownloadTime in TestFlash DLL.

        Python API:
            flmGetDeviceDownloadTime(device: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmGetDeviceDownloadTime(device=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint32 flmGetDeviceDownloadTime(uint32 device)

            Parameters :    device -
                                The index of the device for which to retrieve the download
                                time. E.g. to retrieve the time for the 3rd device, the
                                parameter is 2. For LPT-SPI transports only, device indices
                                start at 1, so the parameter value for the 3rd device would be
                                3 in this case.

            Returns :       See flGetDownloadTime.

            Description :   This is the multiple connection version of flGetDownloadTime.
                            Refer to flGetDownloadTime for more details.

        """
        self.TestFlashDLL.flmGetDeviceDownloadTime.restype = ct.c_uint32
        self.TestFlashDLL.flmGetDeviceDownloadTime.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmGetDeviceDownloadTime(device)
        
        return retval
    # end of flmGetDeviceDownloadTime


    def flGetAvailablePorts(self, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestFlash::flGetAvailablePorts() wrapper for flGetAvailablePorts in TestFlash DLL.

        Python API:
            flGetAvailablePorts(maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.flGetAvailablePorts()
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 flGetAvailablePorts(uint16* maxLen, char* ports,
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
                                passed directly into the flOpenTrans function to open the
                                port.

                            count -
                                This value is set to the number of available ports found.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is used to get a list of available debug ports. A
                            char array, pointed to by the ports parameter, is filled with a
                            comma separated list of port names. A further char array, pointed
                            to by the trans parameter, is filled with a comma separated list
                            of the relevant transport option strings that specify each
                            available debug port.
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
                            to the flOpenTrans function to open the port.

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* portsStr = new char[maxLen];
                char* transStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USBDBG(100)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=USBDBG SPIPORT=1")

                int32 status = flGetAvailablePorts(&maxLen, portsStr, transStr, &count);
                if( status != TFL_OK && maxLen != 0 )
                {
                    // Not enough space - resize the storage
                    delete[] portsStr;
                    portsStr = new char[maxLen];
                    delete[] transStr;
                    transStr = new char[maxLen];
                    status = flGetAvailablePorts(&maxLen, portsStr, transStr, &count);
                }
                if( status != TFL_OK || count == 0 )
                {
                    cout << "Error getting ports, or none found" << endl;
                    delete[] portsStr;
                    delete[] transStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, portsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, transStr, ','); // Use these to open a transport

                // Open the port using the trans string
                // For the purposes of this example, we're just using the first in the list
                status = flOpenTrans(trans.at(0).c_str(), 0, 0);

                if(status == TFL_OK)
                {
                    cout << "Connected!" << endl;

                    // Download code here

                    flClose();
                }

                delete[] portsStr;
                delete[] transStr;

                return;

        """
        self.TestFlashDLL.flGetAvailablePorts.restype = ct.c_int32
        self.TestFlashDLL.flGetAvailablePorts.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestFlashDLL.flGetAvailablePorts(ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of flGetAvailablePorts


    def flGetAvailablePortsEx(self, criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestFlash::flGetAvailablePortsEx() wrapper for flGetAvailablePortsEx in TestFlash DLL.

        Python API:
            flGetAvailablePortsEx(criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.flGetAvailablePortsEx(criteria=0)
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 flGetAvailablePortsEx(uint32 criteria, uint16* maxLen,
                                char* ports, char* trans, uint16* count)

            Parameters :    criteria -
                                Search criteria for enumerating devices. A bit pattern
                                made up one or bitwise combination of TFL_TRANS_CRIT_* values.
                                For devices that have a lockable transport and are locked,
                                the trans string will contain TRANSLOCK=1 as an indicator.
                                Using TFL_TRANS_CRIT_DEFAULT will return the same output as 
                                teGetAvailableDebugPorts.
                                Using TFL_TRANS_CRIT_ALL will output all devices.

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
                                passed directly into the flOpenTrans function to open the
                                port.

                            count -
                                This value is set to the number of available ports found.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function is used to get a list of available debug ports. A
                            char array, pointed to by the ports parameter, is filled with a
                            comma separated list of port names. A further char array, pointed
                            to by the trans parameter, is filled with a comma separated list
                            of the relevant transport option strings that specify each
                            available debug port.
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
                            to the flOpenTrans function to open the port.

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* portsStr = new char[maxLen];
                char* transStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USBDBG(100)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=USBDBG SPIPORT=1")

                int32 status = flGetAvailablePortsEx(TFL_TRANS_CRIT_DEFAULT, &maxLen,
                    portsStr, transStr, &count);
                if( status != TFL_OK && maxLen != 0 )
                {
                    // Not enough space - resize the storage
                    delete[] portsStr;
                    portsStr = new char[maxLen];
                    delete[] transStr;
                    transStr = new char[maxLen];
                    status = flGetAvailablePortsEx(TFL_TRANS_CRIT_DEFAULT, &maxLen,
                        portsStr, transStr, &count);
                }
                if( status != TFL_OK || count == 0 )
                {
                    cout << "Error getting ports, or none found" << endl;
                    delete[] portsStr;
                    delete[] transStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, portsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, transStr, ','); // Use these to open a transport

                // Open the port using the trans string
                // For the purposes of this example, we're just using the first in the list
                status = flOpenTrans(trans.at(0).c_str(), 0, 0);

                if(status == TFL_OK)
                {
                    cout << "Connected!" << endl;

                    // Download code here

                    flClose();
                }

                delete[] portsStr;
                delete[] transStr;

                return;

        """
        self.TestFlashDLL.flGetAvailablePortsEx.restype = ct.c_int32
        self.TestFlashDLL.flGetAvailablePortsEx.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestFlashDLL.flGetAvailablePortsEx(criteria, ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of flGetAvailablePortsEx


    def flmGetAvailablePorts(self, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestFlash::flmGetAvailablePorts() wrapper for flmGetAvailablePorts in TestFlash DLL.

        Python API:
            flmGetAvailablePorts(maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.flmGetAvailablePorts()
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 flmGetAvailablePorts(uint16* maxLen, char* ports,
                                                       char* trans, uint16* count)

            Parameters :    maxLen -
                                See flGetAvailablePorts.

                            ports -
                                See flGetAvailablePorts.

                            trans -
                                See flGetAvailablePorts.

                            count -
                                See flGetAvailablePorts.

            Returns :       See flGetAvailablePorts.

            Description :   This is the multiple connection version of flGetAvailablePorts.
                            Refer to flGetAvailablePorts for more details.
                            <p>
                            NOTE: While the functionality is similar to
                            flGetAvailablePorts, the transport strings returned in the
                            trans parameter cannot be passed directly to flmOpenTrans.
                            flmConvertPort should be used to convert the string into the
                            appropriate string and device mask, both of which can be passed
                            to flmOpenTrans.

        """
        self.TestFlashDLL.flmGetAvailablePorts.restype = ct.c_int32
        self.TestFlashDLL.flmGetAvailablePorts.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestFlashDLL.flmGetAvailablePorts(ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of flmGetAvailablePorts


    def flmGetAvailablePortsEx(self, criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]:
        r"""Function TestFlash::flmGetAvailablePortsEx() wrapper for flmGetAvailablePortsEx in TestFlash DLL.

        Python API:
            flmGetAvailablePortsEx(criteria: int, maxLen: int=0, ports: str='', trans: str='', count: int=0) -> Tuple[int, int, str, str, int]

        Python Example Call Syntax:
            retval, maxLen, ports, trans, count = myDll.flmGetAvailablePortsEx(criteria=0)
            print(retval, maxLen, ports, trans, count)

        Detail From Wrapped C API:
            Function :      int32 flmGetAvailablePortsEx(uint32 criteria, uint16* maxLen,
                                                         char* ports, char* trans, uint16* count)

            Parameters :    criteria -
                                See flGetAvailablePortsEx.

                            maxLen -
                                See flGetAvailablePortsEx.

                            ports -
                                See flGetAvailablePortsEx.

                            trans -
                                See flGetAvailablePortsEx.

                            count -
                                See flGetAvailablePortsEx.

            Returns :       See flGetAvailablePortsEx.

            Description :   This is the multiple connection version of flGetAvailablePortsEx.
                            Refer to flGetAvailablePortsEx for more details.
                            <p>
                            NOTE: While the functionality is similar to
                            flGetAvailablePortsEx, the transport strings returned in the
                            trans parameter cannot be passed directly to flmOpenTrans.
                            flmConvertPort should be used to convert the string into the
                            appropriate string and device mask, both of which can be passed
                            to flmOpenTrans.

        """
        self.TestFlashDLL.flmGetAvailablePortsEx.restype = ct.c_int32
        self.TestFlashDLL.flmGetAvailablePortsEx.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_maxLen = ct.c_uint16(maxLen)
        local_ports = None if ports is None else ct.create_string_buffer(bytes(ports, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_trans = None if trans is None else ct.create_string_buffer(bytes(trans, encoding="UTF-8"), 1024 if maxLen < 1024 else maxLen)
        local_count = ct.c_uint16(count)
        retval = self.TestFlashDLL.flmGetAvailablePortsEx(criteria, ct.byref(local_maxLen), local_ports, local_trans, ct.byref(local_count))
        maxLen = local_maxLen.value
        ports = local_ports.value.decode()
        trans = local_trans.value.decode()
        count = local_count.value
        return retval, maxLen, ports, trans, count
    # end of flmGetAvailablePortsEx


    def flmConvertPort(self, transIn: str, transOut: str='', device: int=0) -> Tuple[int, str, int]:
        r"""Function TestFlash::flmConvertPort() wrapper for flmConvertPort in TestFlash DLL.

        Python API:
            flmConvertPort(transIn: str, transOut: str='', device: int=0) -> Tuple[int, str, int]

        Python Example Call Syntax:
            retval, transOut, device = myDll.flmConvertPort(transIn='abc')
            print(retval, transOut, device)

        Detail From Wrapped C API:
            Function :      int32 flmConvertPort(const char* transIn, char* transOut,
                                                 uint32* device)

            Parameters :    transIn -
                                String of space separated transport options.

                            transOut -
                                Pre-allocated string for receiving the altered transport
                                string. Must be at least the same length as transIn.

                            device -
                                Location for receiving the device identifier extracted from
                                the transport string. This is a port number for the device,
                                not a mask, but can be bit-shifted to create a mask as shown
                                in the example.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This function will convert a transport string returned by
                            flmGetAvailablePorts into a transport string and device
                            identifier. The resulting device mask and the converted string
                            can be used with flmOpenTrans (The SPIPORT specifier is removed
                            from the string).

            Example :

                uint16 maxLen(256);
                uint16 count(0);
                char* portsStr = new char[maxLen];
                char* transStr = new char[maxLen];
                vector<string> ports; // The human readable port strings (e.g. "USBDBG(100)")
                vector<string> trans; // The transport option strings (e.g. "SPITRANS=USBDBG SPIPORT=1")

                int32 status = flmGetAvailablePorts(&maxLen, portsStr, transStr, &count);
                if( status != TFL_OK && maxLen != 0 )
                {
                    // Not enough space - resize the storage
                    delete[] portsStr;
                    portsStr = new char[maxLen];
                    delete[] transStr;
                    transStr = new char[maxLen];
                    status = flmGetAvailablePorts(&maxLen, portsStr, transStr, &count);
                }
                if( status != TFL_OK || count == 0 )
                {
                    cout << "Error getting ports, or none found" << endl;
                    delete[] portsStr;
                    delete[] transStr;
                    return;
                }

                // Split up the comma separated strings of ports / transport options
                split(ports, portsStr, ','); // Use these for user selection (e.g. drop down list)
                split(trans, transStr, ','); // Use these to open a transport

                // Convert the port specification in to a specification suitable for multiple
                // device open
                // For the purposes of this example, we're just using the first in the list
                char* newTransStr = new char[trans.at(0).length() + 1];
                uint32 device;
                status = flmConvertPort(trans.at(0).c_str(), newTransStr, &device);
                if( status != TFL_OK )
                {
                    cout << "Error converting port to transport" << endl;
                    delete[] newTransStr;
                    delete[] portsStr;
                    delete[] transStr;
                    return;
                }

                // Open the port using the trans string
                status = flmOpenTrans(1 << device, newTransStr, 26);

                if(status == TFL_OK)
                {
                    cout << "Connected!" << endl;

                    // Download code here

                    flmClose(1 << device);
                }

                delete[] newTransStr;
                delete[] portsStr;
                delete[] transStr;

                return;

        """
        self.TestFlashDLL.flmConvertPort.restype = ct.c_int32
        self.TestFlashDLL.flmConvertPort.argtypes = [ct.c_char_p, ct.c_char_p, ct.c_void_p]
        local_transIn = None if transIn is None else ct.create_string_buffer(bytes(transIn, encoding="UTF-8"))
        local_transOut = None if transOut is None else ct.create_string_buffer(bytes(transOut, encoding="UTF-8"), 1024)
        local_device = ct.c_uint32(device)
        retval = self.TestFlashDLL.flmConvertPort(local_transIn, local_transOut, ct.byref(local_device))
        transOut = local_transOut.value.decode()
        device = local_device.value
        return retval, transOut, device
    # end of flmConvertPort


    def flGetFirmwareIds(self, source: int, loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]:
        r"""Function TestFlash::flGetFirmwareIds() wrapper for flGetFirmwareIds in TestFlash DLL.

        Python API:
            flGetFirmwareIds(source: int, loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]

        Python Example Call Syntax:
            retval, loaderId, loaderName, stackId, stackName = myDll.flGetFirmwareIds(source=0, maxNameLen=0)
            print(retval, loaderId, loaderName, stackId, stackName)

        Detail From Wrapped C API:
            Function :      int32 flGetFirmwareIds(uint8 source, uint32* loaderId,
                                                   char* loaderName, uint32* stackId,
                                                   char* stackName, uint16 maxNameLen)

            Parameters :    source -
                                Value indicating where the firmware id information should be
                                read from, where:
                                <table>
                                    <tr><td>TFL_CHIP <td>0 <td>(Read from attached chip)
                                    <tr><td>TFL_FILE <td>1 <td>(Read from file)
                                </table>

                            loaderId -
                                Location for receiving the loader id value.

                            loaderName -
                                Pre-allocated string for receiving the loader name.

                            stackId -
                                Location for receiving the stack id value.

                            stackName -
                                Pre-allocated string for receiving the stack name.

                            maxNameLen -
                                The length of the buffers used for the loaderName and
                                stackName strings.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Gets the firmware id information from an attached device or from
                            a pre-loaded file (loaded using flReadProgramFiles).
                            <p>
                            This function is only applicable to BlueCore ICs.

        """
        self.TestFlashDLL.flGetFirmwareIds.restype = ct.c_int32
        self.TestFlashDLL.flGetFirmwareIds.argtypes = [ct.c_uint8, ct.c_void_p, ct.c_char_p, ct.c_void_p, ct.c_char_p, ct.c_uint16]
        local_loaderId = ct.c_uint32(loaderId)
        local_loaderName = None if loaderName is None else ct.create_string_buffer(bytes(loaderName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        local_stackId = ct.c_uint32(stackId)
        local_stackName = None if stackName is None else ct.create_string_buffer(bytes(stackName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        retval = self.TestFlashDLL.flGetFirmwareIds(source, ct.byref(local_loaderId), local_loaderName, ct.byref(local_stackId), local_stackName, maxNameLen)
        loaderId = local_loaderId.value
        loaderName = local_loaderName.value.decode()
        stackId = local_stackId.value
        stackName = local_stackName.value.decode()
        return retval, loaderId, loaderName, stackId, stackName
    # end of flGetFirmwareIds


    def flmGetDeviceFirmwareIds(self, device: int, loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]:
        r"""Function TestFlash::flmGetDeviceFirmwareIds() wrapper for flmGetDeviceFirmwareIds in TestFlash DLL.

        Python API:
            flmGetDeviceFirmwareIds(device: int, loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]

        Python Example Call Syntax:
            retval, loaderId, loaderName, stackId, stackName = myDll.flmGetDeviceFirmwareIds(device=0, maxNameLen=0)
            print(retval, loaderId, loaderName, stackId, stackName)

        Detail From Wrapped C API:
            Function :      int32 flmGetDeviceFirmwareIds(uint32 device,
                                                          uint32* loaderId, char* loaderName,
                                                          uint32* stackId, char* stackName,
                                                          uint16 maxNameLen)

            Parameters :    device -
                                The index of the device for which to retrieve the firmware
                                IDs. E.g. to retrieve the firmware IDs for the 3rd device, the
                                parameter is 2. For LPT-SPI transports only, device indices
                                start at 1, so the parameter value for the 3rd device would be
                                3 in this case.

                            loaderId -
                                See flGetFirmwareIds.

                            loaderName -
                                See flGetFirmwareIds.

                            stackId -
                                See flGetFirmwareIds.

                            stackName -
                                See flGetFirmwareIds.

                            maxNameLen -
                                See flGetFirmwareIds.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This is the multiple connection version of flGetFirmwareIds.
                            Refer to flGetFirmwareIds for more details. This function always
                            returns the firmware id of the chip.
                            <p>
                            This function is only applicable to BlueCore ICs.

        """
        self.TestFlashDLL.flmGetDeviceFirmwareIds.restype = ct.c_int32
        self.TestFlashDLL.flmGetDeviceFirmwareIds.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_char_p, ct.c_void_p, ct.c_char_p, ct.c_uint16]
        local_loaderId = ct.c_uint32(loaderId)
        local_loaderName = None if loaderName is None else ct.create_string_buffer(bytes(loaderName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        local_stackId = ct.c_uint32(stackId)
        local_stackName = None if stackName is None else ct.create_string_buffer(bytes(stackName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        retval = self.TestFlashDLL.flmGetDeviceFirmwareIds(device, ct.byref(local_loaderId), local_loaderName, ct.byref(local_stackId), local_stackName, maxNameLen)
        loaderId = local_loaderId.value
        loaderName = local_loaderName.value.decode()
        stackId = local_stackId.value
        stackName = local_stackName.value.decode()
        return retval, loaderId, loaderName, stackId, stackName
    # end of flmGetDeviceFirmwareIds


    def flmGetFileFirmwareIds(self, loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]:
        r"""Function TestFlash::flmGetFileFirmwareIds() wrapper for flmGetFileFirmwareIds in TestFlash DLL.

        Python API:
            flmGetFileFirmwareIds(loaderId: int=0, loaderName: str='', stackId: int=0, stackName: str='', maxNameLen: int=0) -> Tuple[int, int, str, int, str]

        Python Example Call Syntax:
            retval, loaderId, loaderName, stackId, stackName = myDll.flmGetFileFirmwareIds(maxNameLen=0)
            print(retval, loaderId, loaderName, stackId, stackName)

        Detail From Wrapped C API:
            Function :      int32 flmGetFileFirmwareIds(uint32* loaderId, char* loaderName,
                                                        uint32* stackId, char* stackName,
                                                        uint16 maxNameLen)

            Parameters :    loaderId -
                                See flGetFirmwareIds.

                            loaderName -
                                See flGetFirmwareIds.

                            stackId -
                                See flGetFirmwareIds.

                            stackName -
                                See flGetFirmwareIds.

                            maxNameLen -
                                See flGetFirmwareIds.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Refer to flGetFirmwareIds for more details. This function always
                            returns the firmware id of the current file (not from the chip).
                            <p>
                            This function is only applicable for BlueCore ICs.

        """
        self.TestFlashDLL.flmGetFileFirmwareIds.restype = ct.c_int32
        self.TestFlashDLL.flmGetFileFirmwareIds.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_void_p, ct.c_char_p, ct.c_uint16]
        local_loaderId = ct.c_uint32(loaderId)
        local_loaderName = None if loaderName is None else ct.create_string_buffer(bytes(loaderName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        local_stackId = ct.c_uint32(stackId)
        local_stackName = None if stackName is None else ct.create_string_buffer(bytes(stackName, encoding="UTF-8"), 1024 if maxNameLen < 1024 else maxNameLen)
        retval = self.TestFlashDLL.flmGetFileFirmwareIds(ct.byref(local_loaderId), local_loaderName, ct.byref(local_stackId), local_stackName, maxNameLen)
        loaderId = local_loaderId.value
        loaderName = local_loaderName.value.decode()
        stackId = local_stackId.value
        stackName = local_stackName.value.decode()
        return retval, loaderId, loaderName, stackId, stackName
    # end of flmGetFileFirmwareIds


    def flVerify(self) -> int:
        r"""Function TestFlash::flVerify() wrapper for flVerify in TestFlash DLL.

        Python API:
            flVerify() -> int

        Python Example Call Syntax:
            retval = myDll.flVerify()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flVerify(void)

            Parameters :    None

            Returns :       TFL_ERROR (-1) if there is a general error within TestFlash
                            (normally due to an incorrect sequence of API calls), otherwise
                            one of the codes as follows:
                                <table>
                                    <tr><td>FLASH_ERROR_NONE                        <td> 0
                                    <tr><td>FLASH_ERROR_VERIFY_FAILED               <td> 2
                                </table>

                            <p>It is possible for other error codes (values > 0) to be
                            returned, e.g. if there are transport problems. These error codes
                            will be from the set listed for flGetLastError.

            Description :   This function is used to verify the contents of NVM against the
                            file loaded using flReadProgramFiles. Therefore,
                            flReadProgramFiles must be called prior to calling this function.

        """
        self.TestFlashDLL.flVerify.restype = ct.c_int32
        self.TestFlashDLL.flVerify.argtypes = []
        
        retval = self.TestFlashDLL.flVerify()
        
        return retval
    # end of flVerify


    def flmVerifyBlock(self, deviceMask: int, restartAfter: int) -> int:
        r"""Function TestFlash::flmVerifyBlock() wrapper for flmVerifyBlock in TestFlash DLL.

        Python API:
            flmVerifyBlock(deviceMask: int, restartAfter: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmVerifyBlock(deviceMask=0, restartAfter=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmVerifyBlock(uint32 deviceMask, uint8 restartAfter)

            Parameters :    deviceMask -
                                Specifies which devices will be verified. See flmOpen for the
                                details of this parameter.

                            restartAfter -
                                Set to 1 to restart all devices after completion of the verify
                                process. Set to 0 if restart is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                                <tr><td>TFL_DEVICE_ERROR    <td>-2
                            </table>

            Description :   This is the multiple connection version of flVerify. Refer to
                            flVerify for more details. This function blocks until all devices
                            have verified or failed.

        """
        self.TestFlashDLL.flmVerifyBlock.restype = ct.c_int32
        self.TestFlashDLL.flmVerifyBlock.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmVerifyBlock(deviceMask, restartAfter)
        
        return retval
    # end of flmVerifyBlock


    def flmVerifySpawn(self, deviceMask: int, restartAfter: int) -> int:
        r"""Function TestFlash::flmVerifySpawn() wrapper for flmVerifySpawn in TestFlash DLL.

        Python API:
            flmVerifySpawn(deviceMask: int, restartAfter: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmVerifySpawn(deviceMask=0, restartAfter=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmVerifySpawn(uint32 deviceMask, uint8 restartAfter)

            Parameters :    deviceMask -
                                Specifies which devices will be verified. See flmOpen for the
                                details of this parameter.

                            restartAfter -
                                Set to 1 to restart all devices after completion of the verify
                                process. Set to 0 if restart is not required.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   This is the multiple connection version of flVerify. Refer to
                            flVerify for more details.
                            <p>
                            NOTE: The return value indicates only whether the verify
                            threads started successfully or not. When verify completes,
                            flmGetDeviceError should be called to get the final status.
                            flmGetDeviceProgress should be used to check for completion.

        """
        self.TestFlashDLL.flmVerifySpawn.restype = ct.c_int32
        self.TestFlashDLL.flmVerifySpawn.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmVerifySpawn(deviceMask, restartAfter)
        
        return retval
    # end of flmVerifySpawn


    def flGetFlashInfo(self, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]:
        r"""Function TestFlash::flGetFlashInfo() wrapper for flGetFlashInfo in TestFlash DLL.

        Python API:
            flGetFlashInfo(sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]

        Python Example Call Syntax:
            retval, sectors, sizeMbits, manId, devId = myDll.flGetFlashInfo()
            print(retval, sectors, sizeMbits, manId, devId)

        Detail From Wrapped C API:
            Function :      int32 flGetFlashInfo(uint16* sectors, uint16* sizeMbits,
                                                 uint32* manId, uint32* devId)

            Parameters :    sectors -
                                Location for receiving the number of sectors in the NVM
                                device.
                                <p>
                                Note that the maximum value that can be returned is 65535.
                                If the NVM device sector count exceeds this value then 65535
                                will be returned. See flGetFlashInfoEx to avoid this limitation.

                            sizeMbits -
                                Location for receiving the size of the NVM device in MBits.
                                <p>
                                Note that some chips have reserved sectors, which reduces
                                the amount of space available. This value is rounded to the
                                nearest integer to give the expected total size of the NVM.
                                For a more accurate value, use NvsCmd.

                            manId -
                                Location for receiving the manufacturer ID of the NVM device.
                                <p>
                                Note that for CSR102x ICs, the manufacturer ID cannot be
                                obtained, therefore this value is always set to 0.

                            devId -
                                Location for receiving the device ID of the NVM device.
                                <p>
                                Note that for CSR102x ICs, the device ID cannot be
                                obtained, therefore this value is always set to 0.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Gets the NVM information, including the number of sectors, size,
                            manufacturer ID, and device ID.
                            <p>
                            This function is deprecated. Use flGetFlashInfoEx instead.
                            <p>
                            This function will fail if called when a threaded (spawned)
                            operation is in progress.

            Deprecated :

        """
        self.TestFlashDLL.flGetFlashInfo.restype = ct.c_int32
        self.TestFlashDLL.flGetFlashInfo.argtypes = [ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_sectors = ct.c_uint16(sectors)
        local_sizeMbits = ct.c_uint16(sizeMbits)
        local_manId = ct.c_uint32(manId)
        local_devId = ct.c_uint32(devId)
        retval = self.TestFlashDLL.flGetFlashInfo(ct.byref(local_sectors), ct.byref(local_sizeMbits), ct.byref(local_manId), ct.byref(local_devId))
        sectors = local_sectors.value
        sizeMbits = local_sizeMbits.value
        manId = local_manId.value
        devId = local_devId.value
        return retval, sectors, sizeMbits, manId, devId
    # end of flGetFlashInfo


    def flmGetDeviceFlashInfo(self, device: int, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]:
        r"""Function TestFlash::flmGetDeviceFlashInfo() wrapper for flmGetDeviceFlashInfo in TestFlash DLL.

        Python API:
            flmGetDeviceFlashInfo(device: int, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]

        Python Example Call Syntax:
            retval, sectors, sizeMbits, manId, devId = myDll.flmGetDeviceFlashInfo(device=0)
            print(retval, sectors, sizeMbits, manId, devId)

        Detail From Wrapped C API:
            Function :      int32 flmGetDeviceFlashInfo(uint32 device, uint16* sectors,
                                                        uint16* sizeMbits, uint32* manId,
                                                        uint32* devId)

            Parameters :    device -
                                The index of the device for which to retrieve the NVM
                                information. E.g. to retrieve the information for the 3rd
                                device, the parameter is 2. For LPT-SPI transports only,
                                device indices start at 1, so the parameter value for the 3rd
                                device would be 3 in this case.

                            sectors -
                                See flGetFlashInfo.

                            sizeMbits -
                                See flGetFlashInfo.

                            manId -
                                See flGetFlashInfo.

                            devId -
                                See flGetFlashInfo.

            Returns :       See flGetFlashInfo.

            Description :   This is the multiple connection version of flGetFlashInfo. Refer
                            to flGetFlashInfo for more details.
                            <p>
                            This function is deprecated. Use flmGetDeviceFlashInfoEx instead.

            Deprecated :

        """
        self.TestFlashDLL.flmGetDeviceFlashInfo.restype = ct.c_int32
        self.TestFlashDLL.flmGetDeviceFlashInfo.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_sectors = ct.c_uint16(sectors)
        local_sizeMbits = ct.c_uint16(sizeMbits)
        local_manId = ct.c_uint32(manId)
        local_devId = ct.c_uint32(devId)
        retval = self.TestFlashDLL.flmGetDeviceFlashInfo(device, ct.byref(local_sectors), ct.byref(local_sizeMbits), ct.byref(local_manId), ct.byref(local_devId))
        sectors = local_sectors.value
        sizeMbits = local_sizeMbits.value
        manId = local_manId.value
        devId = local_devId.value
        return retval, sectors, sizeMbits, manId, devId
    # end of flmGetDeviceFlashInfo


    def flGetFlashInfoEx(self, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]:
        r"""Function TestFlash::flGetFlashInfoEx() wrapper for flGetFlashInfoEx in TestFlash DLL.

        Python API:
            flGetFlashInfoEx(sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]

        Python Example Call Syntax:
            retval, sectors, sizeMbits, manId, devId = myDll.flGetFlashInfoEx()
            print(retval, sectors, sizeMbits, manId, devId)

        Detail From Wrapped C API:
            Function :      int32 flGetFlashInfoEx(uint32* sectors, uint32* sizeMbits,
                                                   uint32* manId, uint32* devId)

            Parameters :    sectors -
                                Location for receiving the number of sectors in the NVM
                                device.

                            sizeMbits -
                                Location for receiving the size of the NVM device in MBits.
                                <p>
                                Note that some chips have reserved sectors, which reduces
                                the amount of space available. This value is rounded to the
                                nearest integer to give the expected total size of the NVM.
                                For a more accurate value, use NvsCmd.

                            manId -
                                Location for receiving the manufacturer ID of the NVM device.
                                <p>
                                Note that for CSR102x ICs, the manufacturer ID cannot be
                                obtained, therefore this value is always set to 0.

                            devId -
                                Location for receiving the device ID of the NVM device.
                                <p>
                                Note that for CSR102x ICs, the device ID cannot be
                                obtained, therefore this value is always set to 0.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Gets the NVM information, including the number of sectors, size,
                            manufacturer ID, and device ID.
                            <p>
                            This function will fail if called when a threaded (spawned)
                            operation is in progress.

        """
        self.TestFlashDLL.flGetFlashInfoEx.restype = ct.c_int32
        self.TestFlashDLL.flGetFlashInfoEx.argtypes = [ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_sectors = ct.c_uint32(sectors)
        local_sizeMbits = ct.c_uint32(sizeMbits)
        local_manId = ct.c_uint32(manId)
        local_devId = ct.c_uint32(devId)
        retval = self.TestFlashDLL.flGetFlashInfoEx(ct.byref(local_sectors), ct.byref(local_sizeMbits), ct.byref(local_manId), ct.byref(local_devId))
        sectors = local_sectors.value
        sizeMbits = local_sizeMbits.value
        manId = local_manId.value
        devId = local_devId.value
        return retval, sectors, sizeMbits, manId, devId
    # end of flGetFlashInfoEx


    def flmGetDeviceFlashInfoEx(self, device: int, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]:
        r"""Function TestFlash::flmGetDeviceFlashInfoEx() wrapper for flmGetDeviceFlashInfoEx in TestFlash DLL.

        Python API:
            flmGetDeviceFlashInfoEx(device: int, sectors: int=0, sizeMbits: int=0, manId: int=0, devId: int=0) -> Tuple[int, int, int, int, int]

        Python Example Call Syntax:
            retval, sectors, sizeMbits, manId, devId = myDll.flmGetDeviceFlashInfoEx(device=0)
            print(retval, sectors, sizeMbits, manId, devId)

        Detail From Wrapped C API:
            Function :      int32 flmGetDeviceFlashInfoEx(uint32 device, uint32* sectors,
                                                          uint32* sizeMbits, uint32* manId,
                                                          uint32* devId)

            Parameters :    device -
                                The index of the device for which to retrieve the NVM
                                information. E.g. to retrieve the information for the 3rd
                                device, the parameter is 2. For LPT-SPI transports only,
                                device indices start at 1, so the parameter value for the 3rd
                                device would be 3 in this case.

                            sectors -
                                See flGetFlashInfoEx.

                            sizeMbits -
                                See flGetFlashInfoEx.

                            manId -
                                See flGetFlashInfoEx.

                            devId -
                                See flGetFlashInfoEx.

            Returns :       See flGetFlashInfoEx.

            Description :   This is the multiple connection version of flGetFlashInfoEx. Refer
                            to flGetFlashInfoEx for more details.

        """
        self.TestFlashDLL.flmGetDeviceFlashInfoEx.restype = ct.c_int32
        self.TestFlashDLL.flmGetDeviceFlashInfoEx.argtypes = [ct.c_uint32, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p]
        local_sectors = ct.c_uint32(sectors)
        local_sizeMbits = ct.c_uint32(sizeMbits)
        local_manId = ct.c_uint32(manId)
        local_devId = ct.c_uint32(devId)
        retval = self.TestFlashDLL.flmGetDeviceFlashInfoEx(device, ct.byref(local_sectors), ct.byref(local_sizeMbits), ct.byref(local_manId), ct.byref(local_devId))
        sectors = local_sectors.value
        sizeMbits = local_sizeMbits.value
        manId = local_manId.value
        devId = local_devId.value
        return retval, sectors, sizeMbits, manId, devId
    # end of flmGetDeviceFlashInfoEx


    def flSetFlashType(self, type: int) -> int:
        r"""Function TestFlash::flSetFlashType() wrapper for flSetFlashType in TestFlash DLL.

        Python API:
            flSetFlashType(type: int) -> int

        Python Example Call Syntax:
            retval = myDll.flSetFlashType(type=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flSetFlashType(uint8 type)

            Parameters :    type -
                                The type of NVM to use:
                                <table>
                                    <tr><td>TFL_TYPE_STANDARD                <td> 0
                                    <tr><td>TFL_TYPE_SPIF                    <td> 1
                                    <tr><td>TFL_TYPE_SQIF                    <td> 2
                                    <tr><td>TFL_TYPE_MTP                     <td> 3
                                    <tr><td>TFL_TYPE_OTP                     <td> 4
                                    <tr><td>TFL_TYPE_SMEM                    <td> 5
                                    <tr><td>TFL_TYPE_E2                      <td> 6
                                </table>

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Sets the NVM type to the variant specified. Call this function
                            before any other functions that operate on NVM (unless the
                            default NVM type is appropriate).
                            <p>
                            The default NVM type for BlueCore ICs is TFL_TYPE_STANDARD. This
                            flash memory type is generally used for device firmware, and
                            depending on the chip type, this is either internal to the chip
                            package, or mandatory external flash. TFL_TYPE_SPIF means external
                            "Serial SPI Flash", and TFL_TYPE_SQIF means external "Serial Quad
                            Interface Flash". Some devices may use standard flash and either
                            SPIF or SQIF. Some devices can use generic NVM, which exists in
                            either flash(SMEM), One-Time-Programmable (OTP), or
                            Multi-Time-Programmable (MTP) forms.
                            <p>
                            For CSRA681xx, QCC302x-8x and QCC512x-8x ICs, the default flash
                            type is TFL_TYPE_SQIF.
                            <p>
                            For CSR102x ICs, one of TFL_TYPE_MTP, TFL_TYPE_OTP and
                            TFL_TYPE_SMEM must be selected.

        """
        self.TestFlashDLL.flSetFlashType.restype = ct.c_int32
        self.TestFlashDLL.flSetFlashType.argtypes = [ct.c_uint8]
        
        retval = self.TestFlashDLL.flSetFlashType(type)
        
        return retval
    # end of flSetFlashType


    def flmSetFlashType(self, deviceMask: int, type: int) -> int:
        r"""Function TestFlash::flmSetFlashType() wrapper for flmSetFlashType in TestFlash DLL.

        Python API:
            flmSetFlashType(deviceMask: int, type: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmSetFlashType(deviceMask=0, type=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmSetFlashType(uint32 deviceMask, uint8 type)

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            type -
                                See flSetFlashType.

            Returns :       See flSetFlashType.

            Description :   This is the multiple connection version of flSetFlashType. Refer
                            to flSetFlashType for more details.

        """
        self.TestFlashDLL.flmSetFlashType.restype = ct.c_int32
        self.TestFlashDLL.flmSetFlashType.argtypes = [ct.c_uint32, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmSetFlashType(deviceMask, type)
        
        return retval
    # end of flmSetFlashType


    def flSetPios(self, pioSclk: int, pioMiso: int, reserved: int) -> int:
        r"""Function TestFlash::flSetPios() wrapper for flSetPios in TestFlash DLL.

        Python API:
            flSetPios(pioSclk: int, pioMiso: int, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.flSetPios(pioSclk=0, pioMiso=0, reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flSetPios(uint8 pioSclk, uint8 pioMiso, uint8 reserved)

            Parameters :    pioSclk -
                                The PIO that is connected to SPI SCLK.

                            pioMiso -
                                The PIO that is connected to SPI MISO.

                            reserved -
                                Reserved parameter (currently unused).

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Sets the PIOs that are connected to the serial flash.

        """
        self.TestFlashDLL.flSetPios.restype = ct.c_int32
        self.TestFlashDLL.flSetPios.argtypes = [ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flSetPios(pioSclk, pioMiso, reserved)
        
        return retval
    # end of flSetPios


    def flmSetPios(self, deviceMask: int, pioSclk: int, pioMiso: int, reserved: int) -> int:
        r"""Function TestFlash::flmSetPios() wrapper for flmSetPios in TestFlash DLL.

        Python API:
            flmSetPios(deviceMask: int, pioSclk: int, pioMiso: int, reserved: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmSetPios(deviceMask=0, pioSclk=0, pioMiso=0, reserved=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flmSetPios(uint32 deviceMask, uint8 pioSclk, uint8 pioMiso,
                                              uint8 reserved)

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            pioSclk -
                                The PIO that is connected to SPI SCLK.

                            pioMiso -
                                The PIO that is connected to SPI MISO.

                            reserved -
                                Reserved parameter (currently unused).

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Sets the PIOs that are connected to the serial flash.

        """
        self.TestFlashDLL.flmSetPios.restype = ct.c_int32
        self.TestFlashDLL.flmSetPios.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmSetPios(deviceMask, pioSclk, pioMiso, reserved)
        
        return retval
    # end of flmSetPios


    def flSetSubsysChipSel(self, subSys: int, chipSel: int) -> int:
        r"""Function TestFlash::flSetSubsysChipSel() wrapper for flSetSubsysChipSel in TestFlash DLL.

        Python API:
            flSetSubsysChipSel(subSys: int, chipSel: int) -> int

        Python Example Call Syntax:
            retval = myDll.flSetSubsysChipSel(subSys=0, chipSel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flSetSubsysChipSel(uint8 subSys, uint8 chipSel)

            Parameters :    subSys -
                                The subsystem targetted. Values are device dependent.
                                <p>
                                For CSRA681xx devices, typical values include:
                                <table>
                                    <tr><td>3 = Audio
                                    <tr><td>4 = Application
                                </table>
                                <p>
                                For QCC302x-8x and QCC512x-8x devices, the only supported
                                value is 4 (Application).

                            chipSel -
                                The chip select of the attached flash memory, e.g. 0.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Sets the subsystem and flash chip select parameters.
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx devices, the application subsystem flash must
                            be programmed with a valid image before operations can be
                            performed on the audio subsystem flash.

        """
        self.TestFlashDLL.flSetSubsysChipSel.restype = ct.c_int32
        self.TestFlashDLL.flSetSubsysChipSel.argtypes = [ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flSetSubsysChipSel(subSys, chipSel)
        
        return retval
    # end of flSetSubsysChipSel


    def flmSetSubsysChipSel(self, deviceMask: int, subSys: int, chipSel: int) -> int:
        r"""Function TestFlash::flmSetSubsysChipSel() wrapper for flmSetSubsysChipSel in TestFlash DLL.

        Python API:
            flmSetSubsysChipSel(deviceMask: int, subSys: int, chipSel: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmSetSubsysChipSel(deviceMask=0, subSys=0, chipSel=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flmSetSubsysChipSel(uint32 deviceMask, uint8 subSys,
                                                       uint8 chipSel)

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            subSys -
                                The subsystem targetted. Values are device dependent.
                                <p>
                                For CSRA681xx devices, typical values include:
                                <table>
                                    <tr><td>3 = Audio
                                    <tr><td>4 = Application
                                </table>
                                <p>
                                For QCC302x-8x and QCC512x-8x devices, the only supported
                                value is 4 (Application).

                            chipSel -
                                The chip select of the attached flash memory, e.g. 0.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Sets the subsystem and flash chip select parameters.
                            <p>
                            This function is not applicable for (and has no effect on) 
                            BlueCore or Bluetooth low energy ICs.
                            <p>
                            NOTE: For CSRA681xx devices, the application subsystem flash must
                            be programmed with a valid image before operations can be
                            performed on the audio subsystem flash.

        """
        self.TestFlashDLL.flmSetSubsysChipSel.restype = ct.c_int32
        self.TestFlashDLL.flmSetSubsysChipSel.argtypes = [ct.c_uint32, ct.c_uint8, ct.c_uint8]
        
        retval = self.TestFlashDLL.flmSetSubsysChipSel(deviceMask, subSys, chipSel)
        
        return retval
    # end of flmSetSubsysChipSel


    def flSetSqifAccess(self, fileName: str) -> int:
        r"""Function TestFlash::flSetSqifAccess() wrapper for flSetSqifAccess in TestFlash DLL.

        Python API:
            flSetSqifAccess(fileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flSetSqifAccess(fileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flSetSqifAccess(const char* fileName)

            Parameters :    filename -
                                The name of the file containing the initialisation settings
                                allowing use of SQIF parts from alternative manufacturers.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Defines the single override file to be used to enable access to
                            the specified SQIF.
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx devices, the application subsystem flash must
                            be programmed with a valid image before operations can be
                            performed on the audio subsystem flash.

        """
        self.TestFlashDLL.flSetSqifAccess.restype = ct.c_int32
        self.TestFlashDLL.flSetSqifAccess.argtypes = [ct.c_char_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flSetSqifAccess(local_fileName)
        
        return retval
    # end of flSetSqifAccess


    def flmSetSqifAccess(self, deviceMask: int, fileName: str) -> int:
        r"""Function TestFlash::flmSetSqifAccess() wrapper for flmSetSqifAccess in TestFlash DLL.

        Python API:
            flmSetSqifAccess(deviceMask: int, fileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flmSetSqifAccess(deviceMask=0, fileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32  flmSetSqifAccess(uint32 deviceMask, const char* fileName);

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            fileName -
                                The name of the file containing the initialisation settings
                                allowing use of SQIF parts from alternative manufacturers.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Defines the single override file to be used to enable access to
                            the specified SQIF.
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx devices, the application subsystem flash must
                            be programmed with a valid image before operations can be
                            performed on the audio subsystem flash.

        """
        self.TestFlashDLL.flmSetSqifAccess.restype = ct.c_int32
        self.TestFlashDLL.flmSetSqifAccess.argtypes = [ct.c_uint32, ct.c_char_p]
        local_fileName = None if fileName is None else ct.create_string_buffer(bytes(fileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmSetSqifAccess(deviceMask, local_fileName)
        
        return retval
    # end of flmSetSqifAccess


    def flSetSecurityKey(self, keyValOrFileName: str) -> int:
        r"""Function TestFlash::flSetSecurityKey() wrapper for flSetSecurityKey in TestFlash DLL.

        Python API:
            flSetSecurityKey(keyValOrFileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flSetSecurityKey(keyValOrFileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flSetSecurityKey(const char* keyValOrFileName)

            Parameters :    keyValOrFileName -
                                Either the key value, or the path and filename of a text file
                                that contains the key value.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Writes the security key value to the device.
                            <p>
                            If the keyValOrFileName is not recognised as a key value then
                            it is assumed to be the name of a file, and this file will be
                            opened to read the key value.
                            Valid key values are always a string of HEX digits.
                            32 HEX digits = Raw 128bit key value
                            192 HEX digits = Encrypted key in wrapped key format
                            256 HEX digits = Encrypted key in anti-replay wrapped key format
                            Anything else = name of text file containing the key value
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx, QCC302x-8x, and QCC512x-8x devices, the
                            key is 128 bits long (32 HEX digits).
                            Use of the security key is enabled by calling flEnableSecurity.

        """
        self.TestFlashDLL.flSetSecurityKey.restype = ct.c_int32
        self.TestFlashDLL.flSetSecurityKey.argtypes = [ct.c_char_p]
        local_keyValOrFileName = None if keyValOrFileName is None else ct.create_string_buffer(bytes(keyValOrFileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flSetSecurityKey(local_keyValOrFileName)
        
        return retval
    # end of flSetSecurityKey


    def flmSetSecurityKey(self, deviceMask: int, keyValOrFileName: str) -> int:
        r"""Function TestFlash::flmSetSecurityKey() wrapper for flmSetSecurityKey in TestFlash DLL.

        Python API:
            flmSetSecurityKey(deviceMask: int, keyValOrFileName: str) -> int

        Python Example Call Syntax:
            retval = myDll.flmSetSecurityKey(deviceMask=0, keyValOrFileName='abc')
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmSetSecurityKey(uint32 deviceMask, 
                                                    const char* keyValOrFileName);

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            keyValOrFileName -
                                See flSetSecurityKey.

            Returns :       See flSetSecurityKey.

            Description :   Writes the security key value to the devices.
                            <p>
                            See flSetSecurityKey.

        """
        self.TestFlashDLL.flmSetSecurityKey.restype = ct.c_int32
        self.TestFlashDLL.flmSetSecurityKey.argtypes = [ct.c_uint32, ct.c_char_p]
        local_keyValOrFileName = None if keyValOrFileName is None else ct.create_string_buffer(bytes(keyValOrFileName, encoding="UTF-8"))
        retval = self.TestFlashDLL.flmSetSecurityKey(deviceMask, local_keyValOrFileName)
        
        return retval
    # end of flmSetSecurityKey


    def flEnableSecurity(self, options: int) -> int:
        r"""Function TestFlash::flEnableSecurity() wrapper for flEnableSecurity in TestFlash DLL.

        Python API:
            flEnableSecurity(options: int) -> int

        Python Example Call Syntax:
            retval = myDll.flEnableSecurity(options=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flEnableSecurity(uint32 options)

            Parameters :    options -
                                A value to define what security aspects are to be enabled,
                                where each bit specifies a security aspect as follows:
                                <table>
                                    <tr><td>Bit 0     <td>Encryption
                                    <tr><td>Bit 1     <td>Debug Transport Lock
                                    <tr><td>Bit 2     <td>USB Debug disabled
                                    <tr><td>Bit 3..31 <td>Reserved. Must be set to zero
                                                          unless advised otherwise by QTIL.
                                </table>
                                <p>
                                NOTE: In addition to those listed above, the USBDBG_ALLOWED
                                security function can be set with the SecureKeyCmd tool.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Enables one or more security aspects.
                            <p>
                            Security aspects enabled with this function become active after 
                            the next power cycle, device reset, or flClose/flCloseRet call.
                            See flResetAndStart for details of performing a device reset.
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx, QCC302x-8x, and QCC512x-8x devices, the
                            same key (written with flSetSecurityKey) is used for debug
                            transport locking and encryption, and the Debug Transport Lock bit
                            has no effect unless the Encryption bit is also set (or encryption
                            has been previously enabled). Once both the encryption and debug
                            transport lock security aspects are active, the correct key will
                            need to be supplied when opening a connection. See flOpenUnlock
                            for details.
                            <p>
                            NOTE: If the "USB Debug disabled" option is set, USB Debug will
                            be permanently disabled, with no means to re-enable it. It is
                            not recommended that this is done unless another debug transport
                            (such as TRB) is available.

        """
        self.TestFlashDLL.flEnableSecurity.restype = ct.c_int32
        self.TestFlashDLL.flEnableSecurity.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flEnableSecurity(options)
        
        return retval
    # end of flEnableSecurity


    def flmEnableSecurity(self, deviceMask: int, options: int) -> int:
        r"""Function TestFlash::flmEnableSecurity() wrapper for flmEnableSecurity in TestFlash DLL.

        Python API:
            flmEnableSecurity(deviceMask: int, options: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmEnableSecurity(deviceMask=0, options=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 flmEnableSecurity(uint32 deviceMask, uint32 options);

            Parameters :    deviceMask -
                                A bit mask of the devices to be set. See flmOpen for the
                                details of this parameter.

                            options -
                                see flEnableSecurity for details.

            Returns :       <table>
                                <tr><td>TFL_OK              <td>0
                                <tr><td>TFL_ERROR           <td>-1
                            </table>

            Description :   Enables one or more security aspects.
                            <p>
                            Security aspects enabled with this function become active after
                            the next power cycle, device reset, or flmClose/flmCloseRet call.
                            See flmResetAndStart for details of performing a device reset.
                            <p>
                            This function is not applicable for BlueCore or Bluetooth low
                            energy ICs.
                            <p>
                            NOTE: For CSRA681xx, QCC302x-8x, and QCC512x-8x devices, the
                            same key (written with flmSetSecurityKey) is used for debug
                            transport locking and encryption, and the Debug Transport Lock bit
                            has no effect unless the Encryption bit is also set (or encryption
                            has been previously enabled). Once both the encryption and debug
                            transport lock security aspects are active, the correct key will
                            need to be supplied when opening a connection. See flmOpenUnlock
                            for details.
                            <p>
                            NOTE: If the "USB Debug disabled" option is set, USB Debug will
                            be permanently disabled, with no means to re-enable it. It is
                            not recommended that this is done unless another debug transport
                            (such as TRB) is available.

        """
        self.TestFlashDLL.flmEnableSecurity.restype = ct.c_int32
        self.TestFlashDLL.flmEnableSecurity.argtypes = [ct.c_uint32, ct.c_uint32]
        
        retval = self.TestFlashDLL.flmEnableSecurity(deviceMask, options)
        
        return retval
    # end of flmEnableSecurity


    def flGetChipId(self) -> int:
        r"""Function TestFlash::flGetChipId() wrapper for flGetChipId in TestFlash DLL.

        Python API:
            flGetChipId() -> int

        Python Example Call Syntax:
            retval = myDll.flGetChipId()
            print(retval)

        Detail From Wrapped C API:
            Function :      uint16 flGetChipId(void)

            Parameters :    None

            Returns :       The chip ID, 0 if unknown.

            Description :   Returns the ID of the connected device (if known).

        """
        self.TestFlashDLL.flGetChipId.restype = ct.c_uint16
        self.TestFlashDLL.flGetChipId.argtypes = []
        
        retval = self.TestFlashDLL.flGetChipId()
        
        return retval
    # end of flGetChipId


    def flmGetChipId(self, device: int) -> int:
        r"""Function TestFlash::flmGetChipId() wrapper for flmGetChipId in TestFlash DLL.

        Python API:
            flmGetChipId(device: int) -> int

        Python Example Call Syntax:
            retval = myDll.flmGetChipId(device=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      uint16 flmGetChipId(uint32 device)

            Parameters :    device -
                                The index of the device for which to retrieve the chip ID.
                                E.g. to retrieve the chip ID for the 3rd device, the parameter
                                is 2. For LPT-SPI transports only, device indices start at 1,
                                so the parameter value for the 3rd device would be 3 in this
                                case.

            Returns :       See flGetChipId.

            Description :   This is the multiple connection version of flGetChipId.
                            See flGetChipId for details.

        """
        self.TestFlashDLL.flmGetChipId.restype = ct.c_uint16
        self.TestFlashDLL.flmGetChipId.argtypes = [ct.c_uint32]
        
        retval = self.TestFlashDLL.flmGetChipId(device)
        
        return retval
    # end of flmGetChipId


    def open_ps(self, port: int, device: int) -> int:
        r"""Function TestFlash::open_ps() wrapper for open_ps in TestFlash DLL.

        Python API:
            open_ps(port: int, device: int) -> int

        Python Example Call Syntax:
            retval = myDll.open_ps(port=0, device=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 open_ps(int32 port, int32 device)

            Parameters :    port -
                                Number of the LPT port to be used

                            device -
                                Number referring to the device to be communicated with, 0
                                to 15 referring to the port on the gang programmer. If the
                                gang programmer is not used then this should be set to 0.

            Returns :       non-zero on success, 0 on failure.

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to create the appropriate host side
                            objects to enable PS reads and writes via the SPI or gang
                            programming interface.

            Deprecated :

        """
        self.TestFlashDLL.open_ps.restype = ct.c_int32
        self.TestFlashDLL.open_ps.argtypes = [ct.c_int32, ct.c_int32]
        
        retval = self.TestFlashDLL.open_ps(port, device)
        
        return retval
    # end of open_ps


    def close_ps(self) -> int:
        r"""Function TestFlash::close_ps() wrapper for close_ps in TestFlash DLL.

        Python API:
            close_ps() -> int

        Python Example Call Syntax:
            retval = myDll.close_ps()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 close_ps(void)

            Parameters :    None

            Returns :       1.

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to free any objects associated with
                            open_ps().

            Deprecated :

        """
        self.TestFlashDLL.close_ps.restype = ct.c_int32
        self.TestFlashDLL.close_ps.argtypes = []
        
        retval = self.TestFlashDLL.close_ps()
        
        return retval
    # end of close_ps


    def set_stores(self, store: int):
        r"""Function TestFlash::set_stores() wrapper for set_stores in TestFlash DLL.

        Python API:
            set_stores(store: int)

        Python Example Call Syntax:
            retval = myDll.set_stores(store=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      void set_stores(const uint16 store)

            Parameters :    store -
                                Bit mask to identify the PS store layer to write to. See
                                comments above under PS_STORES.

            Returns :       None

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>Sets the PS store to access.

            Deprecated :

        """
        self.TestFlashDLL.set_stores.restype = None
        self.TestFlashDLL.set_stores.argtypes = [ct.c_uint16]
        
        retval = self.TestFlashDLL.set_stores(store)
        
        return retval
    # end of set_stores


    def write_ps(self, key: int, data: list, keyLen: int) -> int:
        r"""Function TestFlash::write_ps() wrapper for write_ps in TestFlash DLL.

        Python API:
            write_ps(key: int, data: list, keyLen: int) -> int

        Python Example Call Syntax:
            retval = myDll.write_ps(key=0, data=[0,1], keyLen=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 write_ps(const uint16 key, const uint16 *const data,
                                           const uint16 keyLen)

            Parameters :    key -
                                The PS key entry id.

                            data -
                                Pointer to an array holding the PS data to be written.

                            keyLen -
                                The size of the array of PS data.

            Returns :       0 on fail, 1 on success

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to write to the persistent store.

            Deprecated :

        """
        self.TestFlashDLL.write_ps.restype = ct.c_int32
        self.TestFlashDLL.write_ps.argtypes = [ct.c_uint16, ct.c_void_p, ct.c_uint16]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestFlashDLL.write_ps(key, local_data, keyLen)
        
        return retval
    # end of write_ps


    def write_ps_verify(self, key: int, data: list, keyLen: int) -> int:
        r"""Function TestFlash::write_ps_verify() wrapper for write_ps_verify in TestFlash DLL.

        Python API:
            write_ps_verify(key: int, data: list, keyLen: int) -> int

        Python Example Call Syntax:
            retval = myDll.write_ps_verify(key=0, data=[0,1], keyLen=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 write_ps_verify(const uint16 key, const uint16 *const data,
                                                  const uint16 keyLen)

            Parameters :    key -
                                The PS key entry id.

                            data -
                                Pointer to an array holding the PS data to be written.

                            keyLen -
                                The size of the array of PS data.

            Returns :       0 on fail, 1 on success, i.e. the key was verified as written.

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to write and subsequently read and
                            compare the persistent store. Prior to calling this, you could
                            call set_stores with a bit pattern incorporating either
                            PS_STORES_I or PS_STORES_F, but the default for the stores being
                            (PS_STORES_I | PS_STORES_F | PS_STORES_R) means you need not
                            worry about calling set_stores in every case.

            Deprecated :

        """
        self.TestFlashDLL.write_ps_verify.restype = ct.c_int32
        self.TestFlashDLL.write_ps_verify.argtypes = [ct.c_uint16, ct.c_void_p, ct.c_uint16]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * len(data))(*data)
        retval = self.TestFlashDLL.write_ps_verify(key, local_data, keyLen)
        
        return retval
    # end of write_ps_verify


    def read_ps(self, key: int, data: list, maxlen: int, keyLen: int) -> Tuple[int, list]:
        r"""Function TestFlash::read_ps() wrapper for read_ps in TestFlash DLL.

        Python API:
            read_ps(key: int, data: list, maxlen: int, keyLen: int) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, data = myDll.read_ps(key=0, data=[0,1], maxlen=0, keyLen=0)
            print(retval, data)

        Detail From Wrapped C API:
            Function :      int32 read_ps(const uint16 key, uint16 *const data,
                                          const uint16 maxlen, uint16 * const keyLen)

            Parameters :    key -
                                The PS key entry id.

                            data -
                                A preallocated array to receive the PS data to be read.

                            maxlen -
                                The size of the data array

                            keyLen -
                                The actual size of the read key

            Returns :       0 on fail, 1 on success

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to read from the persistent store.

            Deprecated :

        """
        self.TestFlashDLL.read_ps.restype = ct.c_int32
        self.TestFlashDLL.read_ps.argtypes = [ct.c_uint16, ct.c_void_p, ct.c_uint16, ct.c_void_p]
        if data == None:
            data = []
        local_data = (ct.c_uint16 * max(maxLen, len(data)))(*data)
        local_keyLen = ct.c_uint16(keyLen)
        retval = self.TestFlashDLL.read_ps(key, local_data, maxlen, ct.byref(local_keyLen))
        data = local_data[:]
        keyLen = local_keyLen.value
        return retval, data
    # end of read_ps


    def clear_ps(self, key: int) -> int:
        r"""Function TestFlash::clear_ps() wrapper for clear_ps in TestFlash DLL.

        Python API:
            clear_ps(key: int) -> int

        Python Example Call Syntax:
            retval = myDll.clear_ps(key=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 clear_ps(const uint16 key)

            Parameters :    key -
                                The PS key entry id.

            Returns :       0 on fail, 1 on success

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to clear a persistent store entry.

            Deprecated :

        """
        self.TestFlashDLL.clear_ps.restype = ct.c_int32
        self.TestFlashDLL.clear_ps.argtypes = [ct.c_uint16]
        
        retval = self.TestFlashDLL.clear_ps(key)
        
        return retval
    # end of clear_ps


    def factory_set(self) -> int:
        r"""Function TestFlash::factory_set() wrapper for factory_set in TestFlash DLL.

        Python API:
            factory_set() -> int

        Python Example Call Syntax:
            retval = myDll.factory_set()
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 factory_set(void)

            Parameters :    None

            Returns :       0 on fail, 1 on success

            Description :   <i>Use of persistent store functions in TestFlash are deprecated
                            and may disappear in a future release. The persistent store
                            functions in TestEngine should be used instead.</i>
                            <p>This function is used to move PS values to the factory layer.

            Deprecated :

        """
        self.TestFlashDLL.factory_set.restype = ct.c_int32
        self.TestFlashDLL.factory_set.argtypes = []
        
        retval = self.TestFlashDLL.factory_set()
        
        return retval
    # end of factory_set


    def e2_device(self, log2bytes: int, addrmask: int) -> int:
        r"""Function TestFlash::e2_device() wrapper for e2_device in TestFlash DLL.

        Python API:
            e2_device(log2bytes: int, addrmask: int) -> int

        Python Example Call Syntax:
            retval = myDll.e2_device(log2bytes=0, addrmask=0)
            print(retval)

        Detail From Wrapped C API:
            Function :      int32 e2_device(const uint16 log2bytes, const uint16 addrmask)

            Parameters :    log2bytes -
                                Size of the EEPROM device specified in log2 bytes (e.g. 8Kbit
                                device = 10).

                            addrmask -
                                EEPROM device address.

            Returns :       0 on fail, 1 on success

            Description :   <i>This function is deprecated and may disappear in a future
                            release. Use the EEPROM utility API (e2api) for programming
                            EEPROM devices, or alternatively, use the TestEngine function
                            bccmdSetEeprom to write the BlueCore EEPROM header.</i>
                            <p>This function is used to detect an EEPROM device connected
                            to the BlueCore.
                            <p>Before this function can be used a SPI connection must be
                            created with a call to open_ps.

            Deprecated :

        """
        self.TestFlashDLL.e2_device.restype = ct.c_int32
        self.TestFlashDLL.e2_device.argtypes = [ct.c_uint16, ct.c_uint16]
        
        retval = self.TestFlashDLL.e2_device(log2bytes, addrmask)
        
        return retval
    # end of e2_device


    def get_firmware_id(self, id: int, nameBuffer: list, length: int) -> Tuple[int, list]:
        r"""Function TestFlash::get_firmware_id() wrapper for get_firmware_id in TestFlash DLL.

        Python API:
            get_firmware_id(id: int, nameBuffer: list, length: int) -> Tuple[int, list]

        Python Example Call Syntax:
            retval, nameBuffer = myDll.get_firmware_id(id=0, nameBuffer=[0,1], length=0)
            print(retval, nameBuffer)

        Detail From Wrapped C API:
            Function :      int32 get_firmware_id(int32 *const id, uint16 *nameBuffer,
                                                  const uint32 length)

            Parameters :    id -
                                Pointer to a location to take the firmware ID.

                            nameBuffer -
                                Pointer to a pre-allocated array of size given by the length
                                parameter.

                            length -
                                Length of the given name buffer.

            Returns :       0 on fail, 1 on success

            Description :   <i>This function is deprecated and may disappear in a future
                            release. Use the TestFlash function flGetFirmwareIds instead.</i>
                            <p>This function is used to retrieve the firmware ID of the
                            connected BlueCore device.
                            <p>Before this function can be used a SPI connection must be
                            created with a call to open_ps.

            Deprecated :

        """
        self.TestFlashDLL.get_firmware_id.restype = ct.c_int32
        self.TestFlashDLL.get_firmware_id.argtypes = [ct.c_void_p, ct.c_void_p, ct.c_uint32]
        local_id = ct.c_int32(id)
        if nameBuffer == None:
            nameBuffer = []
        local_nameBuffer = (ct.c_uint16 * max(length, len(nameBuffer)))(*nameBuffer)
        retval = self.TestFlashDLL.get_firmware_id(ct.byref(local_id), local_nameBuffer, length)
        id = local_id.value
        nameBuffer = local_nameBuffer[:]
        return retval, nameBuffer
    # end of get_firmware_id



    #
    # DEPRECATED FUNCTIONS
    #
    init_flash = flOpen
    read_program_files = flReadProgramFiles
    program_flash_block = flProgramBlock
    erase_flash = flErase
    gang_program_flash_block = flGangProgramBlock
    get_bit_error_field = flGetBitErrorField
    program_flash_spawn = flProgramSpawn
    gang_program_flash_spawn = flGangProgramSpawn
    get_spawned_progress = flGetProgress
    get_spawned_error = flGetLastError
    reset_and_start = flResetAndStart
    close_flash = flClose
    get_version = flGetVersion
    flGetAvailableSpiPorts = flGetAvailablePorts
    flmGetAvailableSpiPorts = flmGetAvailablePorts
    flInit = flOpen
    flInitTrans = flOpenTrans
    flInitSpiUnlock = flOpenUnlock
    flInitSpiUnlockTrans = flOpenUnlockTrans
    flmOpenSpiUnlock = flmOpenUnlock
    flmOpenSpiUnlockTrans = flmOpenUnlockTrans
    flSetSubsysBank = flSetSubsysChipSel
    flmConvertSpiPort = flmConvertPort
    flmSetSubsysBank = flmSetSubsysChipSel

# endclass TestFlash

  