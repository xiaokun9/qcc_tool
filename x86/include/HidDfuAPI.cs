// HidDfuAPI.cs : Declares the DLL functions for C#.
// Copyright (c) 2022 Qualcomm Technologies International, Ltd.
// All Rights Reserved.
// Qualcomm Technologies International, Ltd. Confidential and Proprietary.

// Auto-generated CS wrapper for HidDfu DLL.
// Created on 2022-11-18 14:03 from HidDfu.h file

using System;
using System.Runtime.InteropServices;
using System.Text;

namespace HidDfuAPI
{
    public class HidDfu
    {
        const CharSet charset = CharSet.Ansi;
        const CallingConvention calling_convention = CallingConvention.StdCall;

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetFirmwareVersions",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuGetFirmwareVersions(StringBuilder versionString, out ushort maxLength, byte checkMatch);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuGetVersion(out ushort major, out ushort minor, out ushort release, out ushort build);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuConnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuConnect(ushort vid, ushort pid, ushort usage, ushort usagePage, out ushort count);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuDisconnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuDisconnect();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuBackup",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuBackup(String fileName, byte resetAfter);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuUpgrade",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuUpgrade(String fileName, byte resetAfter);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuUpgradeBin",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuUpgradeBin(String fileName);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuStop",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuStop(ushort waitForStopMs);

        [DllImport("HidDfu.dll", EntryPoint="hidDfuResetDevice",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuResetDevice();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetProgress",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern byte hidDfuGetProgress();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetResult",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuGetResult();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetLastError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern IntPtr hidDfuGetLastError();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuGetFailedDevicesCount",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern byte hidDfuGetFailedDevicesCount();

        [DllImport("HidDfu.dll", EntryPoint="hidDfuSendCommand",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hidDfuSendCommand(ref byte data, uint length);


	}
}