################################################################################
#
#  TestEngine_ANC_constants.py
#
#  Copyright (c) 2018-2021 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Defines for ANC production test API.
#
################################################################################

from collections import namedtuple

# Total number of filters stores in persistance storage
TOTAL_NUM_FILTERS = 10

# microphone routing configuration - should match the on-chip config done with the ADK configuration tool
# mic instance can be 0,1,2
ANALOG_MIC = 3
DIGITAL_MIC = 6

INSTANCE_0_MASK = (1 << 16)
INSTANCE_1_MASK = (1 << 17)
INSTANCE_01_MASK = (INSTANCE_0_MASK | INSTANCE_1_MASK)

CONFIG_StereoHybridDmics = 1
CONFIG_MonoHybridAmics   = 2
CONFIG_StereoFFAmics = 3
CONFIG_MonoParallelAmics = 4

CONFIG = CONFIG_MonoParallelAmics

ANC_V1P9 = 1
ANC_V2P0 = 2

BOARD = ANC_V2P0

if BOARD == ANC_V2P0:
    IIR_NUM_BITS = 32
    IIR_NUM_COEFFS = 17
    IIR_INT_BITS = 8

elif BOARD == ANC_V1P9:
    IIR_NUM_BITS = 12
    IIR_NUM_COEFFS = 15
    IIR_INT_BITS = 3

if CONFIG == CONFIG_StereoHybridDmics:
    FFA0_MIC_INST = 1   # mic instance for FFA on ANC0
    FFB0_MIC_INST = 1   # mic instance for FFB on ANC0
    FFA1_MIC_INST = 2   # mic instance for FFA on ANC1
    FFB1_MIC_INST = 2   # mic instance for FFB on ANC1  None if not connected.

    # mic channel 0=channel A, 1=channel B
    FFA0_MIC_CHAN = 0   # mic channel for FFA on ANC0
    FFB0_MIC_CHAN = 1   # mic channel for FFB on ANC0
    FFA1_MIC_CHAN = 0   # mic channel for FFA on ANC1
    FFB1_MIC_CHAN = 1   # mic channel for FFB on ANC1

    # mic type 3=analog, 6=digital
    FFA0_MIC_TYPE = DIGITAL_MIC   # mic type for FFA on ANC0
    FFB0_MIC_TYPE = DIGITAL_MIC   # mic type for FFB on ANC0
    FFA1_MIC_TYPE = DIGITAL_MIC   # mic type for FFA on ANC1
    FFB1_MIC_TYPE = DIGITAL_MIC   # mic type for FFB on ANC1
elif CONFIG == CONFIG_MonoHybridAmics:
    FFA0_MIC_INST = 0   # mic instance for FFA on ANC0
    FFB0_MIC_INST = 0   # mic instance for FFB on ANC0
    FFA1_MIC_INST = None   # mic instance for FFA on ANC1
    FFB1_MIC_INST = None   # mic instance for FFB on ANC1  None if not connected.

    # mic channel 0=channel A, 1=channel B
    FFA0_MIC_CHAN = 0   # mic channel for FFA on ANC0
    FFB0_MIC_CHAN = 1   # mic channel for FFB on ANC0
    FFA1_MIC_CHAN = None   # mic channel for FFA on ANC1
    FFB1_MIC_CHAN = None   # mic channel for FFB on ANC1

    # mic type 3=analog, 6=digital
    FFA0_MIC_TYPE = ANALOG_MIC   # mic type for FFA on ANC0
    FFB0_MIC_TYPE = ANALOG_MIC   # mic type for FFB on ANC0
    FFA1_MIC_TYPE = None   # mic type for FFA on ANC1
    FFB1_MIC_TYPE = None   # mic type for FFB on ANC1

elif CONFIG == CONFIG_StereoFFAmics:
    FFA0_MIC_INST = 0   # mic instance for FFA on ANC0
    FFB0_MIC_INST = None   # mic instance for FFB on ANC0
    FFA1_MIC_INST = 0   # mic instance for FFA on ANC1
    FFB1_MIC_INST = None   # mic instance for FFB on ANC1  None if not connected.

    # mic channel 0=channel A, 1=channel B
    FFA0_MIC_CHAN = 0   # mic channel for FFA on ANC0
    FFB0_MIC_CHAN = None   # mic channel for FFB on ANC0
    FFA1_MIC_CHAN = 1   # mic channel for FFA on ANC1
    FFB1_MIC_CHAN = None   # mic channel for FFB on ANC1

    # mic type 3=analog, 6=digital
    FFA0_MIC_TYPE = ANALOG_MIC   # mic type for FFA on ANC0
    FFB0_MIC_TYPE = None   # mic type for FFB on ANC0
    FFA1_MIC_TYPE = ANALOG_MIC   # mic type for FFA on ANC1
    FFB1_MIC_TYPE = None   # mic type for FFB on ANC1

elif CONFIG == CONFIG_MonoParallelAmics:
    FFA0_MIC_INST = 0   # mic instance for FFA on ANC0
    FFB0_MIC_INST = 1   # mic instance for FFB on ANC0
    FFA1_MIC_INST = 0   # mic instance for FFA on ANC1
    FFB1_MIC_INST = 1   # mic instance for FFB on ANC1

    # mic channel 0=channel A, 1=channel B
    FFA0_MIC_CHAN = 0   # mic channel for FFA on ANC0
    FFB0_MIC_CHAN = 0   # mic channel for FFB on ANC0
    FFA1_MIC_CHAN = 1   # mic channel for FFA on ANC1
    FFB1_MIC_CHAN = 0   # mic channel for FFB on ANC1

    # mic type 3=analog, 6=digital
    FFA0_MIC_TYPE = ANALOG_MIC   # mic type for FFA on ANC0
    FFB0_MIC_TYPE = ANALOG_MIC   # mic type for FFB on ANC0
    FFA1_MIC_TYPE = ANALOG_MIC   # mic type for FFA on ANC1
    FFB1_MIC_TYPE = ANALOG_MIC   # mic type for FFB on ANC1

