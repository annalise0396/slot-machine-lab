from gpiozero import LED
from gpiozero import Button
import tm1637
import time
import random

display = tm1637.TM1637(clk=4, dio=22) #GPIO pins 4 and 22


button = Button(12)

red = LED(17)

while True:
    if button.is_pressed:
        random_num = random.randint(1000, 9999) #random number 1000-9999
        display.number(random_num)
        print([b for b in display.buf])
        


