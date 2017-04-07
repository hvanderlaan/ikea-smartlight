#!/usr/bin/env python

# file        : smartlight.py
# purpose     : control ikea tradfri smart light
#
# author      : harald van der laan
# date        : 2017/04/06
# version     : v1.0.0
#
# requirements:
# - libcoap
#
# changelog   :
# - v1.0.0      initial release                                         (harald)

""" smartlight - python framework for the tradfri ikea smart light hub
    this frame works requires libcoap with dtls compiled, more info is found
    in the bin directory. there is also a build script.

    libcoap requires cunit, a2x and doxygen """

from __future__ import print_function

import sys
import ConfigParser

from tradfri import tradfri

def main():
    """ main function """
    conf = ConfigParser.ConfigParser()
    conf.read('tradfri.cfg')
    hubip = conf.get('tradfri', 'hubip')
    securityid = conf.get('tradfri', 'securityid')
    lightbulb = []
    lightgroup = []

    print('[ ] smartlight: receiving tradfri lightbulbs information')
    devices = tradfri.get_tradfri_devices(hubip, securityid)
    groups = tradfri.get_tradfri_groups(hubip, securityid)

    for deviceid in range(len(devices)):
        lightbulb.append(tradfri.get_tradfri_lightbulb(hubip, securityid, str(devices[deviceid])))

    for groupid in range(len(groups)):
        lightgroup.append(tradfri.get_tradfri_group_status(hubip, securityid, str(groups[groupid])))

    print('[+] smartlight: done getting tradfri lightbulbs information')
    print('===========================================================\n')

    for counter in range(len(lightbulb)):
        try:
            if lightbulb[counter]["3311"][0]["5850"] == 0:
                # lightbulb is off
                print('bulbid: {}, name: {}, state: off' .format(counter,
                                                                 lightbulb[counter]["9001"]))
            else:
                # lightbulb is on
                print('bulbid: {}, name: {}, state: on' .format(counter,
                                                                lightbulb[counter]["9001"]))
        except KeyError:
            # not a lightbulb but a controler
            pass

    print()

    for counter in range(len(lightgroup)):
        try:
            if lightgroup[counter]["5850"] == 0:
                print('groupid: {}, name: {}, state off' .format(counter,
                                                                 lightgroup[counter]["9001"]))
            else:
                print('groupid: {}, name: {}, state on' .format(counter,
                                                                lightgroup[counter]["9001"]))
        except KeyError:
            pass

if __name__ == "__main__":
    main()
    sys.exit(0)
