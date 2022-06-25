#import ntptime if boot.py can import stuff 'globally', then import this there and see
#ntptime is an mmpython builtin
import time


actual_time=time.localtime()
def printtime():
    print("Local time before synchronization：%s" %str(time.localtime()))
    
    time.sleep(3)
    # ntptime.settime(timezone=1,server = 'pool.ntp.org') 
    # TypeError: unexpected keyword argument 'timezone' all hail the docs
    success = 1
    for i in range(5):
        try:
            if success == 1:
                ntptime.settime()
                success = 0
            break
        except:
            time.sleep(5)
            continue
    #the dirty way: add 2 hours
    actual_time=list(time.localtime())
    actual_time[3] = actual_time[3] + 2
    print("Local time after sync and modified timezone：%s" %str(actual_time))
