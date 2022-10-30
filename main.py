import RGB1602
import time
import machine
import utime
import write_text

led_onboard = machine.Pin(25, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

#  ---LCD CONFIG -----
colorR = 64
colorG = 128
colorB = 64

lcd = RGB1602.RGB1602(16, 2)

rgb1 = (148, 0, 110)  # 深紫罗兰色
rgb2 = (255, 0, 255)  # 紫色
rgb3 = (144, 249, 15)  # 青白
rgb4 = (0, 128, 60)  # 浅蓝
rgb5 = (255, 209, 0)  # 黄色
rgb6 = (248, 248, 60)  # 幽灵的白色
rgb7 = (80, 80, 145)  # 深蓝色
rgb8 = (255, 0, 0)  # 红色
rgb9 = (0, 255, 0)  # 青色


#  -----
tempTable = {
    10: 'cold',
    20: 'chill',
    30: 'hot'
}


def define_weather(temp):
    for number in tempTable:
        if temp <= number:
            return tempTable[number]


file = open("temp.txt", "a")
number = 22
lcd.setCursor(0, 0)
lcd.setColorWhite()


while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = str(27 - (reading - 0.706) / 0.001721)[0:4]
    lcd.printout(f"The Temp is:")
    lcd.setCursor(0, 1)
    lcd.printout(f"- {str(temperature)[0:4]} C -")
    file.write("hour " + str(number) + ": " + " TEMP-- " + str(temperature) + " c" + "\n")
    number += 1
    file.flush()
    for i in range(1800):
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = str(27 - (reading - 0.706) / 0.001721)[0:4]
        lcd.printout(f"The Temp is:")
        lcd.setCursor(0, 1)
        lcd.printout(f"- {str(temperature)[0:4]} C -")
        led_onboard.toggle()
        utime.sleep(1)