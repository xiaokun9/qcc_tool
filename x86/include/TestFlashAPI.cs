// TestFlashAPI.cs : Declares the DLL functions for C#.
// Copyright (c) 2022 Qualcomm Technologies International, Ltd.
// All Rights Reserved.
// Qualcomm Technologies International, Ltd. Confidential and Proprietary.

// Auto-generated CS wrapper for TestFlash DLL.
// Created on 2022-11-18 15:14 from TestFlash.h file

using System;
using System.Runtime.InteropServices;
using System.Text;

namespace TestFlashAPI
{
    public class TestFlash
    {
        const CharSet charset = CharSet.Ansi;
        const CallingConvention calling_convention = CallingConvention.StdCall;

        [DllImport("TestFlash.dll", EntryPoint="flOpen",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flOpen(int port, int xtal, int delays, int transport);

        [DllImport("TestFlash.dll", EntryPoint="flOpenUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flOpenUnlock(int port, int xtal, int delays, int transport, String unlockKey);

        [DllImport("TestFlash.dll", EntryPoint="flmOpen",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpen(uint deviceMask, int xtal, int transport);

        [DllImport("TestFlash.dll", EntryPoint="flmOpenUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpenUnlock(uint deviceMask, int xtal, int transport, String unlockKey);

        [DllImport("TestFlash.dll", EntryPoint="flOpenTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flOpenTrans(String trans, int xtal, int delays);

        [DllImport("TestFlash.dll", EntryPoint="flOpenUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flOpenUnlockTrans(String trans, int xtal, int delays, String unlockKey);

        [DllImport("TestFlash.dll", EntryPoint="flmOpenTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpenTrans(uint deviceMask, String trans, int xtal);

        [DllImport("TestFlash.dll", EntryPoint="flmOpenUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpenUnlockTrans(uint deviceMask, String trans, int xtal, String unlockKey);

        [DllImport("TestFlash.dll", EntryPoint="flReadProgramFiles",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flReadProgramFiles(String fileName);

        [DllImport("TestFlash.dll", EntryPoint="flmReadProgramFiles",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmReadProgramFiles(String fileName);

        [DllImport("TestFlash.dll", EntryPoint="flProgramBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flProgramBlock();

        [DllImport("TestFlash.dll", EntryPoint="flmProgramBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmProgramBlock(uint deviceMask, byte eraseFirst, byte verifyAfter, byte restartAfter);

        [DllImport("TestFlash.dll", EntryPoint="flErase",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flErase();

        [DllImport("TestFlash.dll", EntryPoint="flmEraseBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmEraseBlock(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flmEraseSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmEraseSpawn(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flGangProgramBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGangProgramBlock(ushort deviceMask, byte eraseFirst, byte restartAfter, byte skipUnused);

        [DllImport("TestFlash.dll", EntryPoint="flGetDetectedDevices",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern ushort flGetDetectedDevices();

        [DllImport("TestFlash.dll", EntryPoint="flGetBitErrorField",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern ushort flGetBitErrorField();

        [DllImport("TestFlash.dll", EntryPoint="flmGetBitErrorField",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint flmGetBitErrorField();

        [DllImport("TestFlash.dll", EntryPoint="flProgramSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flProgramSpawn();

        [DllImport("TestFlash.dll", EntryPoint="flmProgramSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmProgramSpawn(uint deviceMask, byte eraseFirst, byte verifyAfter, byte restartAfter);

        [DllImport("TestFlash.dll", EntryPoint="flGangProgramSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGangProgramSpawn(ushort deviceMask, byte eraseFirst, byte restartAfter, byte skipUnused);

        [DllImport("TestFlash.dll", EntryPoint="flGetProgress",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetProgress();

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceProgress",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetDeviceProgress(uint device);

        [DllImport("TestFlash.dll", EntryPoint="flGetLastError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetLastError();

        [DllImport("TestFlash.dll", EntryPoint="flmGetLastError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetLastError();

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetDeviceError(uint device);

        [DllImport("TestFlash.dll", EntryPoint="flResetAndStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flResetAndStart();

        [DllImport("TestFlash.dll", EntryPoint="flmResetAndStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmResetAndStart(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flClose",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern void flClose();

        [DllImport("TestFlash.dll", EntryPoint="flCloseRet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flCloseRet();

        [DllImport("TestFlash.dll", EntryPoint="flmClose",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern void flmClose(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flmCloseRet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmCloseRet(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flGetVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetVersion(StringBuilder versionStr);

        [DllImport("TestFlash.dll", EntryPoint="flmGetVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetVersion(StringBuilder versionStr);

        [DllImport("TestFlash.dll", EntryPoint="flStopProcessor",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flStopProcessor();

        [DllImport("TestFlash.dll", EntryPoint="flmStopProcessor",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmStopProcessor(uint deviceMask);

        [DllImport("TestFlash.dll", EntryPoint="flGetDownloadTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint flGetDownloadTime();

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceDownloadTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint flmGetDeviceDownloadTime(uint device);

        [DllImport("TestFlash.dll", EntryPoint="flGetAvailablePorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetAvailablePorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestFlash.dll", EntryPoint="flGetAvailablePortsEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetAvailablePortsEx(uint criteria, out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestFlash.dll", EntryPoint="flmGetAvailablePorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetAvailablePorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestFlash.dll", EntryPoint="flmGetAvailablePortsEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetAvailablePortsEx(uint criteria, out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestFlash.dll", EntryPoint="flmConvertPort",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmConvertPort(String transIn, StringBuilder transOut, out uint device);

        [DllImport("TestFlash.dll", EntryPoint="flGetFirmwareIds",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetFirmwareIds(byte source, out uint loaderId, StringBuilder loaderName, out uint stackId, StringBuilder stackName, ushort maxNameLen);

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceFirmwareIds",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetDeviceFirmwareIds(uint device, out uint loaderId, StringBuilder loaderName, out uint stackId, StringBuilder stackName, ushort maxNameLen);

        [DllImport("TestFlash.dll", EntryPoint="flmGetFileFirmwareIds",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetFileFirmwareIds(out uint loaderId, StringBuilder loaderName, out uint stackId, StringBuilder stackName, ushort maxNameLen);

        [DllImport("TestFlash.dll", EntryPoint="flVerify",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flVerify();

        [DllImport("TestFlash.dll", EntryPoint="flmVerifyBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmVerifyBlock(uint deviceMask, byte restartAfter);

        [DllImport("TestFlash.dll", EntryPoint="flmVerifySpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmVerifySpawn(uint deviceMask, byte restartAfter);

        [DllImport("TestFlash.dll", EntryPoint="flGetFlashInfo",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetFlashInfo(out ushort sectors, out ushort sizeMbits, out uint manId, out uint devId);

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceFlashInfo",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetDeviceFlashInfo(uint device, out ushort sectors, out ushort sizeMbits, out uint manId, out uint devId);

        [DllImport("TestFlash.dll", EntryPoint="flGetFlashInfoEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetFlashInfoEx(out uint sectors, out uint sizeMbits, out uint manId, out uint devId);

        [DllImport("TestFlash.dll", EntryPoint="flmGetDeviceFlashInfoEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetDeviceFlashInfoEx(uint device, out uint sectors, out uint sizeMbits, out uint manId, out uint devId);

        [DllImport("TestFlash.dll", EntryPoint="flSetFlashType",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetFlashType(byte aType);

        [DllImport("TestFlash.dll", EntryPoint="flmSetFlashType",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetFlashType(uint deviceMask, byte aType);

        [DllImport("TestFlash.dll", EntryPoint="flSetPios",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetPios(byte pioSclk, byte pioMiso, byte reserved);

        [DllImport("TestFlash.dll", EntryPoint="flmSetPios",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetPios(uint deviceMask, byte pioSclk, byte pioMiso, byte reserved);

        [DllImport("TestFlash.dll", EntryPoint="flSetSubsysChipSel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetSubsysChipSel(byte subSys, byte chipSel);

        [DllImport("TestFlash.dll", EntryPoint="flmSetSubsysChipSel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetSubsysChipSel(uint deviceMask, byte subSys, byte chipSel);

        [DllImport("TestFlash.dll", EntryPoint="flSetSqifAccess",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetSqifAccess(String fileName);

        [DllImport("TestFlash.dll", EntryPoint="flmSetSqifAccess",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetSqifAccess(uint deviceMask, String fileName);

        [DllImport("TestFlash.dll", EntryPoint="flSetSecurityKey",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetSecurityKey(String keyValOrFileName);

        [DllImport("TestFlash.dll", EntryPoint="flmSetSecurityKey",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetSecurityKey(uint deviceMask, String keyValOrFileName);

        [DllImport("TestFlash.dll", EntryPoint="flEnableSecurity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flEnableSecurity(uint options);

        [DllImport("TestFlash.dll", EntryPoint="flmEnableSecurity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmEnableSecurity(uint deviceMask, uint options);

        [DllImport("TestFlash.dll", EntryPoint="flGetChipId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern ushort flGetChipId();

        [DllImport("TestFlash.dll", EntryPoint="flmGetChipId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern ushort flmGetChipId(uint device);

        [DllImport("TestFlash.dll", EntryPoint="open_ps",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int open_ps(int port, int device);

        [DllImport("TestFlash.dll", EntryPoint="close_ps",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int close_ps();

        [DllImport("TestFlash.dll", EntryPoint="set_stores",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern void set_stores(ushort store);

        [DllImport("TestFlash.dll", EntryPoint="write_ps",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int write_ps(ushort key, ushort [] data, ushort keyLen);

        [DllImport("TestFlash.dll", EntryPoint="write_ps_verify",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int write_ps_verify(ushort key, ushort [] data, ushort keyLen);

        [DllImport("TestFlash.dll", EntryPoint="read_ps",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int read_ps(ushort key, ushort [] data, ushort maxlen, out ushort keyLen);

        [DllImport("TestFlash.dll", EntryPoint="clear_ps",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int clear_ps(ushort key);

        [DllImport("TestFlash.dll", EntryPoint="factory_set",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int factory_set();

        [DllImport("TestFlash.dll", EntryPoint="e2_device",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int e2_device(ushort log2bytes, ushort addrmask);

        [DllImport("TestFlash.dll", EntryPoint="get_firmware_id",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int get_firmware_id(out int id, ushort [] nameBuffer, uint length);


// DEPRECATED FUNCTIONS
		[DllImport("TestFlash.dll", EntryPoint="flOpen",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int init_flash(int port, int xtal, int delays, int transport);

		[DllImport("TestFlash.dll", EntryPoint="flReadProgramFiles",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int read_program_files(String fileName);

		[DllImport("TestFlash.dll", EntryPoint="flProgramBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int program_flash_block();

		[DllImport("TestFlash.dll", EntryPoint="flErase",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int erase_flash();

		[DllImport("TestFlash.dll", EntryPoint="flGangProgramBlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int gang_program_flash_block(ushort deviceMask, byte eraseFirst, byte restartAfter, byte skipUnused);

		[DllImport("TestFlash.dll", EntryPoint="flGetBitErrorField",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern ushort get_bit_error_field();

		[DllImport("TestFlash.dll", EntryPoint="flProgramSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int program_flash_spawn();

		[DllImport("TestFlash.dll", EntryPoint="flGangProgramSpawn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int gang_program_flash_spawn(ushort deviceMask, byte eraseFirst, byte restartAfter, byte skipUnused);

		[DllImport("TestFlash.dll", EntryPoint="flGetProgress",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int get_spawned_progress();

		[DllImport("TestFlash.dll", EntryPoint="flGetLastError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int get_spawned_error();

		[DllImport("TestFlash.dll", EntryPoint="flResetAndStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int reset_and_start();

		[DllImport("TestFlash.dll", EntryPoint="flClose",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern void close_flash();

		[DllImport("TestFlash.dll", EntryPoint="flGetVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int get_version(StringBuilder versionStr);

		[DllImport("TestFlash.dll", EntryPoint="flGetAvailablePorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flGetAvailableSpiPorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

		[DllImport("TestFlash.dll", EntryPoint="flmGetAvailablePorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmGetAvailableSpiPorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

		[DllImport("TestFlash.dll", EntryPoint="flOpen",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flInit(int port, int xtal, int delays, int transport);

		[DllImport("TestFlash.dll", EntryPoint="flOpenTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flInitTrans(String trans, int xtal, int delays);

		[DllImport("TestFlash.dll", EntryPoint="flOpenUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flInitSpiUnlock(int port, int xtal, int delays, int transport, String unlockKey);

		[DllImport("TestFlash.dll", EntryPoint="flOpenUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flInitSpiUnlockTrans(String trans, int xtal, int delays, String unlockKey);

		[DllImport("TestFlash.dll", EntryPoint="flmOpenUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpenSpiUnlock(uint deviceMask, int xtal, int transport, String unlockKey);

		[DllImport("TestFlash.dll", EntryPoint="flmOpenUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmOpenSpiUnlockTrans(uint deviceMask, String trans, int xtal, String unlockKey);

		[DllImport("TestFlash.dll", EntryPoint="flSetSubsysChipSel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flSetSubsysBank(byte subSys, byte chipSel);

		[DllImport("TestFlash.dll", EntryPoint="flmConvertPort",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmConvertSpiPort(String transIn, StringBuilder transOut, out uint device);

		[DllImport("TestFlash.dll", EntryPoint="flmSetSubsysChipSel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int flmSetSubsysBank(uint deviceMask, byte subSys, byte chipSel);

	}
}