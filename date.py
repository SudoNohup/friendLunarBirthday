#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from datetime import date

yearCode = [
	#0x04bd8, 0x04ae0, 0x0a570, 0x054d5, 0x0d260, # 1904
	#0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2, # 1909
	#0x04ae0, 0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, # 1914
	#0x0b540, 0x0d6a0, 0x0ada2, 0x095b0, 0x14977, # 1919
	#0x04970, 0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, # 1924
	#0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970, # 1929
	#0x06566, 0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, # 1934
	#0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950, # 1939
	#0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, # 1944
	#0x025d0, 0x092d0, 0x0d2b2, 0x0a950, 0x0b557, # 1949
	#0x06ca0, 0x0b550, 0x15355, 0x04da0, 0x0a5d0, # 1954
	#0x14573, 0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, # 1959
	#0x0aea6, 0x0ab50, 0x04b60, 0x0aae4, 0x0a570, # 1964
	#0x05260, 0x0f263, 0x0d950, 0x05b57, 0x056a0, # 1969
	#0x096d0, 0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, # 1974
	#0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6, # 1979
	#0x095b0, 0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, # 1984
	#0x06a50, 0x06d40, 0x0af46, 0x0ab60, 0x09570, # 1989
	#0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50, # 1994
	#0x06b58, 0x055c0, 0x0ab60, 0x096d5, 0x092e0, # 1999
	#0x0c960, 0x0d954, 0x0d4a0, 0x0da50, 0x07552, # 2004
	#0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5, # 2009
	#0x0a950, 0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, # 2014
	#0x04ba0, 0x0a5b0, 0x15176, 0x052b0, 0x0a930, # 2019
	#0x07954, 0x06aa0, 0x0ad50, 0x05b52, 0x04b60, # 2024
	#0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, # 2029
	#0x05aa0, 0x076a3, 0x096d0, 0x04bd7, 0x04ad0, # 2034
	#0x0a4d0, 0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, # 2039
	#0x0b5a0, 0x056d0, 0x055b2, 0x049b0, 0x0a577, # 2044
	#0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0  # 2049
    #https://github.com/rpplusplus/LunarCalendar/blob/master/src/lunar.cpp
    0x04bd8,0x04ae0,0x0a570,0x054d5,0x0d260,0x0d950,0x16554,0x056a0,0x09ad0,0x055d2,#1900-1909
    0x04ae0,0x0a5b6,0x0a4d0,0x0d250,0x1d255,0x0b540,0x0d6a0,0x0ada2,0x095b0,0x14977,#1910-1919
    0x04970,0x0a4b0,0x0b4b5,0x06a50,0x06d40,0x1ab54,0x02b60,0x09570,0x052f2,0x04970,#1920-1929
    0x06566,0x0d4a0,0x0ea50,0x06e95,0x05ad0,0x02b60,0x186e3,0x092e0,0x1c8d7,0x0c950,#1930-1939
    0x0d4a0,0x1d8a6,0x0b550,0x056a0,0x1a5b4,0x025d0,0x092d0,0x0d2b2,0x0a950,0x0b557,#1940-1949
    0x06ca0,0x0b550,0x15355,0x04da0,0x0a5b0,0x14573,0x052b0,0x0a9a8,0x0e950,0x06aa0,#1950-1959
    0x0aea6,0x0ab50,0x04b60,0x0aae4,0x0a570,0x05260,0x0f263,0x0d950,0x05b57,0x056a0,#1960-1969
    0x096d0,0x04dd5,0x04ad0,0x0a4d0,0x0d4d4,0x0d250,0x0d558,0x0b540,0x0b6a0,0x195a6,#1970-1979
    0x095b0,0x049b0,0x0a974,0x0a4b0,0x0b27a,0x06a50,0x06d40,0x0af46,0x0ab60,0x09570,#1980-1989
    0x04af5,0x04970,0x064b0,0x074a3,0x0ea50,0x06b58,0x055c0,0x0ab60,0x096d5,0x092e0,#1990-1999
    0x0c960,0x0d954,0x0d4a0,0x0da50,0x07552,0x056a0,0x0abb7,0x025d0,0x092d0,0x0cab5,#2000-2009
    0x0a950,0x0b4a0,0x0baa4,0x0ad50,0x055d9,0x04ba0,0x0a5b0,0x15176,0x052b0,0x0a930,#2010-2019
    0x07954,0x06aa0,0x0ad50,0x05b52,0x04b60,0x0a6e6,0x0a4e0,0x0d260,0x0ea65,0x0d530,#2020-2029
    0x05aa0,0x076a3,0x096d0,0x04bd7,0x04ad0,0x0a4d0,0x1d0b6,0x0d250,0x0d520,0x0dd45,#2030-2039
    0x0b5a0,0x056d0,0x055b2,0x049b0,0x0a577,0x0a4b0,0x0aa50,0x1b255,0x06d20,0x0ada0,#2040-2049
    0x14b63,0x09370,0x049f8,0x04970,0x064b0,0x168a6,0x0ea50, 0x06b20,0x1a6c4,0x0aae0,#2050-2059
    0x0a2e0,0x0d2e3,0x0c960,0x0d557,0x0d4a0,0x0da50,0x05d55,0x056a0,0x0a6d0,0x055d4,#2060-2069
    0x052d0,0x0a9b8,0x0a950,0x0b4a0,0x0b6a6,0x0ad50,0x055a0,0x0aba4,0x0a5b0,0x052b0,#2070-2079
    0x0b273,0x06930,0x07337,0x06aa0,0x0ad50,0x14b55,0x04b60,0x0a570,0x054e4,0x0d160,#2080-2089
0x0e968,0x0d520,0x0daa0,0x16aa6,0x056d0,0x04ae0,0x0a9d4,0x0a2d0,0x0d150,0x0f252,#2090-2099
0x0d520
]


