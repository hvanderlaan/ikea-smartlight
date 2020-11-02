#!/usr/bin/env python

# file        : tradfri/tradfriActions.py
# purpose     : module for controling status of the Ikea tradfri smart lights
#
# author      : harald van der laan
# date        : 2017/11/01
# version     : v1.2.0
#
# changelog   :
# - v1.2.0      update for gateway 1.1.15 issues                        (harald)
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfri/tradfriActions.py - controlling the Ikea tradfri smart lights

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# pylint: disable=C0103

import sys
import os
import json
from tradfriStatus import tradfri_get_lightbulb

global coap
coap = '/usr/local/bin/coap-client'

def tradfri_power_light(hubip, apiuser, apikey, lightbulbid, value):
    """ function for power on/off tradfri lightbulb """
    tradfriHub = 'coaps://{}:5684/15001/{}' .format(hubip, lightbulbid)

    if value == 'on':
        payload = '{ "3311": [{ "5850": 1 }] }'
    else:
        payload = '{ "3311": [{ "5850": 0 }] }'

    api = '{} -m put -u "{}" -k "{}" -e \'{}\' "{}"' .format(coap, apiuser, apikey,
                                                                          payload, tradfriHub)

    if os.path.exists(coap):
        os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    return True


def tradfri_dim_light(hubip, apiuser, apikey, lightbulbid, value):
    """ function for dimming tradfri lightbulb """
    dim = float(value) * 2.55
    tradfriHub = 'coaps://{}:5684/15001/{}'.format(hubip, lightbulbid)
    payload = '{ "3311" : [{ "5851" : %s }] }' % int(dim)

    api = '{} -m put -u "{}" -k "{}" -e \'{}\' "{}"'.format(coap, apiuser, apikey,
                                                                         payload, tradfriHub)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    return result

def tradfri_color_light(hubip, apiuser, apikey, lightbulbid, value):
    """ function for color temperature tradfri lightbulb """
    tradfriHub = 'coaps://{}:5684/15001/{}'.format(hubip, lightbulbid)
    payload = None
    colors = get_color_dict()
    
    if value in ['warm', 'normal', 'cold']:
        payload = '{ "3311" : [{ "5706" : "%s"}] }' % (colors[value])
    
    if payload is None:
        color_supported = 'CWS' in tradfri_get_lightbulb(hubip, apiuser, apikey, lightbulbid)[u'3'][u'1']

        if not color_supported:
            print("Your lamp does not support colors.")

    payload = '{ "3311" : [{ "5706" : "%s"}] }' % (colors[value])
    api = '{} -m put -u "{}" -k "{}" -e \'{}\' "{}"'.format(coap, apiuser, apikey,
                                                                         payload, tradfriHub)
    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    return result

def tradfri_power_group(hubip, apiuser, apikey, groupid, value):
    """ function for power on/off tradfri lightbulb """
    tradfriHub = 'coaps://{}:5684/15004/{}' .format(hubip, groupid)

    if value == 'on':
        payload = '{ "5850" : 1 }'
    else:
        payload = '{ "5850" : 0 }'

    api = '{} -m put -u "{}" -k "{}" -e \'{}\' "{}"' .format(coap, apiuser, apikey,
                                                                          payload, tradfriHub)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    return result


def tradfri_dim_group(hubip, apiuser, apikey, groupid, value):
    """ function for dimming tradfri lightbulb """
    tradfriHub = 'coaps://{}:5684/15004/{}'.format(hubip, groupid)
    dim = float(value) * 2.55
    payload = '{ "5851" : %s }' % int(dim)

    api = '{} -m put -u "{}" -k "{}" -e \'{}\' "{}"'.format(coap, apiuser, apikey,
                                                                         payload, tradfriHub)

    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    return result

def get_color_dict():
    return {
    'blue' : '4a418a',
    'light blue' : '6c83ba',
    'saturated purple' : '8f2686',
    'lime' : 'a9d62b',
    'light purple': 'c984bb',
    'yellow' : 'd6e44b',
    'saturated pink' : 'd9337c',
    'dark peach' : 'da5d41',
    'saturated red' : 'dc4b31',
    'cold sky' : 'dcf0f8', 
    'pink' : 'e491af',
    'peach' : 'e57345',
    'warm amber' : 'e78834',
    'light pink' : 'e8bedd',
    'cool daylight' : 'eaf6fb',
    'candlelight' : 'ebb63e',
    'warm' : 'efd275',
    'normal' : 'f1e0b5',
    'sunrise' : 'f2eccf',
    'cold' : 'f5faf6',
    }