# HTTP Credential Sniffer Tool

The "HTTP Credential Sniffer" tool is a Python script that captures and analyzes HTTP packets on a specified network interface. It aims to detect and print possible login credentials (username and password) and the websites (URLs) that users are visiting via HTTP requests.

## How to Use

To use the "HTTP Credential Sniffer" tool, follow these steps:

1. Clone or download the repository containing the "http_credential_sniffer.py" script to your local machine.

2. Open a terminal or command prompt and navigate to the location of the "http_credential_sniffer.py" script.

3. Run the script with Python and specify the network interface you want to sniff for HTTP packets:

python http_credential_sniffer.py <interface>


Replace `<interface>` with the name of the network interface you want to monitor (e.g., "eth0" or "wlan0"). For example:

python http_credential_sniffer.py eth0


Note: You may need to run the script with administrative privileges using `sudo` to capture packets successfully.

4. The script will start sniffing HTTP packets on the specified network interface. When it detects an HTTP packet containing possible login credentials (e.g., a POST request with keywords "uname," "pass," etc.), it will print the captured data on the console.

- If the packet contains POST data, the script will extract and display the possible login credentials found.
- If the packet contains a GET request, the script will attempt to extract and display the URL of the website being visited.

5. The tool will continue to sniff HTTP packets until you manually stop it by pressing `Ctrl + C`.

## Libraries Used

The "HTTP Credential Sniffer" tool uses the following Python library:

- `scapy.all`: This is part of the Scapy library, which provides powerful tools for packet manipulation and network sniffing. The `scapy.sniff()` function is used to capture packets, and the `scapy.Raw` layer is used to extract the payload (data) of the captured packets for analysis.

## Why This Library?

- `scapy.all`: Scapy is a versatile library that allows easy capturing and analysis of network packets. It is well-suited for packet sniffing tasks and provides a straightforward way to work with different packet layers and data.

## please note

this tool is used with arp-spoofer to get the required result or to create a Man-in-the-Middle (MITM) attack scenario

## Disclaimer

This tool is intended for educational and ethical use only. The author does not condone any illegal or unauthorized activities with this tool. Capturing and analyzing network traffic, including HTTP packets, may violate privacy and security laws. Always use this tool responsibly and only on networks you own or have explicit permission to monitor.

**Use at your own risk!**

