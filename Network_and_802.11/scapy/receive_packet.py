#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *


output=sr(IP(dst='google.com')/ICMP())
print '\nOutput is:'
print output
result, unanswered=output
print '\nResult is:'
print result[0]
