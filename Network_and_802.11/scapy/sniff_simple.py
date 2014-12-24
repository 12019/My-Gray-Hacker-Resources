#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

def save():
    a = sniff(filter='icmp', iface='wlp1s0', timeout=10, count=3,  prn=lambda x:x.summary())
    wrpcap('packets.pcap', a)

def open():
    p = rdpcap('packets.pcap', p)
    p.show()

def scan():
    res, unans = sr( IP(dst='192.168.1.114')/TCP(flags='S', dport=(1, 1024)))
    print res.summary()

scan()