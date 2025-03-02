from ipaddress import ip_network

for mask in range(33):
    net1 = ip_network(f'84.77.47.132/{mask}', False)
    net2 = ip_network(f'84.77.48.132/{mask}', False)
    if net1 == net2:
        print(net1, ' | ', net2)

print(int('11100000', 2))
# Ответ: 224
