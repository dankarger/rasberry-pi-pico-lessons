import machine
import time
import utime

#
# sensor_pir = machine.Pin(28, machine.Pin.IN)
# led = machine.Pin(15, machine.Pin.OUT)

#
# def pir_handler(pin):
#     print("ALARM! Motion detected!")
#     for i in range(50):
#         led.value(1)
#         utime.sleep_ms(100)
#         led.value(0)
#
#
# sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
#
# while True:
#     led.value(1)
#     utime.sleep(5)
#     led.value(0)
