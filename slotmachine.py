from gpiozero import LED
from gpiozero import Button
import tm1637
import time
import random
from time import sleep

display = tm1637.TM1637(clk=6, dio=22) #GPIO pins 6 and 22


button = Button(23)
button2 = Button(12)

red = LED(17)

while True:
    if button.is_pressed:
        random_num = random.randint(1000, 9999) #random number 1000-9999
        display.number(random_num)
        digit_list = [int(digit) for digit in str(random_num)]
        while all(x == digit_list[0] for x in digit_list):
            red.on()
            sleep(1)
            red.off()
            sleep(1)
    if button2.is_pressed:
        secret_button = 4444
        display.number(secret_button)
        digit_list_2 = [int(digit) for digit in str(secret_button)]
        while all(x == digit_list_2[0] for x in digit_list_2):
            red.on()
            sleep(1)
            red.off()
            sleep(1)
        
        


