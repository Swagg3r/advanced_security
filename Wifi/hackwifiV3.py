#!/usr/bin/env python

import sys
from scapy.all import *
from netaddr import *

ap_list = []

def f(pkt):
	if pkt.haslayer(Dot11):
		print hexdump(pkt)

def j(pkt):
	if pkt.haslayer(Dot11):
		pkt.show()


def l(pkt):
	if pkt.haslayer(Dot11):
		if pkt.type == 0 and pkt.subtype == 4 :
			ap_list.append(pkt.addr2)
			mac = EUI(pkt.addr2)
			oui = mac.oui
			print "MAC: %s SSID: %s" %(pkt.addr2, pkt.info)


def access_point(pkt):
	if pkt.haslayer(Dot11):
		if pkt.type == 0 and pkt.subtype == 8 :
			if pkt.addr2 not in ap_list :
				ap_list.append(pkt.addr2)
				mac2 = EUI(pkt.addr2)
				oui2 = mac2.oui
				print "MANUFACTURER: %s AP MAC: %s SSID: %s" %(oui2.registration().org, pkt.addr2, pkt.info)


def k(pkt):
	if pkt.haslayer(Dot11):
		# if pkt.type == 0 and pkt.subtype == 8 :
			# print "addr1= "+str(pkt.addr1)
			# print "addr2= "+str(pkt.addr2)
			# print "type= "+str(pkt.type)
			# print "subtype= "+str(pkt.subtype)
			# print "name= "+str(pkt.payload.name)
			# print pkt.info
			if pkt.addr2 not in ap_list :
				ap_list.append(pkt.addr2)
				if pkt.addr2 != None:
					mac = EUI(pkt.addr2)
					try:
						oui = mac.oui
						print "MANUFACTURER: %s  MAC: %s " %(oui.registration().org, pkt.addr2)
					except Exception as e:
						print "MANUFACTURER: ANONYMOUS  MAC: %s " %(pkt.addr2)
					try:
						print pkt.info
					except Exception as e:
						pass
print "Acces point :"
pkts=sniff(iface=sys.argv[1], count=200, prn=access_point)

#print "\nDevices :"
#pkts=sniff(iface=sys.argv[1], prn=k)

print "Affichage des SSID dans les probes request :"
pkts=sniff(iface=sys.argv[1], prn=l)


wrpcap("save.pcap",pkts)

# if pkt.type == 0 and pkt.subtype == 4