# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/1/26 17:41
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------

import requests
import json

dxy_api = 'https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia'
res = requests.get(dxy_api)
data = json.loads(res.text)

from pprint import pprint
print(data)