#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  datetime import *
import time
import pytz
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
PST = pytz.timezone('America/Los_Angeles') 
CST = pytz.timezone('America/Chicago')
EST = pytz.timezone('America/New_York')
GMT = pytz.timezone('Europe/London')
# print pytz.country_timezones('us')

PST_dt = datetime.now(PST)
GMT_dt = datetime.now(GMT)
CST_dt = datetime.now(CST)
EST_dt= datetime.now(EST)
LOCAL_dt = datetime.now()
UTC_dt = datetime.utcnow()

print 'LOCALTIME当地时间:%s' % LOCAL_dt.strftime(TIME_FORMAT)
print 'UTC世界协调时间:%s' % UTC_dt.strftime(TIME_FORMAT)
print 'EST东部标准时间:%s' % EST_dt.strftime(TIME_FORMAT)
print 'CST中部标准时间:%s' % CST_dt.strftime(TIME_FORMAT)
print 'PST太平洋标准时间:%s' % PST_dt.strftime(TIME_FORMAT)
print 'GMT格林威治标准时间:%s' % GMT_dt.strftime(TIME_FORMAT)
