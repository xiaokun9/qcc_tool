// TestEngineAPI.cs : Declares the DLL functions for C#.
// Copyright (c) 2022 Qualcomm Technologies International, Ltd.
// All Rights Reserved.
// Qualcomm Technologies International, Ltd. Confidential and Proprietary.

// Auto-generated CS wrapper for TestEngine DLL.
// Created on 2022-11-18 15:48 from TestEngine.h file

using System;
using System.Runtime.InteropServices;
using System.Text;

namespace TestEngineAPI
{
    public class TestEngine
    {
        const CharSet charset = CharSet.Ansi;
        const CallingConvention calling_convention = CallingConvention.StdCall;

        [DllImport("TestEngine.dll", EntryPoint="teGetVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetVersion(StringBuilder versionStr);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngine",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngine(int transport, String transportDevice, uint dataRate, int retryTimeOut, int usbTimeOut);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngineUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineUnlock(int transport, String transportDevice, int retryTimeOut, int usbTimeOut, String unlockKey);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngineDebug",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineDebug(int port, int multi, int transport);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineDebugUnlock(int port, int multi, int transport, String unlockKey);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineDebugTrans(String trans, int multi);

        [DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineDebugUnlockTrans(String trans, int multi, String unlockKey);

        [DllImport("TestEngine.dll", EntryPoint="closeTestEngine",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int closeTestEngine(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="closeTestEngineEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int closeTestEngineEx(uint handle, ushort options);

        [DllImport("TestEngine.dll", EntryPoint="teGetLastError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint teGetLastError(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetColdReset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetColdReset(uint handle, int usbTimeout);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetWarmReset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetWarmReset(uint handle, int usbTimeout);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPause",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPause(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="radiotestDeepSleep",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestDeepSleep(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmExtLb",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmExtLb(uint handle, ushort pcmMode);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmExtLbIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmExtLbIf(uint handle, ushort pcmMode, ushort pcmIf);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmLb",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmLb(uint handle, ushort pcmMode);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmLbIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmLbIf(uint handle, ushort pcmMode, ushort pcmIf);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmTimingIn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmTimingIn(uint handle, ushort pioOut, ushort pcmIn);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmTimingInIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmTimingInIf(uint handle, ushort pioOut, ushort pcmIn, ushort pcmIf);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmTone",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmTone(uint handle, ushort freq, ushort ampl, ushort dc);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmToneIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmToneIf(uint handle, ushort freq, ushort ampl, ushort dc, ushort pcmIf);

        [DllImport("TestEngine.dll", EntryPoint="radiotestPcmToneStereo",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestPcmToneStereo(uint handle, ushort freq, ushort ampl, ushort dc, ushort channel);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCtsRtsLb",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCtsRtsLb(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRadioStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRadioStatus(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hqGetRadioStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetRadioStatus(uint handle, ushort [] status, int timeout);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRadioStatusArray",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRadioStatusArray(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hqGetRadioStatusArray",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetRadioStatusArray(uint handle, ushort [] status, int timeout);

        [DllImport("TestEngine.dll", EntryPoint="bccmdMemoryGet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdMemoryGet(uint handle, ushort baseAddr, ushort dataLength, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdMemorySet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdMemorySet(uint handle, ushort baseAddr, ushort dataLength, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetBuildId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetBuildId(uint handle, out ushort buildId);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBuildName",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBuildName(uint handle, StringBuilder name, ushort maxLen, out ushort length);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetChipVersion",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetChipVersion(uint handle, out ushort chipVer);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetChipRevision",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetChipRevision(uint handle, out ushort chipRev);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetChipAnaVer",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetChipAnaVer(uint handle, out byte major, out byte minor, out byte vari);

        [DllImport("TestEngine.dll", EntryPoint="bccmdRouteClock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdRouteClock(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdRssiAcl",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdRssiAcl(uint handle, ushort connectionHandle, out short rssi);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetPio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetPio(uint handle, ushort mask, ushort port);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetPio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetPio(uint handle, out ushort mask, out ushort port);

        [DllImport("TestEngine.dll", EntryPoint="bccmdMapPio32",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdMapPio32(uint handle, uint mask, uint pios, out uint errLines);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetPio32",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetPio32(uint handle, uint mask, uint direction, uint value, out uint errLines);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetPio32",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetPio32(uint handle, out uint direction, out uint value);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetAdc",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetAdc(uint handle, ushort adc, out ushort result);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetAio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetAio(uint handle, ushort aio, out ushort result, out byte numBits);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBC5MMGetBatteryVoltage",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBC5MMGetBatteryVoltage(uint handle, out ushort voltage);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetFirmwareCheckMask",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetFirmwareCheckMask(uint handle, out ushort mask);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetFirmwareCheck",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetFirmwareCheck(uint handle, out ushort check);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetExternalClockPeriod",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetExternalClockPeriod(uint handle, out ushort period);

        [DllImport("TestEngine.dll", EntryPoint="bccmdEnableDeviceConnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdEnableDeviceConnect(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdEnableDeviceUnderTestMode",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdEnableDeviceUnderTestMode(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdCheckSqifImageValidationStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdCheckSqifImageValidationStatus(uint handle, out ushort status, ushort timeout);

        [DllImport("TestEngine.dll", EntryPoint="radiotestStereoCodecLB",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestStereoCodecLB(uint handle, ushort sampleRate, ushort reroute);

        [DllImport("TestEngine.dll", EntryPoint="radiotestTxstart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestTxstart(uint handle, ushort frequency, ushort power1, ushort power2, short modulation);

        [DllImport("TestEngine.dll", EntryPoint="radiotestTxdata1",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestTxdata1(uint handle, ushort frequency, ushort power1, ushort power2);

        [DllImport("TestEngine.dll", EntryPoint="radiotestTxdata2",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestTxdata2(uint handle, ushort countryCode, ushort power1, ushort power2);

        [DllImport("TestEngine.dll", EntryPoint="radiotestTxdata3",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestTxdata3(uint handle, ushort frequency, ushort power1, ushort power2);

        [DllImport("TestEngine.dll", EntryPoint="radiotestTxdata4",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestTxdata4(uint handle, ushort frequency, ushort power1, ushort power2);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgTxPower",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgTxPower(uint handle, short power);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRxstart1",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRxstart1(uint handle, ushort frequency, byte hiSide, ushort rxAttenuation);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRxstart2",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRxstart2(uint handle, ushort frequency, byte hiSide, ushort rxAttenuation, ushort sampleSize);

        [DllImport("TestEngine.dll", EntryPoint="hqGetRssi",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetRssi(uint handle, int timeout, ushort maxSize, ushort [] rssiSamples);

        [DllImport("TestEngine.dll", EntryPoint="radiotestBer1",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestBer1(uint handle, ushort frequency, byte hiSide, ushort rxAttenuation, uint sampleSize);

        [DllImport("TestEngine.dll", EntryPoint="radiotestBer2",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestBer2(uint handle, ushort countryCode, byte hiSide, ushort rxAttenuation, uint sampleSize);

        [DllImport("TestEngine.dll", EntryPoint="radiotestBerLoopback",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestBerLoopback(uint handle, ushort frequency, ushort power1, ushort power2, uint sampleSize);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRxLoopback",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRxLoopback(uint handle, ushort frequency, ushort intPA, ushort extPA);

        [DllImport("TestEngine.dll", EntryPoint="radiotestLoopback",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestLoopback(uint handle, ushort frequency, ushort power1, ushort power2);

        [DllImport("TestEngine.dll", EntryPoint="hqGetBer",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetBer(uint handle, int timeout, uint [] berReport);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRxdata1",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRxdata1(uint handle, ushort frequency, byte hiSide, ushort rxAttenuation);

        [DllImport("TestEngine.dll", EntryPoint="radiotestRxdata2",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestRxdata2(uint handle, ushort countryCode, byte hiSide, ushort rxAttenuation);

        [DllImport("TestEngine.dll", EntryPoint="hqGetRxdata",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetRxdata(uint handle, int timeout, ushort [] rxData);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgFreq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgFreq(uint handle, ushort txRxInterval, ushort loopback, ushort report);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgFreqMs",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgFreqMs(uint handle, ushort txRxInterval, ushort loopback, ushort report);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgPkt",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgPkt(uint handle, ushort aType, ushort size);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgBitError",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgBitError(uint handle, uint sampleSize, byte reset);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgTxPaAtten",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgTxPaAtten(uint handle, ushort atten);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgXtalFtrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgXtalFtrim(uint handle, ushort fTrim);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCalcXtalOffset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCalcXtalOffset(double nominalFreqMhz, double actualFreqMhz, out short offset);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgUapLap",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgUapLap(uint handle, ushort uap, uint lap);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgIqTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgIqTrim(uint handle, ushort trim);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgTxIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgTxIf(uint handle, short offset);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgTxTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgTxTrim(uint handle, ushort amAddr);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgLoLvl",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgLoLvl(uint handle, ushort loLvl);

        [DllImport("TestEngine.dll", EntryPoint="radiotestCfgHoppingSeq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestCfgHoppingSeq(uint handle, ushort [] channels);

        [DllImport("TestEngine.dll", EntryPoint="radiotestSettle",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestSettle(uint handle, ushort start, ushort aEnd);

        [DllImport("TestEngine.dll", EntryPoint="hqGetSettle",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetSettle(uint handle, ushort [] results);

        [DllImport("TestEngine.dll", EntryPoint="get_freq_offset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int get_freq_offset(uint handle, out double offset, int sampleSize);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetEeprom",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetEeprom(uint handle, ushort log2bytes, ushort addrMask);

        [DllImport("TestEngine.dll", EntryPoint="psReadBdAddr",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadBdAddr(uint handle, out uint lap, out byte uap, out ushort nap);

        [DllImport("TestEngine.dll", EntryPoint="psRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psRead(uint handle, ushort psKey, ushort store, ushort arrayLen, ushort [] data, out ushort keyLen);

        [DllImport("TestEngine.dll", EntryPoint="psClear",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psClear(uint handle, ushort psKey, ushort store);

        [DllImport("TestEngine.dll", EntryPoint="psClearAll",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psClearAll(uint handle, ushort store);

        [DllImport("TestEngine.dll", EntryPoint="psFactorySet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psFactorySet(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="psFactoryRestoreAll",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psFactoryRestoreAll(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="psFactoryRestore",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psFactoryRestore(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="psSize",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psSize(uint handle, ushort psKey, ushort store, out ushort size);

        [DllImport("TestEngine.dll", EntryPoint="psWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWrite(uint handle, ushort psKey, ushort store, ushort length, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="psWriteVerify",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteVerify(uint handle, ushort psKey, ushort store, ushort length, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="psWriteBdAddr",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteBdAddr(uint handle, uint lap, uint uap, uint nap);

        [DllImport("TestEngine.dll", EntryPoint="psReadModuleId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadModuleId(uint handle, out uint moduleId);

        [DllImport("TestEngine.dll", EntryPoint="psReadXtalFtrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadXtalFtrim(uint handle, out ushort fTrim);

        [DllImport("TestEngine.dll", EntryPoint="psWriteXtalFtrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteXtalFtrim(uint handle, ushort fTrim);

        [DllImport("TestEngine.dll", EntryPoint="psReadXtalOffset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadXtalOffset(uint handle, out short offset);

        [DllImport("TestEngine.dll", EntryPoint="psWriteXtalOffset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteXtalOffset(uint handle, short offset);

        [DllImport("TestEngine.dll", EntryPoint="psWriteModuleSecurityCode",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteModuleSecurityCode(uint handle, ushort [] code);

        [DllImport("TestEngine.dll", EntryPoint="psWriteModuleId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteModuleId(uint handle, uint moduleId);

        [DllImport("TestEngine.dll", EntryPoint="psWriteBaudrate",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteBaudrate(uint handle, ushort value);

        [DllImport("TestEngine.dll", EntryPoint="psWriteRadiotestFirstTrimTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteRadiotestFirstTrimTime(uint handle, uint time);

        [DllImport("TestEngine.dll", EntryPoint="psReadRadiotestFirstTrimTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadRadiotestFirstTrimTime(uint handle, out uint time);

        [DllImport("TestEngine.dll", EntryPoint="psWriteRadiotestLoLvlTrimEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteRadiotestLoLvlTrimEnable(uint handle, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="psReadRadiotestLoLvlTrimEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadRadiotestLoLvlTrimEnable(uint handle, out ushort state);

        [DllImport("TestEngine.dll", EntryPoint="psWriteRadiotestSubsequentTrimTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteRadiotestSubsequentTrimTime(uint handle, uint time);

        [DllImport("TestEngine.dll", EntryPoint="psReadRadiotestSubsequentTrimTime",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadRadiotestSubsequentTrimTime(uint handle, out uint time);

        [DllImport("TestEngine.dll", EntryPoint="psWriteHostInterface",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteHostInterface(uint handle, ushort transport);

        [DllImport("TestEngine.dll", EntryPoint="psReadHostInterface",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadHostInterface(uint handle, out ushort transport);

        [DllImport("TestEngine.dll", EntryPoint="psWriteUsbAttributes",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteUsbAttributes(uint handle, ushort bmAttributes);

        [DllImport("TestEngine.dll", EntryPoint="psWriteDPlusPullup",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteDPlusPullup(uint handle, ushort pioPin);

        [DllImport("TestEngine.dll", EntryPoint="psWriteUsbMaxPower",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteUsbMaxPower(uint handle, ushort maxPower);

        [DllImport("TestEngine.dll", EntryPoint="psWritePioProtectMask",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWritePioProtectMask(uint handle, ushort mask);

        [DllImport("TestEngine.dll", EntryPoint="psReadPioProtectMask",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadPioProtectMask(uint handle, out ushort mask);

        [DllImport("TestEngine.dll", EntryPoint="psWriteTxOffsetHalfMhz",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteTxOffsetHalfMhz(uint handle, short offset);

        [DllImport("TestEngine.dll", EntryPoint="psReadTxOffsetHalfMhz",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadTxOffsetHalfMhz(uint handle, out short offset);

        [DllImport("TestEngine.dll", EntryPoint="psWriteUsrValue",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteUsrValue(uint handle, ushort userNo, ushort length, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="psReadUsrValue",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadUsrValue(uint handle, ushort userNo, ushort maxLen, out ushort length, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="psWritePowerTable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWritePowerTable(uint handle, ushort numEntries, byte [] intPA, byte [] extPA, int [] power);

        [DllImport("TestEngine.dll", EntryPoint="psReadPowerTable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadPowerTable(uint handle, int maxSize, out int numEntries, byte [] intPA, byte [] extPA, int [] power);

        [DllImport("TestEngine.dll", EntryPoint="psWriteVmDisable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psWriteVmDisable(uint handle, byte vmDisable);

        [DllImport("TestEngine.dll", EntryPoint="psReadVmDisable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psReadVmDisable(uint handle, out byte vmDisable);

        [DllImport("TestEngine.dll", EntryPoint="psMergeFromFile",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int psMergeFromFile(uint handle, String filePath);

        [DllImport("TestEngine.dll", EntryPoint="hciSlave",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSlave(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hciSetAfhHostChannelClass",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSetAfhHostChannelClass(uint handle, byte [] cClass);

        [DllImport("TestEngine.dll", EntryPoint="hciReadAfhChannelMap",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadAfhChannelMap(uint handle, ushort aclHandle, out byte mode, byte [] cMap);

        [DllImport("TestEngine.dll", EntryPoint="hciSetEventFilterAutoacceptConnection",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSetEventFilterAutoacceptConnection(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hciWriteInquiryScanActivity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWriteInquiryScanActivity(uint handle, ushort interval, ushort window);

        [DllImport("TestEngine.dll", EntryPoint="hciWritePageScanActivity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWritePageScanActivity(uint handle, ushort interval, ushort window);

        [DllImport("TestEngine.dll", EntryPoint="hciWriteScanEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWriteScanEnable(uint handle, byte scanEnable);

        [DllImport("TestEngine.dll", EntryPoint="hciInquiry",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciInquiry(uint handle, byte inquiryLength, byte numResponses, uint lap);

        [DllImport("TestEngine.dll", EntryPoint="hciGetInquiryResults",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetInquiryResults(uint handle, uint [] lap, byte [] uap, ushort [] nap, ushort [] clockOffset, uint maxLen, out uint dataLen);

        [DllImport("TestEngine.dll", EntryPoint="hciInquiryCancel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciInquiryCancel(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hciCreateConnection",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciCreateConnection(uint handle, uint lap, byte uap, ushort nap, ushort pktType, out ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciCreateConnectionNoInquiry",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciCreateConnectionNoInquiry(uint handle, uint lap, byte uap, ushort nap, ushort pktType, byte pageScanRepMode, byte pageScanMode, ushort clockOffset, byte allowRoleSwitch, out ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciCreateScoConnection",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciCreateScoConnection(uint handle, ushort aclConnectionHandle, ushort pktType, out ushort scoConnectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciSetupScoConnection",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSetupScoConnection(uint handle, ushort aclConnectionHandle, uint txBandwidth, uint rxBandwidth, ushort maxLatency, ushort voiceSetting, byte retransEffort, ushort pktType, out ushort scoConnectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciReadVoiceSetting",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadVoiceSetting(uint handle, out ushort voiceSetting);

        [DllImport("TestEngine.dll", EntryPoint="hciWriteVoiceSetting",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWriteVoiceSetting(uint handle, ushort voiceSetting);

        [DllImport("TestEngine.dll", EntryPoint="hciWriteLinkPolicySettings",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWriteLinkPolicySettings(uint handle, ushort connectionHandle, ushort linkPolicySettings);

        [DllImport("TestEngine.dll", EntryPoint="hciSendAclFile",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSendAclFile(uint handle, ushort connHandle, String fileName);

        [DllImport("TestEngine.dll", EntryPoint="hciSendAclData",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSendAclData(uint handle, ushort connHandle, byte [] data, ushort length);

        [DllImport("TestEngine.dll", EntryPoint="hciGetAclData",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetAclData(uint handle, byte [] data, out uint numBytes);

        [DllImport("TestEngine.dll", EntryPoint="hciGetAclBytesRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetAclBytesRead(uint handle, out uint numBytes);

        [DllImport("TestEngine.dll", EntryPoint="hciGetAclFileName",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetAclFileName(uint handle, StringBuilder fileName, out uint length);

        [DllImport("TestEngine.dll", EntryPoint="hciGetAclState",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetAclState(uint handle, out int state);

        [DllImport("TestEngine.dll", EntryPoint="hciResetAclState",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciResetAclState(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hciReset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReset(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetAnaXtalFtrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetAnaXtalFtrim(uint handle, out ushort fTrim);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetAnaXtalFtrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetAnaXtalFtrim(uint handle, ushort fTrim);

        [DllImport("TestEngine.dll", EntryPoint="hciSniffMode",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSniffMode(uint handle, ushort connectionHandle, ushort sniffMaxInterval, ushort sniffMinInterval, ushort sniffAttempt, ushort sniffTimeout);

        [DllImport("TestEngine.dll", EntryPoint="hciExitSniff",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciExitSniff(uint handle, ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciDisconnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciDisconnect(uint handle, ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciGetConnectionHandle",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetConnectionHandle(uint handle, uint lap, byte uap, ushort nap, out ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciConnectionStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciConnectionStatus(uint handle, ushort connectionHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciEnableDeviceUnderTestMode",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciEnableDeviceUnderTestMode(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="hciGetLinkQuality",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciGetLinkQuality(uint handle, ushort connectionHandle, out byte quality);

        [DllImport("TestEngine.dll", EntryPoint="hciReadBdAddr",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadBdAddr(uint handle, StringBuilder bdAddr);

        [DllImport("TestEngine.dll", EntryPoint="hciReadLocalVersionInformation",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadLocalVersionInformation(uint handle, uint [] versionInfo);

        [DllImport("TestEngine.dll", EntryPoint="hciReadRemoteVersionInformation",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadRemoteVersionInformation(uint handle, ushort connectionHandle, uint [] versionInfo);

        [DllImport("TestEngine.dll", EntryPoint="hciReadRemoteNameRequest",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciReadRemoteNameRequest(uint handle, uint lap, byte uap, ushort nap, byte pageScanRepMode, byte pageScanOffset, ushort clockOffset, StringBuilder remoteName);

        [DllImport("TestEngine.dll", EntryPoint="dmRegisterReq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmRegisterReq(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="dmSlave",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmSlave(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="dmEnableDeviceUnderTestMode",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmEnableDeviceUnderTestMode(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="dmWritePageScanActivity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmWritePageScanActivity(uint handle, ushort interval, ushort window);

        [DllImport("TestEngine.dll", EntryPoint="dmWriteInquiryScanActivity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmWriteInquiryScanActivity(uint handle, ushort interval, ushort window);

        [DllImport("TestEngine.dll", EntryPoint="dmWriteScanEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmWriteScanEnable(uint handle, byte scanEnable);

        [DllImport("TestEngine.dll", EntryPoint="dmSetEventFilterAutoacceptConnection",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int dmSetEventFilterAutoacceptConnection(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBc3PsuTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBc3PsuTrim(uint handle, ushort data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdChargerPsuTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdChargerPsuTrim(uint handle, ushort trim);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBc3BuckReg",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBc3BuckReg(uint handle, ushort data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdPsuSmpsEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdPsuSmpsEnable(uint handle, ushort reg);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBc3MicEn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBc3MicEn(uint handle, ushort data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdPsuHvLinearEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdPsuHvLinearEnable(uint handle, ushort reg);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBc3Led0",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBc3Led0(uint handle, ushort data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdLedEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdLedEnable(uint handle, ushort led, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="bccmdLed0Enable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdLed0Enable(uint handle, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBc3Led1",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBc3Led1(uint handle, ushort data);

        [DllImport("TestEngine.dll", EntryPoint="bccmdLed1Enable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdLed1Enable(uint handle, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="bccmdChargerStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdChargerStatus(uint handle, out ushort state);

        [DllImport("TestEngine.dll", EntryPoint="bccmdChargerDisable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdChargerDisable(uint handle, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="bccmdChargerSuppressLed0",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdChargerSuppressLed0(uint handle, ushort state);

        [DllImport("TestEngine.dll", EntryPoint="hciCreateConnectionNoWait",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciCreateConnectionNoWait(uint handle, uint lap, byte uap, ushort nap, ushort pktType, byte pageScanRepMode, byte pageScanMode, ushort clockOffset, byte allowRoleSwitch);

        [DllImport("TestEngine.dll", EntryPoint="hciWriteAuthenticationEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWriteAuthenticationEnable(uint handle, byte enable);

        [DllImport("TestEngine.dll", EntryPoint="hciLinkKeyRequestNegativeReply",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciLinkKeyRequestNegativeReply(uint handle, uint lap, byte uap, ushort nap);

        [DllImport("TestEngine.dll", EntryPoint="hciWaitForConnectionComplete",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWaitForConnectionComplete(uint handle, out ushort connHandle);

        [DllImport("TestEngine.dll", EntryPoint="hciWaitForLinkKeyRequest",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWaitForLinkKeyRequest(uint handle, out uint lap, out byte uap, out ushort nap);

        [DllImport("TestEngine.dll", EntryPoint="hciWaitForPinCodeRequest",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWaitForPinCodeRequest(uint handle, out uint lap, out byte uap, out ushort nap);

        [DllImport("TestEngine.dll", EntryPoint="hciWaitForEncryptionChange",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciWaitForEncryptionChange(uint handle, out byte enable);

        [DllImport("TestEngine.dll", EntryPoint="hciPinCodeRequestReply",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciPinCodeRequestReply(uint handle, uint lap, byte uap, ushort nap, byte pinCodeLength, byte [] pinCode);

        [DllImport("TestEngine.dll", EntryPoint="hciSetConnectionEncryption",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciSetConnectionEncryption(uint handle, ushort connHandle, byte enable);

        [DllImport("TestEngine.dll", EntryPoint="hciLeReadLocalSupportedFeatures",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciLeReadLocalSupportedFeatures(uint handle, out ulong leFeatures);

        [DllImport("TestEngine.dll", EntryPoint="hciLeTestEnd",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciLeTestEnd(uint handle, out ushort numPackets);

        [DllImport("TestEngine.dll", EntryPoint="hciLeEnhancedReceiverTest",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciLeEnhancedReceiverTest(uint handle, byte channel, byte phy, byte modIndex);

        [DllImport("TestEngine.dll", EntryPoint="hciLeEnhancedTransmitterTest",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hciLeEnhancedTransmitterTest(uint handle, byte channel, byte dataLength, byte payloadType, byte phy);

        [DllImport("TestEngine.dll", EntryPoint="vmWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int vmWrite(uint handle, ushort [] data);

        [DllImport("TestEngine.dll", EntryPoint="vmRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int vmRead(uint handle, ushort [] data, ushort timeout);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetSingleChan",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetSingleChan(uint handle, ushort channel);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetHoppingOn",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetHoppingOn(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmSwitchPower",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmSwitchPower(uint handle, byte powerOn);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmSetFreq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmSetFreq(uint handle, uint freqKHz);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmGetRssi",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmGetRssi(uint handle, out sbyte rssi);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmGetSnr",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmGetSnr(uint handle, out short snr);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmGetIfOffset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmGetIfOffset(uint handle, out short offset);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmGetStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmGetStatus(uint handle, out byte status);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmSetupAudio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmSetupAudio(uint handle, byte route, byte gain, byte channel);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmVerifyRDSPi",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmVerifyRDSPi(uint handle, ushort pi, ushort timeoutMs, out byte matched);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmTxSwitchPower",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmTxSwitchPower(uint handle, byte powerOn);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmTxSetFreq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmTxSetFreq(uint handle, uint freqKHz);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmTxSetPowerLevel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmTxSetPowerLevel(uint handle, short powerLevel);

        [DllImport("TestEngine.dll", EntryPoint="bccmdFmTxSetupAudio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdFmTxSetupAudio(uint handle, byte route, ushort audioGain);

        [DllImport("TestEngine.dll", EntryPoint="bccmdDisconnectAudio",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdDisconnectAudio(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="bccmdAudioGetSource",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdAudioGetSource(uint handle, ushort device, ushort iface, ushort channel, out ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="bccmdAudioGetSink",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdAudioGetSink(uint handle, ushort device, ushort iface, ushort channel, out ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="bccmdAudioConfigure",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdAudioConfigure(uint handle, ushort sid, ushort key, uint value);

        [DllImport("TestEngine.dll", EntryPoint="bccmdDirectChargerPsuTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdDirectChargerPsuTrim(uint handle, ushort trim);

        [DllImport("TestEngine.dll", EntryPoint="teSupportsHq",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teSupportsHq(uint handle, out byte hqSupported);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetAuxDac",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetAuxDac(uint handle, byte enable, byte level);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetMicBiasIf",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetMicBiasIf(uint handle, byte instance, byte enable, byte voltage);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetMicBias",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetMicBias(uint handle, byte enable, byte voltage, byte current, byte enableLowPowerMode);

        [DllImport("TestEngine.dll", EntryPoint="teGetAvailableDebugPorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetAvailableDebugPorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teGetAvailableDebugPortsEx",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetAvailableDebugPortsEx(uint criteria, out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

        [DllImport("TestEngine.dll", EntryPoint="bccmdProvokeFault",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdProvokeFault(uint handle, ushort faultCode);

        [DllImport("TestEngine.dll", EntryPoint="hqGetFaultReports",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetFaultReports(uint handle, ushort maxReports, ushort [] codes, uint [] timestamps, ushort [] repeats, out ushort numReports, int timeout);

        [DllImport("TestEngine.dll", EntryPoint="teGetFaultDesc",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetFaultDesc(uint handle, ushort faultCode, StringBuilder desc);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetMapScoPcm",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetMapScoPcm(uint handle, byte enable);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetVrefConstant",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetVrefConstant(uint handle, out ushort vref);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetVrefAdc",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetVrefAdc(uint handle, out ushort result, out byte numBits);

        [DllImport("TestEngine.dll", EntryPoint="bccmdBC5FMGetI2CState",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdBC5FMGetI2CState(uint handle, out byte sda, out byte scl);

        [DllImport("TestEngine.dll", EntryPoint="refEpGetRssiDbm",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int refEpGetRssiDbm(uint handle, ushort freqMHz, double rssiChip, out double rssiDbm);

        [DllImport("TestEngine.dll", EntryPoint="refEpGetPaLevel",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int refEpGetPaLevel(uint handle, ushort freqMHz, double targetPowerDbm, out ushort intPa, out double powerDbm);

        [DllImport("TestEngine.dll", EntryPoint="refEpWriteCalDataFile",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int refEpWriteCalDataFile(uint handle, String filePath);

        [DllImport("TestEngine.dll", EntryPoint="refEpLoadCalDataFile",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int refEpLoadCalDataFile(uint handle, String filePath);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetVmStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetVmStatus(uint handle, out ushort status, out ushort exitCode);

        [DllImport("TestEngine.dll", EntryPoint="bccmdI2CTransfer",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdI2CTransfer(uint handle, ushort slaveAddr, ushort txOctets, ushort rxOctets, byte restart, byte [] data, out ushort octets);

        [DllImport("TestEngine.dll", EntryPoint="radiotestBle",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int radiotestBle(uint handle, ushort command, byte channel, byte txLength, byte txPayload);

        [DllImport("TestEngine.dll", EntryPoint="hqGetBleRxPktCount",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int hqGetBleRxPktCount(uint handle, int timeout, out ushort pktCount);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetChargerTrims",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetChargerTrims(uint handle, out ushort chgRefTrim, out ushort hVrefTrim, out ushort rTrim, out ushort iTrim, out ushort iExtTrim, out ushort iTermTrim, out ushort vFastTrim, out ushort hystTrim);

        [DllImport("TestEngine.dll", EntryPoint="bccmdCapacitiveSensorRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdCapacitiveSensorRead(uint handle, ushort mask, ushort [] values);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSetSpiLockCustomerKey",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSetSpiLockCustomerKey(uint handle, uint [] custKey);

        [DllImport("TestEngine.dll", EntryPoint="bccmdGetSpiLockStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdGetSpiLockStatus(uint handle, out ushort status);

        [DllImport("TestEngine.dll", EntryPoint="bccmdSpiLockInitiateLock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdSpiLockInitiateLock(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="teGetChipDisplayName",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetChipDisplayName(uint handle, uint maxLen, StringBuilder name);

        [DllImport("TestEngine.dll", EntryPoint="teGetChipFamily",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetChipFamily(uint handle, out byte family);

        [DllImport("TestEngine.dll", EntryPoint="teGetChipId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetChipId(uint handle, out uint chipId);

        [DllImport("TestEngine.dll", EntryPoint="teGetPtapHifs",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetPtapHifs(out ushort length, StringBuilder hifIds, StringBuilder types, StringBuilder names, out ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teMcSetXtalFreqTrim",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teMcSetXtalFreqTrim(uint handle, ushort trimVal, out short mibVal);

        [DllImport("TestEngine.dll", EntryPoint="teMcSetXtalLoadCapacitance",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teMcSetXtalLoadCapacitance(uint handle, ushort value);

        [DllImport("TestEngine.dll", EntryPoint="teGetBuildId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetBuildId(uint handle, byte subsystem, out uint buildId);

        [DllImport("TestEngine.dll", EntryPoint="tePioMap",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePioMap(uint handle, ushort bank, uint mask, uint pios, out uint errLines);

        [DllImport("TestEngine.dll", EntryPoint="tePioSet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePioSet(uint handle, ushort bank, uint mask, uint direction, uint value, out uint errLines);

        [DllImport("TestEngine.dll", EntryPoint="tePioGet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePioGet(uint handle, ushort bank, out uint direction, out uint value);

        [DllImport("TestEngine.dll", EntryPoint="teAudioGetSource",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioGetSource(uint handle, ushort device, ushort iface, ushort channel, out ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioCloseSource",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioCloseSource(uint handle, ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioGetSink",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioGetSink(uint handle, ushort device, ushort iface, ushort channel, out ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioCloseSink",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioCloseSink(uint handle, ushort sid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioConnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioConnect(uint handle, ushort sourceId, ushort sinkId, out ushort tid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioDisconnect",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioDisconnect(uint handle, ushort tid);

        [DllImport("TestEngine.dll", EntryPoint="teAudioConfigure",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioConfigure(uint handle, ushort sid, ushort key, uint value);

        [DllImport("TestEngine.dll", EntryPoint="teAudioCreateOperator",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioCreateOperator(uint handle, ushort capabilityId, out ushort operatorId);

        [DllImport("TestEngine.dll", EntryPoint="teAudioDestroyOperators",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioDestroyOperators(uint handle, ushort [] operators, ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teAudioOperatorMessage",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioOperatorMessage(uint handle, ushort operatorId, ushort [] message, ushort messageLength);

        [DllImport("TestEngine.dll", EntryPoint="teAudioResetOperators",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioResetOperators(uint handle, ushort [] operators, ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teAudioStartOperators",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioStartOperators(uint handle, ushort [] operators, ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teAudioStopOperators",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioStopOperators(uint handle, ushort [] operators, ushort count);

        [DllImport("TestEngine.dll", EntryPoint="teAudioSetAncIirFilter",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioSetAncIirFilter(uint handle, ushort ancInstance, ushort pathId, ushort [] coefficients, ushort numCoeffs);

        [DllImport("TestEngine.dll", EntryPoint="teAudioSetAncLpfFilter",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioSetAncLpfFilter(uint handle, ushort ancInstance, ushort pathId, ushort shift1, ushort shift2);

        [DllImport("TestEngine.dll", EntryPoint="teAudioStreamAncEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioStreamAncEnable(uint handle, ushort anc0, ushort anc1);

        [DllImport("TestEngine.dll", EntryPoint="teAudioMicBiasConfigure",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAudioMicBiasConfigure(uint handle, ushort id, ushort key, uint value);

        [DllImport("TestEngine.dll", EntryPoint="teCapacitiveSensorRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teCapacitiveSensorRead(uint handle, ushort pad, out uint value);

        [DllImport("TestEngine.dll", EntryPoint="teCheckLicense",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teCheckLicense(uint handle, byte featureId, out byte result);

        [DllImport("TestEngine.dll", EntryPoint="teCheckLicenses",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teCheckLicenses(uint handle, ushort numFeatureIds, ushort [] featureIds, byte [] results);

        [DllImport("TestEngine.dll", EntryPoint="teAppDisable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAppDisable(uint handle, ushort reserved);

        [DllImport("TestEngine.dll", EntryPoint="teAppWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAppWrite(uint handle, byte channel, ushort [] data, ushort length);

        [DllImport("TestEngine.dll", EntryPoint="teAppRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAppRead(uint handle, out byte channel, ushort [] data, ushort dataLength, out ushort readLength, ushort timeoutMs);

        [DllImport("TestEngine.dll", EntryPoint="teAdcGet",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teAdcGet(uint handle, ushort adc, ushort delay, ushort extraFlag, out ushort result);

        [DllImport("TestEngine.dll", EntryPoint="teChargerSetConfig",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teChargerSetConfig(uint handle, ushort [] config);

        [DllImport("TestEngine.dll", EntryPoint="teChargerGetStatus",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teChargerGetStatus(uint handle, out ushort status);

        [DllImport("TestEngine.dll", EntryPoint="teNfcConfigure",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teNfcConfigure(uint handle, byte enable);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheInit",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheInit(uint handle, String configDb);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheRead(uint handle, String file, ushort reserved);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheMerge",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheMerge(uint handle, String file);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheReadItem",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheReadItem(uint handle, String key, StringBuilder value, out uint maxLen);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheWriteItem",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheWriteItem(uint handle, String key, String value);

        [DllImport("TestEngine.dll", EntryPoint="teConfigCacheWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teConfigCacheWrite(uint handle, String file, ushort reserved);

        [DllImport("TestEngine.dll", EntryPoint="teChipReset",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teChipReset(uint handle, uint mode);

        [DllImport("TestEngine.dll", EntryPoint="teEnableSecurity",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teEnableSecurity(uint handle, uint options);

        [DllImport("TestEngine.dll", EntryPoint="teI2cTransfer",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teI2cTransfer(uint handle, ushort pioScl, ushort pioSda, ushort devAddr, ushort clockKhz, ushort txOctets, ushort rxOctets, byte [] data, out ushort rxdOctets);

        [DllImport("TestEngine.dll", EntryPoint="teNvmTagRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teNvmTagRead(uint handle, ushort tagId, byte valueLen, byte [] value, out byte readLen);

        [DllImport("TestEngine.dll", EntryPoint="teNvmTagWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teNvmTagWrite(uint handle, ushort tagId, byte valueLen, byte [] value);

        [DllImport("TestEngine.dll", EntryPoint="tePsGetNextKeyId",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePsGetNextKeyId(uint handle, byte keyType, byte resetSearch, out uint keyId, out byte endOfStore);

        [DllImport("TestEngine.dll", EntryPoint="tePsRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePsRead(uint handle, uint keyId, ushort valueLen, ushort [] value, out ushort readLen);

        [DllImport("TestEngine.dll", EntryPoint="tePsWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePsWrite(uint handle, uint keyId, ushort valueLen, ushort [] value);

        [DllImport("TestEngine.dll", EntryPoint="tePsAudioRead",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePsAudioRead(uint handle, uint keyId, ushort valueLen, ushort [] value, out ushort readLen);

        [DllImport("TestEngine.dll", EntryPoint="tePsAudioWrite",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int tePsAudioWrite(uint handle, uint keyId, ushort valueLen, ushort [] value);

        [DllImport("TestEngine.dll", EntryPoint="teRadGetMaxPayloadLen",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadGetMaxPayloadLen(byte pktType, out ushort maxLen);

        [DllImport("TestEngine.dll", EntryPoint="teRadQhsStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadQhsStart(uint handle, byte testMode, byte channel, ushort payloadLen, byte payload, byte phyRate, byte txPower, ushort maxPackets, byte cteLen, byte cteType, byte slotDuration, byte numAntennae, byte [] antennaIds);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxContStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxContStart(uint handle, byte techType, byte channel, byte swGain, byte lePhy);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxGetRssi",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxGetRssi(uint handle, byte techType, byte channel, byte numSamples, out sbyte rssi);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxGetStats",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxGetStats(uint handle, out ushort pktLen, uint [] pktsRxd, uint [] acErrs, uint [] hecErrs, uint [] crcErrs, uint [] totalBitErrs, short [] rssi, out uint reserved);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxPktCfg",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxPktCfg(uint handle, ushort numPkts);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxPktStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxPktStart(uint handle, byte [] channels, byte payload, byte pktType, String bdAddr, byte hopMode, ushort pktLen, byte ltAddr, uint reserved);

        [DllImport("TestEngine.dll", EntryPoint="teRadStop",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadStop(uint handle);

        [DllImport("TestEngine.dll", EntryPoint="teRadTxContStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadTxContStart(uint handle, byte channel, byte power, byte transmitType, byte patternLen, uint bitPattern);

        [DllImport("TestEngine.dll", EntryPoint="teRadTxCwStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadTxCwStart(uint handle, byte channel, byte power);

        [DllImport("TestEngine.dll", EntryPoint="teRadTxPktStart",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadTxPktStart(uint handle, byte [] channels, byte payload, byte pktType, byte power, String bdAddr, byte hopMode, ushort pktLen, byte ltAddr, uint reserved);

        [DllImport("TestEngine.dll", EntryPoint="teRadLeTxBurst",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadLeTxBurst(uint handle, byte hopMode, ushort payloadLen, byte payloadType, byte pktType, byte power);

        [DllImport("TestEngine.dll", EntryPoint="teRadTxEnhanced",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadTxEnhanced(uint handle, byte channel, byte pktType, ushort payloadLen, byte payloadType, uint payloadPattern, byte transmitType, byte ltAddr, byte hopping, String bdAddr, uint maxPkts, byte offSlots, byte power);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxEnhanced",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxEnhanced(uint handle, byte channel, byte pktType, ushort payloadLen, byte payloadType, uint payloadPattern, byte receiveType, byte ltAddr, byte hopping, String bdAddr, uint maxPkts, byte offSlots, byte rxSwGain);

        [DllImport("TestEngine.dll", EntryPoint="teRadRxGetStatsEnhanced",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teRadRxGetStatsEnhanced(uint handle, out uint pktsRxd, out uint acErrs, out uint hecErrs, out uint crcErrs, out uint totalBitErrs, out short rssi, out uint reserved);


// DEPRECATED FUNCTIONS
		[DllImport("TestEngine.dll", EntryPoint="bccmdPsuSmpsEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdPsuBuckReg(uint handle, ushort reg);

		[DllImport("TestEngine.dll", EntryPoint="bccmdPsuHvLinearEnable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdPsuMicEn(uint handle, ushort reg);

		[DllImport("TestEngine.dll", EntryPoint="bccmdLed0Enable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdLed0(uint handle, ushort state);

		[DllImport("TestEngine.dll", EntryPoint="bccmdLed1Enable",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdLed1(uint handle, ushort state);

		[DllImport("TestEngine.dll", EntryPoint="bccmdChargerSuppressLed0",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int bccmdChargerSupressLed0(uint handle, ushort state);

		[DllImport("TestEngine.dll", EntryPoint="openTestEngineDebug",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineSpi(int port, int multi, int transport);

		[DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineSpiTrans(String trans, int multi);

		[DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugUnlock",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineSpiUnlock(int port, int multi, int transport, String unlockKey);

		[DllImport("TestEngine.dll", EntryPoint="openTestEngineDebugUnlockTrans",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern uint openTestEngineSpiUnlockTrans(String trans, int multi, String unlockKey);

		[DllImport("TestEngine.dll", EntryPoint="teGetAvailableDebugPorts",
                CharSet=charset, CallingConvention=calling_convention)]
        public static extern int teGetAvailableSpiPorts(out ushort maxLen, StringBuilder ports, StringBuilder trans, out ushort count);

	}
}