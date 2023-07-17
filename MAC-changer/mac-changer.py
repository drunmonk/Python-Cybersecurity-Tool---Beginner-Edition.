#!/usr/bin/python3

import subprocess
import optparse
import re

# Function to handle command-line arguments
def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options, arguments) = parser.parse_args()

    # Validate user input
    if options.interface not in ["eth0", "wlan0"]:
        parser.error("[+] Please specify a valid interface. For more help, use --help.")
    elif not options.new_mac:
        parser.error("[+] Please specify a new MAC address. For more help, use --help.")
    return options

# Function to change the MAC address of the specified interface
def mac_change(interface, new_mac):
    # Bring the interface down
    subprocess.call(["sudo", "ifconfig", interface, "down"])

    # Change the MAC address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])

    # Bring the interface back up
    subprocess.call(["sudo", "ifconfig", interface, "up"])

# Function to retrieve the current MAC address of the specified interface
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read a MAC address.")

# Main code
options = arguments()  # Get command-line arguments
current_mac = get_current_mac(options.interface)  # Get the current MAC address of the specified interface
print("Current MAC address = " + str(current_mac))

# Change the MAC address to the new MAC address provided by the user
mac_change(options.interface, options.new_mac)

# Get the current MAC address after the change
current_mac = get_current_mac(options.interface)

# Check if the MAC address changed successfully
if current_mac == options.new_mac:
    print("[+] MAC address has been successfully changed to " + current_mac)
else:
    print("[-] MAC address did not change.")
