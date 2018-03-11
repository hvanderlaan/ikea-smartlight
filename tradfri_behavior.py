#!/usr/bin/env python


from time import sleep
import tradfri_lights




I = range(1,100,10)*4
for i in [str(x) for x in I]:
    print(i)
    tradfri_lights.main(["-l","65541","--action","brightness","--value",i])
    sleep(.05)