# return values from TestEngine functions
TE_FAIL = 0
TE_SUCCESS = 1
TE_UNSUPPORTED = 2

TRANSPORT_USBDBG = 256
TRANSPORT_TRB = 128

# available ANC stream keys
STREAM_CODEC_INPUT_GAIN = 0x0302
STREAM_CODEC_RAW_INPUT_GAIN = 0x0304

STREAM_ANC_INSTANCE = 0x1100
STREAM_ANC_INPUT = 0x1101
STREAM_ANC_FFA_DC_FILTER_ENABLE = 0x1102
STREAM_ANC_FFA_DC_FILTER_SHIFT = 0x1103
STREAM_ANC_FFB_DC_FILTER_ENABLE = 0x1104
STREAM_ANC_FFB_DC_FILTER_SHIFT = 0x1105
STREAM_ANC_SM_LPF_FILTER_ENABLE = 0x1106
STREAM_ANC_SM_LPF_FILTER_SHIFT = 0x1107
STREAM_ANC_FFA_GAIN = 0x1108
STREAM_ANC_FFA_GAIN_SHIFT = 0x1109
STREAM_ANC_FFB_GAIN = 0x110a
STREAM_ANC_FFB_GAIN_SHIFT = 0x110b
STREAM_ANC_FB_GAIN = 0x110c
STREAM_ANC_FB_GAIN_SHIFT = 0x110d
STREAM_ANC_FFA_ADAPT_ENABLE = 0x110e
STREAM_ANC_FFB_ADAPT_ENABLE = 0x110f
STREAM_ANC_FB_ADAPT_ENABLE = 0x1110
STREAM_ANC_CONTROL = 0x1111
STREAM_ANC_CONTROL_1			= 0x1112
STREAM_ANC_RX_MIX_FFA_GAIN      = 0x1113
STREAM_ANC_RX_MIX_FFA_SHIFT     = 0x1114
STREAM_ANC_RX_MIX_FFB_GAIN      = 0x1115
STREAM_ANC_RX_MIX_FFB_SHIFT     = 0x1116

# ANC_CONTROL Bits
CONTROL_SEL_POS = 16

DMIC_X0P5_A_SEL = 0x0001
DMIC_X0P5_B_SEL = 0x0002
DMIC_X2_A_SEL   = 0x0004
DMIC_X2_B_SEL   = 0x0008
ANC_FB_MON_SEL  = 0x0030
OUTMIX_EN       = 0x0040
FB_TUNE_DSM_EN  = 0x0080
FB_TUNE_DSM_CLR = 0x0100
FFGAIN_ZCD_EN   = 0x0200
ZCD_SHIFT       = 0x1c00
COEF_SMP_EN     = 0x2000
FFGAIN_SMP_EN   = 0x4000

FB_MON_SEL_POS  = 4
ZCD_SHIFT_POS   = 10

#FB mon valid values
FFA_ON_FBMON     = (0 << FB_MON_SEL_POS)
FB_ON_FBMON      = (1 << FB_MON_SEL_POS)
ANC_OUT_ON_FBMON = (2 << FB_MON_SEL_POS)
FBMON_INV        = (3 << FB_MON_SEL_POS)

# ANC_CONTROL_1 Bits
SELF_RXMIX_EN               = 0x0001
CROSS_RXMIX_EN              = 0x0002
ANC1_USES_ANC0_RX_PCM_INPUT = 0x0004
if(BOARD == ANC_V2P0):
    FFLE_EN                 = 0x0008
elif(BOARD == ANC_V1P9):
    FFLE_EN                 = 0x0020
# address of ANC PSkey
ANC_PSKEY_ACTIVE = 0x204100
ANC_PSKEY_LEAKTHROUGH = 0x204102
if(BOARD == ANC_V1P9):
    ANC_DATA_NUM_BYTES = 371
elif(BOARD == ANC_V2P0):    
    ANC_DATA_NUM_BYTES = 427

# max and min values for coarse (shift) and fine gains
MAX_GAIN_DB = 42    # max gain in dB for combination of coarse and fine gains
MAX_GAIN = 255      # fine gain max value
MAX_GAIN_SHIFT = 6  # coarse gain max value
MIN_GAIN = 0        # minimum fine gain value
MIN_GAIN_SHIFT = -4 # minimum coarse gain value
MIN_GAIN_DB = -24
if(BOARD == ANC_V2P0):
    MIN_GAIN_SHIFT = -8 # minimum coarse gain value
    MIN_GAIN_DB = -48

# in psdata, first 3 words are header information: number of blocks, start length, and number of parameters
OFFSET_PSDATA_HEADER = 3

ANC_INSTANCE_NONE_ID = 0x0000
ANC_INSTANCE_ANC0_ID = 0x0001
ANC_INSTANCE_ANC1_ID = 0x0002

ANC_PATH_NONE_ID = 0x0000
ANC_PATH_FFA_ID = 0x0001
ANC_PATH_FFB_ID = 0x0002
ANC_PATH_FB_ID = 0x0003
ANC_PATH_SM_LPF_ID = 0x0004

if(BOARD == ANC_V1P9):
    AncData = namedtuple ('AncData', ('name', 'device', 'instance', 'channel', 'stream_gain', 'stream_gain_shift', 'smLPF_enable', 'smLPF_shift' , 'dcfilter_enable' , 'dcfilter_shift'))
    ControlBits = namedtuple ('ControlBits', ('name', 'key', 'device', 'instance', 'channel', 'outmix', 'x0p5_a_select', 'x0p5_b_select', 'x2_a_select', 'x2_b_select', 'fbmon_select', 'ffgain_zcd_enable', 'ffle_enable'))
