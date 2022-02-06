import time
from machine import Pin
import machine
import senko #ota
import webrepl

OTA = senko.Senko(user="gamb1t9", repo="micropython_clock", branch="develop", working_dir="main", files = ["boot.py", "main.py"])
    
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


ota_fetch()

#just a comment
led=Pin(2,Pin.OUT)
for i in range(0,10):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)
print("successfull")

webrepl.start()
#just another comment to see whats what
#anadavan
print("dissiz fun! I just have to push code to this branch and the thing will pull it! TEST")