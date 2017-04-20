#!/usr/bin/env python

# file        : tradfri-lights.py
# purpose     : getting status from the Ikea tradfri smart lights
#
# author      : harald van der laan
# date        : 2017/04/10
# version     : v1.1.0
#
# changelog   :
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfri-lights.py - controlling the Ikea tradfri smart lights

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# C0200 -> consider-using-enumerate
# pylint: disable=C0200, C0103

from __future__ import print_function

import sys
import ConfigParser
import argparse

from tradfri import tradfriActions

def parse_args():
    """ function for getting parsed arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['power', 'brightness', 'color'], required=True)
    parser.add_argument('-l', '--lightbulbid', help='lightbulbid got from tradfri-status.py',
                        required=True)
    parser.add_argument('-v', '--value',
                        help='power: on/off, brightness: 0-100, color: warm/normal/cold',
                        required=True)

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
            tradfriActions.tradfri_power_light(hubip, securityid, args.lightbulbid, args.value)
        else:
            sys.stderr.write('[-] Tradfri: power state can only be on/off\n')
            sys.exit(1)
    elif args.action == 'brightness':
        if 1 <= int(args.value) <= 100:
            tradfriActions.tradfri_dim_light(hubip, securityid, args.lightbulbid, args.value)
        else:
            sys.stderr.write('[-] Tradfri: dim value can only be between 1 and 100\n')
            sys.exit(1)
    elif args.action == 'color':
        if args.value == 'warm' or args.value == 'normal' or args.value == 'cold':
            tradfriActions.tradfri_color_light(hubip, securityid, args.lightbulbid, args.value)
        else:
            sys.stderr.write('[-] Tradfri: color value can only be warm/normal/cold\n')
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
