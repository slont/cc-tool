import json

import balance

KEY = "9yPoFVczOD-sa2oF"
SECRET = "lttzLuiRFrQdDzsNO5LNh5YBPAuitdQx"

params = {
  "key": KEY,
  "secret": SECRET
}
print balance.get_leverage_balance(params)