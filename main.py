'''




    ____                                          _     
   / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
  | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
  | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ |
   \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/


    
    export AMPY_PORT=/dev/ttyUSB0
    ampy mkdir /lib
    ampy put BlynkLib.py /lib/BlynkLib.py
    ampy put main.py main.py
    
'''


import BlynkLib
import network
import machine
import time
WIFI_SSID = 'myself'
WIFI_PASS = 'password'

BLYNK_AUTH = '4ssDYO0LRRoMwQHFPWvlakkGF0bYaptf'

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH)


@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')
def toggle(p):
    p.value(not p.value())
pin_x=machine.Pin(2,machine.Pin.OUT)
pin_y=machine.Pin(0,machine.Pin.OUT)
pin_x.value(1)
pin_y.value(1)


@blynk.on("V2")
def v3_write_handler(value):
    x_val=value[0]
    y_val=value[1]
    print('Current X value: {}'.format(x_val))
    print('Current y value: {}'.format(y_val))
    if int(x_val)<500: #left
        pin_x.value(1)
        pin_y.value(0)
    elif (int(y_val)<500): # Down
        pin_x.value(1)
        pin_y.value(1)
    elif int(x_val)>750: # Right
        pin_x.value(0)
        pin_y.value(1)
    elif (int(y_val)>750): # Up
        pin_x.value(0)
        pin_y.value(0)
    else:                   # center
        pin_x.value(1)
        pin_y.value(1)
def runLoop():
    while True:
        blynk.run()
        machine.idle()
runLoop()




