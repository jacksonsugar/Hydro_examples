#!/bin/bash

/opt/vc/bin/raspivid -t 0 -w 300 -h 300 -vf -fps 20 -o - | nc 192.168.1.151 2222
