# ikea-smartlight
python framework for controlling the Ikea smart lights (tradfri)

### requirements
at this moment there is no coap libs with dTLS, the ikea smart lights are using dTLS with coap for security. the only option is to build a new libcoap with dTLS included. libcoap requires `cunit, a2x, doxygen and dot` you need to install these requirements first.

when this is installed run the build script for compiling libcoap
```bash
cd bin
./build.sh
```

the framework also requires `tqdm` for showing progressbars, you could strip it from the sourcecode or install the module for python: `pip install pip --upgrade && pip install tqdm`.

### libcoap usage
```bash
# getting tradfri information
./coap-client -m get -u "Client_identity" -k "<key>" "coaps://<hup>:5684/15001"
# getting tradfri lightbulb status
./coap-client -m get -u "Client_identity" -k "<key>" "coaps://<hup>:5684/15001/65537"

# turn on tradfri lightbulb
./coap-client -m put -u "Client_identity" -k "<key>" -e '{ "3311" : [{ "5850" : 1 ]} }' "coaps://<hup>:5684/15001/65537"
# turn off tradfri lightbulb
./coap-client -m put -u "Client_identity" -k "<key>" -e '{ "3311" : [{ "5850" : 1 ]} }' "coaps://<hup>:5684/15001/65537"
```

### output
```
./get-tradfri-status.py
[ ] smartlight: receiving tradfri lightbulbs information
getting lightbulbs: 100%|████████████████████████████████████████████████████████| 7/7 [00:00<00:00,  9.52 lightbulbs/s]
getting groups: 100%|████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 10.62 groups/s]
[+] smartlight: done getting tradfri lightbulbs information
===========================================================

bulbid: 1, name: lamp tv, state: off
bulbid: 2, name: lamp bank, state: off
bulbid: 3, name: lamp kastje, state: off
bulbid: 4, name: lamp hal boven, state: off
bulbid: 5, name: lamp slaapkamer, state: off
bulbid: 6, name: lamp hal beneden, state: off

groupid: 0, name: hal beneden, state off
groupid: 1, name: slaapkamer, state on
groupid: 2, name: woonkamer, state off
groupid: 3, name: hal boven, state on
```

### todo
- [ ] add change state (power on/off lightbulb)
- [ ] add dimmer value (dimm lightbulb)
- [ ] add change state group (power on/off groups)
- [ ] add dimmer value group (dimm group)
- [ ] add color temperature lightbulb (switch to cold, normal or warm)
- [ ] add color temperature group (switch to cold, normal or warm)

### licensing and credits
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
