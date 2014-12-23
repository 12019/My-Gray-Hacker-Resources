#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

HOST = "google.com"

def traceroute():
    for i in range(1, 28):

        pkt = IP(dst=HOST, ttl=i) / UDP(dport=33434)
        # Send the packet and get a reply
        reply = sr1(pkt, verbose=0)

        if reply is None:
            # No reply =(
            break

        elif reply.type == 3:
            # We've reached our destination
            print "Done!", reply.src
            break

        else:
            # We're in the middle somewhere
            print "%d hops away: " % i , reply.src


if __name__ == '__main__':
    traceroute()