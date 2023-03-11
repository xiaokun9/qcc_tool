'''
########################################################################################
convert_Filter_to_HTF.py
 
Copyright (c) 2020 Qualcomm Technologies International, Ltd.
All Rights Reserved.
Qualcomm Technologies International, Ltd. Confidential and Proprietary.

The purpose of this script is to convert a filter file in a readable text file format to
a .HTF filter format that can be loaded into the QCC file system

########################################################################################
******************* IT IS NOT NECESSARY TO BE CONNECTED TO THE DEVICE ******************
########################################################################################

Usage: python convert_Filter_to_HTF.py [X] [Y] [samplefile.htf]

Where: 	X is a text file holding the filter location parameters
		Y is the ANC filter location to write to
		Y = 1 -> 1st ANC filter'
		Y = 2 -> 2nd ANC filter'
		Y = 3 -> 3rd ANC filter'
		Y = 4 -> 4th ANC filter'
		Y = 5 -> 5th ANC filter'

		'samplefile.htf' -> Name of the file where data will be saved in HTF format

To execute from within iPython (e.g. Anaconda environment):
>>> import sys
>>> sys.argv = ['convert_Filter_to_HTF.py','sampleFilter.txt','1','samplefile.htf']
>>> execfile(sys.argv[0])
########################################################################################
'''


import sys, os, time, subprocess, collections, math
import ctypes as ct
from TestEngine_ANC_API import *
from TestEngine_ANC_constants import *


exitFlag = 0

if len(sys.argv) < 3:
	print 'Usage: python push_filter.py X Y'
	print 'Where X is a text file holding the filter location parameters'
	print 'and where Y is the ANC filter location to write to'
	print 'Y = 1 -> 1st ANC filter'
	print 'Y = 2 -> 2nd ANC filter'
	print 'Y = 3 -> 3rd ANC filter'
	print 'X = ... -> ...th ANC filter'
	print 'X = %d -> %dth ANC filter' % (TOTAL_NUM_FILTERS, TOTAL_NUM_FILTERS)
	exitFlag = 1


if exitFlag != 1:
	if int(sys.argv[2]) <= TOTAL_NUM_FILTERS:
		key = 0x204100
		keyIndex = (int(sys.argv[2]) - 1) * 2
		keyActive = key + keyIndex
		print 'Writing key',hex(keyActive)
	else:
		print '%s is not a valid filter location. The valid range is 1-%d.' % ( sys.argv[2], TOTAL_NUM_FILTERS )
		exitFlag = 1

if exitFlag != 1:
	try:
		file_name = sys.argv[1]
		fileIn    = open(file_name, 'r')
	except:
		print 'Error opening file: %s  Please check that the file exists.' % (file_name)
		exitFlag = 1

	#--------------------------------------------------------------------------------------------------------------------------------------------
	# This function advances to the next line in the  then reads and parses the data of interest which is then returned to the calling point
	#--------------------------------------------------------------------------------------------------------------------------------------------
def read_line_from_file():
	return int(str(next(fileIn,'').split(':',1)[1]).strip(),16)

	#-----------------------------------------------------------------------------
	# Read from filter parameter text file and write contents into parameter array
	#-----------------------------------------------------------------------------
