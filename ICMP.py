import sys
import os
from scapy.all import *
from scapy.layers.inet import IP, Ether, ICMP

#MAC_Ether = Ether(src = "bc:5f:f4:e4:c7:31", dst = "60:32:b1:61:ef:83", type = 0x0800)

ip_v4 = IP(version = 0x04, # deci  
        ihl = 0x05, #decimal 5
        tos = 0x40, #Differentiated Services Field: 0x40 (DSCP: CS2, ECN: Not-ECT)
        flags = 0x2, #Flags: 0x2, Don't fragment. decimal
        #frag = 8,         
        len = 0x3C, #Total Length: 60 decimal
        id = 32776, 
        proto = 0x01, # icmp=1 decimal 
        ttl = 0x80,  # ttl=128 decimal 
        src = "192.168.0.100", 
        dst = "5.13.124.179")

ICMP_Ping = ICMP(type=8,
                 code=0, 
                 seq=101,
                 id=10)
                   
data = "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69"

packet = ip_v4/ICMP_Ping/Raw(load=data)

send(packet)
