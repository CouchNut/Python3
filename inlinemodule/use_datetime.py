#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 获取当前日期和时间
print('----- 获取当前日期和时间 -----')
from datetime import datetime
now = datetime.now()	# 获取当前datetime
print(now)

print(type(now))

# 获取指定日期和时间
print('----- 获取指定日期和时间 -----')

dt = datetime(2015, 4, 19, 12,20)	# 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
print('----- datetime转换为timestamp -----')
stamp = dt.timestamp()	# 把datetime转换为 timestamp
print(stamp)

# timestamp转换为datetime
print('----- timestamp转换为datetime -----')
print(datetime.fromtimestamp(stamp))

# str转换为datetime
print('----- str转换为datetime -----')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print('----- datetime转换为str -----')
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
print('----- datetime加减 -----')
from datetime import timedelta
now2 = datetime.now()
print(now2)
# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
print(now2 + timedelta(hours = 10))
print(now2 - timedelta(days = 1))
print(now2 + timedelta(days = 2, hours = 12))

# 本地时间转换为UTC时间
print('----- 本地时间转换为UTC时间 -----')
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，
# 所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))	# 创建时区 utc+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为 UTC+8:00
print(dt)

# 时区转换
print('----- 时区转换 -----')
# 拿到UTC时间，并强制设置时区为 UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone() 将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间:', bj_dt)
# astimezone() 将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print('东京时间:', tokyo_dt)
# astimezone() 将 bj_dt 转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours = 9)))
print('东京时间:', tokyo_dt2)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
# 均是str，请编写一个函数将其转换为timestamp：
import re
def to_timestamp(dt_str, tz_str):
	# 将dt_str转换为datetime
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	# 将tz_str转换为timezone
	m = re.match(r'^(UTC)([+-]?)([0-9]|0[0-9]|1[0-2]):(00)$', tz_str)
	sign = -1 if m.group(2) is '-' else 1
	tz = sign * int(m.group(3))
	# 本地时间转换时区 UTC 时间
	tz_utc = timezone(timedelta(hours = tz))
	dt_utc = dt.replace(tzinfo=tz_utc)
	return dt_utc.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')


