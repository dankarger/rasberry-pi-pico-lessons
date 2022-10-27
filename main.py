import machine
import utime
import _thread

led_onboard = machine.Pin(25, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

#
# def blink_led():
#     while True:
#         led_onboard.value(1)
#         utime.sleep(1)
#         led_onboard.value(0)
#
#
# _thread.start_new_thread(blink_led, ())

file = open("temp.txt", "w")
number = 1

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    file.write(str(number) + ": " + str(temperature) + "\n")
    number += 1
    file.flush()
    for i in range(10):
        led_onboard.toggle()
        utime.sleep(1)
