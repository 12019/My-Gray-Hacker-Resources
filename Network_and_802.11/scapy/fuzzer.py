#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

send(IP(dst='192.168.1.114')/UDP()/fuzz(DNS()), inter=1,loop=1)
