import RGB1602
import time
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

#  ---LCD CONFIG -----

lcd = RGB1602.RGB1602(16, 2)

#  -----
tempTable = {
    10: 'cold',
    20: 'chill',
    30: 'hot'
}


def define_weather(temp):
    for result in tempTable:
        if temp >= result:
            return tempTable[result]


file = open("temp.txt", "a")
number = 1
lcd.setCursor(0, 0)
lcd.setColorWhite()


while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = str(27 - (reading - 0.706) / 0.001721)[0:4]
    lcd.printout(f"The Temp is:")
    lcd.setCursor(0, 1)
    lcd.printout(f"- {str(temperature)[0:4]} C -")
    file.write("hour " + str(number) + ": " + " TEMP-- " + str(temperature) + " c" + "\n")
    number = number + 1
    file.flush()
    for i in range(1800):
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = str(27 - (reading - 0.706) / 0.001721)[0:4]
        lcd.printout(f"The Temp is:")
        lcd.setCursor(0, 1)
        lcd.printout(f"- {str(temperature)[0:4]} C -")
        led_onboard.toggle()
        utime.sleep(3600)