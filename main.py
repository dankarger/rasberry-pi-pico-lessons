import RGB1602
import time
import machine
import math
import write_text

led_onboard = machine.Pin(25, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

#  ---LCD CONFIG -----
lcd = RGB1602.RGB1602(16, 2)

#  -------------------
tempTable = {
    'very cold': [-10, 10],
    'cold': [11, 19],
    'nice': [20, 25],
    'hot': [25, 40]
}


def define_weather(temp):
    for result in tempTable:
        if tempTable[result][0] <= temp <= tempTable[result][1]:
            return result


while True:
    lcd.setCursor(0, 0)
    lcd.setColorWhite()
    write_text.write_text('Hello World!')
    write_text.reset_lcd(1)
    # lcd.setRGB(rgb1[0], rgb1[1], rgb1[2])
    lcd.setCursor(0, 0)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    # print(temperature)
    write_text.write_text(f"The Temp is:")
    lcd.setCursor(0, 1)
    write_text.write_text(f"- {str(temperature)[0:4]} C -")
    # lcd.setRGB(rgb3[0], rgb3[1], rgb3[2])
    write_text.reset_lcd(3)
    lcd.setCursor(0, 0)

    write_text.write_text(f'It is {define_weather(temperature)}  !')

    # lcd.setRGB(rgb4[0], rgb4[1], rgb4[2])
    time.sleep(2)
    lcd.setCursor(0, 1)
    write_text.write_text('Have fun')
    write_text.write_text('  :)')
    # lcd.setRGB(rgb9[0], rgb9[1], rgb9[2])
    write_text.reset_lcd(3)
    time.sleep(2)