elif(BOARD == ANC_V2P0):
    AncData = namedtuple ('AncData', ('name', 'device', 'instance', 'channel', 'stream_gain', 'stream_gain_shift', 'smLPF_enable', 'smLPF_shift' , 'dcfilter_enable' , 'dcfilter_shift', 'rx_mix_gain', 'rx_mix_shift'))
    ControlBits = namedtuple ('ControlBits', ('name', 'key', 'device', 'instance', 'channel', 'outmix', 'x0p5_a_select', 'x0p5_b_select', 'x2_a_select', 'x2_b_select', 'fbmon_select', 'ffgain_zcd_enable'))
    Control1Bits = namedtuple ('Control1Bits', ('name', 'key', 'device', 'instance', 'channel', 'ffle_enable', 'self_rxmix_enable', 'cross_rxmix_enable', 'anc1_uses_anc0_enable'))
#MicData = namedtuple ('MicData', ('name', 'device', 'instance', 'channel', 'stream_gain'))

if(BOARD == ANC_V1P9):
    FFA0 = AncData('FFA0', FFA0_MIC_TYPE, FFA0_MIC_INST, FFA0_MIC_CHAN, STREAM_ANC_FFA_GAIN, STREAM_ANC_FFA_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT)
    FFB0 = AncData('FFB0', FFB0_MIC_TYPE, FFB0_MIC_INST, FFB0_MIC_CHAN, STREAM_ANC_FFB_GAIN, STREAM_ANC_FFB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFB_DC_FILTER_ENABLE, STREAM_ANC_FFB_DC_FILTER_SHIFT)
    FFA1 = AncData('FFA1', FFA1_MIC_TYPE, FFA1_MIC_INST, FFA1_MIC_CHAN, STREAM_ANC_FFA_GAIN, STREAM_ANC_FFA_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT)
    FFB1 = AncData('FFB1', FFB1_MIC_TYPE, FFB1_MIC_INST, FFB1_MIC_CHAN, STREAM_ANC_FFB_GAIN, STREAM_ANC_FFB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFB_DC_FILTER_ENABLE, STREAM_ANC_FFB_DC_FILTER_SHIFT)
    Anc0Control = ControlBits('Anc0Control', STREAM_ANC_CONTROL, ANALOG_MIC, FFA0_MIC_INST, FFA0_MIC_CHAN, OUTMIX_EN, DMIC_X0P5_A_SEL, DMIC_X0P5_B_SEL, DMIC_X2_A_SEL, DMIC_X2_B_SEL, ANC_FB_MON_SEL, FFGAIN_ZCD_EN, FFLE_EN)
    Anc1Control = ControlBits('Anc1Control', STREAM_ANC_CONTROL, ANALOG_MIC, FFA1_MIC_INST, FFA1_MIC_CHAN, None, DMIC_X0P5_A_SEL, DMIC_X0P5_B_SEL, DMIC_X2_A_SEL, DMIC_X2_B_SEL, ANC_FB_MON_SEL, FFGAIN_ZCD_EN, FFLE_EN)
    FB0 = AncData('FB0', FFA0_MIC_TYPE, FFA0_MIC_INST, FFA0_MIC_CHAN, STREAM_ANC_FB_GAIN, STREAM_ANC_FB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT)        # FB path gain is associated with FFA mic
    FB1 = AncData('FB1', FFA1_MIC_TYPE, FFA1_MIC_INST, FFA1_MIC_CHAN, STREAM_ANC_FB_GAIN, STREAM_ANC_FB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT)        # FB path gain is associated with FFA mic
elif(BOARD == ANC_V2P0):
    FFA0 = AncData('FFA0', FFA0_MIC_TYPE, FFA0_MIC_INST, FFA0_MIC_CHAN, STREAM_ANC_FFA_GAIN, STREAM_ANC_FFA_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT, STREAM_ANC_RX_MIX_FFA_GAIN, STREAM_ANC_RX_MIX_FFA_SHIFT)
    FFB0 = AncData('FFB0', FFB0_MIC_TYPE, FFB0_MIC_INST, FFB0_MIC_CHAN, STREAM_ANC_FFB_GAIN, STREAM_ANC_FFB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFB_DC_FILTER_ENABLE, STREAM_ANC_FFB_DC_FILTER_SHIFT, STREAM_ANC_RX_MIX_FFB_GAIN, STREAM_ANC_RX_MIX_FFB_SHIFT)
    FFA1 = AncData('FFA1', FFA1_MIC_TYPE, FFA1_MIC_INST, FFA1_MIC_CHAN, STREAM_ANC_FFA_GAIN, STREAM_ANC_FFA_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT, STREAM_ANC_RX_MIX_FFA_GAIN, STREAM_ANC_RX_MIX_FFA_SHIFT)
    FFB1 = AncData('FFB1', FFB1_MIC_TYPE, FFB1_MIC_INST, FFB1_MIC_CHAN, STREAM_ANC_FFB_GAIN, STREAM_ANC_FFB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFB_DC_FILTER_ENABLE, STREAM_ANC_FFB_DC_FILTER_SHIFT, STREAM_ANC_RX_MIX_FFB_GAIN, STREAM_ANC_RX_MIX_FFB_SHIFT)
    Anc0Control = ControlBits('Anc0Control', STREAM_ANC_CONTROL, ANALOG_MIC, FFA0_MIC_INST, FFA0_MIC_CHAN, OUTMIX_EN, DMIC_X0P5_A_SEL, DMIC_X0P5_B_SEL, DMIC_X2_A_SEL, DMIC_X2_B_SEL, ANC_FB_MON_SEL, FFGAIN_ZCD_EN)
    Anc1Control = ControlBits('Anc1Control', STREAM_ANC_CONTROL, ANALOG_MIC, FFA1_MIC_INST, FFA1_MIC_CHAN, None, DMIC_X0P5_A_SEL, DMIC_X0P5_B_SEL, DMIC_X2_A_SEL, DMIC_X2_B_SEL, ANC_FB_MON_SEL, FFGAIN_ZCD_EN)
    Anc0Control1 = Control1Bits('Anc0Control1', STREAM_ANC_CONTROL_1, ANALOG_MIC, FFA0_MIC_INST, FFA0_MIC_CHAN, FFLE_EN, SELF_RXMIX_EN, CROSS_RXMIX_EN, None)
    Anc1Control1 = Control1Bits('Anc1Control1', STREAM_ANC_CONTROL_1, ANALOG_MIC, FFA1_MIC_INST, FFA1_MIC_CHAN, FFLE_EN, SELF_RXMIX_EN, CROSS_RXMIX_EN, ANC1_USES_ANC0_RX_PCM_INPUT)
    FB0 = AncData('FB0', FFA0_MIC_TYPE, FFA0_MIC_INST, FFA0_MIC_CHAN, STREAM_ANC_FB_GAIN, STREAM_ANC_FB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT, None, None)        # FB path gain is associated with FFA mic
    FB1 = AncData('FB1', FFA1_MIC_TYPE, FFA1_MIC_INST, FFA1_MIC_CHAN, STREAM_ANC_FB_GAIN, STREAM_ANC_FB_GAIN_SHIFT, STREAM_ANC_SM_LPF_FILTER_ENABLE, STREAM_ANC_SM_LPF_FILTER_SHIFT, STREAM_ANC_FFA_DC_FILTER_ENABLE, STREAM_ANC_FFA_DC_FILTER_SHIFT, None, None)        # FB path gain is associated with FFA mic

