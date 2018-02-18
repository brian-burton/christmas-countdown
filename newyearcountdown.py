import sys
import scrollphat
import time
import datetime
import math

YEAR=2018

try:
  scrollphat.set_brightness(10)
  last_time=0
  while True:
    my_delta = datetime.datetime(year=YEAR,month=1,day=1,hour=0,minute=0) - datetime.datetime.now()
    days_left = math.floor(my_delta.days + (my_delta.seconds/86400))
    hours_left = math.ceil((my_delta.days * 24) + (my_delta.seconds/3600))
    minutes_left = math.ceil((my_delta.days * 24 * 60) + (my_delta.seconds/60))
    seconds_left = math.ceil((my_delta.days * 24 * 3600) + my_delta.seconds)
    if hours_left >= 55:
      count_string = '{0}D'.format(days_left)
    elif minutes_left >= 60:
      count_string = '{0}H'.format(hours_left)
    elif seconds_left >= 60:
      count_string = '{0}M'.format(minutes_left)
    else:
      count_string = '{0}S'.format(seconds_left)
    if count_string != last_time:
      scrollphat.clear_buffer()
      for i in range(11):
        scrollphat.scroll()
        time.sleep(0.01)
      scrollphat.clear_buffer()
      scrollphat.write_string(count_string, 11)
      for i in range(scrollphat.buffer_len()-12):
        scrollphat.scroll()
        time.sleep(0.05)
      last_time = count_string
      time.sleep(0.2)

except KeyboardInterrupt:
  scrollphat.clear()
  sys.exit(-1)
