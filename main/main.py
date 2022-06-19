import time
from machine import Pin
import machine
import webrepl
import sys
import os
sys.path.append("/parts")

try:
    from customtime import printtime
except SyntaxError as e:
    print(sys.print_exception(e))
    pass



ota_fetch()
gc.collect()

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