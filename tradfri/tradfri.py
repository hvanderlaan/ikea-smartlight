#!/usr/bin/env python

# file        : tradfri/tradfri.py.py
# purpose     : function file for controlling tradfri lightbulbs
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

import sys
import os
import json

def get_tradfri_devices(hubip, securityid):
    """ function for getting all paired devices to the hub """
    hub = 'coaps://{}:5684/15001' .format(hubip)
    apicall = 'bin/coap-client -m get -u "Client_identity" -k "{}" "{}" | awk \'NR==4\'' .format(securityid, hub)

    if os.path.exists('bin/coap-client'):
        result = os.popen(apicall)
    else:
        sys.stderr.write('[-] error: could not find libcoap\n')

    return json.loads(result.read().strip('\n'))

def get_tradfri_lightbulb(hubip, securityid, deviceid):
    """ function for getting information of a tradfri lightbulb """
    hub = 'coaps://{}:5684/15001/{}' .format(hubip, deviceid)
    apicall = 'bin/coap-client -m get -u "Client_identity" -k "{}" "{}" | awk \'NR==4\'' .format(securityid, hub)

    if os.path.exists('bin/coap-client'):
        result = os.popen(apicall)
    else:
        sys.stderr.write('[-] error: could not find libcoap\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))

def get_tradfri_groups(hubip, securityid):
    """ function for getting tradfri groups """
    hub = 'coaps://{}:5684/15004' . format(hubip)
    apicall = 'bin/coap-client -m get -u "Client_identity" -k "{}" "{}" | awk \'NR==4\'' .format(securityid, hub)

    if os.path.exists('bin/coap-client'):
        result = os.popen(apicall)
    else:
        sys.stderr.write('[-] error: could not find libcoap\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))

def get_tradfri_group_status(hubip, securityid, groupid):
    """ function for getting tradfri group information """
    hub = 'coaps://{}:5684/15004/{}' .format(hubip, groupid)
    apicall = 'bin/coap-client -m get -u "Client_identity" -k "{}" "{}" | awk \'NR==4\'' .format(securityid, hub)

    if os.path.exists('bin/coap-client'):
        result = os.popen(apicall)
    else:
        sys.stderr.write('[-] error: could not find libcoap\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))
