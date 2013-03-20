#!/usr/bin/env python                                                     
# -*- coding: UTF-8 -*-  
# The code here is the same as "https://code.google.com/p/chinese-lunar-calendar/", I added here for the copyright consideration.

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

def create_arrow_button(arrow_type, shadow_type):
    button = gtk.Button();
    arrow = gtk.Arrow(arrow_type, shadow_type);
    button.add(arrow)
    button.show()
    arrow.show()
    return button


class Calendar:


    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("中国万年历查询")
        self.window.set_size_request(600, 480)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(5)
        self.window.set_resizable(False)
        self.vbox = gtk.VBox(False, 10)
        self.vbox.set_border_width(10)
        self.window.add(self.vbox)

        #self.vbox.show()

        # create a tooltips object
        self.tooltips = gtk.Tooltips()
        self.tooltip1 = gtk.Tooltips()

        #add hbox to show button and combobox
        self.hbox = gtk.HBox(False,5)
        self.vbox.pack_start(self.hbox, False, False, 5) 

        #add yearLeft click button
        self.yearLeft = create_arrow_button(gtk.ARROW_LEFT, gtk.SHADOW_IN)
        self.hbox.pack_start(self.yearLeft, False, False, 3)
        self.tooltips.set_tip(self.yearLeft, "年份向前")  
        self.yearLeft.connect("clicked", self.arrow_callback, "year_left")

        #add yearComboBox for chose
        self.yearDates = []
        self.yearComboBox = gtk.combo_box_entry_new_text()
        for i in range(1900,2050):  
            self.yearDates.append(str(i)+"年")

        for a in self.yearDates:
            self.yearComboBox.append_text(a)

        self.currentyearIndex = self.yearDates.index(str(currentYear) + "年")

        self.yearComboBox.set_active(self.currentyearIndex)
        self.yearComboBox.set_size_request(80,30)
        self.yearComboBox.child.connect('changed', self.ChangedTime)
        self.tooltips.set_tip(self.yearComboBox, "请选择或输入年份")
        self.hbox.pack_start(self.yearComboBox, False, False, 3)

        #add yearRight click button
        self.yearRight = create_arrow_button(gtk.ARROW_RIGHT, gtk.SHADOW_ETCHED_OUT)
        self.hbox.pack_start(self.yearRight, False, False, 3)
        self.tooltips.set_tip(self.yearRight, "年份向后")
        self.yearRight.connect("clicked", self.arrow_callback, "year_right")

        #add separator
        self.separator = gtk.VSeparator()
        self.hbox.pack_start(self.separator, False, False, 10)

        #add monthLeft click button
        self.monthLeft = create_arrow_button(gtk.ARROW_LEFT, gtk.SHADOW_ETCHED_IN)
        self.hbox.pack_start(self.monthLeft, False, False, 3)
        self.tooltips.set_tip(self.monthLeft, "月份向前")
        self.monthLeft.connect("clicked", self.arrow_callback, "month_left")

        #add monthComboBox for chose
        self.monthComboBox = gtk.combo_box_entry_new_text()
        self.monthDates = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
        self.weeks = ["一", "二", "三", "四", "五", "六", "日"]
        for i in self.monthDates:
            self.monthComboBox.append_text(i)

      
        self.currentmonthIndex = self.monthDates.index(str(currentMonth)+"月")
        self.monthComboBox.set_active(self.currentmonthIndex)
        self.monthComboBox.set_size_request(70,30)
        self.monthComboBox.child.connect('changed', self.ChangedTime)
        self.tooltips.set_tip(self.monthComboBox, "请选择月份")
        self.hbox.pack_start(self.monthComboBox, False, False, 3)

        #add monthRight click button
        self.monthRight = create_arrow_button(gtk.ARROW_RIGHT, gtk.SHADOW_ETCHED_OUT)
        self.hbox.pack_start(self.monthRight, False, False, 3)
        self.tooltips.set_tip(self.monthRight, "月份向后")
        self.monthRight.connect("clicked", self.arrow_callback, "month_right")

        #add separator
        self.separator = gtk.VSeparator()
        self.hbox.pack_start(self.separator, False, False, 10)

        #add label to show lunar year and chinese zodiac
        yearDate = Date(currentYear, currentMonth)
        self.lunarLabel = gtk.Entry()
        self.lunarLabel.set_text("农历:[%s]年 生肖:[%s]" \
                                %(yearDate.GanZhiYear(),yearDate.Zodiac()))
        self.lunarLabel.set_editable(False)
        self.lunarLabel.set_size_request(185,30)
        self.hbox.pack_start(self.lunarLabel, False, False, 3)
        self.lunarLabel.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#5F9EA0"))
        self.lunarLabel.modify_font(pango.FontDescription("Sans Bold 10"))

        #add calendar frame and vbox
        self.frame = gtk.Frame("Calendar")
        self.vbox.pack_start(self.frame, True, True, 10)

        self.window.show_all()

        #show current day's calendar
        self.Draw(currentYear, currentMonth)
    

    def Draw(self, year, month):

        self.vbox2 = gtk.VBox(False, 2)
        self.frame.add(self.vbox2)

        self.hbox = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox, False, False, 10)

        #add weeklabel
        self.weeklabel0 = gtk.Label(self.weeks[6])
        self.weeklabel0.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox.pack_start(self.weeklabel0, False, False, 0)

        self.weeklabel1 = gtk.Label(self.weeks[0])
        self.hbox.pack_start(self.weeklabel1, False, False, 0)

        self.weeklabel2 = gtk.Label(self.weeks[1])
        self.hbox.pack_start(self.weeklabel2, False, False, 0)

        self.weeklabel3 = gtk.Label(self.weeks[2])
        self.hbox.pack_start(self.weeklabel3, False, False, 0)

        self.weeklabel4 = gtk.Label(self.weeks[3])
        self.hbox.pack_start(self.weeklabel4, False, False, 0)

        self.weeklabel5 = gtk.Label(self.weeks[4])
        self.hbox.pack_start(self.weeklabel5, False, False, 0)

        self.weeklabel6 = gtk.Label(self.weeks[5])
        self.weeklabel6.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox.pack_start(self.weeklabel6, False, False, 0)

        #set font for week
        for i in range(0, 7):
            exec "self.weeklabel" + str(i) + \
            ".modify_font(pango.FontDescription(\"Sans Bold Italic 12\"))"

        #add solar line1
        self.shbox1 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.shbox1, False, False, 2)

        #add solarlabel0 to solarlabel6
        self.solarlabel0 = gtk.Label()
        self.solarlabel0.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.shbox1.pack_start(self.solarlabel0, True,True, 0)
        self.solarlabel1 = gtk.Label()
        self.shbox1.pack_start(self.solarlabel1, True,True, 0)
        self.solarlabel2 = gtk.Label()
        self.shbox1.pack_start(self.solarlabel2, True,True, 0)
        self.solarlabel3 = gtk.Label()
        self.shbox1.pack_start(self.solarlabel3, True,True, 0)
        self.solarlabel4 = gtk.Label()
        self.shbox1.pack_start(self.solarlabel4, True,True, 0)
        self.solarlabel5 = gtk.Label()
        self.shbox1.pack_start(self.solarlabel5, True,True, 0)
        self.solarlabel6 = gtk.Label()
        self.solarlabel6.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("red"))
        self.shbox1.pack_start(self.solarlabel6, True,True, 0)

        #add lunar line1
        self.lhbox1 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.lhbox1, False, False, 2)

        #add lunarlabel0 to lunarlabel6
        self.lunarlabel0 = gtk.Label()
        self.lunarlabel0.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.lhbox1.pack_start(self.lunarlabel0, True,True, 0)
        self.lunarlabel1 = gtk.Label()
        self.lhbox1.pack_start(self.lunarlabel1, True,True, 0)
        self.lunarlabel2 = gtk.Label()
        self.lhbox1.pack_start(self.lunarlabel2, True,True, 0)
        self.lunarlabel3 = gtk.Label()
        self.lhbox1.pack_start(self.lunarlabel3, True,True, 0)
        self.lunarlabel4 = gtk.Label()
        self.lhbox1.pack_start(self.lunarlabel4, True,True, 0)
        self.lunarlabel5 = gtk.Label()
        self.lhbox1.pack_start(self.lunarlabel5, True,True, 0)
        self.lunarlabel6 = gtk.Label()
        self.lunarlabel6.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.lhbox1.pack_start(self.lunarlabel6, True,True, 0)

        #add solar line2
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add solarlabel7 to solarlabel13
        self.solarlabel7 = gtk.Label()
        self.solarlabel7.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel7, True,True, 0)
        self.solarlabel8 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel8, True,True, 0)
        self.solarlabel9 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel9, True,True, 0)
        self.solarlabel10 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel10, True,True, 0)
        self.solarlabel11 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel11, True,True, 0)
        self.solarlabel12 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel12, True,True, 0)
        self.solarlabel13 = gtk.Label()
        self.solarlabel13.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel13, True,True, 0)

        #add lunar line2
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add lunarlabel8 to lunarlabel14
        self.lunarlabel7 = gtk.Label()
        self.lunarlabel7.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel7, True,True, 0)
        self.lunarlabel8 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel8, True,True, 0)
        self.lunarlabel9 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel9, True,True, 0)
        self.lunarlabel10 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel10, True,True, 0)
        self.lunarlabel11 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel11, True,True, 0)
        self.lunarlabel12 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel12, True,True, 0)
        self.lunarlabel13 = gtk.Label()
        self.lunarlabel13.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel13, True,True, 0)

        #add solar line3
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add solarlabel15 to solarlabel21
        self.solarlabel14 = gtk.Label()
        self.solarlabel14.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel14, True,True, 0)
        self.solarlabel15 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel15, True,True, 0)
        self.solarlabel16 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel16, True,True, 0)
        self.solarlabel17 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel17, True,True, 0)
        self.solarlabel18 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel18, True,True, 0)
        self.solarlabel19 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel19, True,True, 0)
        self.solarlabel20 = gtk.Label()
        self.solarlabel20.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel20, True,True, 0)

        #add lunar line3
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add lunarlabel15 to lunarlabel21
        self.lunarlabel14 = gtk.Label()
        self.lunarlabel14.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel14, True,True, 0)
        self.lunarlabel15 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel15, True,True, 0)
        self.lunarlabel16 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel16, True,True, 0)
        self.lunarlabel17 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel17, True,True, 0)
        self.lunarlabel18 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel18, True,True, 0)
        self.lunarlabel19 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel19, True,True, 0)
        self.lunarlabel20 = gtk.Label()
        self.lunarlabel20.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel20, True,True, 0)

        #add solar line4
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add solarlabel22 to solarlabel28
        self.solarlabel21 = gtk.Label()
        self.solarlabel21.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel21, True,True, 0)
        self.solarlabel22 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel22, True,True, 0)
        self.solarlabel23 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel23, True,True, 0)
        self.solarlabel24 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel24, True,True, 0)
        self.solarlabel25 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel25, True,True, 0)
        self.solarlabel26 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel26, True,True, 0)
        self.solarlabel27 = gtk.Label()
        self.solarlabel27.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel27, True,True, 0)

        #add lunar line4
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add lunarlabel22 to lunarlabel28
        self.lunarlabel21 = gtk.Label()
        self.lunarlabel21.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel21, True,True, 0)
        self.lunarlabel22 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel22, True,True, 0)
        self.lunarlabel23 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel23, True,True, 0)
        self.lunarlabel24 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel24, True,True, 0)
        self.lunarlabel25 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel25, True,True, 0)
        self.lunarlabel26 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel26, True,True, 0)
        self.lunarlabel27 = gtk.Label()
        self.lunarlabel27.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel27, True,True, 0)

        #add solar line5
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add solarlabel29 to solarlabel35
        self.solarlabel28 = gtk.Label()
        self.solarlabel28.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel28, True,True, 0)
        self.solarlabel29 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel29, True,True, 0)
        self.solarlabel30 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel30, True,True, 0)
        self.solarlabel31 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel31, True,True, 0)
        self.solarlabel32 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel32, True,True, 0)
        self.solarlabel33 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel33, True,True, 0)
        self.solarlabel34 = gtk.Label()
        self.solarlabel34.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel34, True,True, 0)
        #add lunar line5
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add lunarlabel29 to lunarlabel35
        self.lunarlabel28 = gtk.Label()
        self.lunarlabel28.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel28, True,True, 0)
        self.lunarlabel29 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel29, True,True, 0)
        self.lunarlabel30 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel30, True,True, 0)
        self.lunarlabel31 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel31, True,True, 0)
        self.lunarlabel32 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel32, True,True, 0)
        self.lunarlabel33 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel33, True,True, 0)
        self.lunarlabel34 = gtk.Label()
        self.lunarlabel34.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel34, True,True, 0)

        #add solar line5
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add solarlabel36 to solarlabel42
        self.solarlabel35 = gtk.Label()
        self.solarlabel35.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel35, True,True, 0)
        self.solarlabel36 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel36, True,True, 0)
        self.solarlabel37 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel37, True,True, 0)
        self.solarlabel38 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel38, True,True, 0)
        self.solarlabel39 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel39, True,True, 0)
        self.solarlabel40 = gtk.Label()
        self.hbox2.pack_start(self.solarlabel40, True,True, 0)
        self.solarlabel41 = gtk.Label()
        self.solarlabel41.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.solarlabel41, True,True, 0)
        #add lunar line6
        self.hbox2 = gtk.HBox(True, 5)
        self.vbox2.pack_start(self.hbox2, False, False, 2)

        #add lunarlabel36 to lunarlabel42
        self.lunarlabel35 = gtk.Label()
        self.lunarlabel35.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel35, True,True, 0)
        self.lunarlabel36 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel36, True,True, 0)
        self.lunarlabel37 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel37, True,True, 0)
        self.lunarlabel38 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel38, True,True, 0)
        self.lunarlabel39 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel39, True,True, 0)
        self.lunarlabel40 = gtk.Label()
        self.hbox2.pack_start(self.lunarlabel40, True,True, 0)
        self.lunarlabel41 = gtk.Label()
        self.lunarlabel41.modify_fg(gtk.STATE_NORMAL,gtk.gdk.color_parse("red"))
        self.hbox2.pack_start(self.lunarlabel41, True,True, 0)

        self.window.show_all()


        solarMonthFirstDay = Date(year, month, 1)
        for day in range(1, solarMonthFirstDay.SolarDaysInMonth() + 1):
            solarDay = Date(year, month, day)
            weekday = solarMonthFirstDay.Weekday()
            self.num = day + weekday - 1
            solarDay.SolarToLunar()
            lunarday = solarDay.LunarDay()
            lunarmonth = solarDay.LunarMonth()
            originallunarday = solarDay.OriginalLunarDay()
 
            if self.num < (weekday+solarMonthFirstDay.SolarDaysInMonth()):
                exec "self.solarlabel" + str(self.num) + ".set_text" + "(" + "\"" + str(day) + "\"" + ")"
                sh = solarDay.SolarHoliday()
                lh = solarDay.LunarHoliday()

            #destroy label0-label6 if the solar first day star at label7
            if self.solarlabel7.get_text() == "1":
                self.shbox1.destroy()
                self.lhbox1.destroy()

            if lh is not None:
                exec "self.lunarlabel" + str(self.num) + ".set_text" + "(" + "\"" + lh + "\"" + ")"
                exec "self.tooltips.set_tip(self.lunarlabel" +str(self.num) + "," + "\"" \
                     + "阳历: " + str(year) + "年" + str(month) + "月" + str(day) + "日" + "  " + "星期"  \
                + str(self.weeks[solarDay.Weekday() - 1]) + "\\n"\
                     + "农历: " + str(solarDay.lunarYear - 1) + "年" + "  " +  lunarmonth + "  "\
                + originallunarday + "\\n"\
                     + "干支: " + solarDay.GanZhiYear() + "年" + "  "\
                + solarDay.GanZhiMonth() + "月" + "  " \
                + solarDay.GanZhiDay() + "日" + "\\n"\
                     + "节日: "+ lh + "\")"
                exec "self.lunarlabel" + str(self.num) + ".modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse(\"#0000FF\"))"
                exec "self.lunarlabel" + str(self.num) + ".modify_font(pango.FontDescription(\"Sans Bold 10\"))" 

            elif sh is not None:
                exec "self.lunarlabel" + str(self.num) + ".set_text" + "(" + "\"" + sh + "\"" + ")"
                exec "self.tooltips.set_tip(self.lunarlabel" +str(self.num) + "," + "\"" \
                     + "阳历: " + str(year) + "年" + str(month) + "月" + str(day) + "日" + "  " + "星期"  \
                + str(self.weeks[solarDay.Weekday() - 1]) + "\\n"\
                     + "农历: " + str(solarDay.lunarYear - 1) + "年" + "  " +  lunarmonth + "  "\
                + originallunarday + "\\n"\
                     + "干支: " + solarDay.GanZhiYear() + "年" + "  "\
                + solarDay.GanZhiMonth() + "月" + "  " \
                + solarDay.GanZhiDay() + "日" + "\\n"\
                     + "节日: "+ sh + "\")"
                exec "self.lunarlabel" + str(self.num) + ".modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse(\"#FF4500\"))"
                exec "self.lunarlabel" + str(self.num) + ".modify_font(pango.FontDescription(\"Sans Bold 10\"))"

            else:
                exec "self.lunarlabel" + str(self.num) + ".set_text" + "(" + "\"" + lunarday + "\"" + ")"
                exec "self.tooltips.set_tip(self.lunarlabel" +str(self.num) + "," + "\"" \
                     + "阳历: " + str(year) + "年" + str(month) + "月" + str(day) + "日" + "  " + "星期"  \
                + str(self.weeks[solarDay.Weekday() - 1]) + "\\n"\
                     + "农历: " + str(solarDay.lunarYear - 1) + "年" + "  " +  lunarmonth + "  "\
                + originallunarday + "\\n"\
                     + "干支: " + solarDay.GanZhiYear() + "年" + "  "\
                + solarDay.GanZhiMonth() + "月" + "  " \
                + solarDay.GanZhiDay() + "日"\
                     + "\")"


    def ChangedTime(self, yearChosed=currentYear, monthChosed=currentMonth):
        self.yearChosed=int(self.yearComboBox.get_child().get_text().decode('utf-8')[:-1])
        self.monthChosed=int(self.monthComboBox.get_child().get_text().decode('utf-8')[:-1])

        self.yearDate = Date(self.yearChosed, self.monthChosed)
        self.lunarLabel.set_text("农历:[%s]年 生肖:[%s]" %(self.yearDate.GanZhiYear(),self.yearDate.Zodiac()))

        self.currentyearIndex =  self.yearDates.index(str(self.yearChosed) + "年")
        self.currentmonthIndex = self.monthDates.index(str(self.monthChosed) + "月")

        self.vbox2.destroy()
        self.Draw(self.yearChosed, self.monthChosed)



    #click arrow button event
    def arrow_callback(self, widget, data):
        """respose to the arrow button which clicked"""

        if data == "year_left":
            self.currentyearIndex -= 1
            self.yearComboBox.set_active(self.currentyearIndex)
            self.ChangedTime(self.yearChosed, self.monthChosed)
            self.vbox2.destroy()
            self.Draw(self.yearChosed, self.monthChosed)

        elif data == "year_right":
            self.currentyearIndex += 1
            self.yearComboBox.set_active(self.currentyearIndex)
            self.ChangedTime(self.yearChosed, self.monthChosed)
            self.vbox2.destroy()
            self.Draw(self.yearChosed, self.monthChosed)

        elif data == "month_left":
            # the valid month should be in 2 to 12
            # since the index start from 0, so the month larger than index as 1
            if self.currentmonthIndex < 1 or self.currentmonthIndex > 11: return
            self.currentmonthIndex -= 1
            self.monthComboBox.set_active(self.currentmonthIndex)
            self.ChangedTime(self.yearChosed, self.monthChosed)
            self.vbox2.destroy()
            self.Draw(self.yearChosed, self.monthChosed)

        elif data == "month_right":
            # the valid month should be in 1 to 11
            # since the index start from 0, so the month larger than index as 1
            if self.currentmonthIndex < 0 or self.currentmonthIndex > 10: return
            self.currentmonthIndex += 1
            self.monthComboBox.set_active(self.currentmonthIndex)
            self.ChangedTime(self.yearChosed, self.monthChosed)
            self.vbox2.destroy()
            self.Draw(self.yearChosed, self.monthChosed)


def main():
    gtk.main()
    return 0 

if __name__ == "__main__":
    Calendar()
    main()
