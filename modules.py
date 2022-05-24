# import turtle
# # import time
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
# # time.sleep(3)
# turtle.done()

#if we want to import only something from turtle then we can do:
# from turtle import circle, forward,right,done
# forward(150)
# right(250)
# circle(76)
# done()

# from turtle import *
# forward(150)
# right(250)
# forward(150)
# circle(75)
# done()

# print(dir())
# print(dir(__builtins__))
# for i in dir(__builtins__):
#     print(i)

#webbrowser module

# import webbrowser
# webbrowser.open("https://www.python.org/",new=1) #open new tab with link
#or use webbrowser.open_new(url)

# chrome=webbrowser.get(using='google-chrome')
# chrome.open_new("https://www.python.org/")

# Time and DateTime

# import time
# print(time.gmtime(0))
# print(time.localtime())
# print(time.localtime(time.time()))
# print(time.time())

# time_here=time.localtime()
# print(time_here)
# print("Year:",time_here[0],time_here.tm_year)
# print("Month:",time_here[1],time_here.tm_mon)
# print("Day:",time_here[2],time_here.tm_mday)

# import time
# from time import perf_counter as my_timer #we can use time or monotonic instead of perf_counter
# import random
# input("press enter to start")
# wait_time=random.randint(1,6)
# time.sleep(wait_time)
# start_time=my_timer()
# input("press enter to stop")
# end_time=my_timer()
# print("started at "+time.strftime("%x",time.localtime(start_time)))
# print("ended at "+time.strftime("%x",time.localtime(end_time)))
# print("your reaction time was {} seconds".format(end_time-start_time))

#we can use process_time instead of perf_counter to know time how much cpu spend

# import time
# print("time : ",time.get_clock_info('time'))
# print("perf_counter : ",time.get_clock_info('perf_counter'))
# print("monotonic : ",time.get_clock_info('monotonic'))
# print("process_time : ",time.get_clock_info('process_time'))

# import time
# print("The epoch on this system starts at "+time.strftime('%c',time.gmtime(0)))
# print("The current timezone is {0} with an offset of {1} ".format(time.tzname[0],time.timezone))

# if time.daylight!=0:
#     print("Daylight saving time is in effect for this location")
#     print("The DST Timezone is" +time.tzname[1])
# print("Local time is "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# print("Local time is "+time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))

#datetime

# import datetime
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# import imp
# import pytz
# import datetime

# country='Europe/Moscow'
# tz_to_display=pytz.timezone(country)
# local_time=datetime.datetime.now(tz=tz_to_display)
# print("the time in {} is {} ".format(country,local_time))
# print("utc is {} ".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)

# for x in sorted(pytz.country_names):
#     print(x+" : "+pytz.country_names[x])

# for x in sorted(pytz.country_names):
#     print("{}: {}: {} ".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))

import datetime
import pytz

local_time=datetime.datetime.now()
utc_time=datetime.datetime.utcnow()

print("Naive local time {} ".format(local_time))
print("Naive UTC {} ".format(utc_time))

aware_local_time=pytz.utc.localize(local_time).astimezone()
aware_utc_time=pytz.utc.localize(utc_time)

print("Aware local time {},time zone {}".format(aware_local_time,aware_local_time.tzinfo))
print("Aware UTC time {},time zone {}".format(aware_utc_time,aware_utc_time.tzinfo))

gap_time=datetime.datetime(2015,10,25,13,0,0)
print(gap_time.timestamp())

s=1445733000
t=s+(60*60)
gb=pytz.timezone('GB')
dt1=pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) #timestamp use localdate
dt2=pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb) #so use utcfromtimestamp
print("{} seconds since the epoch is {} ".format(s,dt1))
print("{} seconds since the epoch is {} ".format(t,dt2))
