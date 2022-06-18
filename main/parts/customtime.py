import ntptime
#ntptime is an mmpython builtin
import time

def printtime():
    print("Local time before synchronization：%s" %str(time.localtime()))

    time.sleep(3)
    ntptime.settime()

    print("Local time after synchronization：%s" %str(time.localtime()))