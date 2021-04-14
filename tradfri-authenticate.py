#!/usr/bin/env python3

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

import os
import sys
import configparser

from tradfri import tradfriActions

def main():
    """ main function """
    conf = configparser.ConfigParser()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    conf.read(script_dir + '/tradfri.cfg')

    hubip = input("\nhub ip:\t\t")
    securityCode = input("security code: \t")

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
