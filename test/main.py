import time
import machine
import senko #ota

def ota_init():
    OTA = senko.Senko(user="gamb1t9", repo="micropython_clock", working_dir="test", files = ["boot.py", "main.py"])
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

led=Pin(2,Pin.OUT)

for i in range(0,20):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)

