import time
from machine import Pin
import machine
import webrepl

from parts/time import printtime



ota_fetch()

print("i'll flash for a couple of times just to amuse you")
#just a comment
led=Pin(2,Pin.OUT)
for i in range(0,10):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)

webrepl.start()
#just another comment to see whats what
#anadavan
print("READY")
printtime()