import network
import time
import webrepl
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.ifconfig(('192.168.0.250', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
nic.connect('WONDERLAND', 'Kiskutya9')
time.sleep(3)
if nic.isconnected():
    print("connected. IPs: " +str(nic.ifconfig()))
    webrepl.start()
