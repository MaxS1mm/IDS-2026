from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

sniff(prn=packet_handler, store=False)