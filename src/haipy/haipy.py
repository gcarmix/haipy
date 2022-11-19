#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
haipy main module
@author: gcarmix

"""
import re
import sys
import json
import argparse
import os
#from pkg_resources import resource_filename
from importlib_resources import files
STR_VERSION = '1.0.3'
commons = [
  "MD5","SHA-1","SHA-256","SHA-512","bcrypt",
  "NTLM","NetNTLMv2","NetNTLMv1-VANILLA / NetNTLMv1+ESS",
  "BLAKE2-512","SHA3-224","SHA3-256","SHA3-512","Keccak-256",
  "Keccak-512","CRC-32B","CRC-32","CRC-16","CRC-64","GOST R 34.11-94",
  "Apache MD5","MD5(APR)","md5apr1","Domain Cached Credentials",
  "Domain Cached Credentials 2","LM","RIPEMD-160","scrypt"
]

def help_text():
    """Shows help"""
    print("haipy v"+ STR_VERSION + " Hash Identifier Python (derived from haiti)\r\n")
    print("Usage: haipy -h or haipy --help for instructions")

def check_common(line):
    """check if hash is between commons"""
    if line['name'] in commons:
        return 1
    return 2

def main():
    """main method"""
    lines = []
    if len(sys.argv) < 2:
        help_text()
        sys.exit(0)


    parser = argparse.ArgumentParser()
    parser.add_argument("hashcode",
                        help="The hash code to be identified")
    parser.add_argument("--no-color",
                        help="Disable colorized output",
                        action="store_true")
    parser.add_argument("--extended",
                        help="List all possible hash algorithms including ones using salt",
                        action="store_true")
    parser.add_argument("--hashcat-only",
                        help="Show only hashcat references",
                        action="store_true")
    parser.add_argument("--john-only",
                        help="Show only john the ripper references",
                        action="store_true")
    parser.add_argument("--samples",
                        help="show samples for given hash type e.g. (haipy --samples MD5)",
                        action="store_true")



    args = parser.parse_args()


    if not args.no_color and os.name != 'nt':
        colcyan = '\033[96m'
        colgreen = '\033[92m'
        colend = '\033[0m'
    else:
        colcyan = ''
        colgreen = ''
        colend = ''




    with open(files('haipy.data').joinpath('prototypes.json'),'rt',encoding='utf-8') as protofile:
        prototypes = json.load(protofile)
        if args.samples:
            for proto in prototypes:
                for mode in proto['modes']:
                    if mode['name'] == args.hashcode.upper():
                        for sample in mode['samples']:
                            print(sample)
                        return
        else:
            for proto in prototypes:
                if re.match(proto['regex'],args.hashcode):
                    for mode in proto['modes']:
                        if mode['extended'] is False or args.extended:
                            if mode['hashcat'] is not None and not args.john_only :
                                hashcat_str = colcyan + " [HC: " + str(mode['hashcat']) + "]" + colend
                            else:
                                hashcat_str = ""
                            if mode['john'] is not None and not args.hashcat_only :
                                john_str = colgreen + "[JtR: " + str(mode['john']) + "]" + colend
                            else:
                                john_str = ""

                            lines.append({
                              'name':mode['name'],
                              'string': mode['name'] + hashcat_str + john_str})
            lines.sort(key=check_common)
            for line in lines:
                print(line['string'])
