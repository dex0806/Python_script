import sys
import os
from scapy.all import *
from scapy.layers.inet import IP, Ether, ICMP

class Ping:
    def ping_host():
        ip = input("Enter the ip address or url:\n")
        mac = Ether(src = "bc:5f:f4:e4:c7:31", dst = "60:32:b1:61:ef:83", type = 0x0800)
        ip_v4 = IP(version = 4, ihl = 5, tos = 0x0, flags = 0x2, len = 60, id = 14488, proto = "\x69\x63\x6d\x70", ttl = 128,  src = "192.168.0.100", dst=ip)
        icmp = ICMP(id=1, seq=1)
        data = "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69"
        ping =  mac / ip_v4 / icmp / Raw(load=data)
        sendp(ping)
    ping_host()