#AFE_GAIN = MicData('AFE0', FFA0_MIC_TYPE, FFA0_MIC_INST, FFA0_MIC_CHAN, STREAM_CODEC_INPUT_GAIN)

# ANC parameters available for tuning, shared between QACT, ANC tuning library in apps P1, and anc tuning capability in audio subsystem
if(BOARD == ANC_V1P9):
    ANC_PARAM_LIST = [
            'OFFSET_ANC_USECASE_L',
            'OFFSET_FF_A_MIC_SENSITIVITY_L',
            'OFFSET_FF_B_MIC_SENSITIVITY_L',
            'OFFSET_FF_A_FE_GAIN_L',
            'OFFSET_FF_B_FE_GAIN_L',
            'OFFSET_SPKR_RECEIVE_SENSITIVITY_L',
            'OFFSET_SPKR_RECEIVER_IMPEDANCE_L',
            'OFFSET_SPKR_RECEIVER_PA_GAIN_L',
            'OFFSET_FF_A_ENABLE_L',
            'OFFSET_FF_B_ENABLE_L',
            'OFFSET_FB_ENABLE_L',
            'OFFSET_FFA_IN_ENABLE_L',
            'OFFSET_FFB_IN_ENABLE_L',
            'OFFSET_FF_A_INPUT_DEVICE_L',
            'OFFSET_FF_B_INPUT_DEVICE_L',
            'OFFSET_FB_MON_L',
            'OFFSET_FF_OUT_ENABLE_L',
            'OFFSET_SMLPF_ENABLE_L',
            'OFFSET_FF_FLEX_ENABLE_L',
            'OFFSET_FF_A_GAIN_ENABLE_L',
            'OFFSET_FF_B_GAIN_ENABLE_L',
            'OFFSET_FB_GAIN_ENABLE_L',
            'OFFSET_FF_A_DCFLT_ENABLE_L',
            'OFFSET_FF_B_DCFLT_ENABLE_L',
            'OFFSET_DMIC_X2_FF_A_ENABLE_L',
            'OFFSET_DMIC_X2_FF_B_ENABLE_L',
            'OFFSET_ANC_FF_A_SHIFT_L',
            'OFFSET_ANC_FF_B_SHIFT_L',
            'OFFSET_ANC_FB_SHIFT_L',
            'OFFSET_ANC_FF_A_DEN_COEFF0_L',
            'OFFSET_ANC_FF_A_DEN_COEFF1_L',
            'OFFSET_ANC_FF_A_DEN_COEFF2_L',
            'OFFSET_ANC_FF_A_DEN_COEFF3_L',
            'OFFSET_ANC_FF_A_DEN_COEFF4_L',
            'OFFSET_ANC_FF_A_DEN_COEFF5_L',
            'OFFSET_ANC_FF_A_DEN_COEFF6_L',
            'OFFSET_ANC_FF_A_NUM_COEFF0_L',
            'OFFSET_ANC_FF_A_NUM_COEFF1_L',
            'OFFSET_ANC_FF_A_NUM_COEFF2_L',
            'OFFSET_ANC_FF_A_NUM_COEFF3_L',
            'OFFSET_ANC_FF_A_NUM_COEFF4_L',
            'OFFSET_ANC_FF_A_NUM_COEFF5_L',
            'OFFSET_ANC_FF_A_NUM_COEFF6_L',
            'OFFSET_ANC_FF_A_NUM_COEFF7_L',
            'OFFSET_ANC_FF_A_GAIN_SCALE_L',
            'OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FF_A_GAIN_L',
            'OFFSET_ANC_FF_B_DEN_COEFF0_L',
            'OFFSET_ANC_FF_B_DEN_COEFF1_L',
            'OFFSET_ANC_FF_B_DEN_COEFF2_L',
            'OFFSET_ANC_FF_B_DEN_COEFF3_L',
            'OFFSET_ANC_FF_B_DEN_COEFF4_L',
            'OFFSET_ANC_FF_B_DEN_COEFF5_L',
            'OFFSET_ANC_FF_B_DEN_COEFF6_L',
            'OFFSET_ANC_FF_B_NUM_COEFF0_L',
            'OFFSET_ANC_FF_B_NUM_COEFF1_L',
            'OFFSET_ANC_FF_B_NUM_COEFF2_L',
            'OFFSET_ANC_FF_B_NUM_COEFF3_L',
            'OFFSET_ANC_FF_B_NUM_COEFF4_L',
            'OFFSET_ANC_FF_B_NUM_COEFF5_L',
            'OFFSET_ANC_FF_B_NUM_COEFF6_L',
            'OFFSET_ANC_FF_B_NUM_COEFF7_L',
            'OFFSET_ANC_FF_B_GAIN_SCALE_L',
            'OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FF_B_GAIN_L',
            'OFFSET_ANC_FB_DEN_COEFF0_L',
            'OFFSET_ANC_FB_DEN_COEFF1_L',
            'OFFSET_ANC_FB_DEN_COEFF2_L',
            'OFFSET_ANC_FB_DEN_COEFF3_L',
            'OFFSET_ANC_FB_DEN_COEFF4_L',
            'OFFSET_ANC_FB_DEN_COEFF5_L',
            'OFFSET_ANC_FB_DEN_COEFF6_L',
            'OFFSET_ANC_FB_NUM_COEFF0_L',
            'OFFSET_ANC_FB_NUM_COEFF1_L',
            'OFFSET_ANC_FB_NUM_COEFF2_L',
            'OFFSET_ANC_FB_NUM_COEFF3_L',
            'OFFSET_ANC_FB_NUM_COEFF4_L',
            'OFFSET_ANC_FB_NUM_COEFF5_L',
            'OFFSET_ANC_FB_NUM_COEFF6_L',
            'OFFSET_ANC_FB_NUM_COEFF7_L',
            'OFFSET_ANC_FB_GAIN_SCALE_L',
            'OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FB_GAIN_L',
            'OFFSET_ANC_FF_A_LPF_SHIFT0_L',
            'OFFSET_ANC_FF_A_LPF_SHIFT1_L',
            'OFFSET_ANC_FF_B_LPF_SHIFT0_L',
            'OFFSET_ANC_FF_B_LPF_SHIFT1_L',
            'OFFSET_ANC_FB_LPF_SHIFT0_L',
            'OFFSET_ANC_FB_LPF_SHIFT1_L',
            'OFFSET_FF_A_DCFLT_SHIFT_L',
            'OFFSET_FF_B_DCFLT_SHIFT_L',
            'OFFSET_SM_LPF_SHIFT_L',
            'OFFSET_ANC_USECASE_R',
            'OFFSET_FF_A_MIC_SENSITIVITY_R',
            'OFFSET_FF_B_MIC_SENSITIVITY_R',
            'OFFSET_FF_A_FE_GAIN_R',
            'OFFSET_FF_B_FE_GAIN_R',
            'OFFSET_SPKR_RECEIVE_SENSITIVITY_R',
            'OFFSET_SPKR_RECEIVER_IMPEDANCE_R',
            'OFFSET_SPKR_RECEIVER_PA_GAIN_R',
            'OFFSET_FF_A_ENABLE_R',
            'OFFSET_FF_B_ENABLE_R',
            'OFFSET_FB_ENABLE_R',
            'OFFSET_FFA_IN_ENABLE_R',
            'OFFSET_FFB_IN_ENABLE_R',
            'OFFSET_FF_A_INPUT_DEVICE_R',
            'OFFSET_FF_B_INPUT_DEVICE_R',
            'OFFSET_FB_MON_R',
            'OFFSET_FF_OUT_ENABLE_R',
            'OFFSET_SMLPF_ENABLE_R',
            'OFFSET_FF_FLEX_ENABLE_R',
            'OFFSET_FF_A_GAIN_ENABLE_R',
            'OFFSET_FF_B_GAIN_ENABLE_R',
            'OFFSET_FB_GAIN_ENABLE_R',
            'OFFSET_FF_A_DCFLT_ENABLE_R',
            'OFFSET_FF_B_DCFLT_ENABLE_R',
            'OFFSET_DMIC_X2_FF_A_ENABLE_R',
            'OFFSET_DMIC_X2_FF_B_ENABLE_R',
            'OFFSET_ANC_FF_A_SHIFT_R',
            'OFFSET_ANC_FF_B_SHIFT_R',
            'OFFSET_ANC_FB_SHIFT_R',
            'OFFSET_ANC_FF_A_DEN_COEFF0_R',
            'OFFSET_ANC_FF_A_DEN_COEFF1_R',
            'OFFSET_ANC_FF_A_DEN_COEFF2_R',
            'OFFSET_ANC_FF_A_DEN_COEFF3_R',
            'OFFSET_ANC_FF_A_DEN_COEFF4_R',
            'OFFSET_ANC_FF_A_DEN_COEFF5_R',
            'OFFSET_ANC_FF_A_DEN_COEFF6_R',
            'OFFSET_ANC_FF_A_NUM_COEFF0_R',
            'OFFSET_ANC_FF_A_NUM_COEFF1_R',
            'OFFSET_ANC_FF_A_NUM_COEFF2_R',
            'OFFSET_ANC_FF_A_NUM_COEFF3_R',
            'OFFSET_ANC_FF_A_NUM_COEFF4_R',
            'OFFSET_ANC_FF_A_NUM_COEFF5_R',
            'OFFSET_ANC_FF_A_NUM_COEFF6_R',
            'OFFSET_ANC_FF_A_NUM_COEFF7_R',
            'OFFSET_ANC_FF_A_GAIN_SCALE_R',
            'OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FF_A_GAIN_R',
            'OFFSET_ANC_FF_B_DEN_COEFF0_R',
            'OFFSET_ANC_FF_B_DEN_COEFF1_R',
            'OFFSET_ANC_FF_B_DEN_COEFF2_R',
            'OFFSET_ANC_FF_B_DEN_COEFF3_R',
            'OFFSET_ANC_FF_B_DEN_COEFF4_R',
            'OFFSET_ANC_FF_B_DEN_COEFF5_R',
            'OFFSET_ANC_FF_B_DEN_COEFF6_R',
            'OFFSET_ANC_FF_B_NUM_COEFF0_R',
            'OFFSET_ANC_FF_B_NUM_COEFF1_R',
            'OFFSET_ANC_FF_B_NUM_COEFF2_R',
            'OFFSET_ANC_FF_B_NUM_COEFF3_R',
            'OFFSET_ANC_FF_B_NUM_COEFF4_R',
            'OFFSET_ANC_FF_B_NUM_COEFF5_R',
            'OFFSET_ANC_FF_B_NUM_COEFF6_R',
            'OFFSET_ANC_FF_B_NUM_COEFF7_R',
            'OFFSET_ANC_FF_B_GAIN_SCALE_R',
            'OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FF_B_GAIN_R',
            'OFFSET_ANC_FB_DEN_COEFF0_R',
            'OFFSET_ANC_FB_DEN_COEFF1_R',
            'OFFSET_ANC_FB_DEN_COEFF2_R',
            'OFFSET_ANC_FB_DEN_COEFF3_R',
            'OFFSET_ANC_FB_DEN_COEFF4_R',
            'OFFSET_ANC_FB_DEN_COEFF5_R',
            'OFFSET_ANC_FB_DEN_COEFF6_R',
            'OFFSET_ANC_FB_NUM_COEFF0_R',
            'OFFSET_ANC_FB_NUM_COEFF1_R',
            'OFFSET_ANC_FB_NUM_COEFF2_R',
            'OFFSET_ANC_FB_NUM_COEFF3_R',
            'OFFSET_ANC_FB_NUM_COEFF4_R',
            'OFFSET_ANC_FB_NUM_COEFF5_R',
            'OFFSET_ANC_FB_NUM_COEFF6_R',
            'OFFSET_ANC_FB_NUM_COEFF7_R',
            'OFFSET_ANC_FB_GAIN_SCALE_R',
            'OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FB_GAIN_R',
            'OFFSET_ANC_FF_A_LPF_SHIFT0_R',
            'OFFSET_ANC_FF_A_LPF_SHIFT1_R',
            'OFFSET_ANC_FF_B_LPF_SHIFT0_R',
            'OFFSET_ANC_FF_B_LPF_SHIFT1_R',
            'OFFSET_ANC_FB_LPF_SHIFT0_R',
            'OFFSET_ANC_FB_LPF_SHIFT1_R',
            'OFFSET_FF_A_DCFLT_SHIFT_R',
            'OFFSET_FF_B_DCFLT_SHIFT_R',
            'OFFSET_SM_LPF_SHIFT_R',
            ]
