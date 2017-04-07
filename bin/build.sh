#!/bin/bash
git clone https://github.com/obgm/libcoap.git
cd libcoap
git checkout origin/dtls
git checkout -b dtls
git submodule update --init ext/tinydtls
cd ext/tinydtls
autoreconf
./configure
cd ../../
./autogen.sh
./configure --disable-shared --enable-tests
make
cp -r libcoap/examples/.libs .
cp libcoap/examples/coap-client
