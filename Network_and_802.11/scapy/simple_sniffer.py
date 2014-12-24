#!/usr/bin/env python

__author__ = "bt3"

''' A simple sniffer '''

'''
DOCUMENTATION:
# sniffer that dissects and dumps the packets out
# filter allows to specify a BPF, wireshark style to packets,
# for example, to sniff all HTTP packets you use a BPF filter of tcp
# and port 80
# iface parameter tells the sniffer which network interface to sniff on
# prn parameter specifies a callback function to every packet that matches the filter
# and it will receive packet as its single parameter
# count specifies how many packets you want to sniff (blank: infinite)
sniff(filter'', iface='any', prn=function, count=N)
'''


from scapy.all import *

# our packet callback
def packet_callback(packet):
    print packet.show()

# fire up the sniffer on all interfaces, with no filtering
sniff(prn=packet_callback, count=1)


