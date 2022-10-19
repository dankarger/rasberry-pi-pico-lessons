from machine import Pin
import time
import random

# Led:
# value = 1
# led = Pin(25, Pin.OUT)
# led_external = Pin(15, Pin.OUT)

# Button
# button = Pin(14, Pin.IN, Pin.PULL_DOWN)

led_red = Pin(15, Pin.OUT)
led_amber = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)

while True:
    led_red.value(1)
    time.sleep(0.2)
    led_amber.value(1)
    time.sleep(0.2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    time.sleep(0.5)
    led_green.value(0)
    led_amber.value(1)
    time.sleep(0.3)
    led_amber.value(0)
#
# while True:
#     led(1)
#     led_external(0)
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
#
# while True:
#     if button.value() == 1:
#         print("You pressed the button! Value:{}".format(value) + ' times')
#         value = value + 1
#         time.sleep(0.3)

#
# while True:
#     # if button.value() == 1:
#     #     # print(button.value())
#     #     print('t')
#     #     led_external.value(0)
#     #     time.sleep(2)
#     led_external.value(1)
#     led(1)
#     time.sleep(1)
#     print('2')
#     led(0)
#     led_external(0)
