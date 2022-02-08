import network
import time
import senko #ota
import machine

OTA = senko.Senko(user="gamb1t9", repo="micropython_clock", branch="develop", working_dir="main", files = ["boot.py", "main.py", "test/time.py"])
    
def ota_pull():
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

def ota_fetch():
    if OTA.fetch():
        print("There are available updates on the DEVELOP branch")
        ota_pull()
    else:
        print("there are NO updates on dev!!!")



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