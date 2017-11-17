# TimeZoneConvert 

故事发生在某个周末，提前报名好了国外的CTF想长长见识，官方写着“12:00 UTC start”，算好了时差就睡了，凌晨四点起来，打开了网站，发现比赛并没有开始，原来是时差算错了，晚上8点才开始，当时我就决定得弄个小脚本，辅助我这个倒不过时间的脑子。

### CAN DO

- 显示当地时间、UTC、EST、PST、GMT、CST。

### TO DO

- [ ] 按照指定格式输入时间和时区，转换成其他时区
- [ ] 输入某个城市，查询时间
- [ ] 增加多个时间显示风格
- [ ] 增加 usage
- [ ] 以后想到再加



### Function

- ```python
  from  datetime import *
  import pytz 
  ```


- 查询时区，可以根据国家代码查找这个国家的所有时区

  ```python
  >>> pytz.country_timezones('us') 
  [u'America/New_York', u'America/Detroit', u'America/Kentucky/Louisville', u'America/Kentucky/Monticello', u'America/Indiana/Indianapolis', u'America/Indiana/Vincennes', u'America/Indiana/Winamac', u'America/Indiana/Marengo', u'America/Indiana/Petersburg', u'America/Indiana/Vevay', u'America/Chicago', u'America/Indiana/Tell_City', u'America/Indiana/Knox', u'America/Menominee', u'America/North_Dakota/Center', u'America/North_Dakota/New_Salem', u'America/North_Dakota/Beulah', u'America/Denver', u'America/Boise', u'America/Phoenix', u'America/Los_Angeles', u'America/Anchorage', u'America/Juneau', u'America/Sitka', u'America/Metlakatla', u'America/Yakutat', u'America/Nome', u'America/Adak', u'Pacific/Honolulu']
  ```

- 获取某个时区的当前时间

  ```python
  datetime.now(tz)
  datetime.utcnow() # utc time
  ```

- 将datatime数据格式以特定格式转换为string

  ```python
  datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
  ```

  ​