Month = [
	'正月', '二月', '三月', '四月', '五月', '六月',
	'七月', '八月', '九月', '十月', '十一月', '腊月']
Day = [
	'初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十',
	'十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
	'廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十']
Gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
Zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
Zodiac = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
solarTerm = [
	'立春', '雨水', '清明', '春分', '惊蛰', '谷雨',
	'立夏', '小满', '芒种', '夏至', '小暑', '大暑',
	'立秋', '处暑', '白露', '秋分', '寒露', '霜降',
	'立冬', '小雪', '大雪', '冬至', '小寒', '大寒']
solarTermCode = [0, 21208, 42467, 63836, 85337, 107014,
	128867, 150921, 173149, 195551, 218072, 240693,
	263343, 285989, 308563, 331033, 353350, 375494,
	397447, 419210, 440795, 462224, 483532, 504758]
solarHoliday = {
	'0101':'元旦', '0214':'情人节', '0308':'妇女节', '0312':'植树节',
	'0401':'愚人节', '0501':'劳动节', '0504':'青年节', '0601':'儿童节', '0701':'建党节',
	'0801':'建军节', '0910':'教师节', '1001':'国庆节', '1225':'圣诞节'}
lunarHoliday = {
	'0101':'春节', '0115':'元宵', '0505':'端午', '0707':'七夕',
	'0815':'中秋', '0909':'重阳', '1208':'腊八'}

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
friendBirthday = {
    '0204':'tiantian','1226':'xxxx'
}

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
baseDate = date(1900, 1, 31) # 1900年1月31日星期三（庚子年正月初一壬寅日）

