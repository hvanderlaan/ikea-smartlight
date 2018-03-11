#!/usr/bin/env python


from time import sleep
import "tradfri-lights"

I = range(0,100,10)
print(I)
for i in I: 
    tradfri-lights -l 65541 --action brightness --value i
    sleep(2)
