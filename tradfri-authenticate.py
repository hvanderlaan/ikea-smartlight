#!/usr/bin/env python

# file        : tradfri-authenticate.py
# purpose     : authenticate api user and generate configuration file
#
# author      : maltejur
# date        : 2020/10/24

"""
    tradfri-authenticate.py - authenticate api user and generate configuration file

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# C0200 -> consider-using-enumerate
# pylint: disable=C0200, C0103

from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import time
import ConfigParser

from tradfri import tradfriActions

def main():
    """ main function """
    conf = ConfigParser.ConfigParser()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    conf.read(script_dir + '/tradfri.cfg')

    hubip = raw_input("\nhub ip:\t\t")
    securityCode = raw_input("security code: \t")

    print("\n[ ] acquiring api key ...", end="")

    apiuser, apikey = tradfriActions.tradfri_authenticate(hubip, securityCode)

    print("\r[+]\n\nuser:\t{}\napikey:\t{}\n".format(apiuser, apikey))

    print("[ ] writing configuration file ...", end="")

    conf.add_section('tradfri')
    conf.set("tradfri", "hubip", hubip)
    conf.set("tradfri", "apiuser", apiuser)
    conf.set("tradfri", "apikey", apikey)
    conf.write(open(script_dir + '/tradfri.cfg','w'))

    print("\r[+]\n")

    print("all done!\n")

if __name__ == "__main__":
    main()
    sys.exit(0)
