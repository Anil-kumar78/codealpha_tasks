import socket
import struct
import textwrap

#Unpack the ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

#Return properly formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

def ipv4(addr):
    return '.'.join(map(str, addr))

def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

def tcp_segment(data):
    src_port, dest_port, sequence, acknowledgment, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flags = offset_reserved_flags & 0xfff
    return src_port, dest_port, sequence, acknowledgment, flags, data[offset:]

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        
        print('\nEthernet Frame:')
        print(f'Destination: {dest_mac}')
        print(f'Source: {src_mac}')
        print(f'Protocol: {eth_proto}')
        
        # IPv4
        if eth_proto == 8:
            version, header_length, ttl, proto, src, target, data = ipv4_packet(data)
            print('\nIPv4 Packet:')
            print(f'Version: {version}')
            print(f'Header Length: {header_length}')
            print(f'TTL: {ttl}')
            print(f'Protocol: {proto}')
            print(f'Source: {src}')
            print(f'Target: {target}')
            
            # Unpack ICMP packet
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                print('\nICMP Packet:')
                print(f'Type: {icmp_type}')
                print(f'Code: {code}')
                print(f'Checksum: {checksum}')
                
            # Unpack TCP segment
            elif proto == 6:
                src_port, dest_port, sequence, acknowledgment, flags, data = tcp_segment(data)
                print('\nTCP Segment:')
                print(f'Source Port: {src_port}')
                print(f'Destination Port: {dest_port}')
                print(f'Sequence: {sequence}')
                print(f'Acknowledgment: {acknowledgment}')
                print(f'Flags: {flags}')

if __name__ == '__main__':
    main()
