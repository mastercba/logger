# logger.py


from machine import Pin, I2C
from time import sleep
from . import time_date
from . import ota_updater
# from . import ssd1306


# ESP32 BlueLed Pin
led = Pin(13, Pin.OUT, value=0)  # BlueLed Pin


class MainLogger:
    def __init__(self):
        print('start LOGGER')
        process()


# ----------------------------------------------------------
def process():
    while True:
        blink_blue_led()  # BBL
        date = time_date.MyTimeDate()  # read Time&Date
        dt = date.readTimeDate()
        print(dt[0], ":", dt[1], "/", dt[2], "/", dt[3], "/", dt[4])
        if dt[0] == 21 and dt[1] == 00:  # refresh Time&Date
            date = time_date.MyTimeDate()
            dt = date.readTimeDate()
            newFirmware()  # CHECK/DOWNLOAD/INSTALL/REBOOT


# ----------------------------------------------------------

# BlinkBlueLed
def blink_blue_led():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(5.0)

# NewUPdate2install?
def newFirmware():
    from main import ota_updater
    ota_updater = ota_updater.OTAUpdater('https://github.com/mastercba/logger')
    ota_updater.download_and_install_update_if_available('TORRIMORA', 'santino989')
    # ota_updater.using_network('TORRIMORA', 'santino989')
    ota_updater.check_for_update_to_install_during_next_reboot()
        
        
        
        
        
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