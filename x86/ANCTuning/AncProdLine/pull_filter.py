'''
########################################################################################################
 pull_filter.py
 
 Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
 All Rights Reserved.
 Qualcomm Technologies International, Ltd. Confidential and Proprietary.

 The purpose of this script is to 'pull' filter data from QCC and write it to a human readable text file

   Usage: python pull_filter.py X ['sampleFilter.txt']
   Where X is the ANC filter location to read'
        X = 1 -> 1st ANC filter'
        X = 2 -> 2nd ANC filter'
        X = 3 -> 3rd ANC filter'
        X = ... -> ...th ANC filter'
        X = n -> nth ANC filter'
    The second argument, if present, denotes the name of the file where the data will be saved.

    To execute from within iPython (e.g. Anaconda environment):
        >>> import sys
        >>> sys.argv = ['pull_filter.py','1']
        >>> execfile(sys.argv[0])

 Set the verboseFlag to 1 to print on screen the results of the internal functions
########################################################################################################
'''

import sys, os, time, subprocess, collections, math
import ctypes as ct
global L_R_FLAG
L_R_FLAG = ''
from TestEngine_ANC_API import *
from TestEngine_ANC_constants import *
import numpy as np

verboseFlag = 0

exitFlag = 0
if len(sys.argv) < 2:
  print '\nUsage: python pull_filter.py X [\'sampleFilter.txt\']'
  print 'Where X is the ANC filter location to read'
  print 'X = 1 -> 1st ANC filter'
  print 'X = 2 -> 2nd ANC filter'
  print 'X = 3 -> 3rd ANC filter'
  print 'X = ... -> ...th ANC filter'
  print 'X = %d -> %dth ANC filter' % (TOTAL_NUM_FILTERS, TOTAL_NUM_FILTERS)
  print '\n   The second argument, if present, denotes the name of the file where the data will be saved.'
  exitFlag = 1

if exitFlag != 1:
    if int(sys.argv[1]) <= TOTAL_NUM_FILTERS:
        key = 0x204100
        keyIndex = (int(sys.argv[1]) - 1) * 2
        key = key + keyIndex
        print 'Reading key',hex(key)

    else:
        print '%s is not a valid filter location. The valid range is 1-%d.' % ( sys.argv[1], TOTAL_NUM_FILTERS )
        exitFlag = 1

