#!C:\qtil\ADK_Toolkit_1.2.15.35_x64\tools\pyenv37\Scripts\python.exe
'''
=============================================================================
 Copyright (c) 2022 Qualcomm Technologies International, Ltd.
 All Rights Reserved.
 Qualcomm Technologies International, Ltd. Confidential and Proprietary.
============================================================================= 
'''
import os
import ntpath
import platform
import sys
import argparse
import subprocess
import shutil
import datetime
import wave

#Some defines
WIN_PATH           = "\\"
LINUX_PATH         = "/"
DEFAULT_OUTPUT_DIR = "C:\\Temp\\aptx\\output"
DEFAULT_LOG        = "log.txt"
APTX_BT_FILE_EXT   = ".btaptx"
APTX_FILE_EXT      = ".aptx"
WAV_EXT            = ".wav"
PCM_EXT            = ".pcm"

VALID_FS           = [ 16000, 32000, 44100, 48000, 88200, 96000, 192000 ]

#Executable names
ANALYZECOMPRESSED = "AnalyzeCompressed.exe"
APTXDECREF        = "AptxDecRef.exe"
DEINTERLEAVER     = "Deinterleaver.exe"
APTXHDDECREF      = "aptX-HD-DecRef.exe"
APTXPACKETHEADER  = "aptx-adaptive-packet-header-strip_NEW_BYTE_SWAP.exe"
APTXADV2          = "test-decoder.exe"
APTXVOICE         = "test-decoder-voice.exe"
APTXADV3          = "ax3-test-decoder.exe"
SLIMBUS2APTX      = "slimbus2aptx-adaptive3.exe"

#Errors
"""
System Errors
ERR_SYS_01 - Something about the host system is not supported
ERR_SYS_02 - File read/write/access error

Decoding Errors
ERR_DEC_01 - Processing output file not found 
"""

def write_wav( infile, outfile, config ):
    try:
        wavefile = wave.open( outfile, mode="wb" )
    except OSError:
        config[ "log" ].write( "\tERR_SYS_02: Could not open %s for writing\n" % (outfile) )
        return 1
        
    try:
        config[ "log" ].write( "\tOpening input file %s\n" % (infile) )
        pcmfile = open( infile, 'rb' )
    except OSError:
        config[ "log" ].write( "\tERR_DEC_01: Could not find input file %s\n" % (infile) )
        return 1
    
    config[ "log" ].write( "\tCreating WAV file %s. Channels: %d, Bit Depth: %d, FS: %d\n" % (outfile,config[ "channels" ],config[ "samp_width" ],config[ "fs" ]) )
    
    wavefile.setnchannels( int(config[ "channels" ]) )
    wavefile.setsampwidth( int(config[ "samp_width" ]) )
    wavefile.setframerate( int(config[ "fs" ]) )
    
    while True:
        pcm = pcmfile.read( 1000 * int(config[ "samp_width" ]) )
        wavefile.writeframes( pcm )
        if( len( pcm ) < ( 1000 * int(config[ "samp_width" ])) ):
            break

        
    wavefile.close()
    pcmfile.close()
    

