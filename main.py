import RGB1602
import time
import machine
import utime
import write_text
import _thread

led_onboard = machine.Pin(25, machine.Pin.OUT)
right_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)


screen_number = 1

# button thread
global button_pressed
# button_pressed = False
temp = 0


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


reading = sensor_temp.read_u16() * conversion_factor
temperature = 27 - (reading - 0.706) / 0.001721


def screen_one(temp):
    lcd.clear()
    lcd.setCursor(0, 0)
    # write_text.write_text(f"The Temp is:")
    # lcd.setCursor(0, 1)
    # write_text.write_text(f"- {temp} C -")
    lcd.printout(f"The Temp is:")
    lcd.setCursor(0, 1)
    lcd.printout(f"- {temp} C -")


def screen_two(temp):
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout(f'It is {define_weather(int(temp))} !')


def button_handler(pin):
    global screen_number
    global reading
    global temperature
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    if screen_number == 1:
        screen_number = 2
        print("screen: " + str(screen_number))
        screen_one(str(temperature)[0:4])
    elif screen_number == 2:
        screen_number = 1
        print("screen: " + str(screen_number))
        screen_two(temperature)
    # right_button.irq(handler=None)


right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)


#
# file = open("temp.txt", "w")
hour_number = 1


lcd.setColorWhite()

screen_one(str(temperature)[0:4])
#
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    temp = temperature
    if screen_number == 1:
        screen_one(str(temperature)[0:4])
#     # elif screen_number == 2:
#     #     screen_two(temperature)
#     # file.write("hour " + str(hour_number) + ": " + " TEMP-- " + str(temperature) + " c" + "\n")
#     # hour_number += 1
#     # file.flush()
    for i in range(10):
        led_onboard.toggle()
        utime.sleep(3)
#     utime.sleep(1)