if(BOARD == ANC_V2P0):
    ANC_PARAM_LIST = [
            'OFFSET_ANC_USECASE_L',
            'OFFSET_FF_A_MIC_SENSITIVITY_L',
            'OFFSET_FF_B_MIC_SENSITIVITY_L',
            'OFFSET_FF_A_FE_GAIN_L',
            'OFFSET_FF_B_FE_GAIN_L',
            'OFFSET_SPKR_RECEIVE_SENSITIVITY_L',
            'OFFSET_SPKR_RECEIVER_IMPEDANCE_L',
            'OFFSET_SPKR_RECEIVER_PA_GAIN_L',
            'OFFSET_FF_A_ENABLE_L',
            'OFFSET_FF_B_ENABLE_L',
            'OFFSET_FB_ENABLE_L',
            'OFFSET_FFA_IN_ENABLE_L',
            'OFFSET_FFB_IN_ENABLE_L',
            'OFFSET_ANC_OUTMIX_ENABLE_L',
            'OFFSET_ANC0_USES_ANC1_RX_PCM_INPUT',
            'OFFSET_FF_A_INPUT_DEVICE_L',
            'OFFSET_FF_B_INPUT_DEVICE_L',
            'OFFSET_FB_MON_L',
            'OFFSET_FF_OUT_ENABLE_L',
            'OFFSET_SMLPF_ENABLE_L',
            'OFFSET_SELF_RXMIX_ENABLE_L',
            'OFFSET_CROSS_RXMIX_ENABLE_L',
            'OFFSET_FF_FLEX_ENABLE_L',
            'OFFSET_FF_A_GAIN_ENABLE_L',
            'OFFSET_FF_B_GAIN_ENABLE_L',
            'OFFSET_FB_GAIN_ENABLE_L',
            'OFFSET_FF_A_DCFLT_ENABLE_L',
            'OFFSET_FF_B_DCFLT_ENABLE_L',
            'OFFSET_DMIC_X2_FF_A_ENABLE_L',
            'OFFSET_DMIC_X2_FF_B_ENABLE_L',
            'OFFSET_ANC_FF_A_SHIFT_L',
            'OFFSET_ANC_FF_B_SHIFT_L',
            'OFFSET_ANC_FB_SHIFT_L',
            'OFFSET_ANC_RX_MIX_FFa_SHIFT_L',
            'OFFSET_ANC_RX_MIX_FFb_SHIFT_L',
            'OFFSET_ANC_FF_A_DEN_COEFF0_L',
            'OFFSET_ANC_FF_A_DEN_COEFF1_L',
            'OFFSET_ANC_FF_A_DEN_COEFF2_L',
            'OFFSET_ANC_FF_A_DEN_COEFF3_L',
            'OFFSET_ANC_FF_A_DEN_COEFF4_L',
            'OFFSET_ANC_FF_A_DEN_COEFF5_L',
            'OFFSET_ANC_FF_A_DEN_COEFF6_L',
            'OFFSET_ANC_FF_A_DEN_COEFF7_L',
            'OFFSET_ANC_FF_A_NUM_COEFF0_L',
            'OFFSET_ANC_FF_A_NUM_COEFF1_L',
            'OFFSET_ANC_FF_A_NUM_COEFF2_L',
            'OFFSET_ANC_FF_A_NUM_COEFF3_L',
            'OFFSET_ANC_FF_A_NUM_COEFF4_L',
            'OFFSET_ANC_FF_A_NUM_COEFF5_L',
            'OFFSET_ANC_FF_A_NUM_COEFF6_L',
            'OFFSET_ANC_FF_A_NUM_COEFF7_L',
            'OFFSET_ANC_FF_A_NUM_COEFF8_L',
            'OFFSET_ANC_FF_A_GAIN_SCALE_L',
            'OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FF_A_GAIN_L',
            'OFFSET_ANC_RX_MIX_FF_A_GAIN_L',
            'OFFSET_ANC_FF_B_DEN_COEFF0_L',
            'OFFSET_ANC_FF_B_DEN_COEFF1_L',
            'OFFSET_ANC_FF_B_DEN_COEFF2_L',
            'OFFSET_ANC_FF_B_DEN_COEFF3_L',
            'OFFSET_ANC_FF_B_DEN_COEFF4_L',
            'OFFSET_ANC_FF_B_DEN_COEFF5_L',
            'OFFSET_ANC_FF_B_DEN_COEFF6_L',
            'OFFSET_ANC_FF_B_DEN_COEFF7_L',
            'OFFSET_ANC_FF_B_NUM_COEFF0_L',
            'OFFSET_ANC_FF_B_NUM_COEFF1_L',
            'OFFSET_ANC_FF_B_NUM_COEFF2_L',
            'OFFSET_ANC_FF_B_NUM_COEFF3_L',
            'OFFSET_ANC_FF_B_NUM_COEFF4_L',
            'OFFSET_ANC_FF_B_NUM_COEFF5_L',
            'OFFSET_ANC_FF_B_NUM_COEFF6_L',
            'OFFSET_ANC_FF_B_NUM_COEFF7_L',
            'OFFSET_ANC_FF_B_NUM_COEFF8_L',
            'OFFSET_ANC_FF_B_GAIN_SCALE_L',
            'OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FF_B_GAIN_L',
            'OFFSET_ANC_RX_MIX_FF_B_GAIN_L',
            'OFFSET_ANC_FB_DEN_COEFF0_L',
            'OFFSET_ANC_FB_DEN_COEFF1_L',
            'OFFSET_ANC_FB_DEN_COEFF2_L',
            'OFFSET_ANC_FB_DEN_COEFF3_L',
            'OFFSET_ANC_FB_DEN_COEFF4_L',
            'OFFSET_ANC_FB_DEN_COEFF5_L',
            'OFFSET_ANC_FB_DEN_COEFF6_L',
            'OFFSET_ANC_FB_DEN_COEFF7_L',
            'OFFSET_ANC_FB_NUM_COEFF0_L',
            'OFFSET_ANC_FB_NUM_COEFF1_L',
            'OFFSET_ANC_FB_NUM_COEFF2_L',
            'OFFSET_ANC_FB_NUM_COEFF3_L',
            'OFFSET_ANC_FB_NUM_COEFF4_L',
            'OFFSET_ANC_FB_NUM_COEFF5_L',
            'OFFSET_ANC_FB_NUM_COEFF6_L',
            'OFFSET_ANC_FB_NUM_COEFF7_L',
            'OFFSET_ANC_FB_NUM_COEFF8_L',
            'OFFSET_ANC_FB_GAIN_SCALE_L',
            'OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_L',
            'OFFSET_ANC_FB_GAIN_L',
            'OFFSET_ANC_FF_A_LPF_SHIFT0_L',
            'OFFSET_ANC_FF_A_LPF_SHIFT1_L',
            'OFFSET_ANC_FF_B_LPF_SHIFT0_L',
            'OFFSET_ANC_FF_B_LPF_SHIFT1_L',
            'OFFSET_ANC_FB_LPF_SHIFT0_L',
            'OFFSET_ANC_FB_LPF_SHIFT1_L',
            'OFFSET_FF_A_DCFLT_SHIFT_L',
            'OFFSET_FF_B_DCFLT_SHIFT_L',
            'OFFSET_SM_LPF_SHIFT_L',
            'OFFSET_ANC_USECASE_R',
            'OFFSET_FF_A_MIC_SENSITIVITY_R',
            'OFFSET_FF_B_MIC_SENSITIVITY_R',
            'OFFSET_FF_A_FE_GAIN_R',
            'OFFSET_FF_B_FE_GAIN_R',
            'OFFSET_SPKR_RECEIVE_SENSITIVITY_R',
            'OFFSET_SPKR_RECEIVER_IMPEDANCE_R',
            'OFFSET_SPKR_RECEIVER_PA_GAIN_R',
            'OFFSET_FF_A_ENABLE_R',
            'OFFSET_FF_B_ENABLE_R',
            'OFFSET_FB_ENABLE_R',
            'OFFSET_FFA_IN_ENABLE_R',
            'OFFSET_FFB_IN_ENABLE_R',
            'OFFSET_ANC_OUTMIX_ENABLE_R',
            'OFFSET_ANC1_USES_ANC0_RX_PCM_INPUT',
            'OFFSET_FF_A_INPUT_DEVICE_R',
            'OFFSET_FF_B_INPUT_DEVICE_R',
            'OFFSET_FB_MON_R',
            'OFFSET_FF_OUT_ENABLE_R',
            'OFFSET_SMLPF_ENABLE_R',
            'OFFSET_SELF_RXMIX_ENABLE_R',
            'OFFSET_CROSS_RXMIX_ENABLE_R',
            'OFFSET_FF_FLEX_ENABLE_R',
            'OFFSET_FF_A_GAIN_ENABLE_R',
            'OFFSET_FF_B_GAIN_ENABLE_R',
            'OFFSET_FB_GAIN_ENABLE_R',
            'OFFSET_FF_A_DCFLT_ENABLE_R',
            'OFFSET_FF_B_DCFLT_ENABLE_R',
            'OFFSET_DMIC_X2_FF_A_ENABLE_R',
            'OFFSET_DMIC_X2_FF_B_ENABLE_R',
            'OFFSET_ANC_FF_A_SHIFT_R',
            'OFFSET_ANC_FF_B_SHIFT_R',
            'OFFSET_ANC_FB_SHIFT_R',
            'OFFSET_ANC_RX_MIX_FFa_SHIFT_R',
            'OFFSET_ANC_RX_MIX_FFb_SHIFT_R',
            'OFFSET_ANC_FF_A_DEN_COEFF0_R',
            'OFFSET_ANC_FF_A_DEN_COEFF1_R',
            'OFFSET_ANC_FF_A_DEN_COEFF2_R',
            'OFFSET_ANC_FF_A_DEN_COEFF3_R',
            'OFFSET_ANC_FF_A_DEN_COEFF4_R',
            'OFFSET_ANC_FF_A_DEN_COEFF5_R',
            'OFFSET_ANC_FF_A_DEN_COEFF6_R',
            'OFFSET_ANC_FF_A_DEN_COEFF7_R',
            'OFFSET_ANC_FF_A_NUM_COEFF0_R',
            'OFFSET_ANC_FF_A_NUM_COEFF1_R',
            'OFFSET_ANC_FF_A_NUM_COEFF2_R',
            'OFFSET_ANC_FF_A_NUM_COEFF3_R',
            'OFFSET_ANC_FF_A_NUM_COEFF4_R',
            'OFFSET_ANC_FF_A_NUM_COEFF5_R',
            'OFFSET_ANC_FF_A_NUM_COEFF6_R',
            'OFFSET_ANC_FF_A_NUM_COEFF7_R',
            'OFFSET_ANC_FF_A_NUM_COEFF8_R',
            'OFFSET_ANC_FF_A_GAIN_SCALE_R',
            'OFFSET_ANC_FF_A_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FF_A_GAIN_R',
            'OFFSET_ANC_RX_MIX_FF_A_GAIN_R',
            'OFFSET_ANC_FF_B_DEN_COEFF0_R',
            'OFFSET_ANC_FF_B_DEN_COEFF1_R',
            'OFFSET_ANC_FF_B_DEN_COEFF2_R',
            'OFFSET_ANC_FF_B_DEN_COEFF3_R',
            'OFFSET_ANC_FF_B_DEN_COEFF4_R',
            'OFFSET_ANC_FF_B_DEN_COEFF5_R',
            'OFFSET_ANC_FF_B_DEN_COEFF6_R',
            'OFFSET_ANC_FF_B_DEN_COEFF7_R',
            'OFFSET_ANC_FF_B_NUM_COEFF0_R',
            'OFFSET_ANC_FF_B_NUM_COEFF1_R',
            'OFFSET_ANC_FF_B_NUM_COEFF2_R',
            'OFFSET_ANC_FF_B_NUM_COEFF3_R',
            'OFFSET_ANC_FF_B_NUM_COEFF4_R',
            'OFFSET_ANC_FF_B_NUM_COEFF5_R',
            'OFFSET_ANC_FF_B_NUM_COEFF6_R',
            'OFFSET_ANC_FF_B_NUM_COEFF7_R',
            'OFFSET_ANC_FF_B_NUM_COEFF8_R',
            'OFFSET_ANC_FF_B_GAIN_SCALE_R',
            'OFFSET_ANC_FF_B_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FF_B_GAIN_R',
            'OFFSET_ANC_RX_MIX_FF_B_GAIN_R',
            'OFFSET_ANC_FB_DEN_COEFF0_R',
            'OFFSET_ANC_FB_DEN_COEFF1_R',
            'OFFSET_ANC_FB_DEN_COEFF2_R',
            'OFFSET_ANC_FB_DEN_COEFF3_R',
            'OFFSET_ANC_FB_DEN_COEFF4_R',
            'OFFSET_ANC_FB_DEN_COEFF5_R',
            'OFFSET_ANC_FB_DEN_COEFF6_R',
            'OFFSET_ANC_FB_DEN_COEFF7_R',
            'OFFSET_ANC_FB_NUM_COEFF0_R',
            'OFFSET_ANC_FB_NUM_COEFF1_R',
            'OFFSET_ANC_FB_NUM_COEFF2_R',
            'OFFSET_ANC_FB_NUM_COEFF3_R',
            'OFFSET_ANC_FB_NUM_COEFF4_R',
            'OFFSET_ANC_FB_NUM_COEFF5_R',
            'OFFSET_ANC_FB_NUM_COEFF6_R',
            'OFFSET_ANC_FB_NUM_COEFF7_R',
            'OFFSET_ANC_FB_NUM_COEFF8_R',
            'OFFSET_ANC_FB_GAIN_SCALE_R',
            'OFFSET_ANC_FB_GAIN_SCALE_DEFAULT_R',
            'OFFSET_ANC_FB_GAIN_R',
            'OFFSET_ANC_FF_A_LPF_SHIFT0_R',
            'OFFSET_ANC_FF_A_LPF_SHIFT1_R',
            'OFFSET_ANC_FF_B_LPF_SHIFT0_R',
            'OFFSET_ANC_FF_B_LPF_SHIFT1_R',
            'OFFSET_ANC_FB_LPF_SHIFT0_R',
            'OFFSET_ANC_FB_LPF_SHIFT1_R',
            'OFFSET_FF_A_DCFLT_SHIFT_R',
            'OFFSET_FF_B_DCFLT_SHIFT_R',
            'OFFSET_SM_LPF_SHIFT_R',
            ]