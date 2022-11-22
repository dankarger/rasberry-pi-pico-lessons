import RGB1602
import time
lcd = RGB1602.RGB1602(16, 2)


def write_text(text):
    lcd.setCursor(0, 0)
    for letter in text:
        lcd.printout(letter)
        time.sleep(0.1)


def reset_lcd(seconds):
    time.sleep(seconds)
    lcd.clear()
