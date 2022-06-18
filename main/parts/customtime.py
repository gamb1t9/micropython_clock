import ntptime
#ntptime is an mmpython builtin
import time

def printtime():
    print("Local time before synchronization：%s" %str(time.localtime()))
    
    time.sleep(3)
    # ntptime.settime(timezone=1,server = 'pool.ntp.org') 
    # TypeError: unexpected keyword argument 'timezone' all hail the docs
    ntptime.settime()

    print("Local time after synchronization：%s" %str(time.localtime()))