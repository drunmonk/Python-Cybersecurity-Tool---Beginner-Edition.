#!/usr/bin/python

import optparse
import scapy.all as scapy

# Function to handle command-line arguments
def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target IP or range of IP addresses")
    (options, arguments) = parser.parse_args()

    # Validate user input
    if not options.target:
        parser.error("[+] Please specify a target IP or range of IP addresses. For more help, use --help.")
    return options

# Function to perform ARP scan
def scan(ip):
    # Create an ARP request packet for the specified IP or IP range
    arp_request = scapy.ARP(pdst=ip)

    # Create an Ethernet frame with the broadcast MAC address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the ARP request and Ethernet frame to create an ARP request broadcast packet
    arp_request_broadcast = broadcast / arp_request

    # Send the ARP request broadcast packet and receive responses
    # The srp() function returns two lists, the first one containing answered packets and the second one containing unanswered packets
    # We use [0] to select the list of answered packets
    # The verbose option is set to False to suppress output to the console
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Create a list to store the IP-MAC address pairs of the active hosts
    clients = []

    # Process the responses and extract IP-MAC address pairs
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients.append(client_dict)

    return clients

# Function to print the scan results
def print_result(clients):
    print("\tIP\t\t\t\tMAC\n--------------------------------------------------")
    for person in clients:
        print(person["IP"] + "\t\t|\t" + person["MAC"])

# Main code
options = arguments()  # Get command-line arguments
result = scan(options.target)  # Perform ARP scan
print_result(result)  # Print the scan results
