import network
import time
import senko #ota
import machine
import ntptime #mmpython builtin
from machine import Pin
import webrepl
import sys
import os
import gc

branch = "develop"
print(type(branch))


OTA = senko.Senko(user="gamb1t9", repo="micropython_clock", branch="%s" % branch, working_dir="main", files = ["boot.py", "main.py", "parts/customtime.py"] )

def ota_pull():
    gc.collect()
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

def ota_fetch():
    gc.collect()
    if OTA.fetch():
        print("There are available updates on the %s branch" % str(branch))
        ota_pull()
    else:
        print("there are NO updates on dev!!!")



# Wifi stuff
ssid="WONDERLAND"
pw="Kiskutya9"
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.ifconfig(('192.168.0.250', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

# retry if fails
for i in range(5):
    while True:
        try:
            if not nic.isconnected():
                nic.connect(ssid, pw)
            break
        except OSError: #Wifi Internal Error
            print("Failed at try " + str(i) + ", trying again...")
            time.sleep(2)
            continue

print("connected. IPs: " +str(nic.ifconfig()))

# time.sleep(3)
# if not nic.isconnected():
#     while not nic.isconnected():
#             print("unable to connect, trying again in 3")
#             time.sleep(3)
#             nic.connect(ssid, pw)
# else:
#     print("connected. IPs: " +str(nic.ifconfig()))