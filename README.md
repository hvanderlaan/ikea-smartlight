# ikea-smartlights
python framework for controlling the Ikea smart lights (tradfri)

## setup

### requirements
at this moment there is no coap libs with dTLS, the ikea smart lights are using dTLS with coap for security. the only option is to build a new libcoap with dTLS included. libcoap requires `cunit, a2x, doxygen and dot` you need to install these requirements first.

```bash
sudo apt-get install automake libtool
git clone --depth 1 --recursive -b dtls https://github.com/home-assistant/libcoap.git
cd libcoap
./autogen.sh
./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr"
make
sudo make install
```

the framework also requires `tqdm` for showing progressbars, you could strip it from the sourcecode or install the module for python: `pip install pip --upgrade && pip install tqdm`.

### authentication
you will need to authenticate the api before you first use it. to do this, run `python tradfri-authenticate.py` and enter the ip of your hub and the security code (on the back of the hub). the script will automaticaly create a configuration file containing the api key

## usage

### status
```
python tradfri-status.py
```
```
[ ] tradfri: requireing all tradfri devices, please wait ...
tradfri lightbulbs: 100%|█████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 10.93 lightbulb/s]
tradfri groups: 100%|█████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 10.50 group/s]
[+] tradfri: device information gathered
===========================================================

bulbid 65537, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65538, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65539, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65540, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65542, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65541, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65544, name: TRADFRI bulb E27, bightness: 254, state: off


groupid: 137274, name: hal beneden, state: off
groupid: 183216, name: slaapkamer, state: off
groupid: 140387, name: woonkamer, state: off
groupid: 186970, name: hal boven, state: off
```

### turn on a light
```
python tradfri-lights.py -a power -l {LIGHTBULB_ID} -v on
```

### dim the light
```
python tradfri-lights.py -a brightness -l {LIGHTBULB_ID} -v 50
```

### turn off all ligths in room
```
python tradfri-groups.py -a power -g {GROUP_ID} -v off
```

### libcoap usage
```bash
# getting tradfri pre shared key
coap-client -m post -u "Client_identity" -k "<key>" -e '{"9090":"IDENTITY"}' "coaps://<hub>:5684/15011/9063"
# getting tradfri information
./coap-client -m get -u "IDENTITY" -k "<psk>" "coaps://<hup>:5684/15001"
# getting tradfri lightbulb status
./coap-client -m get -u "IDENTITY" -k "<psk>" "coaps://<hup>:5684/15001/65537"

# turn on tradfri lightbulb
./coap-client -m put -u "IDENTITY" -k "<psk>" -e '{ "3311" : [{ "5850" : 1 }] }' "coaps://<hup>:5684/15001/65537"
# turn off tradfri lightbulb
./coap-client -m put -u "IDENTITY" -k "<psk>" -e '{ "3311" : [{ "5850" : 0 }] }' "coaps://<hup>:5684/15001/65537"
```

## HomeKit code
getting the apple HomeKit code for your gateway. first ensure you have the pre shared key.
```bash
coap-client -m get -u "IDENTITY" -k "PRE SHARED KEY" "coaps://IP_ADDRESS:5684/15011/15012" 2> /dev/null
# Apple HomeKit code looks like: { ... 9083: XXX-XX-XXX, ...}
# XXX-XX-XXX is your HomeKit code
```

## todo
- [ ] add support for new color lightbulbs
- [X] add change state (power on/off lightbulb)
- [X] add dimmer value (dimm lightbulb)
- [X] add change state group (power on/off groups)
- [X] add dimmer value group (dimm group)
- [X] add color temperature lightbulb (switch to cold, normal or warm)

## licensing and credits
ikea-smartlight is licensed under the GPLv3:
```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For the full license, see the LICENSE file.
```
