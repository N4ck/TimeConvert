#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  datetime import *
import time
import sys
import optparse
import pytz

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
# 选择timezone
PST = pytz.timezone('America/Los_Angeles') 
CST = pytz.timezone('America/Chicago')
EST = pytz.timezone('America/New_York')
LOCAL = pytz.timezone("Asia/Shanghai")
UTC = pytz.utc 
GMT = pytz.timezone('Europe/London')
# print pytz.country_timezones('us')


def convert2EST(input_time):
#本地时间转EST时间(-13:00)
	# 将字符串input_time按照format转换成datetime格式
	time = datetime.strptime(input_time,TIME_FORMAT)
	# 将time根据timezone打上标签，比如该时间为LOCAL时间
	localized_time = LOCAL.localize(time)
	# 根据timezone做时区转换，使用astimezone()
	converted_time = localized_time.astimezone(EST)
	# 返回str格式时间
	return converted_time.strftime(TIME_FORMAT)

def convert2UTC(input_time):
#本地时间转UTC时间(-8:00)
	time = datetime.strptime(input_time,TIME_FORMAT)
	localized_time = LOCAL.localize(time)
	converted_time = localized_time.astimezone(UTC)
	return converted_time.strftime(TIME_FORMAT)

def convert2PST(input_time):
#本地时间转PST时间(-16:00)
	time = datetime.strptime(input_time,TIME_FORMAT)
	localized_time = LOCAL.localize(time)
	converted_time = localized_time.astimezone(PST)
	return converted_time.strftime(TIME_FORMAT)

def convert2CST(input_time):
#本地时间转CST时间(-14:00)
	time = datetime.strptime(input_time,TIME_FORMAT)
	localized_time = LOCAL.localize(time)
	converted_time = localized_time.astimezone(CST)
	return converted_time.strftime(TIME_FORMAT)

def convert2GMT(input_time):
#本地时间转GMT时间(-8:00)
	time = datetime.strptime(input_time,TIME_FORMAT)
	localized_time = LOCAL.localize(time)
	converted_time = localized_time.astimezone(GMT)
	return converted_time.strftime(TIME_FORMAT)

def convert2LOCAL(input_time,timezone):

	time = datetime.strptime(input_time,TIME_FORMAT)
	if timezone == 'UTC':
		localized_time = UTC.localize(time)
	elif timezone == 'GMT':
		localized_time = GMT.localize(time)
	elif timezone == 'EST':
		localized_time = EST.localize(time)
	elif timezone == 'PST':
		localized_time = PST.localize(time)
	elif timezone == 'CST':
		localized_time = CST.localize(time)

	converted_time = localized_time.astimezone(LOCAL)
	return converted_time.strftime(TIME_FORMAT)

# local = "2017-12-1 22:52:16"

def main():
	if len(sys.argv) == 3:
		local = sys.argv[1]+' '+sys.argv[2]
		print 'convert2EST:%s' % convert2EST(local)
		print 'convert2CST:%s' % convert2CST(local)
		print 'convert2PST:%s' % convert2PST(local)
		print 'convert2UTC:%s' % convert2UTC(local)
		print 'convert2GMT:%s' % convert2GMT(local)

if __name__ == "__main__":
	timezone = ['UTC','GMT','PST','CST','LOCAL','EST']
	parser = optparse.OptionParser("Usage: %prog [options] date time(like 2017-12-1 12:00:00)")
	# parser.add_option("-t", "--time", 
	# 				dest = "TIME_FORMAT",
 #    				default = "now", type = "str",
 #    help = "[optional]standard time format 24H,like 2017-12-1 12:00:00,default=now")
	# parser.add_option("-s", "--system", dest="12/24",
	# 			   default = 24, type = "int",  
 #                 help = "[optional]Hour system,12 or 24,default=24")
	parser.add_option("-z", "--timezone", dest="timezone",
				   default = "LOCAL", type = "str",  
                 help = "[optional]timezone CST/EST/UTC/GMT/PST/LOCAL,default=LOCAL")
	(options, args) = parser.parse_args()

	if len(args) < 1:
		parser.print_help()
		# 显示timezone当前时间
		PST_dt = datetime.now(PST)
		GMT_dt = datetime.now(GMT)
		CST_dt = datetime.now(CST)
		EST_dt= datetime.now(EST)
		LOCAL_dt = datetime.now()
		UTC_dt = datetime.utcnow()
		# 以标准格式输出时间
		print 'LOCALTIME当地时间:%s' % LOCAL_dt.strftime(TIME_FORMAT)
		print 'UTC世界协调时间:%s' % UTC_dt.strftime(TIME_FORMAT)
		print 'EST东部标准时间:%s' % EST_dt.strftime(TIME_FORMAT)
		print 'CST中部标准时间:%s' % CST_dt.strftime(TIME_FORMAT)
		print 'PST太平洋标准时间:%s' % PST_dt.strftime(TIME_FORMAT)
		print 'GMT格林威治标准时间:%s' % GMT_dt.strftime(TIME_FORMAT)
		
		sys.exit(0)
	elif (len(args) == 2 and ((options.timezone).upper()) == 'LOCAL'):
		local = args[0]+' '+args[1]
		print 'convert2EST:%s' % convert2EST(local)
		print 'convert2CST:%s' % convert2CST(local)
		print 'convert2PST:%s' % convert2PST(local)
		print 'convert2UTC:%s' % convert2UTC(local)
		print 'convert2GMT:%s' % convert2GMT(local)
	elif (len(args) == 2 and ((options.timezone).upper())!= 'LOCAL'):
		local = args[0]+' '+args[1]
		tz = (options.timezone).upper()
		if (tz in timezone):
			print tz+'2LOCAL:%s' % convert2LOCAL(local,tz)
		else :
			print 'No such timezone.'
			sys.exit(0)


				