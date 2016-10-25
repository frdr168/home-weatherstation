#!/bin/bash
echo $1
if [ "${1}" == "on" ]; then
     echo 255 > /sys/class/leds/led1/brightness
else
     echo 0 > /sys/class/leds/led1/brightness
fi
