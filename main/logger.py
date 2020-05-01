# logger.py  v0.1.1 r1.1



import machine
from time import sleep

#from machine import Pin, I2C
#from . import ssd1306
#from time import sleep


class MainLogger:
    def __init__(self):
        print('start LOGGER v0.1.1 r1.1')
#        led = Pin(13, Pin.OUT)
#        # ESP32 Pin assignment 
#        i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
#        oled_width = 128
#        oled_height = 64
#        oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
#        oled.text('start LOGGER 0.4', 0, 0)
#        oled.show()
#        print('done !')       
#        while True:
#            led.value(0)
#            sleep(0.1)
#            led.value(1)
#            sleep(0.1)

#        try:
#            sleep(2)

#             oled.text('start LOGGER 0.4 !', 0, 0)
#            oled.text('Hello, World 2!', 0, 10)
#            oled.text('Hello, World 3!', 0, 20)
#            oled.text('Hello, World 4!', 0, 30)
#            oled.text('Hello, World 5!', 0, 40)
#            oled.text('Hello, World 6!', 0, 50)
#            oled.show()
#        except OSError as e:
#            print('Failed to read sensor.')


#def process():
#	import time

#	for i in range(0,10):
#		print(i*3)

#	time.sleep(3)