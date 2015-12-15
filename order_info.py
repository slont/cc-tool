import urllib2
import threading
import json

BASE_URL = "https://coincheck.jp/api/"

def get(name):
  global BASE_URL

  url = BASE_URL + name
  res = urllib2.urlopen(url)
  return json.loads(res.read())

def get_ticker():
  return get("ticker")

def get_trades():
  return get("trades")

def get_order_books():
  return get("get_order_books")