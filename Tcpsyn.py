import sys
import os
from scapy.all import *
from scapy.layers.inet import IP, Ether, TCP

#MAC_Ether = Ether(src = "bc:5f:f4:e4:c7:31", dst = "60:32:b1:61:ef:83", type = 0x0800)

#dst_ip = input("Enter the ip address or url:\n")


ip_v4 = IP(version = 4, 
        ihl = 0x05, 
        tos = 0x00,
        flags = 0x2,
        #frag = 8,         
        len = 0x28, 
        id = 14488, 
        proto = 6, 
        ttl = 64,  
        src = "192.168.0.100", 
        dst = "31.186.217.190")

tcp = TCP(sport = 52023,
          dport =  80,
          seq = 169913423,
          ack = 0,
          flags = 0x002,
          window = 4128)
          #options = [('MSS', 1640)])
          
          
        
packet = ip_v4 / tcp

send(packet)
