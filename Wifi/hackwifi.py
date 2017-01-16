#! /usr/bin/env python

import sys
from scapy.all import *
from netaddr import *

WifiAccessP = []
WifiDevices = []


#wrpcap("save.pcap", pkts)

def ShowProbeReq(pkt):
	if pkt.type==0 and pkt.subtype==0x04:
		print "    MAC : %s SSID : %s" %(pkt.addr2, pkt.info) 

print "## Access Points : ##"

def ShowAccessPoints(pkt):
	if pkt.type==0 and pkt.subtype==8 and pkt.addr2 not in WifiAccessP :
		WifiAccessP.append(pkt.addr2)
		mac = EUI(str(pkt.addr2))
		oui = mac.oui
		print "Manufacturer : %s MAC : %s SSID : %s" %(oui.registration().org, pkt.addr2, pkt.info) 
		
#sniff(iface=sys.argv[1], prn = ShowAccessPoints,  count=200)

print "\n\n## Devices : ##"

def ShowDevices(pkt):
	if pkt.haslayer(Dot11) :
		if pkt.addr2 != None and pkt.addr2 not in WifiDevices and pkt.addr2 not in WifiAccessP:
			WifiDevices.append(str(pkt.addr2))
			mac = EUI(str(pkt.addr2))
			try:
				oui = mac.oui
				print "Manufacturer : %s MAC : %s " %(oui.registration().org, pkt.addr2)
			except Exception as e:
				print "UNREGISTERED Device ! MAC : %s " %(pkt.addr2)

#sniff(iface=sys.argv[1], prn = ShowDevices, count=1000)

sniff(iface=sys.argv[1], prn = ShowProbeReq, count=1000)

