#!/usr/bin/env python

# file        : tradfri/tradfriStatus.py
# purpose     : getting status from the Ikea tradfri smart lights
#
# author      : harald van der laan
# date        : 2017/11/01
# version     : v1.2.0
#
# changelog   :
# - v1.2.0      update for new gateway 1.1.15 issues                    (harald)
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfriStatus.py - module for getting status of the Ikea tradfri smart lights

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# pylint: disable=C0103

import sys
import os
import json

global coap
coap = '/usr/local/bin/coap-client'
timeout = 5

def tradfri_get_devices(hubip, apiuser, apikey):
    """ function for getting all tradfri device ids """
    tradfriHub = 'coaps://{}:5684/15001' .format(hubip)
    api = '{} -m get -u "{}" -k "{}" "{}" -B {} 2> /dev/null' .format(coap, apiuser, apikey,
                                                                      tradfriHub, timeout)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap.\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))

def tradfri_get_lightbulb(hubip, apiuser, apikey, deviceid):
    """ function for getting tradfri lightbulb information """
    tradfriHub = 'coaps://{}:5684/15001/{}' .format(hubip, deviceid)
    api = '{} -m get -u "{}" -k "{}" "{}" -B {} 2> /dev/null' .format(coap, apiuser, apikey,
                                                                      tradfriHub, timeout)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap.\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))

def tradfri_get_groups(hubip, apiuser, apikey):
    """ function for getting tradfri groups """
    tradfriHub = 'coaps://{}:5684/15004'.format(hubip)
    api = '{} -m get -u "{}" -k "{}" "{}" -B {} 2> /dev/null' .format(coap, apiuser, apikey,
                                                                      tradfriHub, timeout)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap.\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))

def tradfri_get_group(hubip, apiuser, apikey, groupid):
    """ function for getting tradfri group information """
    tradfriHub = 'coaps://{}:5684/15004/{}'.format(hubip, groupid)
    api = '{} -m get -u "{}" -k "{}" "{}" -B {} 2> /dev/null' .format(coap, apiuser, apikey,
                                                                      tradfriHub, timeout)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap.\n')
        sys.exit(1)

    return json.loads(result.read().strip('\n'))
