import RGB1602
import time
import machine
import math
import write_text

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

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

# space_invader = [0x4,0xe,0x1f,0x15,0x1f,0xa,0x1b,0x0]
# lcd.display(0, space_invader)

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
    write_text.write_text(f"- {str(temperature)[0:4]} C")
    # lcd.setRGB(rgb3[0], rgb3[1], rgb3[2])
    # reset_lcd(3)
    lcd.setCursor(0, 0)
    write_text.write_text(' - :)')
    # lcd.setRGB(rgb4[0], rgb4[1], rgb4[2])
    time.sleep(2)
    write_text.write_text(' Bye Bye!')
    # lcd.setRGB(rgb9[0], rgb9[1], rgb9[2])
    write_text.reset_lcd(3)
    time.sleep(2)
