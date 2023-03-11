################################################################################
#
#  Copyright (c) 2021-2022 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
################################################################################

Running MultiProgCmd
-----------------------
Run the tool with "-help" to see the usage instructions.

NOTES:
1. It is recommended that a mappings file is used to map device port IDs to the fixed long IDs so that passed / failed
   devices can be easily identified by the physical USB port or TRB adapter connected to each device. See the
   BlueSuite 3.x User Guide for more information regarding transport mapping.
2. It is recommended that the -devmask option is used to specify the mask of devices to be programmed based on the
   number and location of the connected devices. If a device can't be opened, it is recorded as a failure. If -devmask
   is not specified, MultiProgCmd will attempt to program all devices for the matching transport type it finds. This
   means that if a device can't be opened, it will not be recorded as a failure.
