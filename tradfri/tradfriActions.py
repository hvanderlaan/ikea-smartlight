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
import random

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

    if value == 'warm':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("33135", "27211")
    elif value == 'normal':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("30140", "26909")
    elif value == 'cold':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("24930", "24684")

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

def tradfri_authenticate(hubip, securitycode, apiuser = "TRADFRI_PY_API_" + str(random.randint(0, 1000)) ):
    """ function for authenticating tradfri and getting apikey """
    tradfriHub = 'coaps://{}:5684/15011/9063'.format(hubip)
    payload = '{"9090":"' + apiuser + '"}'

    api = '{} -m post -u "Client_identity" -k "{}" -e \'{}\' "{}"'.format(coap, securitycode,
                                                                         payload, tradfriHub)
                                                                         
    if os.path.exists(coap):
        result = os.popen(api)
    else:
        sys.stderr.write('[-] libcoap: could not find libcoap\n')
        sys.exit(1)

    try:
        apikey = json.loads(result.read().strip('\n').split('\n')[-1])["9091"]
    except ValueError:
        raise Exception("Didn't receive valid apikey. This is because the api isn't reachable or the api user already exists.")

    return apiuser,apikey