for line in fileIn:
	if 'ANC_ENABLE_REGISTERS' in line:
		setParam('OFFSET_FF_B_ENABLE_L',   read_line_from_file())
		setParam('OFFSET_FF_A_ENABLE_L',   read_line_from_file())
		setParam('OFFSET_FB_ENABLE_L',     read_line_from_file())
		setParam('OFFSET_FF_OUT_ENABLE_L', read_line_from_file())
		setParam('OFFSET_FF_B_ENABLE_R',   read_line_from_file())
		setParam('OFFSET_FF_A_ENABLE_R',   read_line_from_file())
		setParam('OFFSET_FB_ENABLE_R',     read_line_from_file())
		setParam('OFFSET_FF_OUT_ENABLE_R', read_line_from_file())

	if 'LEFT_FEEDFORWARD_(FF)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		setParam('OFFSET_FF_B_DCFLT_ENABLE_L', read_line_from_file())
		setParam('OFFSET_FF_B_DCFLT_SHIFT_L',  read_line_from_file())
		next(fileIn,'')
		#setParam('OFFSET_ANC_FF_B_SHIFT_L', read_line_from_file())
		#setParam('OFFSET_ANC_FF_B_GAIN_L',  read_line_from_file())
		GAINS['FFB0_shift'] = read_line_from_file()
		GAINS['FFB0_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_B_LPF_SHIFT0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_LPF_SHIFT1_L', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_B_DEN_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF7_L', read_line_from_file())

	if 'LEFT_FEEDBACK_(FB)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		setParam('OFFSET_SMLPF_ENABLE_L', read_line_from_file())
		setParam('OFFSET_SM_LPF_SHIFT_L', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_FF_A_DCFLT_ENABLE_L', read_line_from_file())
		setParam('OFFSET_FF_A_DCFLT_SHIFT_L',  read_line_from_file())
		next(fileIn,'')
		#setParam('OFFSET_ANC_FF_A_SHIFT_L', read_line_from_file())
		#setParam('OFFSET_ANC_FF_A_GAIN_L',  read_line_from_file())
		GAINS['FFA0_shift'] = read_line_from_file()
		GAINS['FFA0_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_A_LPF_SHIFT0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_LPF_SHIFT1_L', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_A_DEN_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF7_L', read_line_from_file())

	if 'LEFT_ECHO_CANCELLATION_(EC)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		#setParam('OFFSET_ANC_FB_SHIFT_L', read_line_from_file())
		#setParam('OFFSET_ANC_FB_GAIN_L',  read_line_from_file())
		GAINS['FB0_shift'] = read_line_from_file()
		GAINS['FB0_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FB_LPF_SHIFT0_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_LPF_SHIFT1_L', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FB_DEN_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF0_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF1_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF2_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF3_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF4_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF5_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF6_L', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF7_L', read_line_from_file())

	if 'RIGHT_FEEDFORWARD_(FF)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		setParam('OFFSET_FF_B_DCFLT_ENABLE_R', read_line_from_file())
		setParam('OFFSET_FF_B_DCFLT_SHIFT_R',  read_line_from_file())
		next(fileIn,'')
		#setParam('OFFSET_ANC_FF_B_SHIFT_R', read_line_from_file())
		#setParam('OFFSET_ANC_FF_B_GAIN_R',  read_line_from_file())
		GAINS['FFB1_shift'] = read_line_from_file()
		GAINS['FFB1_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_B_LPF_SHIFT0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_LPF_SHIFT1_R', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_B_DEN_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_DEN_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_NUM_COEFF7_R', read_line_from_file())

	if 'RIGHT_FEEDBACK_(FB)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		setParam('OFFSET_SMLPF_ENABLE_R', read_line_from_file())
		setParam('OFFSET_SM_LPF_SHIFT_R', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_FF_A_DCFLT_ENABLE_R', read_line_from_file())
		setParam('OFFSET_FF_A_DCFLT_SHIFT_R',  read_line_from_file())
		next(fileIn,'')
		#setParam('OFFSET_ANC_FF_A_SHIFT_R', read_line_from_file())
		#setParam('OFFSET_ANC_FF_A_GAIN_R',  read_line_from_file())
		GAINS['FFA1_shift'] = read_line_from_file()
		GAINS['FFA1_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_A_LPF_SHIFT0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_LPF_SHIFT1_R', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FF_A_DEN_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_DEN_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_NUM_COEFF7_R', read_line_from_file())

	if 'RIGHT_ECHO_CANCELLATION_(EC)_FILTER_BLOCK_PARAMETERS' in line:
		next(fileIn,'')
		#setParam('OFFSET_ANC_FB_SHIFT_R', read_line_from_file())
		#setParam('OFFSET_ANC_FB_GAIN_R',  read_line_from_file())
		GAINS['FB1_shift'] = read_line_from_file()
		GAINS['FB1_gain']  = read_line_from_file()
		next(fileIn,'')
		setParam('OFFSET_ANC_FB_LPF_SHIFT0_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_LPF_SHIFT1_R', read_line_from_file())
		next(fileIn,'')
		setParam('OFFSET_ANC_FB_DEN_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_DEN_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF0_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF1_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF2_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF3_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF4_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF5_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF6_R', read_line_from_file())
		setParam('OFFSET_ANC_FB_NUM_COEFF7_R', read_line_from_file())

	if 'LEFT_CODEC_PARAMS' in line:
		setParam('OFFSET_DMIC_X2_FF_A_ENABLE_L',    read_line_from_file())
		setParam('OFFSET_DMIC_X2_FF_B_ENABLE_L',    read_line_from_file())
		setParam('OFFSET_FF_A_FE_GAIN_L',           read_line_from_file())
		setParam('OFFSET_FF_B_FE_GAIN_L',           read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVER_PA_GAIN_L',  read_line_from_file())

	if 'LEFT_UNUSED_PARAMS' in line:
		setParam('OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_L',   read_line_from_file())
		setParam('OFFSET_ANC_FB_GAIN_SCALE_L',           read_line_from_file())
		setParam('OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_GAIN_SCALE_L',         read_line_from_file())
		setParam('OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_L', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_GAIN_SCALE_L',         read_line_from_file())
		setParam('OFFSET_ANC_USECASE_L',                 read_line_from_file())
		setParam('OFFSET_FB_GAIN_ENABLE_L',              read_line_from_file())
		setParam('OFFSET_FB_MON_L',                      read_line_from_file())
		setParam('OFFSET_FFA_IN_ENABLE_L',               read_line_from_file())
		setParam('OFFSET_FFB_IN_ENABLE_L',               read_line_from_file())
		setParam('OFFSET_FF_A_GAIN_ENABLE_L',            read_line_from_file())
		setParam('OFFSET_FF_A_INPUT_DEVICE_L',           read_line_from_file())
		setParam('OFFSET_FF_A_MIC_SENSITIVITY_L',        read_line_from_file())
		setParam('OFFSET_FF_B_GAIN_ENABLE_L',            read_line_from_file())
		setParam('OFFSET_FF_B_INPUT_DEVICE_L',           read_line_from_file())
		setParam('OFFSET_FF_B_MIC_SENSITIVITY_L',        read_line_from_file())
		setParam('OFFSET_FF_FLEX_ENABLE_L',              read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVER_IMPEDANCE_L',     read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVE_SENSITIVITY_L',    read_line_from_file())

	if 'RIGHT_CODEC_PARAMS' in line:
		setParam('OFFSET_DMIC_X2_FF_A_ENABLE_R',    read_line_from_file())
		setParam('OFFSET_DMIC_X2_FF_B_ENABLE_R',    read_line_from_file())
		setParam('OFFSET_FF_A_FE_GAIN_R',           read_line_from_file())
		setParam('OFFSET_FF_B_FE_GAIN_R',           read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVER_PA_GAIN_R',  read_line_from_file())

	if 'RIGHT_UNUSED_PARAMS' in line:
		setParam('OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_R',   read_line_from_file())
		setParam('OFFSET_ANC_FB_GAIN_SCALE_R',           read_line_from_file())
		setParam('OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_A_GAIN_SCALE_R',         read_line_from_file())
		setParam('OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_R', read_line_from_file())
		setParam('OFFSET_ANC_FF_B_GAIN_SCALE_R',         read_line_from_file())
		setParam('OFFSET_ANC_USECASE_R',                 read_line_from_file())
		setParam('OFFSET_FB_GAIN_ENABLE_R',              read_line_from_file())
		setParam('OFFSET_FB_MON_R',                      read_line_from_file())
		setParam('OFFSET_FFA_IN_ENABLE_R',               read_line_from_file())
		setParam('OFFSET_FFB_IN_ENABLE_R',               read_line_from_file())
		setParam('OFFSET_FF_A_GAIN_ENABLE_R',            read_line_from_file())
		setParam('OFFSET_FF_A_INPUT_DEVICE_R',           read_line_from_file())
		setParam('OFFSET_FF_A_MIC_SENSITIVITY_R',        read_line_from_file())
		setParam('OFFSET_FF_B_GAIN_ENABLE_R',            read_line_from_file())
		setParam('OFFSET_FF_B_INPUT_DEVICE_R',           read_line_from_file())
		setParam('OFFSET_FF_B_MIC_SENSITIVITY_R',        read_line_from_file())
		setParam('OFFSET_FF_FLEX_ENABLE_R',              read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVER_IMPEDANCE_R',     read_line_from_file())
		setParam('OFFSET_SPKR_RECEIVE_SENSITIVITY_R',    read_line_from_file())

fileIn.close()
updatePsdata()

if len(sys.argv) > 3:
	writeHTF(filename= sys.argv[3], key=keyActive)

print('Process finished')