class Date:
	def __init__(self, year, month = -1, day = -1, weekday = -1):
		self.solarYear = year
		self.solarMonth = month
		self.solarDay = day
		self.weekday = weekday # 0 is Monday, 1 is TuesDay, ...
		self.lunarYear = -1
		self.lunarMonth = -1
		self.lunarDay = -1
		
		self.lunarYearDays = 0
		self.lunarDaysInMonth = [0] * 13
		self.lunarMonthDay = [29, 30]
		self.solarDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


	# Determines if is solar leap year
	def IsSolarLeapYear(self):
		return self.solarYear % 4 == 0 \
			and self.solarYear % 100 != 0 \
			or self.solarYear % 400 == 0


	# Returns count of days in month
	def SolarDaysInMonth(self):
		return self.IsSolarLeapYear() and self.solarMonth == 2 \
			and 29 \
			or self.solarDaysInMonth[self.solarMonth - 1]


	# Returns offset days from base date
	def SolarDaysFromBaseDate(self):
		selfDate = date(self.solarYear, self.solarMonth, self.solarDay)
		return (selfDate - baseDate).days


	# Translates solar date to lunar date
	def SolarToLunar(self):
		date = Date(-1, -1, -1)
		offset = self.SolarDaysFromBaseDate()
		for iYear in range(len(yearCode)):
			self.lunarYearDays = Date(iYear + 1900).LunarYearDays()
			if offset < self.lunarYearDays:
				date.year = iYear + 1900
				break
			offset -= self.lunarYearDays
		
		for iMonth in range(13):
			a = Date(date.year, iMonth + 1)
			a.CalcLunarDaysInMonth()
			if offset < a.lunarDaysInMonth[iMonth]:
				date.month = iMonth;
				break
			offset -= a.lunarDaysInMonth[iMonth]
		
		date.day = offset

		if self.LunarLeapMonth() > 0 and date.month >= self.LunarLeapMonth():
			date.month -= 1
		
		self.lunarYear = date.year + 1
		self.lunarMonth = (date.month + 1)%12
		#self.lunarMonth = (date.month + 1)
		#print 'setlunarMonth'+str(self.lunarMonth)
		self.lunarDay = date.day + 1


	# Returns which month is lunar leap month;
	# Returns 0 if no lunar leap month
	def LunarLeapMonth(self):
		return yearCode[self.solarYear - baseDate.year] & 0xf


	# Calculates lunar days in month;
	# Stores data in a global list
	def CalcLunarDaysInMonth(self):
		code = yearCode[self.solarYear - baseDate.year]

		code >>= 4
		for iMonth in range(12):
			self.lunarDaysInMonth[11 - iMonth] = self.lunarMonthDay[code & 0x1]
			code >>= 1

		if self.LunarLeapMonth() > 0:
			self.lunarDaysInMonth.insert(self.LunarLeapMonth(), self.lunarMonthDay[code & 0x1])


	# Returns count of days in lunar year
	def LunarYearDays(self):
		self.CalcLunarDaysInMonth()
		monthNum = self.LunarLeapMonth() == 0 and 12 or 13
		for m in range(monthNum):
			self.lunarYearDays += self.lunarDaysInMonth[m]

		return self.lunarYearDays


	#
	def Zodiac(self):
		return Zodiac[Zhi.index(self.GanZhiYear().decode('utf-8')[-1:])]

		monthNum = self.GetLeapMonth() == 0 and 12 or 13
		for m in range(monthNum):
			self.yearDays += self.daysInMonth[m]

		return self.yearDays


	#
	def LunarMonth(self):
		#print 'Date.py lunarMonth'+str(self.lunarMonth)
		return Month[self.lunarMonth - 1] 		
	#
	def LunarDay(self):
		if self.lunarDay == 1 and self.LunarLeapMonth() > 0:
			if self.LunarLeapMonth() == self.lunarMonth:
				return '闰' + Month[self.LunarLeapMonth() - 1]
			else:
				return self.LunarMonth()
		if self.lunarDay == 1:
			return self.LunarMonth()
		return Day[self.lunarDay - 1]


        #
	def OriginalLunarDay(self):
		return Day[self.lunarDay - 1]


	#
	def Weekday(self):
		if self.weekday != -1:
			return Weekday[self.weekday]
		else:
			offset = self.SolarDaysFromBaseDate()
			return (offset + baseDate.weekday()) % 7 + 1


	#
	def GanZhiYear(self):
		x = self.solarYear % 60 - 4
		y = x >= 0 and x or x + 60

		return Gan[y % 10] + Zhi[y % 12]


	#
	def GanZhiMonth(self):
		yearGan = self.GanZhiYear().decode('utf-8')[:-1]
		monthZhi = Zhi[(2 + self.lunarMonth - 1) % 12]

		if yearGan == Gan[0] or yearGan == Gan[5]:
			return Gan[(2 + self.lunarMonth - 1) % 10] + monthZhi
		elif yearGan == Gan[1] or yearGan == Gan[6]:
			return Gan[(4 + self.lunarMonth - 1) % 10] + monthZhi
		elif yearGan == Gan[2] or yearGan == Gan[7]:
			return Gan[(6 + self.lunarMonth - 1) % 10] + monthZhi
		elif yearGan == Gan[3] or yearGan == Gan[8]:
			return Gan[(8 + self.lunarMonth - 1) % 10] + monthZhi
		elif yearGan == Gan[4] or yearGan == Gan[9]:
			return Gan[(0 + self.lunarMonth - 1) % 10] + monthZhi


	#
	def GanZhiDay(self):
		C = self.solarYear / 100
		y = self.solarYear % 100
		M = self.solarMonth
		d = self.solarDay
		i = M % 2 == 0 and 6 or 0
		
		g = (4 * C + C / 4 + 5 * y + y / 4 + 3 * (M + 1) / 5 + d - 3) % 10
		z = (8 * C + C / 4 + 5 * y + y / 4 + 3 * (M + 1) / 5 + d + 7 + i) % 12

		return Gan[g - 1] + Zhi[z - 1]


	#
	def Zodiac(self):
		return Zodiac[Zhi.index(self.GanZhiYear().decode('utf-8')[-1:])]
		
		
	# Returns 24 solar terms in the solar year
	def SolarTerm(self):
		for i in range(12):
			s[i] = date((31556925974.7 * (self.solarYear - 1900) \
				+ solarTermCode[i] * 60000) \
				+ date(1900, 0, 6, 2, 5))
		return s


	#
	def SolarHoliday(self):
		month = self.solarMonth < 10 \
			and '0%s' % self.solarMonth \
			or str(self.solarMonth)
		day = self.solarDay < 10 \
			and '0%s' % self.solarDay \
			or str(self.solarDay)

		if solarHoliday.has_key(month + day):
			return solarHoliday[month + day]
		return None


	#
	def LunarHoliday(self):
		month = self.lunarMonth < 10 \
			and '0%s' % self.lunarMonth \
			or str(self.lunarMonth)
		day = self.lunarDay < 10 \
			and '0%s' % self.lunarDay \
			or str(self.lunarDay)

		if lunarHoliday.has_key(month + day):
			return lunarHoliday[month + day]
		return None

    #

	def FriendBirthday(self):
		month = self.lunarMonth < 10 \
			and '0%s' % self.lunarMonth \
			or str(self.lunarMonth)
		day = self.lunarDay < 10 \
			and '0%s' % self.lunarDay \
			or str(self.lunarDay)

		if friendBirthday.has_key(month + day):
			return friendBirthday[month + day]
		return None

