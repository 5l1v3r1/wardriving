#!/usr/bin/env python
from scapy.all import *
import datetime
ssidListe = []
def SSIDBul(pkt) :
    if pkt.haslayer(Dot11Beacon) :
        ssid = str(pkt.info)
        mac = str(pkt.addr2)
        if not ssid in ssidListe:
            ssidListe.append(ssid)
            print "Mac: ",mac," SSID: ",ssid
            log=str(datetime.datetime.now().strftime("%d %B %Y %I:%M%p"))+"|"+str(mac)+"|"+str(ssid)+"\n"
            dosya=open("ssid.txt","a")
            dosya.write(log)
            dosya.close()

sniff(iface="wlan0", prn = SSIDBul)
