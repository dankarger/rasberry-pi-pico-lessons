import RGB1602
import time
lcd = RGB1602.RGB1602(16, 2)


def write_text(text):
    lcd.setCursor(0, 0)
    time.sleep(0.3)
    for letter in text:
        lcd.printout(letter)
        time.sleep(0.3)


def reset_lcd(seconds):
    time.sleep(seconds)
    lcd.clear()
