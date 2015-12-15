import json
import datetime
import threading
import os.path

import order_info as info

def init():
  global file_path

  if not os.path.isfile(file_path):
    with open(file_path, "w") as f:
      f.write("timestamp,last,bid,ask,high,low,volume\n")

def output():
  global f, before_ticker

  ticker = info.get_ticker()
  if ticker != before_ticker:
    line = str(ticker["timestamp"]) + ","\
      + str(ticker["last"]) + ","\
      + str(ticker["bid"]) + ","\
      + str(ticker["ask"]) + ","\
      + str(ticker["high"]) + ","\
      + str(ticker["low"]) + ","\
      + str(ticker["volume"]) + "\n"
    f.write(line)
    before_ticker = ticker
   
  t = threading.Timer(1, output)
  t.start()

file_path = "./data/ticker/" + str(datetime.date.today()) + ".csv"

init()

f = open(file_path, "a")
before_ticker = info.get_ticker()
t = threading.Thread(target=output)
t.start()