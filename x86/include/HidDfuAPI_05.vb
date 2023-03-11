' HidDfuAPI_05.vb : Declares the DLL functions for vb2005.
' Copyright (c) 2022 Qualcomm Technologies International, Ltd.
' All Rights Reserved.
' Qualcomm Technologies International, Ltd. Confidential and Proprietary.

' Auto-generated VB 05 wrapper for HidDfu DLL.
' Created on 2022-11-18 14:03 from HidDfu.h file

Imports System.Text
Imports System.Runtime.InteropServices


Module HidDfu
    Public Const HIDDFU_ERROR_NONE As Integer = 0
    Public Const HIDDFU_ERROR_SEQUENCE As Integer = -1
    Public Const HIDDFU_ERROR_CONNECTION As Integer = -2
    Public Const HIDDFU_ERROR_FILE_OPEN_FAILED As Integer = -3
    Public Const HIDDFU_ERROR_FILE_WRITE_FAILED As Integer = -4
    Public Const HIDDFU_ERROR_FILE_INVALID_FORMAT As Integer = -5
    Public Const HIDDFU_ERROR_FILE_CRC_INCORRECT As Integer = -6
    Public Const HIDDFU_ERROR_FILE_READ_FAILED As Integer = -7
    Public Const HIDDFU_ERROR_UPGRADE_FAILED As Integer = -8
    Public Const HIDDFU_ERROR_RESET_FAILED As Integer = -9
    Public Const HIDDFU_ERROR_OUT_OF_MEM As Integer = -10
    Public Const HIDDFU_ERROR_INVALID_PARAMETER As Integer = -11
    Public Const HIDDFU_ERROR_DRIVER_INTERFACE_FAILURE As Integer = -12
    Public Const HIDDFU_ERROR_OPERATION_FAILED_TO_START As Integer = -13
    Public Const HIDDFU_ERROR_BUSY As Integer = -14
    Public Const HIDDFU_ERROR_CLEAR_STATUS_FAILED As Integer = -15
    Public Const HIDDFU_ERROR_DEVICE_FIRMWARE As Integer = -16
    Public Const HIDDFU_ERROR_UNSUPPORTED As Integer = -17
    Public Const HIDDFU_ERROR_OPERATION_PARTIAL_SUCCESS As Integer = -18
    Public Const HIDDFU_ERROR_PARAM_TOO_SMALL As Integer = -19
    Public Const HIDDFU_ERROR_UNKNOWN As Integer = -20
    Public Const HIDDFU_ERROR_VERSION_MISMATCH As Integer = -21
    Public Const HIDDFU_ERROR_NO_OP_IN_PROGRESS As Integer = -22
    Public Const HIDDFU_ERROR_NO_RESPONSE As Integer = -23
    Public Const HIDDFU_ERROR_OP_PARTIAL_SUCCESS_NO_RESPONSE As Integer = -24
    Public Const PROGRESS_REBOOT_VALUE As Integer = 95
    Public Const RESTART_DELAY_SEC As UInteger = 60UI

    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetFirmwareVersions", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetFirmwareVersions (ByVal versionString As StringBuilder, ByRef maxLength As UShort, ByVal checkMatch As Byte) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetVersion", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetVersion (ByRef major As UShort, ByRef minor As UShort, ByRef release As UShort, ByRef build As UShort) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuConnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuConnect (ByVal vid As UShort, ByVal pid As UShort, ByVal usage As UShort, ByVal usagePage As UShort, ByRef count As UShort) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuDisconnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuDisconnect () As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuBackup", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuBackup (ByVal fileName As String, ByVal resetAfter As Byte) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuUpgrade", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuUpgrade (ByVal fileName As String, ByVal resetAfter As Byte) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuUpgradeBin", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuUpgradeBin (ByVal fileName As String) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuStop", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuStop (ByVal waitForStopMs As UShort) As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuResetDevice", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuResetDevice () As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetProgress", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetProgress () As Byte
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetResult", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetResult () As Integer
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetLastError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetLastError () As IntPtr
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuGetFailedDevicesCount", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuGetFailedDevicesCount () As Byte
    End Function
    <DllImport("HidDfu.dll", EntryPoint:="hidDfuSendCommand", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hidDfuSendCommand (ByRef data As Byte, ByVal length As UInteger) As Integer
    End Function

End Module