if exitFlag != 1:
    CURDIR = os.path.dirname(os.path.realpath(sys.argv[0]))

    #----------------------------------------------------------------------------------------
    # IMPORTANT to update this path variable per version and location of ADK tools location
    # location of TestEngine.dll
    #----------------------------------------------------------------------------------------
    BluesuitePath = r'C:\Program Files (x86)\QTIL\BlueSuite 3.2.1\x64'

    #TRANSPORT_USBDBG = 256
    #TRANSPORT_TRB = 128

    TRANSPORT = TRANSPORT_USBDBG
    if TRANSPORT == TRANSPORT_TRB:
        TransportText = 'TRB'
    else:
        if TRANSPORT == TRANSPORT_USBDBG:
            TransportText = 'USB'

    try:
        #--------------------------------------------------------------------------------------------------------------
        # Connect to QCC via USB or TRB and Read audio key data but suppress the print to screen messages to keep things neat.
        #--------------------------------------------------------------------------------------------------------------
        old_stdout = sys.stdout
        if verboseFlag == 0:
            sys.stdout = open(os.devnull, 'w')
        engine, handle = ANCConnectDUT( BluesuitePath, 256)
    except:
        sys.stdout = old_stdout
        print "QCC device not detected on",TransportText
        print "First connect to USB, then Power On, then ANC ON"
        handle = -1


    if handle != -1:
        readAudioKey(engine, handle, key)
        sys.stdout = old_stdout
        registerList = ['']
        registerList.append('ANC_ENABLE_REGISTERS')
        registerList.append('  Left_FF     : 0x%08X' % (getParam('OFFSET_FF_B_ENABLE_L')))
        registerList.append('  Left_FB     : 0x%08X' % (getParam('OFFSET_FF_A_ENABLE_L')))
        registerList.append('  Left_EC     : 0x%08X' % (getParam('OFFSET_FB_ENABLE_L')))
        registerList.append('  Left_path   : 0x%08X' % (getParam('OFFSET_FF_OUT_ENABLE_L')))
        registerList.append('  Right_FF    : 0x%08X' % (getParam('OFFSET_FF_B_ENABLE_R')))
        registerList.append('  Right_FB    : 0x%08X' % (getParam('OFFSET_FF_A_ENABLE_R')))
        registerList.append('  Right_EC    : 0x%08X' % (getParam('OFFSET_FB_ENABLE_R')))
        registerList.append('  Right_path  : 0x%08X' % (getParam('OFFSET_FF_OUT_ENABLE_R')))

        registerList.append('')
        registerList.append('LEFT_FEEDFORWARD_(FF)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Left_FF_DC_Block')
        registerList.append('  Enable      : 0x%08X' % (getParam('OFFSET_FF_B_DCFLT_ENABLE_L')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_B_DCFLT_SHIFT_L')))
        registerList.append('Left_FF_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FF_B_SHIFT_L')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_L')))
        registerList.append('Left_FF_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FF_B_LPF_SHIFT0_L')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FF_B_LPF_SHIFT1_L')))
        registerList.append('Left_FF_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF0_L')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF1_L')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF2_L')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF3_L')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF4_L')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF5_L')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF6_L')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF0_L')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF1_L')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF2_L')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF3_L')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF4_L')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF5_L')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF6_L')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF7_L')))

        registerList.append('')
        registerList.append('LEFT_FEEDBACK_(FB)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Left_smLPF')
        registerList.append('  Enable      : 0x%08X' % (getParam('OFFSET_SMLPF_ENABLE_L')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_SM_LPF_SHIFT_L')))
        registerList.append('Left_FB_DC_Block')
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_A_DCFLT_ENABLE_L')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_A_DCFLT_SHIFT_L')))
        registerList.append('Left_FB_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FF_A_SHIFT_L')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_L')))
        registerList.append('Left_FB_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FF_A_LPF_SHIFT0_L')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FF_A_LPF_SHIFT1_L')))
        registerList.append('Left_FB_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF0_L')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF1_L')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF2_L')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF3_L')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF4_L')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF5_L')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF6_L')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF0_L')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF1_L')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF2_L')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF3_L')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF4_L')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF5_L')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF6_L')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF7_L')))

        registerList.append('')
        registerList.append('LEFT_ECHO_CANCELLATION_(EC)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Left_EC_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FB_SHIFT_L')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_L')))
        registerList.append('Left_EC_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FB_LPF_SHIFT0_L')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FB_LPF_SHIFT1_L')))
        registerList.append('Left_EC_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF0_L')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF1_L')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF2_L')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF3_L')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF4_L')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF5_L')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF6_L')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF0_L')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF1_L')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF2_L')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF3_L')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF4_L')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF5_L')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF6_L')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF7_L')))

        registerList.append('')
        registerList.append('RIGHT_FEEDFORWARD_(FF)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Right_FF_DC_Block')
        registerList.append('  Enable      : 0x%08X' % (getParam('OFFSET_FF_B_DCFLT_ENABLE_R')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_B_DCFLT_SHIFT_R')))
        registerList.append('Right_FF_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FF_B_SHIFT_R')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_R')))
        registerList.append('Right_FF_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FF_B_LPF_SHIFT0_R')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FF_B_LPF_SHIFT1_R')))
        registerList.append('Right_FF_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF0_R')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF1_R')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF2_R')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF3_R')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF4_R')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF5_R')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_DEN_COEFF6_R')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF0_R')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF1_R')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF2_R')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF3_R')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF4_R')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF5_R')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF6_R')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FF_B_NUM_COEFF7_R')))

        registerList.append('')
        registerList.append('RIGHT_FEEDBACK_(FB)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Right_smLPF')
        registerList.append('  Enable      : 0x%08X' % (getParam('OFFSET_SMLPF_ENABLE_R')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_SM_LPF_SHIFT_R')))
        registerList.append('Right_FB_DC_Block')
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_A_DCFLT_ENABLE_R')))
        registerList.append('  Shift       : 0x%08X' % (getParam('OFFSET_FF_A_DCFLT_SHIFT_R')))
        registerList.append('Right_FB_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FF_A_SHIFT_R')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_R')))
        registerList.append('Right_FB_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FF_A_LPF_SHIFT0_R')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FF_A_LPF_SHIFT1_R')))
        registerList.append('Right_FB_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF0_R')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF1_R')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF2_R')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF3_R')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF4_R')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF5_R')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_DEN_COEFF6_R')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF0_R')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF1_R')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF2_R')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF3_R')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF4_R')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF5_R')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF6_R')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FF_A_NUM_COEFF7_R')))

        registerList.append('')
        registerList.append('RIGHT_ECHO_CANCELLATION_(EC)_FILTER_BLOCK_PARAMETERS')
        registerList.append('Right_EC_Gain')
        registerList.append('  Course_gain : 0x%08X' % (getParam('OFFSET_ANC_FB_SHIFT_R')))
        registerList.append('  Fine_gain   : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_R')))
        registerList.append('Right_EC_LPF')
        registerList.append('  Shift_0     : 0x%08X' % (getParam('OFFSET_ANC_FB_LPF_SHIFT0_R')))
        registerList.append('  Shift_1     : 0x%08X' % (getParam('OFFSET_ANC_FB_LPF_SHIFT1_R')))
        registerList.append('Right_EC_Coefficients')
        registerList.append('  DEN_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF0_R')))
        registerList.append('  DEN_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF1_R')))
        registerList.append('  DEN_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF2_R')))
        registerList.append('  DEN_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF3_R')))
        registerList.append('  DEN_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF4_R')))
        registerList.append('  DEN_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF5_R')))
        registerList.append('  DEN_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FB_DEN_COEFF6_R')))
        registerList.append('  NUM_COEFF0  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF0_R')))
        registerList.append('  NUM_COEFF1  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF1_R')))
        registerList.append('  NUM_COEFF2  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF2_R')))
        registerList.append('  NUM_COEFF3  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF3_R')))
        registerList.append('  NUM_COEFF4  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF4_R')))
        registerList.append('  NUM_COEFF5  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF5_R')))
        registerList.append('  NUM_COEFF6  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF6_R')))
        registerList.append('  NUM_COEFF7  : 0x%08X' % (getParam('OFFSET_ANC_FB_NUM_COEFF7_R')))

        # Left codec parameters
        registerList.append('')
        registerList.append('LEFT_CODEC_PARAMS')
        registerList.append('  OFFSET_DMIC_X2_FF_A_ENABLE_L         : 0x%08X' % (getParam('OFFSET_DMIC_X2_FF_A_ENABLE_L')))
        registerList.append('  OFFSET_DMIC_X2_FF_B_ENABLE_L         : 0x%08X' % (getParam('OFFSET_DMIC_X2_FF_B_ENABLE_L')))
        registerList.append('  OFFSET_FF_A_FE_GAIN_L                : 0x%08X' % (getParam('OFFSET_FF_A_FE_GAIN_L')))
        registerList.append('  OFFSET_FF_B_FE_GAIN_L                : 0x%08X' % (getParam('OFFSET_FF_B_FE_GAIN_L')))
        registerList.append('  OFFSET_SPKR_RECEIVER_PA_GAIN_L       : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVER_PA_GAIN_L')))

        # Left unused parameters
        registerList.append('')
        registerList.append('LEFT_UNUSED_PARAMS')
        registerList.append('  OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_L   : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_L')))
        registerList.append('  OFFSET_ANC_FB_GAIN_SCALE_L           : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_SCALE_L')))
        registerList.append('  OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_L : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_L')))
        registerList.append('  OFFSET_ANC_FF_A_GAIN_SCALE_L         : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_SCALE_L')))
        registerList.append('  OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_L : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_L')))
        registerList.append('  OFFSET_ANC_FF_B_GAIN_SCALE_L         : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_SCALE_L')))
        registerList.append('  OFFSET_ANC_USECASE_L                 : 0x%08X' % (getParam('OFFSET_ANC_USECASE_L')))
        registerList.append('  OFFSET_FB_GAIN_ENABLE_L              : 0x%08X' % (getParam('OFFSET_FB_GAIN_ENABLE_L')))
        registerList.append('  OFFSET_FB_MON_L                      : 0x%08X' % (getParam('OFFSET_FB_MON_L')))
        registerList.append('  OFFSET_FFA_IN_ENABLE_L               : 0x%08X' % (getParam('OFFSET_FFA_IN_ENABLE_L')))
        registerList.append('  OFFSET_FFB_IN_ENABLE_L               : 0x%08X' % (getParam('OFFSET_FFB_IN_ENABLE_L')))
        registerList.append('  OFFSET_FF_A_GAIN_ENABLE_L            : 0x%08X' % (getParam('OFFSET_FF_A_GAIN_ENABLE_L')))
        registerList.append('  OFFSET_FF_A_INPUT_DEVICE_L           : 0x%08X' % (getParam('OFFSET_FF_A_INPUT_DEVICE_L')))
        registerList.append('  OFFSET_FF_A_MIC_SENSITIVITY_L        : 0x%08X' % (getParam('OFFSET_FF_A_MIC_SENSITIVITY_L')))
        registerList.append('  OFFSET_FF_B_GAIN_ENABLE_L            : 0x%08X' % (getParam('OFFSET_FF_B_GAIN_ENABLE_L')))
        registerList.append('  OFFSET_FF_B_INPUT_DEVICE_L           : 0x%08X' % (getParam('OFFSET_FF_B_INPUT_DEVICE_L')))
        registerList.append('  OFFSET_FF_B_MIC_SENSITIVITY_L        : 0x%08X' % (getParam('OFFSET_FF_B_MIC_SENSITIVITY_L')))
        registerList.append('  OFFSET_FF_FLEX_ENABLE_L              : 0x%08X' % (getParam('OFFSET_FF_FLEX_ENABLE_L')))
        registerList.append('  OFFSET_SPKR_RECEIVER_IMPEDANCE_L     : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVER_IMPEDANCE_L')))
        registerList.append('  OFFSET_SPKR_RECEIVE_SENSITIVITY_L    : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVE_SENSITIVITY_L')))

        # Right codec parameters
        registerList.append('')
        registerList.append('RIGHT_CODEC_PARAMS')
        registerList.append('  OFFSET_DMIC_X2_FF_A_ENABLE_R         : 0x%08X' % (getParam('OFFSET_DMIC_X2_FF_A_ENABLE_R')))
        registerList.append('  OFFSET_DMIC_X2_FF_B_ENABLE_R         : 0x%08X' % (getParam('OFFSET_DMIC_X2_FF_B_ENABLE_R')))
        registerList.append('  OFFSET_FF_A_FE_GAIN_R                : 0x%08X' % (getParam('OFFSET_FF_A_FE_GAIN_R')))
        registerList.append('  OFFSET_FF_B_FE_GAIN_R                : 0x%08X' % (getParam('OFFSET_FF_B_FE_GAIN_R')))
        registerList.append('  OFFSET_SPKR_RECEIVER_PA_GAIN_R       : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVER_PA_GAIN_R')))

        # Right unused parameters
        registerList.append('')
        registerList.append('RIGHT_UNUSED_PARAMS')
        registerList.append('  OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_R   : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_R')))
        registerList.append('  OFFSET_ANC_FB_GAIN_SCALE_R           : 0x%08X' % (getParam('OFFSET_ANC_FB_GAIN_SCALE_R')))
        registerList.append('  OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_R : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_R')))
        registerList.append('  OFFSET_ANC_FF_A_GAIN_SCALE_R         : 0x%08X' % (getParam('OFFSET_ANC_FF_A_GAIN_SCALE_R')))
        registerList.append('  OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_R : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_R')))
        registerList.append('  OFFSET_ANC_FF_B_GAIN_SCALE_R         : 0x%08X' % (getParam('OFFSET_ANC_FF_B_GAIN_SCALE_R')))
        registerList.append('  OFFSET_ANC_USECASE_R                 : 0x%08X' % (getParam('OFFSET_ANC_USECASE_R')))
        registerList.append('  OFFSET_FB_GAIN_ENABLE_R              : 0x%08X' % (getParam('OFFSET_FB_GAIN_ENABLE_R')))
        registerList.append('  OFFSET_FB_MON_R                      : 0x%08X' % (getParam('OFFSET_FB_MON_R')))       
        registerList.append('  OFFSET_FFA_IN_ENABLE_R               : 0x%08X' % (getParam('OFFSET_FFA_IN_ENABLE_R')))       
        registerList.append('  OFFSET_FFB_IN_ENABLE_R               : 0x%08X' % (getParam('OFFSET_FFB_IN_ENABLE_R')))         
        registerList.append('  OFFSET_FF_A_GAIN_ENABLE_R            : 0x%08X' % (getParam('OFFSET_FF_A_GAIN_ENABLE_R')))
        registerList.append('  OFFSET_FF_A_INPUT_DEVICE_R           : 0x%08X' % (getParam('OFFSET_FF_A_INPUT_DEVICE_R')))
        registerList.append('  OFFSET_FF_A_MIC_SENSITIVITY_R        : 0x%08X' % (getParam('OFFSET_FF_A_MIC_SENSITIVITY_R')))
        registerList.append('  OFFSET_FF_B_GAIN_ENABLE_R            : 0x%08X' % (getParam('OFFSET_FF_B_GAIN_ENABLE_R')))
        registerList.append('  OFFSET_FF_B_INPUT_DEVICE_R           : 0x%08X' % (getParam('OFFSET_FF_B_INPUT_DEVICE_R')))
        registerList.append('  OFFSET_FF_B_MIC_SENSITIVITY_R        : 0x%08X' % (getParam('OFFSET_FF_B_MIC_SENSITIVITY_R')))
        registerList.append('  OFFSET_FF_FLEX_ENABLE_R              : 0x%08X' % (getParam('OFFSET_FF_FLEX_ENABLE_R')))
        registerList.append('  OFFSET_SPKR_RECEIVER_IMPEDANCE_R     : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVER_IMPEDANCE_R')))
        registerList.append('  OFFSET_SPKR_RECEIVE_SENSITIVITY_R    : 0x%08X' % (getParam('OFFSET_SPKR_RECEIVE_SENSITIVITY_R')))

        engine.closeTestEngine(handle)

        if len(sys.argv) > 2:
            print 'Creating file', sys.argv[2]
            fileOut = open(sys.argv[2],'w')
            for listEntry in registerList:
                fileOut.write(listEntry + '\n')

            fileOut.close()
        else:
            for i in registerList:
                print i

        print 'Process finished'
