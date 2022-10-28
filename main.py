import RGB1602
import time
import math

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


# set the cursor to column 0, line 1


def write_text(text):
    lcd.setCursor(0, 0)
    time.sleep(0.3)
    for letter in text:
        lcd.printout(letter)
        time.sleep(0.3)


def reset_lcd(seconds):
    time.sleep(seconds)
    lcd.clear()


while True:
    lcd.setCursor(0, 0)
    lcd.setColorWhite()
    write_text('Hello World!')
    reset_lcd(1)
    lcd.setRGB(rgb1[0], rgb1[1], rgb1[2])
    lcd.setCursor(0, 0)
    write_text("Nice to meet You")
    lcd.setRGB(rgb3[0], rgb3[1], rgb3[2])
    # reset_lcd(3)
    lcd.setCursor(0, 1)
    write_text(':)')
    lcd.setRGB(rgb4[0], rgb4[1], rgb4[2])
    time.sleep(2)
    write_text(' Bye Bye!')
    lcd.setRGB(rgb9[0], rgb9[1], rgb9[2])
    reset_lcd(3)
    time.sleep(2)

#
#
#
# import RGB1602
# import time
# import math
# import write_text
#
# colorR = 64
# colorG = 128
# colorB = 64
#
# lcd = RGB1602.RGB1602(16, 2)
#
# t = 0
#
# while True:
#     r = int((abs(math.sin(3.14 * t / 180))) * 255);
#     g = int((abs(math.sin(3.14 * (t + 60) / 180))) * 255);
#     b = int((abs(math.sin(3.14 * (t + 120) / 180))) * 255);
#     t = t + 3;
#
#     lcd.setRGB(r, g, b);
#     # set the cursor to column 0, line 1
#     lcd.setCursor(0, 0)
#     # print the number of seconds since reset:
#
#     # print the number of seconds since reset:
#     lcd.printout("1Waveshare")
#     # write_text.write_text('Hello World')
#     lcd.setCursor(0, 1)
#
#     # lcd.printout("Hello,World!")
#     time.sleep(0.3)
