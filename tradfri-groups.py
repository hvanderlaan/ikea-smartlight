#!/usr/bin/env python

# file        : tradfri-groups.py
# purpose     : controlling status from the Ikea tradfri smart groups
#
# author      : harald van der laan
# date        : 2017/04/10
# version     : v1.1.0
#
# changelog   :
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfri-groupss.py - controlling the Ikea tradfri smart groups

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

from __future__ import print_function

import sys
import ConfigParser
import argparse

from tradfri import tradfriActions

def parse_args():
    """ function for getting parsed arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['power', 'brightness', 'color'], required=Ture)
    parser.add_argument('-g', '--groupid', help='groupid got from tradfri-status.py',
                        required=True)
    parser.add_argument('-v', '--value',
                        help='power: on/off, brightness', required=True)

    args = parser.parse_args()

    return args

def main():
    """ main function """
    args = parse_args()
    conf = ConfigParser.ConfigParser()
    conf.read('tradfri.cfg')

    hubip = conf.get('tradfri', 'hubip')
    securityid = conf.get('tradfri', 'securityid')

    if args.action == 'power':
        if args.value == 'on' or args.value == 'off':
            tradfriActions.tradfri_power_group(hubip, securityid, args.groupid, args.value)
        else:
            sys.stderr.write('[-] tradfri: power state can only be on/off\n')
            sys.exit(1)
    elif args.action == 'brightness':
        if 1 <= argv.value <= 100:
            tradfriActions.tradfri_dim_group(hubip, securityid, args.groupid, args.value)
        else:
            sys.stderr.write('[-] tradfri: dim value can only be obetween 1 - 100\n')
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)