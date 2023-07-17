# Network Scanner Tool

The "Network Scanner" tool is a Python script that allows you to scan a target IP address or a range of IP addresses to discover active hosts on the network. It uses ARP (Address Resolution Protocol) to perform an ARP scan and obtain information about the IP-MAC address pairs of the hosts.

## How to Use

To use the "Network Scanner" tool, follow these steps:

1. Clone or download the repository containing the "network_scanner.py" script to your local machine.

2. Open a terminal or command prompt and navigate to the location of the "network_scanner.py" script.

3. Run the script with Python and provide the target IP address or IP address range you want to scan:

python network_scanner.py -t <target_ip_or_range>


Replace `<target_ip_or_range>` with the target IP address or IP address range you want to scan. For example, to scan a single IP address:

python network_scanner.py -t 192.168.1.1


To scan an IP address range:

python network_scanner.py -t 192.168.1.1/24


Note: You may need to run the script with administrative privileges using `sudo` to perform the ARP scan successfully.

4. The script will perform an ARP scan on the target IP address or IP address range and display a list of active hosts along with their corresponding MAC addresses.

## Libraries Used

The "Network Scanner" tool uses the following Python libraries:

- `optparse`: Used to handle command-line options and arguments provided by the user. This library simplifies parsing and processing command-line inputs for the tool.

- `scapy.all`: This is part of the Scapy library, which provides powerful tools for packet manipulation and network scanning. The `scapy.all` module is used to create ARP packets and send them on the network to perform the ARP scan.

## Why These Libraries?

- `optparse`: The tool requires the user to specify the target IP address or IP address range through command-line options. The `optparse` library makes it easy to define and handle these options.

- `scapy.all`: Scapy is a versatile library that allows easy crafting and manipulation of network packets, including ARP packets. It simplifies the process of sending custom packets and capturing their responses, making it an excellent choice for network scanning and reconnaissance tasks.

## Disclaimer

This tool is intended for educational and ethical use only. The author does not condone any illegal or unauthorized activities with this tool. Always use this tool responsibly and only on networks and hosts you own or have explicit permission to scan.

**Use at your own risk!**

