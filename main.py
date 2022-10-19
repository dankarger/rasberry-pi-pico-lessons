from machine import Pin
import time
import random

# Led:
value = 1
led = Pin(25, Pin.OUT)
led_external = Pin(15, Pin.OUT)

# Button
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# while True:
#     led(1)
#     led_external(b)
#     print('Value:{}'.format(value))
#     value = value + 1
#     time.sleep(0.5)
#     led_external(1)
#     time.sleep(0.25)
#     led_external(0)
#     time.sleep(0.25)
#     led(0)
#     led_external(1)
#     print('Led Off')
#     time.sleep(1)

while True:
    if button.value() == 1:
        print("You pressed the button! Value:{}".format(value) + ' times')
        value = value + 1
        time.sleep(0.3)
