import ipaddress as ip
ip_address = ip.IPv4Network('192.0.2.0/25')
for addrs in ip_address:
    print(f"{addrs}")
