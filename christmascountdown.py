import sys
import scrollphat
import time
import datetime
import math

YEAR=2017

try:
  scrollphat.set_brightness(10)
  last_time=0
  while True:
    my_delta = datetime.datetime(year=YEAR,month=12,day=25,hour=0,minute=0) - datetime.datetime.now()
    my_delta_days = my_delta.days
    my_delta_hours = math.floor(my_delta.seconds/3600)
    hour_string = '{0}'.format(my_delta_days * 24 + my_delta_hours)
    if hour_string != last_time:
      scrollphat.clear_buffer()
      for i in range(11):
        scrollphat.scroll()
        time.sleep(0.01)
      scrollphat.write_string(hour_string, 11)
      for i in range(scrollphat.buffer_len()-12):
        scrollphat.scroll()
        time.sleep(0.05)
      last_time = hour_string
      time.sleep(0.5)

except KeyboardInterrupt:
  scrollphat.clear()
  sys.exit(-1)
