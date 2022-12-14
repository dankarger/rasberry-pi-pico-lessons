# Example using PIO to drive a set of WS2812 LEDs.

import array
import time
import rp2
import machine
from machine import Pin
import utime
import _thread
import math

# Configure the number of WS2812 LEDs.
NUM_LEDS = 8

potentiometer = machine.ADC(26)
conversion_factor = 1000 / (65535)
rate = 1000 - math.floor(potentiometer.read_u16() * conversion_factor)

sensor_pir = machine.Pin(28, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1).side(0)[T3 - 1]
    jmp(not_x, "do_zero").side(1)[T1 - 1]
    jmp("bitloop").side(1)[T2 - 1]
    label("do_zero")
    nop().side(0)[T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on Pin(22).
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(0))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])


def rate_reader():
    global rate
    while True:
        # potentiometer.read_u16() > 770
        voltage = potentiometer.read_u16() * conversion_factor
        if voltage < 10:
            rate = 0
        else:
            rate =math.ceil(voltage)
        print(math.floor(voltage))
        utime.sleep(rate)


_thread.start_new_thread(rate_reader, ())

# Cycle colours.
def pir_handler(pin):
    for i in range(4 * NUM_LEDS):
        for j in range(NUM_LEDS):
            r = j * 100 // (NUM_LEDS - 1)
            b = 100 - j * 100 // (NUM_LEDS - 1)
            if j!=i % NUM_LEDS:
                r >>= 3
                b >>= 3
            ar[j] = r << 16 | b
        sm.put(ar, 8)
        time.sleep_ms(rate)


    # Fade out.
    for i in range(24):
        for j in range(NUM_LEDS):
            ar[j] >>= 1
        sm.put(ar, 8)
        time.sleep_ms(100)


sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)