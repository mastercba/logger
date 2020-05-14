# time_date.py


import network
import time
import utime
import machine
from ntptime import settime


# year, month, day, day_of_week, hour, minute, second, day_of_year
# date = list()

class MyTimeDate:
    def __init__(self):
        # print('init MyTimeDate...')
        year = 2000
        while year < 2019:
            try:
                settime()
            except:
                pass
            rtc = machine.RTC()
            utcNTPtime = utime.time()
            myTime = utcNTPtime - 14400
            (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime(myTime)
            date = (year, month, mday, hour, minute, second, weekday, yearday)
            # rtc.init((year, month, mday, hour, minute, second, weekday, yearday))
            # machine.RTC.datetime((year, month, mday, hour, minute, second, weekday, yearday))
        self.year = year
        self.month = month
        self.mday = mday
        self.hour = hour
        self.minute = minute
        self.second = second
        self.weekday = weekday
        self.yearday = yearday
        # print(date)

    # read local TimeDate
    def readTimeDate(self):
        print('read MyTimeDate...')
        # print("Hora:",self.hour)
        # print("Minute:",self.minute)
        return self.hour, self.minute, self.year, self.month, self.mday