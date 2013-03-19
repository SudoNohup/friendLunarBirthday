#!/usr/bin/env python                                                     
# -*- coding: UTF-8 -*-  

import pygtk
import gtk
import os
import sys
import pango

from date import *
import time

currentTime = time.localtime()
currentYear = currentTime[0]
currentMonth = currentTime[1]

def main():
    strbuf = 'Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Private\n'
    outfile = open("cal.csv","w")
    for year in range(2013,2050):
        for month in range(1,12):
            solarMonthFirstDay = Date(year, month, 1)
            for day in range(1,solarMonthFirstDay.SolarDaysInMonth()+1):
                solarDay = Date(year, month, day)
                #weekday = solarMonthFirstDay.weekday()
                #self.num = day + weekday -1
                solarDay.SolarToLunar()
                lunarday = solarDay.LunarDay()
                lunarmonth = solarDay.LunarMonth()

                originallunarday = solarDay.OriginalLunarDay()

                fh = solarDay.FriendBirthday()
                
                
                if fh is not None:
                      #print fh
                      #print "year"+str(year)+"month"+str(month)+"day"+str(day)
                      ss = fh+','+formatstr(day)+'/'+formatstr(month)+'/'+formatstr(year%100)+',07:10:00 AM,'+formatstr(day)+'/'+formatstr(month)+'/'+formatstr(year%100)+',07:15:00 AM,False,birthday,True'
                      print ss
                      strbuf += ss+'\n'
    outfile.write(strbuf)
    return 0

def formatstr(num):
    if (num < 10):
        resstr = '0'+str(num)
    else:
        resstr = str(num)
    return resstr

if __name__ == "__main__":
    main()
