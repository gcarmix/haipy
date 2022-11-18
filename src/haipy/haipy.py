#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import sys
import json
import argparse
from pkg_resources import resource_filename


def help():
    print("haipy v1.0 Hash Identifier Python (derived from haiti)\r\n")
    print("Usage: haipy -h or haipy --help for instructions")

def main():
    if (len(sys.argv) < 2):
        help()
        sys.exit(0)


    parser = argparse.ArgumentParser()
    parser.add_argument("hashcode", help="The hash code to be identified")
    parser.add_argument("--no-color",help="Disable colorized output",action="store_true")
    parser.add_argument("--extended",help="List all possible hash algorithms including ones using salt",action="store_true")
    parser.add_argument("--hashcat-only",help="Show only hashcat references",action="store_true")
    parser.add_argument("--john-only",help="Show only john the ripper references",action="store_true")
    #parser.add_argument("--help",help="Show this help")

    args = parser.parse_args()

    #if args.help:
    #    help()
    if not args.no_color:
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



    with open(resource_filename('haipy','data/prototypes.json'),'rt') as protofile:
        prototypes = json.load(protofile)
        for x in prototypes:
            if re.match(x['regex'],args.hashcode):
                for mode in x['modes']:
                    if(mode['extended'] == False or args.extended ):
                        if(mode['hashcat'] != None and not args.john_only):
                            hashcat_str = bcolors.OKCYAN + "\t\t HC: " + str(mode['hashcat']) + bcolors.ENDC
                        else:
                            hashcat_str = ""
                        if(mode['john'] != None and not args.hashcat_only):
                            john_str = bcolors.OKGREEN + "\t\t JtR: " + str(mode['john']) + bcolors.ENDC
                        else:
                            john_str = ""
                        print(mode['name'] + hashcat_str + john_str)

