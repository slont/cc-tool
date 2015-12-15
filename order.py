import urllib2

BASE_URL = "https://coincheck.jp/api/"

def order(params):
  global BASE_URL

  url = BASE_URL + 