def decode_aptx_adaptive_v2_2( config ):
    print( "Processing aptX Adaptive v2.2..." )
    config[ "log" ].write( "Running decode_aptx_adaptive_v2_2\n" )
    #Verify the out_dir exists
    if( not os.path.exists( config[ "outdir" ] ) ):
        config[ "log" ].write( "ERR_SYS_02: decode_aptx_adaptive_v2_2 - output directory %s not found\n" % ( config[ "outdir" ] ) )
        return 1
        
    #Create a list of files to decode
    files = []
    
    if( config[ "is_dir" ] ):
        #Get the list of files from the directory
        filtered_files = []
        dir_files = os.listdir( config[ "inpath" ] )
        for f in dir_files:
            if( f.lower().endswith( ".bin" ) ):
                filtered_files.append( config["inpath"] + "/" + f )
            
        files = filtered_files
    else:
        files.append( config[ "inpath" ] )
        
    config[ "log" ].write( "Found %d file(s):\n" % (len(files) ))
        
    for orig_file in files:
        config[ "log" ].write( "Processing input file %s\n" % (orig_file) )
        #Get the file name
        basename = os.path.basename( orig_file )
        #Copy the original file to the output location
        safe_file = config[ "outdir" ] + config[ "path_sep" ] + basename
        config[ "log" ].write( "\tCopying %s to %s\n" % (orig_file, safe_file) )
        shutil.copyfile( orig_file, safe_file, follow_symlinks=True )
              
        #Run Analyze compressed tool
        print( "Running AnalyzeCompressed..." )
        cmd = [ os.path.join(config["exe_path"], ANALYZECOMPRESSED), safe_file ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #The output file from the previous command outputs a .raw regardless
        ac_name = safe_file + ".raw"
        #Check if file exists
        if( not os.path.exists( ac_name ) ):
            config[ "log" ].write( "\tERR_DEC_01: decode_aptx_adaptive_v2_2 - Expected to find %s after running AnalyzeCompressed" % (ac_name) )
            #This could be a one-off error, so continue the loop
            continue
            
        #Run the slimbus tool
        print( "Stripping Slimbus Packet Header..." ) 
        #Lots of -v options are valid for increased verbosity of output
        cmd = [os.path.join(config["exe_path"],SLIMBUS2APTX), "-v", "-v", "-v", "-v", "-r", str(config[ "fs" ]), "--outdir", config[ "outdir" ], ac_name]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #Strip off the .raw ending and get add a -left.aptx3 and -right.aptx3
        sb_name_left  = safe_file + "-left.aptx3"
        sb_name_right = safe_file + "-right.aptx3"
        out_left      = safe_file + "-left" + WAV_EXT
        out_right     = safe_file + "-right" + WAV_EXT
        if( os.path.exists( sb_name_left ) ):
            print( "Running aptX Adaptive v2.2 for left channel..." )
            cmd = [os.path.join(config["exe_path"],APTXADV3 ), "-i", sb_name_left, "-o", out_left ]
            config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
            process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            process.communicate()
            process.wait()
        else:
            config[ "log" ].write( "\tERR_DEC_01: Could not find %s\n" % (sb_name_left) )
            
        if( os.path.exists( sb_name_right ) ):
            print( "Running aptX Adaptive v2.2 for right channel..." )
            cmd = [os.path.join(config["exe_path"],APTXADV3), "-i", sb_name_right, "-o", out_right ]
            config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
            process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            process.communicate()
            process.wait()
        else:
            config[ "log" ].write( "\tERR_DEC_01: Could not find %s\n" % (sb_name_right) )
            
        
        return 0


def decode_aptx_adaptive_v2_1( config ):
    print( "Processing aptX Adaptive v2.1..." )
    config[ "log" ].write( "Running decode_aptx_adaptive_v2_1\n" )
    #Verify the out_dir exists
    if( not os.path.exists( config[ "outdir" ] ) ):
        config[ "log" ].write( "ERR_SYS_02: decode_aptx_adaptive_v2_1 - output directory %s not found" % ( config[ "outdir" ] ) )
        return 1
        
    #Create a list of files to decode
    files = []
    
    if( config[ "is_dir" ] ):
        #Get the list of files from the directory
        filtered_files = []
        dir_files = os.listdir( config[ "inpath" ] )
        for f in dir_files:
            if( f.lower().endswith( ".bin" ) ):
                filtered_files.append( config["inpath"] + "/" + f )
            
        files = filtered_files
    else:
        #Add the single file to the list
        files.append( config[ "inpath" ] )
        
    config[ "log" ].write( "Found %d file(s):\n" % (len(files) ))

    for orig_file in files:
        config[ "log" ].write( "Processing input file %s\n" % (orig_file) )
        #Get the file name
        basename = os.path.basename( orig_file )
        #Copy the original file to the output location
        safe_file = config[ "outdir" ] + config[ "path_sep" ] + basename
        config[ "log" ].write( "\tCopying %s to %s\n" % (orig_file, safe_file) )
        shutil.copyfile( orig_file, safe_file, follow_symlinks=True )
        
        #Run Analyze compressed tool
        print( "Running AnalyzeCopressed..." )
        cmd = [ os.path.join(config["exe_path"],ANALYZECOMPRESSED), safe_file ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #The output file from the previous command outputs a .raw regardless
        ac_name = safe_file + ".raw"
        #Check if file exists
        if( not os.path.exists( ac_name ) ):
            config[ "log" ].write( "\tERR_DEC_01: decode_aptx_adaptive_v2_1 - Expected to find %s after running AnalyzeCompressed\n" % (ac_name) )
            #This could be a one-off error, so continue the loop
            continue
            
        #Run the packet header strip tool   
        print( "Stripping Packet Header..." )
        cmd = [ os.path.join(config["exe_path"],APTXPACKETHEADER), "-e", "-b", "8", ac_name, "-d", config[ "outdir" ] ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #Get the name of the output file from the Packet header tool 
        ac_name_list = ac_name.split( ".raw" )
        ph_name = ac_name_list[ 0 ] + "-clean.raw" 
        
        
        #Rename the file to the appropriate extension
        ph_basename = os.path.basename( ph_name )
        ph_basename_parts = ph_basename.split( "." )
        ph_base = ph_basename_parts[ 0 ]
        aptx_file = config[ "outdir" ] + config[ "path_sep" ] + ph_base + APTX_FILE_EXT
        config[ "log" ].write( "\tMoving %s to %s\n" % (ph_name, aptx_file) )
        shutil.move( ph_name, aptx_file )
 
        #Run the aptX Adaptive reference decoder
        print( "Running aptX Adaptive v2.1 decoder..." )
        infile  = aptx_file
        #outfile = aptx_file.split( "." )
        #outfile = outfile[ 0 ] + WAV_EXT   
        outfile = safe_file + WAV_EXT
        cmd = [ os.path.join(config["exe_path"],APTXADV2), "-i", infile, "-o", outfile ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
    return 0
    
def decode_aptx_voice( config ):
    print( "Processing aptX Voice..." )
    config[ "log" ].write( "Running decode_aptx_voice\n" )
    #Verify output directory exists
    if( not os.path.exists( config[ "outdir" ] ) ):
        config[ "log" ].write( "ERR_SYS_02: decode_aptx_voice - output directory %s not found\n" % ( config[ "outdir" ] ) )
        return 1
        
    #Create a list of files to decode
    files = []
    
    if( config[ "is_dir" ] ):
        #Get the list of files from the directory
        filtered_files = []
        dir_files = os.listdir( config[ "inpath" ] )
        for f in dir_files:
            if( f.lower().endswith( ".bin" ) ):
                filtered_files.append( config["inpath"] + "/" + f )
            
        files = filtered_files
    else:
        #Add the single file to the list
        files.append( config[ "inpath" ] )
        
    config[ "log" ].write( "Found %d file(s):\n" % (len(files) ))
    
    for orig_file in files:
        config[ "log" ].write( "Processing input file %s\n" % (orig_file) )
        #Get the file name
        basename = os.path.basename( orig_file )
        #Copy the original file to the output location
        safe_file = config[ "outdir" ] + config[ "path_sep" ] + basename
        config[ "log" ].write( "\tCopying %s to %s\n" % (orig_file, safe_file) )
        shutil.copyfile( orig_file, safe_file, follow_symlinks=True )
        
        print( "Running AnalyzeCopressed..." )
        cmd = [ os.path.join(config["exe_path"],ANALYZECOMPRESSED), safe_file ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #The output file from the previous command outputs a .raw regardless
        ac_name = safe_file + ".raw"
        #Check if file exists
        if( not os.path.exists( ac_name ) ):
            config[ "log" ].write( "\tERR_DEC_01: decode_aptx_voice - Expected to find %s after running AnalyzeCompressed\n" % (ac_name) )
            #This could be a one-off error, so continue the loop
            continue
            
        #Rename the file to the appropriate extension
        ph_basename = os.path.basename( ac_name )
        ph_basename_parts = ph_basename.split( "." )
        ph_base = ph_basename_parts[ 0 ]
        aptx_file = config[ "outdir" ] + config[ "path_sep" ] + ph_base + APTX_FILE_EXT
        config[ "log" ].write( "\tMoving %s to %s\n" % (ac_name, aptx_file) )
        shutil.move( ac_name, aptx_file )
        
        #Run the aptx voice reference decoder 
        print( "Running aptX Voice Decoder..." )
        infile  = aptx_file   
        outfile = safe_file + WAV_EXT
        cmd = [ os.path.join(config["exe_path"],APTXVOICE), "-i", infile, "-o", outfile, "-x", "sp0", "-y" ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
    return 0
    

def decode_aptx_hd( config ):
    print( "Processing aptX HD..." )
    config[ "log" ].write( "Running decode_aptx_hd\n" )
    #Verify the out_dir exists
    if( not os.path.exists( config[ "outdir" ] ) ):
        config[ "log" ].write( "ERR_SYS_02: decode_aptx_hd - output directory %s not found\n" % ( config[ "outdir" ] ) )
        return 1
    
    #Create a list of files to decode
    files = []
    
    if( config[ "is_dir" ] ):
        #Get the list of files from the directory
        filtered_files = []
        dir_files = os.listdir( config[ "inpath" ] )
        for f in dir_files:
            if( f.lower().endswith( ".bin" ) ):
                filtered_files.append( config["inpath"] + "/" + f )
            
        files = filtered_files
    else:
        #Add the single file to the list
        files.append( config[ "inpath" ] ) 
        
    config[ "log" ].write( "Found %d file(s):\n" % (len(files) ))

    for orig_file in files:
        config[ "log" ].write( "Processing input file %s\n" % (orig_file) )
        #Get the file name
        basename = os.path.basename( orig_file )
        #Copy the original file to the output location
        safe_file = config[ "outdir" ] + config[ "path_sep" ] + basename
        config[ "log" ].write( "\tCopying %s to %s\n" % (orig_file, safe_file) )
        shutil.copyfile( orig_file, safe_file, follow_symlinks=True )
        
        print( "Running AnalyzeCopressed..." )
        cmd = [ os.path.join(config["exe_path"],ANALYZECOMPRESSED), safe_file ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #The output file from the previous command outputs a .raw regardless
        ac_name = safe_file + ".raw"
        #Check if file exists
        if( not os.path.exists( ac_name ) ):
            config[ "log" ].write( "\tERR_DEC_01: decode_aptx_hd - Expected to find %s after running AnalyzeCompressed\n" % (ac_name) )
            #This could be a one-off error, so continue the loop
            continue
        
        #Rename the file to the appropriate extension
        ac_basename = os.path.basename( ac_name )
        ac_basename_parts = ac_basename.split( "." )
        ac_base = ac_basename_parts[ 0 ]
        dst = config[ "outdir" ] + config[ "path_sep" ] + ac_base + APTX_BT_FILE_EXT
        config[ "log" ].write( "\tMoving %s to %s\n" % (ac_name, dst) )
        shutil.move( ac_name, dst )
 
        #Run the aptx HD reference decoder 
        print( "Running aptX HD Decoder..." )
        cmd = [ os.path.join(config["exe_path"],APTXHDDECREF), ac_base, config[ "outdir" ], config[ "outdir" ] ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #Create the wav file
        print( "Creating WAV file..." )
        output_wav = safe_file + WAV_EXT
        input_raw = config[ "outdir" ] + config[ "path_sep" ] + ac_base + "_btaptx" + PCM_EXT
        write_wav( input_raw, output_wav, config )
        
    return 0
    
def decode_aptx_classic( config ):
    print( "Processing aptX Classic..." )
    config[ "log" ].write( "Running decode_aptx_classic\n" )
    #Verify the out_dir exists
    if( not os.path.exists( config[ "outdir" ] ) ):
        config[ "log" ].write( "ERR_SYS_02: decode_aptx_classic - output directory %s not found\n" % ( config[ "outdir" ] ) )
        return 1
    
    #Create a list of files to decode
    files = []
    
    if( config[ "is_dir" ] ):
        #Get the list of files from the directory
        filtered_files = []
        dir_files = os.listdir( config[ "inpath" ] )
        for f in dir_files:
            if( f.lower().endswith( ".bin" ) ):
                filtered_files.append( config["inpath"] + "/" + f )
            
        files = filtered_files
    else:
        #Add the single file to the list
        files.append( config[ "inpath" ] )
        
    config[ "log" ].write( "Found %d file(s):\n" % (len(files) ))
    
    for orig_file in files:
        config[ "log" ].write( "Processing input file %s\n" % (orig_file) )
        #Get the file name
        basename = os.path.basename( orig_file )
        #Copy the original file to the output location
        safe_file = config[ "outdir" ] + config[ "path_sep" ] + basename
        config[ "log" ].write( "\tCopying %s to %s\n" % (orig_file, safe_file) )
        shutil.copyfile( orig_file, safe_file, follow_symlinks=True )
        #Run AnalyzeCompressed tool
        print( "Running AnalyzeCopressed..." )
        cmd = [ os.path.join( config[ "exe_path"], ANALYZECOMPRESSED ), safe_file ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
              
        #The output file from the previous command outputs a .raw regardless
        ac_name = safe_file + ".raw"
        #Check if file exists
        if( not os.path.exists( ac_name ) ):
            config[ "log" ].write( "\tError: decode_aptx_classic - Expected to find %s after running AnalyzeCompressed\n" % (ac_name) )
            #This could be a one-off error, so continue the loop
            continue
        
        #Rename the file to the appropriate extension
        ac_basename = os.path.basename( ac_name )
        ac_basename_parts = ac_basename.split( "." )
        ac_base = ac_basename_parts[ 0 ]
        dst = config[ "outdir" ] + config[ "path_sep" ] + ac_base + APTX_BT_FILE_EXT
        config[ "log" ].write( "\tMoving %s to %s\n" % (ac_name, dst) )
        shutil.move( ac_name, dst )
 
        #Run the aptx reference decoder 
        print( "Running aptX Classic Decoder..." )
        cmd = [ os.path.join( config[ "exe_path"], APTXDECREF ), ac_base, config[ "outdir" ], config[ "outdir" ], "BE" ]
        config[ "log" ].write( "\tRunning command: %s\n" % (cmd) )
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        process.communicate()
        process.wait()
        
        #Create the wav file
        print( "Creating WAV file..." )
        output_wav = safe_file + WAV_EXT
        input_raw = config[ "outdir" ] + config[ "path_sep" ] + ac_base + "_btaptx" + PCM_EXT
        write_wav( input_raw, output_wav, config )
            
    return 0




def main():
    print( "=============================================================================" )
    print( "Snapdragon Sound aptX Adaptive Codec Decoder tool (C) QTIL 2022" )
    print( "=============================================================================" )
    #Check for python version info
    version = sys.version_info[ 0 ] 
    if( version != 3 ):
        print( "ERR_SYS_01: This script must be run with Python version 3.x. Exiting." )
        return 1 
        
    #Check for Windows version
    if( platform.system() != "Windows" ):
        print( "ERR_SYS_01: Due to restrictions of some executables, only Windows is supported at this time. Exiting." )
        return 1

    parser = argparse.ArgumentParser(description="Decodes aptX streams offline", 
             formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument( "--infile", dest="infile", help="A single input file to decode.", default=None )
    parser.add_argument( "--indir", dest="indir", help="A directory location with one or more files to decode.", default=None )
    parser.add_argument( "--outdir", dest="outdir", help="A directory to write the output files. If not specified, the default is C:\\Temp\\aptx\\output_<datetime>. If you specify a directory that already exists, it will be overwritten.", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument( "--config", dest="config", help="Required to define the input decode stream(s):\n1 - aptX Classic\n2 - aptX HD\n3 - aptX Adaptive R1 & R2.1\n4 - aptX Adaptive R2.2\n5 - aptX Voice", default=None )
    parser.add_argument( "--fs", dest="sampling_freq", help="Defines the expected output sampling frequency (Default: 48000)", default=int(48000))
    args = parser.parse_args()
        
    #########################################
    # Create a config dictionary to pass to the processing functions
    config = {
       "inpath"    : None,        #The input file or input directory (required)
       "is_dir"    : False,       #Set to True if inpath is a directory (required)
       "outdir"    : None,        #The output directory (required)
       "path_sep"  : WIN_PATH,    #Path separator for building paths (required)
       "fs"        : 48000,       #The target sampling frequency (used by some functions)
       "samp_width": 2,           #Number of bytes per PCM of the expected audio output
       "channels"  : 2,           #Number of channels of the expected audio output
       "log"       : None,        #The reference to log file
       "exe_path"  : None         #The path to the exe files
    } 
    
    #########################################
    # Sanity checks
    #Verify the user used the indir and infile correctly
    if( args.indir is None and args.infile is None ):
        print( "Error: Either --indir or --infile is required. Exiting." )
        return 1
        
    if( args.indir is not None and args.infile is not None ):
        print( "Error: Use either --indir or --infile, not both. Exiting." )
        return 1
        
    #Verify the input file/path exists    
    if( args.infile is not None ):    
        #Detect that file/directory exists
        if( not os.path.exists( args.infile ) ):
            print( "Error: Path %s is not accessable or does not exist. Exiting." % (args.infile) )
            return 1
            
        #Set the config 
        config[ "inpath" ] = args.infile 
            
    if( args.indir is not None ):    
        #Detect that file/directory exists
        if( not os.path.exists( args.indir ) ):
            print( "Error: Path %s is not accessable or does not exist. Exiting." % (args.indir) )
            return 1
            
        #Set the config 
        config[ "inpath" ] = args.indir 
        config[ "is_dir" ] = True
    
    #Check to ensure the fs entry is valid    
    if( type( args.sampling_freq )is not int ):
        print( "Error: The value %s is not a valid sampling frequency for argument --fs. Exiting." % ( args.sampling_freq ) )
        return 1
        
    fs = int( args.sampling_freq )
    fs_is_valid = False 
    for freq in VALID_FS:
        if( fs == freq ):
            fs_is_valid = True 
            
    if( not fs_is_valid ):
        print( "Error: The value %d is not a supported sampling frequency. Exiting." % (fs) )
        return 1
        
    #Assing the config fs
    config[ "fs" ] = fs        
    
    #########################################
    # Handle output directory creation
    outdir = args.outdir
    cwd    = os.getcwd()
    #This is the default case
    if( outdir is DEFAULT_OUTPUT_DIR ):
        #Create an output directory that is based on the current timestamp
        #so multiple runs can be made 
        mytime = datetime.datetime.now()
        outdir = DEFAULT_OUTPUT_DIR + "_" + mytime.strftime( "%Y_%m_%d_%H_%M_%S" )
        if( os.path.exists( outdir ) ):
            print( "Error: Attempted to create an output directory %s, but it already exists."
                   "Exiting" % (outdir) )
            return 1
        #Create the output directory
        os.makedirs( outdir, mode=0o777 )
    else:
        #Check that the output directory exists and issue a warning if it does
        if( os.path.exists( outdir ) ):
            print( "Warning: Output directory %s already exists. Existing data may be overwritten." % (outdir) )
        else:
            print( "Info: Creating output directory %s." % (outdir) )
            os.makedirs( outdir, mode=0o777 )
    
    #Set the config's output directory 
    config[ "outdir" ] = outdir
        
    ret_val = 0
    if( args.config is None ):
        print( "Error: A configuration (--config) is required. Exiting." )
        return 1 
    
    config_id = None    
    try:
        config_id = int( args.config ) 
    except:
        print( "Error: Unrecognised configuration '%s'. Exiting." % (args.config) )
        return 1
        
    #Set the log file at the end of the sanity check
    log_file = config[ "outdir" ] + config[ "path_sep" ] + DEFAULT_LOG
    try:    
        mytime = datetime.datetime.now()
        f = open( log_file, "w" )
        config[ "log" ] = f
        f.write( "Opened log file %s at %s\n" % (log_file, mytime.strftime( "%Y_%m_%d_%H_%M_%S" )))
        f.write( "Command line args: %s\n" % (args) )        
    except OSError:
        print( "Error: Could not open log file %s. Exiting." % (log_file) )
        return 1
        
    #Setup the exe file path
    script_path = os.path.realpath( __file__ )
    config[ "log" ].write( "aptXOfflineDecoder script path: %s\n" % ( script_path ) )
    #head is the directory that contains this script 
    head, tail = ntpath.split( script_path )
    #head is the parent directory (i.e. offline_decoder)
    head, tail = ntpath.split( head )
    #Construct the exe directory path 
    exe_path = os.path.join( head, "exes" )
    config[ "exe_path" ] = exe_path
    config[ "log" ].write( "Setting exe path to %s\n" % (exe_path) )
    
    if not os.path.exists( os.path.join(config["exe_path"],ANALYZECOMPRESSED) ) :
        print( "Error: Unable to find %s in %s." % (ANALYZECOMPRESSED,config["exe_path"]) )
        print( "If this is your first time using this tool, please see the user guide or contact your QCOM representaive on how to obtain %s" %
               (ANALYZECOMPRESSED) ) 
        config[ "log" ].write( "SYS_ERR_02: Unable to find required executable [%s]. Exe directory: %s" % (ANALYZECOMPRESSED,config["exe_path"]) )               
        return 1               
        
    #########################################
    # Run the configuration
    if( config_id == 1 ):
        #Detect that the executables exist
        if( os.path.exists( os.path.join(config["exe_path"],ANALYZECOMPRESSED) ) and os.path.exists( os.path.join(config["exe_path"],APTXDECREF) )):
            #Run the aptX classic decoder
            config[ "samp_width" ] = 2
            ret_val = decode_aptx_classic( config )
        else:
            config[ "log" ].write( "SYS_ERR_02: Unable to find required executables [%s,%s]. Exe directory: %s\n" % (ANALYZECOMPRESSED,APTXDECREF,config["exe_path"]) )
            ret_val = 1
    elif( config_id == 2 ):
        if( os.path.exists( os.path.join( config[ "exe_path"], ANALYZECOMPRESSED ) ) and os.path.exists( os.path.join( config[ "exe_path"], APTXHDDECREF ) ) ):
            #Run the aptX HD decoder
            config[ "samp_width" ] = 4
            ret_val = decode_aptx_hd( config )
        else:
            config[ "log" ].write( "SYS_ERR_02: Unable to find required executables [%s,%s,%s]. Exe directory: %s" % (ANALYZECOMPRESSED,APTXHDDECREF,config["exe_path"]) )
            ret_val = 1
    elif( config_id == 3 ):
        if( os.path.exists( os.path.join( config[ "exe_path"], ANALYZECOMPRESSED ) ) and os.path.exists( os.path.join( config[ "exe_path"], APTXPACKETHEADER ) ) and 
            os.path.exists( os.path.join( config[ "exe_path" ], APTXADV2 ) ) ):
            #Run the aptX R2.1 decoder
            config[ "samp_width" ] = 3
            ret_val = decode_aptx_adaptive_v2_1( config )
        else:
            config[ "log" ].write( "SYS_ERR_02: Unable to find required executables [%s,%s,%s,%s]. Exe directory: %s" % (ANALYZECOMPRESSED,APTXPACKETHEADER,APTXADV2,config["exe_path"]) )
            ret_val = 1
    elif( config_id == 4 ):
        if( os.path.exists( os.path.join( config[ "exe_path"], ANALYZECOMPRESSED ) ) and os.path.exists( os.path.join( config[ "exe_path"], APTXADV3 ) ) and 
            os.path.exists( os.path.join( config[ "exe_path"], SLIMBUS2APTX ) ) ):
            #Run the aptX R2.2 decoder
            config[ "samp_width" ] = 3
            ret_val = decode_aptx_adaptive_v2_2( config )
        else:
            config[ "log" ].write( "SYS_ERR_02: Unable to find required executables [%s,%s,%s,%s]. Exe directory: %s" % (ANALYZECOMPRESSED,APTXADV3,SLIMBUS2APTX,config["exe_path"]) )
            ret_val = 1
    elif( config_id == 5 ):
        if( os.path.exists( os.path.join( config[ "exe_path"], ANALYZECOMPRESSED ) ) and os.path.exists( os.path.join( config[ "exe_path"], APTXVOICE ) ) ):
            #Run the aptX Voice decoder
            config[ "samp_width"] = 3
            #If the fs is not set, set it to 32 kHz by default
            if( fs_is_valid == False ):
                config[ "fs" ] = 32000
            ret_val = decode_aptx_voice( config )
        else:
            config[ "log" ].write( "SYS_ERR_02: Unable to find required executables [%s,%s]. Exe directory: %s" % (ANALYZECOMPRESSED,APTXVOICE,config["exe_path"]) )
            ret_val = 1
    else:
        print( "Error: Unrecognised config %s. Exiting." % (args.config) )
        return 1
    
    if( ret_val != 0 ):
        print( "Offline decoded finished with errors. See log at %s" % (log_file) )
        return ret_val 
    else:
        print( "Offline decoding complete." )
        return ret_val

if __name__ == "__main__":
    sys.exit( main() )


