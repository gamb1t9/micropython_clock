from network import WLAN
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'WONDERLAND':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'Kiskutya9'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break