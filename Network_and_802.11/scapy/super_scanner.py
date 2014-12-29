#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *
import netaddr
import random

RANGE = "192.168.1.0/24"
PORTS = [22,23,80,443,449]

addresses = netaddr.IPNetwork(RANGE)

def portScan(host, ports):
    for dstPort in ports:
        srcPort = random.randint(1025,65534)
        resp = sr1(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)

        if (str(type(resp)) == "<type 'NoneType'>"):
            print host + ":" + str(dstPort) + " is filtered (silently dropped)."

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                send_rst = sr(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags="R"),timeout=1,verbose=0)
                print host + ":" + str(dstPort) + " is open."
            elif (resp.getlayer(TCP).flags == 0x14):
                print host + ":" + str(dstPort) + " is closed."
            elif(resp.haslayer(ICMP)):
                if(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                    print host + ":" + str(dstPort) + " is filtered (silently dropped)."

def super_scanner():
    liveCounter = 0
    for addr in addresses:
        if (addr == addresses.network or addr == addresses.broadcast):
            continue

        resp = sr1(IP(dst=str(addr))/ICMP(),timeout=2,verbose=0)
        if (str(type(resp)) == "<type 'NoneType'>"):
            print str(addr) + " is down or not responding."
        elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print str(addr) + " is blocking ICMP."
        else:
            portScan(str(addr),PORTS)
            liveCounter += 1

    print "Out of " + str(addresses.size) + " hosts, " + str(liveCounter) + " are online."

if __name__ == '__main__':
    super_scanner()