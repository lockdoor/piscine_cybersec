import scapy.all as scapy
from scapy.all import TCP, Raw
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest = 'interface', help = 'Interface Name for which packet is supposed to be captured.')
    options = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please specify the name of the interface, use --help for more info.')
        
    return options.interface

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(TCP) and (packet[TCP].sport == 21 or packet[TCP].dport == 21):
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")
            if payload.startswith("STOR") or payload.startswith("RETR"):
                command, filename = payload.split(" ", 1)
                print(f"[FTP] {command.strip()} -> {filename.strip()}")

if __name__ == '__main__':
    interface = get_args()
    sniffer(interface)
