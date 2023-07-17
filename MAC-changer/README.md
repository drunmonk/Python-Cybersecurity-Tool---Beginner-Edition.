# Mac Changer Tool

The "Mac Changer" tool is a Python script that allows you to change the MAC address of a network interface on your system. It provides a simple command-line interface for specifying the network interface and the new MAC address you want to set.

## How to Use

To use the "Mac Changer" tool, follow these steps:

1. Clone or download the repository containing the "mac_changer.py" script to your local machine.

2. Open a terminal or command prompt and navigate to the location of the "mac_changer.py" script.

3. Run the script with Python and provide the necessary options:

python3 mac_changer.py -i <interface> -m <new_mac_address>

Replace `<interface>` with the name of the network interface you want to modify (e.g., "eth0" or "wlan0"), and `<new_mac_address>` with the new MAC address you wish to set. For example:

python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55


Note: You may need to run the script with administrative privileges using `sudo` to change the MAC address successfully.

4. The script will attempt to change the MAC address of the specified network interface. If successful, it will display a message indicating the new MAC address. Otherwise, it will notify you that the MAC address did not change.

## Libraries Used

The "Mac Changer" tool uses the following Python libraries:

- `subprocess`: Used to execute system commands to bring the network interface down, change the MAC address, and bring it back up.

- `optparse`: Used to parse command-line options and arguments provided by the user. This library simplifies handling command-line inputs for the tool.

- `re` (Regular Expressions): Used to extract the current MAC address from the output of the `ifconfig` command. Regular expressions are employed to find and retrieve the MAC address pattern from the text.

## Why These Libraries?

- `subprocess`: The tool needs to interact with the system to manipulate network interfaces and change the MAC address. The `subprocess` library provides a straightforward way to run system commands from Python.

- `optparse`: The tool requires the user to provide input through command-line options. The `optparse` library makes it easy to define and handle these options.

- `re` (Regular Expressions): The tool needs to extract the current MAC address from the output of the `ifconfig` command. Regular expressions are a powerful tool for pattern matching in strings, making it efficient to extract the required information.

## Disclaimer

This tool is intended for educational and ethical use only. The author does not condone any illegal or unauthorized activities with this tool. Always use this tool responsibly and only on systems you own or have explicit permission to modify.

**Use at your own risk!**

