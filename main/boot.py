import network
import time
# enable station interface and connect to WiFi access point
ssid="WONDERLAND"
pw="Kiskutya9"
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.ifconfig(('192.168.0.250', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
nic.connect(ssid, pw)
time.sleep(3)
if not nic.isconnected():
    while not nic.isconnected():
            print("unable to connect, trying again in 3")
            time.sleep(3)
            nic.connect(ssid, pw)
else:
    print("connected. IPs: " +str(nic.ifconfig()))