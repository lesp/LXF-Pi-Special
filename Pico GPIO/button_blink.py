from machine import Pin
import time
led = Pin(15, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)
led.low()
while True:
    if button.value() == 0:
        led.toggle()
        print("Toggle")
        time.sleep(0.2)
    else:
        pass