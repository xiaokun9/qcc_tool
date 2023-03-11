' TestEngineAPI_05.vb : Declares the DLL functions for vb2005.
' Copyright (c) 2022 Qualcomm Technologies International, Ltd.
' All Rights Reserved.
' Qualcomm Technologies International, Ltd. Confidential and Proprietary.

' Auto-generated VB 05 wrapper for TestEngine DLL.
' Created on 2022-11-18 15:48 from TestEngine.h file

Imports System.Text
Imports System.Runtime.InteropServices


Module TestEngine
    Public Const BER_BIT_COUNT As Integer = 0
    Public Const BER_BIT_ERRORS As Integer = 1
    Public Const BER_ACCESS_CODE As Integer = 2
    Public Const BER_RCVD_PKTS As Integer = 3
    Public Const BER_EXP_PKTS As Integer = 4
    Public Const BER_HDR_ERRORS As Integer = 5
    Public Const BER_CRC_ERRORS As Integer = 6
    Public Const BER_UNCORR_ERRORS As Integer = 7
    Public Const BER_SYNC_ERRORS As Integer = 8
    Public Const BER_MAX As Integer = 9
    Public Const VM_STATUS_BOOT As Integer = 0
    Public Const VM_STATUS_FAIL As Integer = 1
    Public Const VM_STATUS_RUN As Integer = 2
    Public Const VM_STATUS_PANIC As Integer = 3
    Public Const VM_STATUS_EXIT As Integer = 4
    Public Const CVC_PRODTEST_PASS As Integer = 1
    Public Const CVC_PRODTEST_FAIL As Integer = 2
    Public Const CVC_PRODTEST_NO_CHECK As Integer = 3
    Public Const CVC_PRODTEST_FILE_NOT_FOUND As Integer = 4
    Public Const TE_ERROR_NONE As Integer = &H0
    Public Const TE_ERROR_BCCMD_NO_SUCH_VARID As Integer = &H1
    Public Const TE_ERROR_BCCMD_DATA_EXCEEDED As Integer = &H2
    Public Const TE_ERROR_BCCMD_VAR_HAS_NO_VALUE As Integer = &H3
    Public Const TE_ERROR_BCCMD_BAD_VALUE As Integer = &H4
    Public Const TE_ERROR_BCCMD_NO_ACCESS As Integer = &H5
    Public Const TE_ERROR_BCCMD_READ_ONLY As Integer = &H6
    Public Const TE_ERROR_BCCMD_WRITE_ONLY As Integer = &H7
    Public Const TE_ERROR_BCCMD_OTHER_ERROR As Integer = &H8
    Public Const TE_ERROR_BCCMD_PERMISSION_DENIED As Integer = &H9
    Public Const TE_ERROR_HCI_UNKNOWN_COMMAND As Integer = &H10000
    Public Const TE_ERROR_HCI_UNKNOWN_CONNECTION_ID As Integer = &H20000
    Public Const TE_ERROR_HCI_HARDWARE_FAILURE As Integer = &H30000
    Public Const TE_ERROR_HCI_PAGE_TIMEOUT As Integer = &H40000
    Public Const TE_ERROR_HCI_AUTHENTICATION_FAILURE As Integer = &H50000
    Public Const TE_ERROR_HCI_PIN_MISSING As Integer = &H60000
    Public Const TE_ERROR_HCI_MEMORY_CAPACITY_EXCEEDED As Integer = &H70000
    Public Const TE_ERROR_HCI_CONNECTION_TIMEOUT As Integer = &H80000
    Public Const TE_ERROR_HCI_CONNECTION_LIMIT_EXCEEDED As Integer = &H90000
    Public Const TE_ERROR_HCI_SYNCHRONOUS_CONNECTION_LIMIT_EXCEEDED As Integer = &HA0000
    Public Const TE_ERROR_HCI_ACL_CONNECTION_ALREADY_EXISTS As Integer = &HB0000
    Public Const TE_ERROR_HCI_COMMAND_DISALLOWED As Integer = &HC0000
    Public Const TE_ERROR_HCI_CONNECTION_REJECTED_LIMITED_RESOURCES As Integer = &HD0000
    Public Const TE_ERROR_HCI_CONNECTION_REJECTED_SECURITY_REASONS As Integer = &HE0000
    Public Const TE_ERROR_HCI_CONNECTION_REJECTED_UNACCEPTABLE_BD_ADDR As Integer = &HF0000
    Public Const TE_ERROR_HCI_CONNECTION_ACCEPT_TIMEOUT_EXCEEDED As Integer = &H100000
    Public Const TE_ERROR_HCI_UNSUPPORTED_FEATURE As Integer = &H110000
    Public Const TE_ERROR_HCI_INVALID_COMMAND_PARAMETERS As Integer = &H120000
    Public Const TE_ERROR_HCI_REMOTE_USER_TERMINATED_CONNECTION As Integer = &H130000
    Public Const TE_ERROR_HCI_REMOTE_DEVICE_TERMINATED_CONNECTION_LOW_RESOURCES As Integer = &H140000
    Public Const TE_ERROR_HCI_REMOTE_DEVICE_TERMINATED_CONNECTION_POWER_OFF As Integer = &H150000
    Public Const TE_ERROR_HCI_CONNECTION_TERMINATED_BY_LOCAL_HOST As Integer = &H160000
    Public Const TE_ERROR_HCI_REPEATED_ATTEMPTS As Integer = &H170000
    Public Const TE_ERROR_HCI_PAIRING_NOT_ALLOWED As Integer = &H180000
    Public Const TE_ERROR_HCI_UNKNOWN_LMP_PDU As Integer = &H190000
    Public Const TE_ERROR_HCI_UNSUPPORTED_REMOTE_FEATURE As Integer = &H1A0000
    Public Const TE_ERROR_HCI_SCO_OFFSET_REJECTED As Integer = &H1B0000
    Public Const TE_ERROR_HCI_SCO_INTERVAL_REJECTED As Integer = &H1C0000
    Public Const TE_ERROR_HCI_SCO_AIR_MODE_REJECTED As Integer = &H1D0000
    Public Const TE_ERROR_HCI_INVALID_LMP_PARAMETERS As Integer = &H1E0000
    Public Const TE_ERROR_HCI_UNSPECIFIED_ERROR As Integer = &H1F0000
    Public Const TE_ERROR_HCI_UNSUPPORTED_LMP_PARAMETER_VALUE As Integer = &H200000
    Public Const TE_ERROR_HCI_ROLE_CHANGE_NOT_ALLOWED As Integer = &H210000
    Public Const TE_ERROR_HCI_LMP_RESPONSE_TIMEOUT As Integer = &H220000
    Public Const TE_ERROR_HCI_LMP_ERROR_TRANSACTION_COLLISION As Integer = &H230000
    Public Const TE_ERROR_HCI_LMP_PDU_NOT_ALLOWED As Integer = &H240000
    Public Const TE_ERROR_HCI_ENCRYPTION_MODE_NOT_ACCEPTABLE As Integer = &H250000
    Public Const TE_ERROR_HCI_LINK_KEY_CANNOT_BE_CHANGED As Integer = &H260000
    Public Const TE_ERROR_HCI_REQUESTED_QOS_NOT_SUPPORTED As Integer = &H270000
    Public Const TE_ERROR_HCI_INSTANT_PASSED As Integer = &H280000
    Public Const TE_ERROR_HCI_PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED As Integer = &H290000
    Public Const TE_ERROR_HCI_DIFFERENT_TRANSACTION_COLLISION As Integer = &H2A0000
    Public Const TE_ERROR_HCI_RESERVED_1 As Integer = &H2B0000
    Public Const TE_ERROR_HCI_QOS_UNACCEPTABLE_PARAMETER As Integer = &H2C0000
    Public Const TE_ERROR_HCI_QOS_REJECTED As Integer = &H2D0000
    Public Const TE_ERROR_HCI_CHANNEL_CLASSIFICATION_NOT_SUPPORTED As Integer = &H2E0000
    Public Const TE_ERROR_HCI_INSUFFICIENT_SECURITY As Integer = &H2F0000
    Public Const TE_ERROR_HCI_PARAMETER_OUT_OF_MANDATORY_RANGE As Integer = &H300000
    Public Const TE_ERROR_HCI_RESERVED_2 As Integer = &H310000
    Public Const TE_ERROR_HCI_ROLE_SWITCH_PENDING As Integer = &H320000
    Public Const TE_ERROR_HCI_RESERVED_3 As Integer = &H330000
    Public Const TE_ERROR_HCI_RESERVED_SLOT_VIOLATION As Integer = &H340000
    Public Const TE_ERROR_HCI_ROLE_SWITCH_FAILED As Integer = &H350000
    Public Const TE_ERROR_OUT_OF_MEMORY As Integer = &H1000001
    Public Const TE_ERROR_BAD_PARAM As Integer = &H1000002
    Public Const TE_ERROR_CONNECTION_SETUP As Integer = &H1000003
    Public Const TE_ERROR_FILE_OPEN As Integer = &H1000004
    Public Const TE_ERROR_INSUFFICIENT_SPACE As Integer = &H1000005
    Public Const TE_ERROR_INVALID_SEQUENCE As Integer = &H1000006
    Public Const TE_ERROR_MIBCMD_NO_SESSION As Integer = &H1000010
    Public Const TE_ERROR_MIBCMD_GET As Integer = &H1000011
    Public Const TE_ERROR_MIBCMD_SET As Integer = &H1000012
    Public Const TE_ERROR_CONFIG_READ As Integer = &H1000020
    Public Const TE_ERROR_CONFIG_WRITE As Integer = &H1000021
    Public Const TE_ERROR_CONFIG_ELEMENT_NOT_FOUND As Integer = &H1000022
    Public Const TE_ERROR_CONFIG_DATABASE As Integer = &H1000023
    Public Const TE_ERROR_CONFIG_GENERAL As Integer = &H1000024
    Public Const TE_CHIP_FAMILY_UNKNOWN As Integer = &H0
    Public Const TE_CHIP_FAMILY_BLUECORE As Integer = &H1
    Public Const TE_CHIP_FAMILY_MULTI As Integer = &H4
    Public Const TE_SUBSYSTEM_BT As Integer = 0
    Public Const TE_SUBSYSTEM_AUDIO As Integer = 1
    Public Const TE_SUBSYSTEM_APPS0 As Integer = 2
    Public Const TE_SUBSYSTEM_APPS1 As Integer = 3
    Public Const TE_TRANS_CRIT_NOLOCK As Integer = &H1
    Public Const TE_TRANS_CRIT_UNLOCKED As Integer = &H2
    Public Const TE_TRANS_CRIT_LOCKED As Integer = &H4
    Public Const TE_TRANS_CRIT_ALL As Integer = &H7
    Public Const TE_TRANS_CRIT_DEFAULT As Integer = &H3
    Public Const BCSP As Integer = &H1
    Public Const USB As Integer = &H2
    Public Const H4 As Integer = &H4
    Public Const H5 As Integer = &H8
    Public Const H4DS As Integer = &H10
    Public Const PTAP As Integer = &H40
    Public Const TRB As Integer = &H80
    Public Const USBDBG As Integer = &H100
    Public Const DEBUG_LPTSPI As Integer = 1
    Public Const DEBUG_USBSPI As Integer = 2
    Public Const DEBUG_USBTRB As Integer = 3
    Public Const DEBUG_USBDBG As Integer = 4
    Public Const SPI_LPT As Integer = DEBUG_LPTSPI
    Public Const SPI_USB As Integer = DEBUG_USBSPI
    Public Const TE_INVALID_HANDLE_VALUE As UInteger = 0UI
    Public Const TE_INVALID_HANDLE As Integer = -1
    Public Const TE_ERROR As Integer = 0
    Public Const TE_OK As Integer = 1
    Public Const TE_UNSUPPORTED_FUNCTION As Integer = 2
    Public Const SQIF_APP_VALIDATION_RUNNING As Byte = &H0
    Public Const SQIF_APP_VALIDATION_PASS As Byte = &H1
    Public Const SQIF_APP_VALIDATION_PASS_NO_APP As Byte = &H2
    Public Const TE_CLOSE_EX_RESET_RELOCK_NO_WAIT As UShort = 0US
    Public Const TE_CLOSE_EX_RESET_RELOCK_WAIT As UShort = 1US
    Public Const TE_CLOSE_EX_NO_RESET_NO_RELOCK As UShort = 2US

    <DllImport("TestEngine.dll", EntryPoint:="teGetVersion", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetVersion (ByVal versionStr As StringBuilder) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngine", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngine (ByVal transport As Integer, ByVal transportDevice As String, ByVal dataRate As UInteger, ByVal retryTimeOut As Integer, ByVal usbTimeOut As Integer) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngineUnlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngineUnlock (ByVal transport As Integer, ByVal transportDevice As String, ByVal retryTimeOut As Integer, ByVal usbTimeOut As Integer, ByVal unlockKey As String) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngineDebug", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngineDebug (ByVal port As Integer, ByVal multi As Integer, ByVal transport As Integer) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngineDebugUnlock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngineDebugUnlock (ByVal port As Integer, ByVal multi As Integer, ByVal transport As Integer, ByVal unlockKey As String) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngineDebugTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngineDebugTrans (ByVal trans As String, ByVal multi As Integer) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="openTestEngineDebugUnlockTrans", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function openTestEngineDebugUnlockTrans (ByVal trans As String, ByVal multi As Integer, ByVal unlockKey As String) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="closeTestEngine", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function closeTestEngine (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="closeTestEngineEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function closeTestEngineEx (ByVal handle As UInteger, ByVal options As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetLastError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetLastError (ByVal handle As UInteger) As UInteger
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetColdReset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetColdReset (ByVal handle As UInteger, ByVal usbTimeout As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetWarmReset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetWarmReset (ByVal handle As UInteger, ByVal usbTimeout As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPause", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPause (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestDeepSleep", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestDeepSleep (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmExtLb", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmExtLb (ByVal handle As UInteger, ByVal pcmMode As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmExtLbIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmExtLbIf (ByVal handle As UInteger, ByVal pcmMode As UShort, ByVal pcmIf As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmLb", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmLb (ByVal handle As UInteger, ByVal pcmMode As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmLbIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmLbIf (ByVal handle As UInteger, ByVal pcmMode As UShort, ByVal pcmIf As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmTimingIn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmTimingIn (ByVal handle As UInteger, ByVal pioOut As UShort, ByVal pcmIn As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmTimingInIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmTimingInIf (ByVal handle As UInteger, ByVal pioOut As UShort, ByVal pcmIn As UShort, ByVal pcmIf As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmTone", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmTone (ByVal handle As UInteger, ByVal freq As UShort, ByVal ampl As UShort, ByVal dc As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmToneIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmToneIf (ByVal handle As UInteger, ByVal freq As UShort, ByVal ampl As UShort, ByVal dc As UShort, ByVal pcmIf As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestPcmToneStereo", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestPcmToneStereo (ByVal handle As UInteger, ByVal freq As UShort, ByVal ampl As UShort, ByVal dc As UShort, ByVal channel As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCtsRtsLb", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCtsRtsLb (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRadioStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRadioStatus (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetRadioStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetRadioStatus (ByVal handle As UInteger, ByVal status() As UShort, ByVal timeout As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRadioStatusArray", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRadioStatusArray (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetRadioStatusArray", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetRadioStatusArray (ByVal handle As UInteger, ByVal status() As UShort, ByVal timeout As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdMemoryGet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdMemoryGet (ByVal handle As UInteger, ByVal baseAddr As UShort, ByVal dataLength As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdMemorySet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdMemorySet (ByVal handle As UInteger, ByVal baseAddr As UShort, ByVal dataLength As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetBuildId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetBuildId (ByVal handle As UInteger, ByRef buildId As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBuildName", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBuildName (ByVal handle As UInteger, ByVal name As StringBuilder, ByVal maxLen As UShort, ByRef length As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetChipVersion", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetChipVersion (ByVal handle As UInteger, ByRef chipVer As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetChipRevision", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetChipRevision (ByVal handle As UInteger, ByRef chipRev As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetChipAnaVer", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetChipAnaVer (ByVal handle As UInteger, ByRef major As Byte, ByRef minor As Byte, ByRef vari As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdRouteClock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdRouteClock (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdRssiAcl", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdRssiAcl (ByVal handle As UInteger, ByVal connectionHandle As UShort, ByRef rssi As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetPio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetPio (ByVal handle As UInteger, ByVal mask As UShort, ByVal port As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetPio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetPio (ByVal handle As UInteger, ByRef mask As UShort, ByRef port As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdMapPio32", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdMapPio32 (ByVal handle As UInteger, ByVal mask As UInteger, ByVal pios As UInteger, ByRef errLines As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetPio32", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetPio32 (ByVal handle As UInteger, ByVal mask As UInteger, ByVal direction As UInteger, ByVal value As UInteger, ByRef errLines As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetPio32", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetPio32 (ByVal handle As UInteger, ByRef direction As UInteger, ByRef value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetAdc", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetAdc (ByVal handle As UInteger, ByVal adc As UShort, ByRef result As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetAio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetAio (ByVal handle As UInteger, ByVal aio As UShort, ByRef result As UShort, ByRef numBits As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBC5MMGetBatteryVoltage", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBC5MMGetBatteryVoltage (ByVal handle As UInteger, ByRef voltage As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetFirmwareCheckMask", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetFirmwareCheckMask (ByVal handle As UInteger, ByRef mask As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetFirmwareCheck", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetFirmwareCheck (ByVal handle As UInteger, ByRef check As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetExternalClockPeriod", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetExternalClockPeriod (ByVal handle As UInteger, ByRef period As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdEnableDeviceConnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdEnableDeviceConnect (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdEnableDeviceUnderTestMode", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdEnableDeviceUnderTestMode (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdCheckSqifImageValidationStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdCheckSqifImageValidationStatus (ByVal handle As UInteger, ByRef status As UShort, ByVal timeout As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestStereoCodecLB", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestStereoCodecLB (ByVal handle As UInteger, ByVal sampleRate As UShort, ByVal reroute As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestTxstart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestTxstart (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort, ByVal modulation As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestTxdata1", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestTxdata1 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestTxdata2", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestTxdata2 (ByVal handle As UInteger, ByVal countryCode As UShort, ByVal power1 As UShort, ByVal power2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestTxdata3", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestTxdata3 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestTxdata4", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestTxdata4 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgTxPower", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgTxPower (ByVal handle As UInteger, ByVal power As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRxstart1", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRxstart1 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRxstart2", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRxstart2 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort, ByVal sampleSize As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetRssi", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetRssi (ByVal handle As UInteger, ByVal timeout As Integer, ByVal maxSize As UShort, ByVal rssiSamples() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestBer1", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestBer1 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort, ByVal sampleSize As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestBer2", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestBer2 (ByVal handle As UInteger, ByVal countryCode As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort, ByVal sampleSize As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestBerLoopback", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestBerLoopback (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort, ByVal sampleSize As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRxLoopback", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRxLoopback (ByVal handle As UInteger, ByVal frequency As UShort, ByVal intPA As UShort, ByVal extPA As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestLoopback", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestLoopback (ByVal handle As UInteger, ByVal frequency As UShort, ByVal power1 As UShort, ByVal power2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetBer", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetBer (ByVal handle As UInteger, ByVal timeout As Integer, ByVal berReport() As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRxdata1", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRxdata1 (ByVal handle As UInteger, ByVal frequency As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestRxdata2", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestRxdata2 (ByVal handle As UInteger, ByVal countryCode As UShort, ByVal hiSide As Byte, ByVal rxAttenuation As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetRxdata", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetRxdata (ByVal handle As UInteger, ByVal timeout As Integer, ByVal rxData() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgFreq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgFreq (ByVal handle As UInteger, ByVal txRxInterval As UShort, ByVal loopback As UShort, ByVal report As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgFreqMs", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgFreqMs (ByVal handle As UInteger, ByVal txRxInterval As UShort, ByVal loopback As UShort, ByVal report As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgPkt", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgPkt (ByVal handle As UInteger, ByVal aType As UShort, ByVal size As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgBitError", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgBitError (ByVal handle As UInteger, ByVal sampleSize As UInteger, ByVal reset As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgTxPaAtten", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgTxPaAtten (ByVal handle As UInteger, ByVal atten As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgXtalFtrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgXtalFtrim (ByVal handle As UInteger, ByVal fTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCalcXtalOffset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCalcXtalOffset (ByVal nominalFreqMhz As Double, ByVal actualFreqMhz As Double, ByRef offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgUapLap", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgUapLap (ByVal handle As UInteger, ByVal uap As UShort, ByVal lap As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgIqTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgIqTrim (ByVal handle As UInteger, ByVal trim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgTxIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgTxIf (ByVal handle As UInteger, ByVal offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgTxTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgTxTrim (ByVal handle As UInteger, ByVal amAddr As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgLoLvl", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgLoLvl (ByVal handle As UInteger, ByVal loLvl As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestCfgHoppingSeq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestCfgHoppingSeq (ByVal handle As UInteger, ByVal channels() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestSettle", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestSettle (ByVal handle As UInteger, ByVal start As UShort, ByVal aEnd As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetSettle", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetSettle (ByVal handle As UInteger, ByVal results() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="get_freq_offset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function get_freq_offset (ByVal handle As UInteger, ByRef offset As Double, ByVal sampleSize As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetEeprom", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetEeprom (ByVal handle As UInteger, ByVal log2bytes As UShort, ByVal addrMask As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadBdAddr", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadBdAddr (ByVal handle As UInteger, ByRef lap As UInteger, ByRef uap As Byte, ByRef nap As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psRead (ByVal handle As UInteger, ByVal psKey As UShort, ByVal store As UShort, ByVal arrayLen As UShort, ByVal data() As UShort, ByRef keyLen As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psClear", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psClear (ByVal handle As UInteger, ByVal psKey As UShort, ByVal store As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psClearAll", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psClearAll (ByVal handle As UInteger, ByVal store As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psFactorySet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psFactorySet (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psFactoryRestoreAll", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psFactoryRestoreAll (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psFactoryRestore", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psFactoryRestore (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psSize", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psSize (ByVal handle As UInteger, ByVal psKey As UShort, ByVal store As UShort, ByRef size As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWrite (ByVal handle As UInteger, ByVal psKey As UShort, ByVal store As UShort, ByVal length As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteVerify", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteVerify (ByVal handle As UInteger, ByVal psKey As UShort, ByVal store As UShort, ByVal length As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteBdAddr", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteBdAddr (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As UInteger, ByVal nap As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadModuleId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadModuleId (ByVal handle As UInteger, ByRef moduleId As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadXtalFtrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadXtalFtrim (ByVal handle As UInteger, ByRef fTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteXtalFtrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteXtalFtrim (ByVal handle As UInteger, ByVal fTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadXtalOffset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadXtalOffset (ByVal handle As UInteger, ByRef offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteXtalOffset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteXtalOffset (ByVal handle As UInteger, ByVal offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteModuleSecurityCode", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteModuleSecurityCode (ByVal handle As UInteger, ByVal code() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteModuleId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteModuleId (ByVal handle As UInteger, ByVal moduleId As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteBaudrate", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteBaudrate (ByVal handle As UInteger, ByVal value As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteRadiotestFirstTrimTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteRadiotestFirstTrimTime (ByVal handle As UInteger, ByVal time As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadRadiotestFirstTrimTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadRadiotestFirstTrimTime (ByVal handle As UInteger, ByRef time As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteRadiotestLoLvlTrimEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteRadiotestLoLvlTrimEnable (ByVal handle As UInteger, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadRadiotestLoLvlTrimEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadRadiotestLoLvlTrimEnable (ByVal handle As UInteger, ByRef state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteRadiotestSubsequentTrimTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteRadiotestSubsequentTrimTime (ByVal handle As UInteger, ByVal time As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadRadiotestSubsequentTrimTime", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadRadiotestSubsequentTrimTime (ByVal handle As UInteger, ByRef time As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteHostInterface", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteHostInterface (ByVal handle As UInteger, ByVal transport As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadHostInterface", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadHostInterface (ByVal handle As UInteger, ByRef transport As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteUsbAttributes", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteUsbAttributes (ByVal handle As UInteger, ByVal bmAttributes As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteDPlusPullup", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteDPlusPullup (ByVal handle As UInteger, ByVal pioPin As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteUsbMaxPower", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteUsbMaxPower (ByVal handle As UInteger, ByVal maxPower As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWritePioProtectMask", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWritePioProtectMask (ByVal handle As UInteger, ByVal mask As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadPioProtectMask", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadPioProtectMask (ByVal handle As UInteger, ByRef mask As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteTxOffsetHalfMhz", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteTxOffsetHalfMhz (ByVal handle As UInteger, ByVal offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadTxOffsetHalfMhz", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadTxOffsetHalfMhz (ByVal handle As UInteger, ByRef offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteUsrValue", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteUsrValue (ByVal handle As UInteger, ByVal userNo As UShort, ByVal length As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadUsrValue", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadUsrValue (ByVal handle As UInteger, ByVal userNo As UShort, ByVal maxLen As UShort, ByRef length As UShort, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWritePowerTable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWritePowerTable (ByVal handle As UInteger, ByVal numEntries As UShort, ByVal intPA() As Byte, ByVal extPA() As Byte, ByVal power() As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadPowerTable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadPowerTable (ByVal handle As UInteger, ByVal maxSize As Integer, ByRef numEntries As Integer, ByVal intPA() As Byte, ByVal extPA() As Byte, ByVal power() As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psWriteVmDisable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psWriteVmDisable (ByVal handle As UInteger, ByVal vmDisable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psReadVmDisable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psReadVmDisable (ByVal handle As UInteger, ByRef vmDisable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="psMergeFromFile", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function psMergeFromFile (ByVal handle As UInteger, ByVal filePath As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSlave", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSlave (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSetAfhHostChannelClass", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSetAfhHostChannelClass (ByVal handle As UInteger, ByVal cClass() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadAfhChannelMap", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadAfhChannelMap (ByVal handle As UInteger, ByVal aclHandle As UShort, ByRef mode As Byte, ByVal cMap() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSetEventFilterAutoacceptConnection", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSetEventFilterAutoacceptConnection (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWriteInquiryScanActivity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWriteInquiryScanActivity (ByVal handle As UInteger, ByVal interval As UShort, ByVal window As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWritePageScanActivity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWritePageScanActivity (ByVal handle As UInteger, ByVal interval As UShort, ByVal window As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWriteScanEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWriteScanEnable (ByVal handle As UInteger, ByVal scanEnable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciInquiry", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciInquiry (ByVal handle As UInteger, ByVal inquiryLength As Byte, ByVal numResponses As Byte, ByVal lap As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetInquiryResults", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetInquiryResults (ByVal handle As UInteger, ByVal lap() As UInteger, ByVal uap() As Byte, ByVal nap() As UShort, ByVal clockOffset() As UShort, ByVal maxLen As UInteger, ByRef dataLen As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciInquiryCancel", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciInquiryCancel (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciCreateConnection", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciCreateConnection (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByVal pktType As UShort, ByRef connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciCreateConnectionNoInquiry", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciCreateConnectionNoInquiry (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByVal pktType As UShort, ByVal pageScanRepMode As Byte, ByVal pageScanMode As Byte, ByVal clockOffset As UShort, ByVal allowRoleSwitch As Byte, ByRef connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciCreateScoConnection", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciCreateScoConnection (ByVal handle As UInteger, ByVal aclConnectionHandle As UShort, ByVal pktType As UShort, ByRef scoConnectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSetupScoConnection", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSetupScoConnection (ByVal handle As UInteger, ByVal aclConnectionHandle As UShort, ByVal txBandwidth As UInteger, ByVal rxBandwidth As UInteger, ByVal maxLatency As UShort, ByVal voiceSetting As UShort, ByVal retransEffort As Byte, ByVal pktType As UShort, ByRef scoConnectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadVoiceSetting", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadVoiceSetting (ByVal handle As UInteger, ByRef voiceSetting As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWriteVoiceSetting", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWriteVoiceSetting (ByVal handle As UInteger, ByVal voiceSetting As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWriteLinkPolicySettings", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWriteLinkPolicySettings (ByVal handle As UInteger, ByVal connectionHandle As UShort, ByVal linkPolicySettings As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSendAclFile", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSendAclFile (ByVal handle As UInteger, ByVal connHandle As UShort, ByVal fileName As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSendAclData", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSendAclData (ByVal handle As UInteger, ByVal connHandle As UShort, ByVal data() As Byte, ByVal length As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetAclData", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetAclData (ByVal handle As UInteger, ByVal data() As Byte, ByRef numBytes As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetAclBytesRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetAclBytesRead (ByVal handle As UInteger, ByRef numBytes As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetAclFileName", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetAclFileName (ByVal handle As UInteger, ByVal fileName As StringBuilder, ByRef length As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetAclState", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetAclState (ByVal handle As UInteger, ByRef state As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciResetAclState", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciResetAclState (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReset (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetAnaXtalFtrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetAnaXtalFtrim (ByVal handle As UInteger, ByRef fTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetAnaXtalFtrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetAnaXtalFtrim (ByVal handle As UInteger, ByVal fTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSniffMode", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSniffMode (ByVal handle As UInteger, ByVal connectionHandle As UShort, ByVal sniffMaxInterval As UShort, ByVal sniffMinInterval As UShort, ByVal sniffAttempt As UShort, ByVal sniffTimeout As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciExitSniff", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciExitSniff (ByVal handle As UInteger, ByVal connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciDisconnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciDisconnect (ByVal handle As UInteger, ByVal connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetConnectionHandle", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetConnectionHandle (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByRef connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciConnectionStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciConnectionStatus (ByVal handle As UInteger, ByVal connectionHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciEnableDeviceUnderTestMode", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciEnableDeviceUnderTestMode (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciGetLinkQuality", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciGetLinkQuality (ByVal handle As UInteger, ByVal connectionHandle As UShort, ByRef quality As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadBdAddr", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadBdAddr (ByVal handle As UInteger, ByVal bdAddr As StringBuilder) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadLocalVersionInformation", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadLocalVersionInformation (ByVal handle As UInteger, ByVal versionInfo() As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadRemoteVersionInformation", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadRemoteVersionInformation (ByVal handle As UInteger, ByVal connectionHandle As UShort, ByVal versionInfo() As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciReadRemoteNameRequest", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciReadRemoteNameRequest (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByVal pageScanRepMode As Byte, ByVal pageScanOffset As Byte, ByVal clockOffset As UShort, ByVal remoteName As StringBuilder) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmRegisterReq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmRegisterReq (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmSlave", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmSlave (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmEnableDeviceUnderTestMode", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmEnableDeviceUnderTestMode (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmWritePageScanActivity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmWritePageScanActivity (ByVal handle As UInteger, ByVal interval As UShort, ByVal window As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmWriteInquiryScanActivity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmWriteInquiryScanActivity (ByVal handle As UInteger, ByVal interval As UShort, ByVal window As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmWriteScanEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmWriteScanEnable (ByVal handle As UInteger, ByVal scanEnable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="dmSetEventFilterAutoacceptConnection", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function dmSetEventFilterAutoacceptConnection (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBc3PsuTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBc3PsuTrim (ByVal handle As UInteger, ByVal data As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdChargerPsuTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdChargerPsuTrim (ByVal handle As UInteger, ByVal trim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBc3BuckReg", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBc3BuckReg (ByVal handle As UInteger, ByVal data As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdPsuSmpsEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdPsuSmpsEnable (ByVal handle As UInteger, ByVal reg As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBc3MicEn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBc3MicEn (ByVal handle As UInteger, ByVal data As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdPsuHvLinearEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdPsuHvLinearEnable (ByVal handle As UInteger, ByVal reg As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBc3Led0", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBc3Led0 (ByVal handle As UInteger, ByVal data As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdLedEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdLedEnable (ByVal handle As UInteger, ByVal led As UShort, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdLed0Enable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdLed0Enable (ByVal handle As UInteger, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBc3Led1", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBc3Led1 (ByVal handle As UInteger, ByVal data As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdLed1Enable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdLed1Enable (ByVal handle As UInteger, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdChargerStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdChargerStatus (ByVal handle As UInteger, ByRef state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdChargerDisable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdChargerDisable (ByVal handle As UInteger, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdChargerSuppressLed0", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdChargerSuppressLed0 (ByVal handle As UInteger, ByVal state As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciCreateConnectionNoWait", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciCreateConnectionNoWait (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByVal pktType As UShort, ByVal pageScanRepMode As Byte, ByVal pageScanMode As Byte, ByVal clockOffset As UShort, ByVal allowRoleSwitch As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWriteAuthenticationEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWriteAuthenticationEnable (ByVal handle As UInteger, ByVal enable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciLinkKeyRequestNegativeReply", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciLinkKeyRequestNegativeReply (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWaitForConnectionComplete", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWaitForConnectionComplete (ByVal handle As UInteger, ByRef connHandle As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWaitForLinkKeyRequest", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWaitForLinkKeyRequest (ByVal handle As UInteger, ByRef lap As UInteger, ByRef uap As Byte, ByRef nap As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWaitForPinCodeRequest", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWaitForPinCodeRequest (ByVal handle As UInteger, ByRef lap As UInteger, ByRef uap As Byte, ByRef nap As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciWaitForEncryptionChange", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciWaitForEncryptionChange (ByVal handle As UInteger, ByRef enable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciPinCodeRequestReply", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciPinCodeRequestReply (ByVal handle As UInteger, ByVal lap As UInteger, ByVal uap As Byte, ByVal nap As UShort, ByVal pinCodeLength As Byte, ByVal pinCode() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciSetConnectionEncryption", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciSetConnectionEncryption (ByVal handle As UInteger, ByVal connHandle As UShort, ByVal enable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciLeReadLocalSupportedFeatures", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciLeReadLocalSupportedFeatures (ByVal handle As UInteger, ByRef leFeatures As ULong) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciLeTestEnd", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciLeTestEnd (ByVal handle As UInteger, ByRef numPackets As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciLeEnhancedReceiverTest", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciLeEnhancedReceiverTest (ByVal handle As UInteger, ByVal channel As Byte, ByVal phy As Byte, ByVal modIndex As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hciLeEnhancedTransmitterTest", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hciLeEnhancedTransmitterTest (ByVal handle As UInteger, ByVal channel As Byte, ByVal dataLength As Byte, ByVal payloadType As Byte, ByVal phy As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="vmWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function vmWrite (ByVal handle As UInteger, ByVal data() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="vmRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function vmRead (ByVal handle As UInteger, ByVal data() As UShort, ByVal timeout As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetSingleChan", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetSingleChan (ByVal handle As UInteger, ByVal channel As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetHoppingOn", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetHoppingOn (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmSwitchPower", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmSwitchPower (ByVal handle As UInteger, ByVal powerOn As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmSetFreq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmSetFreq (ByVal handle As UInteger, ByVal freqKHz As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmGetRssi", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmGetRssi (ByVal handle As UInteger, ByRef rssi As SByte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmGetSnr", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmGetSnr (ByVal handle As UInteger, ByRef snr As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmGetIfOffset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmGetIfOffset (ByVal handle As UInteger, ByRef offset As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmGetStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmGetStatus (ByVal handle As UInteger, ByRef status As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmSetupAudio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmSetupAudio (ByVal handle As UInteger, ByVal route As Byte, ByVal gain As Byte, ByVal channel As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmVerifyRDSPi", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmVerifyRDSPi (ByVal handle As UInteger, ByVal pi As UShort, ByVal timeoutMs As UShort, ByRef matched As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmTxSwitchPower", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmTxSwitchPower (ByVal handle As UInteger, ByVal powerOn As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmTxSetFreq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmTxSetFreq (ByVal handle As UInteger, ByVal freqKHz As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmTxSetPowerLevel", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmTxSetPowerLevel (ByVal handle As UInteger, ByVal powerLevel As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdFmTxSetupAudio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdFmTxSetupAudio (ByVal handle As UInteger, ByVal route As Byte, ByVal audioGain As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdDisconnectAudio", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdDisconnectAudio (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdAudioGetSource", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdAudioGetSource (ByVal handle As UInteger, ByVal device As UShort, ByVal iface As UShort, ByVal channel As UShort, ByRef sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdAudioGetSink", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdAudioGetSink (ByVal handle As UInteger, ByVal device As UShort, ByVal iface As UShort, ByVal channel As UShort, ByRef sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdAudioConfigure", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdAudioConfigure (ByVal handle As UInteger, ByVal sid As UShort, ByVal key As UShort, ByVal value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdDirectChargerPsuTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdDirectChargerPsuTrim (ByVal handle As UInteger, ByVal trim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teSupportsHq", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teSupportsHq (ByVal handle As UInteger, ByRef hqSupported As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetAuxDac", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetAuxDac (ByVal handle As UInteger, ByVal enable As Byte, ByVal level As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetMicBiasIf", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetMicBiasIf (ByVal handle As UInteger, ByVal instance As Byte, ByVal enable As Byte, ByVal voltage As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetMicBias", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetMicBias (ByVal handle As UInteger, ByVal enable As Byte, ByVal voltage As Byte, ByVal current As Byte, ByVal enableLowPowerMode As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetAvailableDebugPorts", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetAvailableDebugPorts (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetAvailableDebugPortsEx", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetAvailableDebugPortsEx (ByVal criteria As UInteger, ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdProvokeFault", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdProvokeFault (ByVal handle As UInteger, ByVal faultCode As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetFaultReports", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetFaultReports (ByVal handle As UInteger, ByVal maxReports As UShort, ByVal codes() As UShort, ByVal timestamps() As UInteger, ByVal repeats() As UShort, ByRef numReports As UShort, ByVal timeout As Integer) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetFaultDesc", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetFaultDesc (ByVal handle As UInteger, ByVal faultCode As UShort, ByVal desc As StringBuilder) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetMapScoPcm", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetMapScoPcm (ByVal handle As UInteger, ByVal enable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetVrefConstant", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetVrefConstant (ByVal handle As UInteger, ByRef vref As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetVrefAdc", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetVrefAdc (ByVal handle As UInteger, ByRef result As UShort, ByRef numBits As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdBC5FMGetI2CState", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdBC5FMGetI2CState (ByVal handle As UInteger, ByRef sda As Byte, ByRef scl As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="refEpGetRssiDbm", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function refEpGetRssiDbm (ByVal handle As UInteger, ByVal freqMHz As UShort, ByVal rssiChip As Double, ByRef rssiDbm As Double) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="refEpGetPaLevel", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function refEpGetPaLevel (ByVal handle As UInteger, ByVal freqMHz As UShort, ByVal targetPowerDbm As Double, ByRef intPa As UShort, ByRef powerDbm As Double) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="refEpWriteCalDataFile", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function refEpWriteCalDataFile (ByVal handle As UInteger, ByVal filePath As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="refEpLoadCalDataFile", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function refEpLoadCalDataFile (ByVal handle As UInteger, ByVal filePath As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetVmStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetVmStatus (ByVal handle As UInteger, ByRef status As UShort, ByRef exitCode As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdI2CTransfer", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdI2CTransfer (ByVal handle As UInteger, ByVal slaveAddr As UShort, ByVal txOctets As UShort, ByVal rxOctets As UShort, ByVal restart As Byte, ByVal data() As Byte, ByRef octets As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="radiotestBle", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function radiotestBle (ByVal handle As UInteger, ByVal command As UShort, ByVal channel As Byte, ByVal txLength As Byte, ByVal txPayload As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="hqGetBleRxPktCount", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function hqGetBleRxPktCount (ByVal handle As UInteger, ByVal timeout As Integer, ByRef pktCount As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetChargerTrims", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetChargerTrims (ByVal handle As UInteger, ByRef chgRefTrim As UShort, ByRef hVrefTrim As UShort, ByRef rTrim As UShort, ByRef iTrim As UShort, ByRef iExtTrim As UShort, ByRef iTermTrim As UShort, ByRef vFastTrim As UShort, ByRef hystTrim As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdCapacitiveSensorRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdCapacitiveSensorRead (ByVal handle As UInteger, ByVal mask As UShort, ByVal values() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSetSpiLockCustomerKey", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSetSpiLockCustomerKey (ByVal handle As UInteger, ByVal custKey() As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdGetSpiLockStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdGetSpiLockStatus (ByVal handle As UInteger, ByRef status As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="bccmdSpiLockInitiateLock", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function bccmdSpiLockInitiateLock (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetChipDisplayName", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetChipDisplayName (ByVal handle As UInteger, ByVal maxLen As UInteger, ByVal name As StringBuilder) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetChipFamily", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetChipFamily (ByVal handle As UInteger, ByRef family As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetChipId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetChipId (ByVal handle As UInteger, ByRef chipId As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetPtapHifs", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetPtapHifs (ByRef length As UShort, ByVal hifIds As StringBuilder, ByVal types As StringBuilder, ByVal names As StringBuilder, ByRef count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teMcSetXtalFreqTrim", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teMcSetXtalFreqTrim (ByVal handle As UInteger, ByVal trimVal As UShort, ByRef mibVal As Short) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teMcSetXtalLoadCapacitance", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teMcSetXtalLoadCapacitance (ByVal handle As UInteger, ByVal value As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teGetBuildId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teGetBuildId (ByVal handle As UInteger, ByVal subsystem As Byte, ByRef buildId As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePioMap", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePioMap (ByVal handle As UInteger, ByVal bank As UShort, ByVal mask As UInteger, ByVal pios As UInteger, ByRef errLines As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePioSet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePioSet (ByVal handle As UInteger, ByVal bank As UShort, ByVal mask As UInteger, ByVal direction As UInteger, ByVal value As UInteger, ByRef errLines As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePioGet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePioGet (ByVal handle As UInteger, ByVal bank As UShort, ByRef direction As UInteger, ByRef value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioGetSource", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioGetSource (ByVal handle As UInteger, ByVal device As UShort, ByVal iface As UShort, ByVal channel As UShort, ByRef sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioCloseSource", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioCloseSource (ByVal handle As UInteger, ByVal sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioGetSink", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioGetSink (ByVal handle As UInteger, ByVal device As UShort, ByVal iface As UShort, ByVal channel As UShort, ByRef sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioCloseSink", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioCloseSink (ByVal handle As UInteger, ByVal sid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioConnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioConnect (ByVal handle As UInteger, ByVal sourceId As UShort, ByVal sinkId As UShort, ByRef tid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioDisconnect", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioDisconnect (ByVal handle As UInteger, ByVal tid As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioConfigure", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioConfigure (ByVal handle As UInteger, ByVal sid As UShort, ByVal key As UShort, ByVal value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioCreateOperator", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioCreateOperator (ByVal handle As UInteger, ByVal capabilityId As UShort, ByRef operatorId As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioDestroyOperators", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioDestroyOperators (ByVal handle As UInteger, ByVal operators() As UShort, ByVal count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioOperatorMessage", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioOperatorMessage (ByVal handle As UInteger, ByVal operatorId As UShort, ByVal message() As UShort, ByVal messageLength As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioResetOperators", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioResetOperators (ByVal handle As UInteger, ByVal operators() As UShort, ByVal count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioStartOperators", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioStartOperators (ByVal handle As UInteger, ByVal operators() As UShort, ByVal count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioStopOperators", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioStopOperators (ByVal handle As UInteger, ByVal operators() As UShort, ByVal count As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioSetAncIirFilter", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioSetAncIirFilter (ByVal handle As UInteger, ByVal ancInstance As UShort, ByVal pathId As UShort, ByVal coefficients() As UShort, ByVal numCoeffs As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioSetAncLpfFilter", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioSetAncLpfFilter (ByVal handle As UInteger, ByVal ancInstance As UShort, ByVal pathId As UShort, ByVal shift1 As UShort, ByVal shift2 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioStreamAncEnable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioStreamAncEnable (ByVal handle As UInteger, ByVal anc0 As UShort, ByVal anc1 As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAudioMicBiasConfigure", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAudioMicBiasConfigure (ByVal handle As UInteger, ByVal id As UShort, ByVal key As UShort, ByVal value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teCapacitiveSensorRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teCapacitiveSensorRead (ByVal handle As UInteger, ByVal pad As UShort, ByRef value As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teCheckLicense", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teCheckLicense (ByVal handle As UInteger, ByVal featureId As Byte, ByRef result As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teCheckLicenses", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teCheckLicenses (ByVal handle As UInteger, ByVal numFeatureIds As UShort, ByVal featureIds() As UShort, ByVal results() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAppDisable", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAppDisable (ByVal handle As UInteger, ByVal reserved As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAppWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAppWrite (ByVal handle As UInteger, ByVal channel As Byte, ByVal data() As UShort, ByVal length As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAppRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAppRead (ByVal handle As UInteger, ByRef channel As Byte, ByVal data() As UShort, ByVal dataLength As UShort, ByRef readLength As UShort, ByVal timeoutMs As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teAdcGet", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teAdcGet (ByVal handle As UInteger, ByVal adc As UShort, ByVal delay As UShort, ByVal extraFlag As UShort, ByRef result As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teChargerSetConfig", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teChargerSetConfig (ByVal handle As UInteger, ByVal config() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teChargerGetStatus", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teChargerGetStatus (ByVal handle As UInteger, ByRef status As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teNfcConfigure", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teNfcConfigure (ByVal handle As UInteger, ByVal enable As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheInit", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheInit (ByVal handle As UInteger, ByVal configDb As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheRead (ByVal handle As UInteger, ByVal file As String, ByVal reserved As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheMerge", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheMerge (ByVal handle As UInteger, ByVal file As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheReadItem", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheReadItem (ByVal handle As UInteger, ByVal key As String, ByVal value As StringBuilder, ByRef maxLen As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheWriteItem", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheWriteItem (ByVal handle As UInteger, ByVal key As String, ByVal value As String) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teConfigCacheWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teConfigCacheWrite (ByVal handle As UInteger, ByVal file As String, ByVal reserved As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teChipReset", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teChipReset (ByVal handle As UInteger, ByVal mode As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teEnableSecurity", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teEnableSecurity (ByVal handle As UInteger, ByVal options As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teI2cTransfer", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teI2cTransfer (ByVal handle As UInteger, ByVal pioScl As UShort, ByVal pioSda As UShort, ByVal devAddr As UShort, ByVal clockKhz As UShort, ByVal txOctets As UShort, ByVal rxOctets As UShort, ByVal data() As Byte, ByRef rxdOctets As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teNvmTagRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teNvmTagRead (ByVal handle As UInteger, ByVal tagId As UShort, ByVal valueLen As Byte, ByVal value() As Byte, ByRef readLen As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teNvmTagWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teNvmTagWrite (ByVal handle As UInteger, ByVal tagId As UShort, ByVal valueLen As Byte, ByVal value() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePsGetNextKeyId", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePsGetNextKeyId (ByVal handle As UInteger, ByVal keyType As Byte, ByVal resetSearch As Byte, ByRef keyId As UInteger, ByRef endOfStore As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePsRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePsRead (ByVal handle As UInteger, ByVal keyId As UInteger, ByVal valueLen As UShort, ByVal value() As UShort, ByRef readLen As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePsWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePsWrite (ByVal handle As UInteger, ByVal keyId As UInteger, ByVal valueLen As UShort, ByVal value() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePsAudioRead", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePsAudioRead (ByVal handle As UInteger, ByVal keyId As UInteger, ByVal valueLen As UShort, ByVal value() As UShort, ByRef readLen As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="tePsAudioWrite", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function tePsAudioWrite (ByVal handle As UInteger, ByVal keyId As UInteger, ByVal valueLen As UShort, ByVal value() As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadGetMaxPayloadLen", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadGetMaxPayloadLen (ByVal pktType As Byte, ByRef maxLen As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadQhsStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadQhsStart (ByVal handle As UInteger, ByVal testMode As Byte, ByVal channel As Byte, ByVal payloadLen As UShort, ByVal payload As Byte, ByVal phyRate As Byte, ByVal txPower As Byte, ByVal maxPackets As UShort, ByVal cteLen As Byte, ByVal cteType As Byte, ByVal slotDuration As Byte, ByVal numAntennae As Byte, ByVal antennaIds() As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxContStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxContStart (ByVal handle As UInteger, ByVal techType As Byte, ByVal channel As Byte, ByVal swGain As Byte, ByVal lePhy As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxGetRssi", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxGetRssi (ByVal handle As UInteger, ByVal techType As Byte, ByVal channel As Byte, ByVal numSamples As Byte, ByRef rssi As SByte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxGetStats", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxGetStats (ByVal handle As UInteger, ByRef pktLen As UShort, ByVal pktsRxd() As UInteger, ByVal acErrs() As UInteger, ByVal hecErrs() As UInteger, ByVal crcErrs() As UInteger, ByVal totalBitErrs() As UInteger, ByVal rssi() As Short, ByRef reserved As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxPktCfg", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxPktCfg (ByVal handle As UInteger, ByVal numPkts As UShort) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxPktStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxPktStart (ByVal handle As UInteger, ByVal channels() As Byte, ByVal payload As Byte, ByVal pktType As Byte, ByVal bdAddr As String, ByVal hopMode As Byte, ByVal pktLen As UShort, ByVal ltAddr As Byte, ByVal reserved As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadStop", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadStop (ByVal handle As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadTxContStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadTxContStart (ByVal handle As UInteger, ByVal channel As Byte, ByVal power As Byte, ByVal transmitType As Byte, ByVal patternLen As Byte, ByVal bitPattern As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadTxCwStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadTxCwStart (ByVal handle As UInteger, ByVal channel As Byte, ByVal power As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadTxPktStart", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadTxPktStart (ByVal handle As UInteger, ByVal channels() As Byte, ByVal payload As Byte, ByVal pktType As Byte, ByVal power As Byte, ByVal bdAddr As String, ByVal hopMode As Byte, ByVal pktLen As UShort, ByVal ltAddr As Byte, ByVal reserved As UInteger) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadLeTxBurst", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadLeTxBurst (ByVal handle As UInteger, ByVal hopMode As Byte, ByVal payloadLen As UShort, ByVal payloadType As Byte, ByVal pktType As Byte, ByVal power As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadTxEnhanced", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadTxEnhanced (ByVal handle As UInteger, ByVal channel As Byte, ByVal pktType As Byte, ByVal payloadLen As UShort, ByVal payloadType As Byte, ByVal payloadPattern As UInteger, ByVal transmitType As Byte, ByVal ltAddr As Byte, ByVal hopping As Byte, ByVal bdAddr As String, ByVal maxPkts As UInteger, ByVal offSlots As Byte, ByVal power As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxEnhanced", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxEnhanced (ByVal handle As UInteger, ByVal channel As Byte, ByVal pktType As Byte, ByVal payloadLen As UShort, ByVal payloadType As Byte, ByVal payloadPattern As UInteger, ByVal receiveType As Byte, ByVal ltAddr As Byte, ByVal hopping As Byte, ByVal bdAddr As String, ByVal maxPkts As UInteger, ByVal offSlots As Byte, ByVal rxSwGain As Byte) As Integer
    End Function
    <DllImport("TestEngine.dll", EntryPoint:="teRadRxGetStatsEnhanced", _
    CharSet:=CharSet.Ansi, CallingConvention:=CallingConvention.StdCall)> _
    Function teRadRxGetStatsEnhanced (ByVal handle As UInteger, ByRef pktsRxd As UInteger, ByRef acErrs As UInteger, ByRef hecErrs As UInteger, ByRef crcErrs As UInteger, ByRef totalBitErrs As UInteger, ByRef rssi As Short, ByRef reserved As UInteger) As Integer
    End Function

' DEPRECATED FUNCTIONS
Declare Function bccmdPsuBuckReg Lib "TestEngine.dll" Alias "bccmdPsuSmpsEnable" (ByVal handle As UInteger, ByVal reg As UShort) As Integer
Declare Function bccmdPsuMicEn Lib "TestEngine.dll" Alias "bccmdPsuHvLinearEnable" (ByVal handle As UInteger, ByVal reg As UShort) As Integer
Declare Function bccmdLed0 Lib "TestEngine.dll" Alias "bccmdLed0Enable" (ByVal handle As UInteger, ByVal state As UShort) As Integer
Declare Function bccmdLed1 Lib "TestEngine.dll" Alias "bccmdLed1Enable" (ByVal handle As UInteger, ByVal state As UShort) As Integer
Declare Function bccmdChargerSupressLed0 Lib "TestEngine.dll" Alias "bccmdChargerSuppressLed0" (ByVal handle As UInteger, ByVal state As UShort) As Integer
Declare Function openTestEngineSpi Lib "TestEngine.dll" Alias "openTestEngineDebug" (ByVal port As Integer, ByVal multi As Integer, ByVal transport As Integer) As UInteger
Declare Function openTestEngineSpiTrans Lib "TestEngine.dll" Alias "openTestEngineDebugTrans" (ByVal trans As String, ByVal multi As Integer) As UInteger
Declare Function openTestEngineSpiUnlock Lib "TestEngine.dll" Alias "openTestEngineDebugUnlock" (ByVal port As Integer, ByVal multi As Integer, ByVal transport As Integer, ByVal unlockKey As String) As UInteger
Declare Function openTestEngineSpiUnlockTrans Lib "TestEngine.dll" Alias "openTestEngineDebugUnlockTrans" (ByVal trans As String, ByVal multi As Integer, ByVal unlockKey As String) As UInteger
Declare Function teGetAvailableSpiPorts Lib "TestEngine.dll" Alias "teGetAvailableDebugPorts" (ByRef maxLen As UShort, ByVal ports As StringBuilder, ByVal trans As StringBuilder, ByRef count As UShort) As Integer
End Module


