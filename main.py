from machine import Pin
import time
import random

value = 0
led = Pin(25, Pin.OUT)
led_external = Pin(15, Pin.OUT)

while True:
    led(1)
    led_external(b)
    print('Value:{}'.format(value))
    value = value + 1
    time.sleep(0.5)
    led_external(1)
    time.sleep(0.25)
    led_external(0)
    time.sleep(0.25)
    led(0)
    led_external(1)
    print('Led Off')
    time.sleep(1)
#
#
# import machine
# import utime
#
# led_external = machine.Pin(15, machine.Pin.OUT)
#
# while True:
#     led_external.toggle()
#     utime.sleep(5)
