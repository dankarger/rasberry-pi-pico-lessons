import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

file = open("temp.txt", "w")


while True:
    number = 1
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    file.write(str(temperature) + "\n")
    number += 1
    file.flush()
    utime.sleep(1)