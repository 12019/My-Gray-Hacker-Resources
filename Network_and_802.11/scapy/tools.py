#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

HOST ='www.google.com'

def tr():
    print traceroute(HOST)

def pi():
    print arping('192.168.1.114')

#pi()

#tr()

print sniff(iface="wlp1s0",prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\t%Dot11Beacon.info%\t%PrismHeader.channel%\tDot11Beacon.cap%}"))