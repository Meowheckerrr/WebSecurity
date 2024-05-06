from scapy.all import *


targetIP='10.10.52.12'
payload = "Mozilla"


def sendIcmpRequeset(targetIP,payload):
    
    rawPayload = bytes(payload,'utf8')
    conStructPacket = IP(dst=targetIP)/ICMP()/Raw(load=rawPayload)
    send(conStructPacket)

sendIcmpRequeset(targetIP,payload)