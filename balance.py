import urllib2
import hmac
import hashlib
import time
import json

BASE_URL = "https://coincheck.jp/api/accounts/"

def get(name, params):
  global BASE_URL

  key = params["key"]
  secret = params["secret"]
  nonce = str(int(time.time()))
  url = BASE_URL + name
  message = nonce + url
  signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
  headers = {
    "ACCESS-KEY": key,
    "ACCESS-NONCE": nonce,
    "ACCESS-SIGNATURE": signature
  }

  req = urllib2.Request(url, headers=headers)
  res = urllib2.urlopen(req)
  return json.loads(res.read())

def get_balance(params):
  return get("balance", params)

def get_leverage_balance(params):
  return get("leverage_balance", params)