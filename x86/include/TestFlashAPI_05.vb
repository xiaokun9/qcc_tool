' TestFlashAPI_05.vb : Declares the DLL functions for vb2005.
' Copyright (c) 2022 Qualcomm Technologies International, Ltd.
' All Rights Reserved.
' Qualcomm Technologies International, Ltd. Confidential and Proprietary.

' Auto-generated VB 05 wrapper for TestFlash DLL.
' Created on 2022-11-18 15:14 from TestFlash.h file

Imports System.Text
Imports System.Runtime.InteropServices


Module TestFlash
    Public Const TFL_OK As Integer = 0
    Public Const TFL_ERROR As Integer = -1
    Public Const TFL_DEVICE_ERROR As Integer = -2
    Public Const TFL_ERROR_UNSUPPORTED As Integer = -3
    Public Const TFL_SPI_LPT As Integer = &H1
    Public Const TFL_SPI_USB As Integer = &H2
    Public Const TFL_TRB As Integer = &H3
    Public Const TFL_USBDBG As Integer = &H4
    Public Const TFL_CHIP As Integer = 0
    Public Const TFL_FILE As Integer = 1
    Public Const TFL_ERROR_OPEN_FAILED As Integer = &H1001
    Public Const TFL_ERROR_DEVICE_OPEN As Integer = &H1002
    Public Const TFL_ERROR_DEVICE_NOT_OPEN As Integer = &H1003
    Public Const TFL_ERROR_DEVICE_BUSY As Integer = &H1004
    Public Const TFL_ERROR_THREAD_ERROR As Integer = &H1005
    Public Const TFL_ERROR_RESET_FAIL As Integer = &H1006
    Public Const TFL_ERROR_WRONG_TRANS As Integer = &H1008
    Public Const TFL_ERROR_SPIUNLOCK As Integer = &H1009
    Public Const TFL_MAX_DEVICES As Integer = 32
    Public Const TFL_ALL_DEVICES As Integer = &HFFFFFFFF
    Public Const TFL_TYPE_STANDARD As Integer = &H0
    Public Const TFL_TYPE_SPIF As Integer = &H1
    Public Const TFL_TYPE_SQIF As Integer = &H2
    Public Const TFL_TYPE_MTP As Integer = &H3
    Public Const TFL_TYPE_OTP As Integer = &H4
    Public Const TFL_TYPE_SMEM As Integer = &H5
    Public Const TFL_TYPE_E2 As Integer = &H6
    Public Const TFL_TRANS_CRIT_NOLOCK As Integer = &H1
    Public Const TFL_TRANS_CRIT_UNLOCKED As Integer = &H2
    Public Const TFL_TRANS_CRIT_LOCKED As Integer = &H4
    Public Const TFL_TRANS_CRIT_ALL As Integer = &H7
    Public Const TFL_TRANS_CRIT_DEFAULT As Integer = &H3

    <DllImport("TestFlash.dll", EntryPoint:="flOpen", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flOpen (ByVal port As Integer, ByVal xtal As Integer, ByVal delays As Integer, ByVal transport As Integer) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flOpenUnlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flOpenUnlock (ByVal port As Integer, ByVal xtal As Integer, ByVal delays As Integer, ByVal transport As Integer, ByVal unlockKey As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmOpen", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmOpen (ByVal deviceMask As UInteger, ByVal xtal As Integer, ByVal transport As Integer) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmOpenUnlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmOpenUnlock (ByVal deviceMask As UInteger, ByVal xtal As Integer, ByVal transport As Integer, ByVal unlockKey As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flOpenTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flOpenTrans (ByVal trans As String, ByVal xtal As Integer, ByVal delays As Integer) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flOpenUnlockTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flOpenUnlockTrans (ByVal trans As String, ByVal xtal As Integer, ByVal delays As Integer, ByVal unlockKey As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmOpenTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmOpenTrans (ByVal deviceMask As UInteger, ByVal trans As String, ByVal xtal As Integer) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmOpenUnlockTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmOpenUnlockTrans (ByVal deviceMask As UInteger, ByVal trans As String, ByVal xtal As Integer, ByVal unlockKey As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flReadProgramFiles", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flReadProgramFiles (ByVal fileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmReadProgramFiles", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmReadProgramFiles (ByVal fileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flProgramBlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flProgramBlock () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmProgramBlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmProgramBlock (ByVal deviceMask As UInteger, ByVal eraseFirst As Byte, ByVal verifyAfter As Byte, ByVal restartAfter As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flErase", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flErase () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmEraseBlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmEraseBlock (ByVal deviceMask As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmEraseSpawn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmEraseSpawn (ByVal deviceMask As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGangProgramBlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGangProgramBlock (ByVal deviceMask As UShort, ByVal eraseFirst As Byte, ByVal restartAfter As Byte, ByVal skipUnused As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetDetectedDevices", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetDetectedDevices () As UShort
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetBitErrorField", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetBitErrorField () As UShort
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetBitErrorField", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetBitErrorField () As UInteger
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flProgramSpawn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flProgramSpawn () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmProgramSpawn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmProgramSpawn (ByVal deviceMask As UInteger, ByVal eraseFirst As Byte, ByVal verifyAfter As Byte, ByVal restartAfter As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGangProgramSpawn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGangProgramSpawn (ByVal deviceMask As UShort, ByVal eraseFirst As Byte, ByVal restartAfter As Byte, ByVal skipUnused As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetProgress", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetProgress () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceProgress", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceProgress (ByVal device As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetLastError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetLastError () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetLastError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetLastError () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceError (ByVal device As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flResetAndStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flResetAndStart () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmResetAndStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmResetAndStart (ByVal deviceMask As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flClose", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Sub flClose ()
    End Sub
    <DllImport("TestFlash.dll", EntryPoint:="flCloseRet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flCloseRet () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmClose", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Sub flmClose (ByVal deviceMask As UInteger)
    End Sub
    <DllImport("TestFlash.dll", EntryPoint:="flmCloseRet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmCloseRet (ByVal deviceMask As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetVersion", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetVersion (ByVal versionStr As StringBuilder) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetVersion", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetVersion (ByVal versionStr As StringBuilder) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flStopProcessor", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flStopProcessor () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmStopProcessor", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmStopProcessor (ByVal deviceMask As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetDownloadTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetDownloadTime () As UInteger
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceDownloadTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceDownloadTime (ByVal device As UInteger) As UInteger
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetAvailablePorts", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetAvailablePorts (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetAvailablePortsEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetAvailablePortsEx (ByVal criteria As UInteger, ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetAvailablePorts", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetAvailablePorts (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetAvailablePortsEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetAvailablePortsEx (ByVal criteria As UInteger, ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmConvertPort", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmConvertPort (ByVal transIn As String, ByVal transOut As StringBuilder, ByRef device As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetFirmwareIds", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetFirmwareIds (ByVal source As Byte, ByRef loaderId As UInteger, ByVal loaderName As StringBuilder, ByRef stackId As UInteger, ByVal stackName As StringBuilder, ByVal maxNameLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceFirmwareIds", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceFirmwareIds (ByVal device As UInteger, ByRef loaderId As UInteger, ByVal loaderName As StringBuilder, ByRef stackId As UInteger, ByVal stackName As StringBuilder, ByVal maxNameLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetFileFirmwareIds", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetFileFirmwareIds (ByRef loaderId As UInteger, ByVal loaderName As StringBuilder, ByRef stackId As UInteger, ByVal stackName As StringBuilder, ByVal maxNameLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flVerify", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flVerify () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmVerifyBlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmVerifyBlock (ByVal deviceMask As UInteger, ByVal restartAfter As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmVerifySpawn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmVerifySpawn (ByVal deviceMask As UInteger, ByVal restartAfter As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetFlashInfo", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetFlashInfo (ByRef sectors As UShort, ByRef sizeMbits As UShort, ByRef manId As UInteger, ByRef devId As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceFlashInfo", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceFlashInfo (ByVal device As UInteger, ByRef sectors As UShort, ByRef sizeMbits As UShort, ByRef manId As UInteger, ByRef devId As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetFlashInfoEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetFlashInfoEx (ByRef sectors As UInteger, ByRef sizeMbits As UInteger, ByRef manId As UInteger, ByRef devId As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetDeviceFlashInfoEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetDeviceFlashInfoEx (ByVal device As UInteger, ByRef sectors As UInteger, ByRef sizeMbits As UInteger, ByRef manId As UInteger, ByRef devId As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flSetFlashType", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flSetFlashType (ByVal aType As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmSetFlashType", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmSetFlashType (ByVal deviceMask As UInteger, ByVal aType As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flSetPios", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flSetPios (ByVal pioSclk As Byte, ByVal pioMiso As Byte, ByVal reserved As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmSetPios", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmSetPios (ByVal deviceMask As UInteger, ByVal pioSclk As Byte, ByVal pioMiso As Byte, ByVal reserved As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flSetSubsysChipSel", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flSetSubsysChipSel (ByVal subSys As Byte, ByVal chipSel As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmSetSubsysChipSel", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmSetSubsysChipSel (ByVal deviceMask As UInteger, ByVal subSys As Byte, ByVal chipSel As Byte) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flSetSqifAccess", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flSetSqifAccess (ByVal fileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmSetSqifAccess", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmSetSqifAccess (ByVal deviceMask As UInteger, ByVal fileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flSetSecurityKey", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flSetSecurityKey (ByVal keyValOrFileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmSetSecurityKey", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmSetSecurityKey (ByVal deviceMask As UInteger, ByVal keyValOrFileName As String) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flEnableSecurity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flEnableSecurity (ByVal options As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmEnableSecurity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmEnableSecurity (ByVal deviceMask As UInteger, ByVal options As UInteger) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flGetChipId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flGetChipId () As UShort
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="flmGetChipId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function flmGetChipId (ByVal device As UInteger) As UShort
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="open_ps", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function open_ps (ByVal port As Integer, ByVal device As Integer) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="close_ps", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function close_ps () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="set_stores", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Sub set_stores (ByVal store As UShort)
    End Sub
    <DllImport("TestFlash.dll", EntryPoint:="write_ps", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function write_ps (ByVal key As UShort, ByVal data() As UShort, ByVal keyLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="write_ps_verify", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function write_ps_verify (ByVal key As UShort, ByVal data() As UShort, ByVal keyLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="read_ps", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function read_ps (ByVal key As UShort, ByVal data() As UShort, ByVal maxlen As UShort, ByRef keyLen As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="clear_ps", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function clear_ps (ByVal key As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="factory_set", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function factory_set () As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="e2_device", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function e2_device (ByVal log2bytes As UShort, ByVal addrmask As UShort) As Integer
    End Function
    <DllImport("TestFlash.dll", EntryPoint:="get_firmware_id", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function get_firmware_id (ByRef id As Integer, ByVal nameBuffer() As UShort, ByVal length As UInteger) As Integer
    End Function

' DEPRECATED FUNCTIONS
Declare Function init_flash Lib "TestFlash.dll" Alias "flOpen" (ByVal port As Integer, ByVal xtal As Integer, ByVal delays As Integer, ByVal transport As Integer) As Integer
Declare Function read_program_files Lib "TestFlash.dll" Alias "flReadProgramFiles" (ByVal fileName As String) As Integer
Declare Function program_flash_block Lib "TestFlash.dll" Alias "flProgramBlock" () As Integer
Declare Function erase_flash Lib "TestFlash.dll" Alias "flErase" () As Integer
Declare Function gang_program_flash_block Lib "TestFlash.dll" Alias "flGangProgramBlock" (ByVal deviceMask As UShort, ByVal eraseFirst As Byte, ByVal restartAfter As Byte, ByVal skipUnused As Byte) As Integer
Declare Function get_bit_error_field Lib "TestFlash.dll" Alias "flGetBitErrorField" () As UShort
Declare Function program_flash_spawn Lib "TestFlash.dll" Alias "flProgramSpawn" () As Integer
Declare Function gang_program_flash_spawn Lib "TestFlash.dll" Alias "flGangProgramSpawn" (ByVal deviceMask As UShort, ByVal eraseFirst As Byte, ByVal restartAfter As Byte, ByVal skipUnused As Byte) As Integer
Declare Function get_spawned_progress Lib "TestFlash.dll" Alias "flGetProgress" () As Integer
Declare Function get_spawned_error Lib "TestFlash.dll" Alias "flGetLastError" () As Integer
Declare Function reset_and_start Lib "TestFlash.dll" Alias "flResetAndStart" () As Integer
Declare Sub close_flash Lib "TestFlash.dll" Alias "flClose" ()
Declare Function get_version Lib "TestFlash.dll" Alias "flGetVersion" (ByVal versionStr As StringBuilder) As Integer
Declare Function flGetAvailableSpiPorts Lib "TestFlash.dll" Alias "flGetAvailablePorts" (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
Declare Function flmGetAvailableSpiPorts Lib "TestFlash.dll" Alias "flmGetAvailablePorts" (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
Declare Function flInit Lib "TestFlash.dll" Alias "flOpen" (ByVal port As Integer, ByVal xtal As Integer, ByVal delays As Integer, ByVal transport As Integer) As Integer
Declare Function flInitTrans Lib "TestFlash.dll" Alias "flOpenTrans" (ByVal trans As String, ByVal xtal As Integer, ByVal delays As Integer) As Integer
Declare Function flInitSpiUnlock Lib "TestFlash.dll" Alias "flOpenUnlock" (ByVal port As Integer, ByVal xtal As Integer, ByVal delays As Integer, ByVal transport As Integer, ByVal unlockKey As String) As Integer
Declare Function flInitSpiUnlockTrans Lib "TestFlash.dll" Alias "flOpenUnlockTrans" (ByVal trans As String, ByVal xtal As Integer, ByVal delays As Integer, ByVal unlockKey As String) As Integer
Declare Function flmOpenSpiUnlock Lib "TestFlash.dll" Alias "flmOpenUnlock" (ByVal deviceMask As UInteger, ByVal xtal As Integer, ByVal transport As Integer, ByVal unlockKey As String) As Integer
Declare Function flmOpenSpiUnlockTrans Lib "TestFlash.dll" Alias "flmOpenUnlockTrans" (ByVal deviceMask As UInteger, ByVal trans As String, ByVal xtal As Integer, ByVal unlockKey As String) As Integer
Declare Function flSetSubsysBank Lib "TestFlash.dll" Alias "flSetSubsysChipSel" (ByVal subSys As Byte, ByVal chipSel As Byte) As Integer
Declare Function flmConvertSpiPort Lib "TestFlash.dll" Alias "flmConvertPort" (ByVal transIn As String, ByVal transOut As StringBuilder, ByRef device As UInteger) As Integer
Declare Function flmSetSubsysBank Lib "TestFlash.dll" Alias "flmSetSubsysChipSel" (ByVal deviceMask As UInteger, ByVal subSys As Byte, ByVal chipSel As Byte) As Integer
End Module


