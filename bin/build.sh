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
cd ../
cp -r libcoap/examples/.lib .
cp libcoap/examples/coap-client
rm -r libcoap
