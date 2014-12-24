#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

# Set port & MAC address
FAKE_IP = "10.0.4.4" # Use something that nobody else is going to have
MAC_ADDR = "60:67:20:eb:7b:bc" # My actual MAC address

# Broadcast our fake IP address
srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(psrc=FAKE_IP, hwsrc=MAC_ADDR))

source_port += 1
ip_header = IP(dst=dest, src=FAKE_IP) # Set the source port to
ans = sr1(ip_header / TCP(dport=80, sport=source_port,  flags="S", seq=random.randint(0, 1000))) # SYN
# ans is the SYN-ACK
reply = ip_header / TCP(dport=80, sport=source_port, seq=ans.ack, ack = ans.seq + 1, flags="A") # ACK
send(reply) # Send ACK
pkt = ip_header / TCP(dport=80, sport=source_port, seq=reply.seq, flags="AP") / "GET / HTTP/1.1\r\n\r\n" # Send our real packet
send(pkt)


ip = IP(src='192.168.1.114', dst='192.168.1.25')
SYN = TCP(sport=1024, dport=80, flags='S', seq=12345)
packet = ip/SYN

SYNACK = sr1(packet)
ack = SYNACK.seq + 1