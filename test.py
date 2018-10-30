import BAC0

bacnet=BAC0.connect(ip='192.168.1.123/24')


print(bacnet.devices)
