#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import sys
import json
import argparse
import os
#from pkg_resources import resource_filename
from importlib_resources import files
STR_VERSION = '1.0.2'
commons = [
  "MD5","SHA-1","SHA-256","SHA-512","bcrypt","NTLM","NetNTLMv2","NetNTLMv1-VANILLA / NetNTLMv1+ESS","BLAKE2-512","SHA3-224","SHA3-256","SHA3-512","Keccak-256","Keccak-512","CRC-32B","CRC-32","CRC-16","CRC-64","GOST R 34.11-94","Apache MD5","MD5(APR)","md5apr1","Domain Cached Credentials","Domain Cached Credentials 2","LM","RIPEMD-160","scrypt"
]

def help():
    print("haipy v"+ STR_VERSION + "Hash Identifier Python (derived from haiti)\r\n")
    print("Usage: haipy -h or haipy --help for instructions")

def check_common(line):
    if(line['name'] in commons):
        return 1
    else:
        return 2

def main():
    lines = []
    if (len(sys.argv) < 2):
        help()
        sys.exit(0)


    parser = argparse.ArgumentParser()
    parser.add_argument("hashcode", help="The hash code to be identified")
    parser.add_argument("--no-color",help="Disable colorized output",action="store_true")
    parser.add_argument("--extended",help="List all possible hash algorithms including ones using salt",action="store_true")
    parser.add_argument("--hashcat-only",help="Show only hashcat references",action="store_true")
    parser.add_argument("--john-only",help="Show only john the ripper references",action="store_true")
    parser.add_argument("--samples",help="show samples for given hash type e.g. (haipy --samples MD5)",action="store_true")



    args = parser.parse_args()


    if not args.no_color and os.name != 'nt':
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
    else:
        class bcolors:
            HEADER = ''
            OKBLUE = ''
            OKCYAN = ''
            OKGREEN = ''
            WARNING = ''
            ENDC = ''
            BOLD = ''
            UNDERLINE = ''



    with open(files('haipy.data').joinpath('prototypes.json'),'rt') as protofile:
        prototypes = json.load(protofile)
        if(args.samples):
            for x in prototypes:
                for mode in x['modes']:
                    if(mode['name'] == args.hashcode.upper()):
                        for sample in mode['samples']:
                            print(sample)
                        return
        else:
            for x in prototypes:
                if re.match(x['regex'],args.hashcode):
                    for mode in x['modes']:
                        if(mode['extended'] == False or args.extended ):
                            if(mode['hashcat'] != None and not args.john_only):
                                hashcat_str = bcolors.OKCYAN + " [HC: " + str(mode['hashcat']) + "]" +  bcolors.ENDC
                            else:
                                hashcat_str = ""
                            if(mode['john'] != None and not args.hashcat_only):
                                john_str = bcolors.OKGREEN + "[JtR: " + str(mode['john']) + "]" + bcolors.ENDC
                            else:
                                john_str = ""
    
                            lines.append({'name':mode['name'],'string': mode['name'] + hashcat_str + john_str})
            lines.sort(key=check_common)
            for line in lines:
                print(line['string'])


