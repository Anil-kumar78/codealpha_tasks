# codealpha_tasks
Collecting workspace informationHere’s a GitHub repository description for your sniffer.py file:

---

# Network Packet Sniffer

A Python-based network packet sniffer that captures and analyzes Ethernet, IPv4, ICMP, and TCP packets. This tool uses raw sockets to intercept network traffic and extract key details such as MAC addresses, IP addresses, protocols, and more.

## Features

- **Ethernet Frame Parsing**: Extracts destination MAC, source MAC, and protocol type.
- **IPv4 Packet Parsing**: Extracts version, header length, TTL, protocol, source IP, and destination IP.
- **ICMP Packet Parsing**: Extracts type, code, and checksum.
- **TCP Segment Parsing**: Extracts source port, destination port, sequence number, acknowledgment number, and flags.

## Usage

Run the script with administrator privileges:

```bash
sudo python sniffer.py
```

The script will continuously capture and display packet details in the terminal.

## Requirements

- Python 3.x
- Root/Administrator privileges (required for raw socket access)

## Disclaimer

This project is for educational purposes only. Ensure you have permission to monitor network traffic on the interface before using this tool.

---
A Python-based network packet sniffer that captures and analyzes Ethernet, IPv4, ICMP, and TCP packets. This tool uses raw sockets to intercept network traffic and extract key details such as MAC addresses, IP addresses, protocols, and more.

Features
Ethernet Frame Parsing: Extracts destination MAC, source MAC, and protocol type.
IPv4 Packet Parsing: Extracts version, header length, TTL, protocol, source IP, and destination IP.
ICMP Packet Parsing: Extracts type, code, and checksum.
TCP Segment Parsing: Extracts source port, destination port, sequence number, acknowledgment number, and flags.
Usage
Run the script with administrator privileges:

The script will continuously capture and display packet details in the terminal.

Requirements
Python 3.x
Root/Administrator privileges (required for raw socket access)
Disclaimer
This project is for educational purposes only. Ensure you have permission to monitor network traffic on the interface before using this tool.

