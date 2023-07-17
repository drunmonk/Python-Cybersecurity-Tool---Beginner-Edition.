# ARP Spoofing Tool

The "ARP Spoofing Tool" is a Python script that performs ARP spoofing, a technique used to intercept network traffic between two devices on the same local network. It allows an attacker to send fake ARP messages to the target devices, causing them to update their ARP tables and redirect traffic to the attacker's machine.

## How to Use

To use the "ARP Spoofing Tool," follow these steps:

1. Clone or download the repository containing the "arp_spoof.py" script to your local machine.

2. Open a terminal or command prompt and navigate to the location of the "arp_spoof.py" script.

3. Run the script with Python and provide the target IP and the IP you want to impersonate (spoof):

python3 arp_spoof.py -t <target_ip> -s <spoof_ip>


Replace `<target_ip>` with the IP address of the target you want to intercept the traffic for, and `<spoof_ip>` with the IP address you want to impersonate. For example:

python3 arp_spoof.py -t 192.168.142.148 -s 192.168.142.2


Note: You may need to run the script with administrative privileges using `sudo` to send ARP packets successfully.

4. The script will start sending ARP packets to perform ARP spoofing between the target and the spoofed IP addresses. It will also display the number of packets sent every 2 seconds.

5. To stop the ARP spoofing attack, press `Ctrl + C` to terminate the script. The script will then automatically restore the ARP tables for both the target and the spoofed devices.

## Libraries Used

The "ARP Spoofing Tool" uses the following Python library:

- `scapy.all`: This is part of the Scapy library, which provides powerful tools for packet manipulation and network scanning. In this script, Scapy is used to craft and send ARP packets for ARP spoofing.

## Why This Library?

- `scapy.all`: Scapy is a versatile library that allows easy crafting and manipulation of network packets, including ARP packets. It provides a straightforward way to construct custom packets and send them on the network, making it an excellent choice for ARP spoofing.

## Disclaimer

This tool is intended for educational and ethical use only. The author does not condone any illegal or unauthorized activities with this tool. ARP spoofing is a serious attack and may lead to legal consequences if used without proper authorization. Always use this tool responsibly and only on networks and devices you own or have explicit permission to test.

**Use at your own risk!**

