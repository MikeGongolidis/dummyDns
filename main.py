import socket
import argparse 


from utils import *

def lookup_domain(domain_name):
    
    query = build_query(domain_name,1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(query,("8.8.8.8",53))

    resp, _ = sock.recvfrom(1024) 

    response = parse_dns_packet(resp)

    print([ip_to_string(ip.data) for ip in response.answers])
    


def main():
    parser = argparse.ArgumentParser(description='Domain name and DNS type parser')
    parser.add_argument('domain', type=str, help='Domain name')
    parser.add_argument('record_type', type=int, help='DNS type')

    args = parser.parse_args()

    domain_name = args.domain
    record_type = args.record_type
    #lookup_domain(domain_name)
    print(resolveP(domain_name, record_type))
    
if __name__ == '__main__':
    main()