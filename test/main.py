import time
import machine
import senko #ota

OTA = senko.Senko(user="gamb1t9", repo="micropython_clock", working_dir="test", files = ["boot.py", "main.py"])
    
def ota_pull():
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

def ota_fetch():
    if OTA.fetch()
        print("There are available updates on the master")


ota_fetch()
#just a comment
led=Pin(2,Pin.OUT)
for i in range(0,20):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)

