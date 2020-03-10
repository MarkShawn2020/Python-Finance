# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/1/26 12:44
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------

# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/1/25 16:19
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup


DXY_URL = "https://3g.dxy.cn/newh5/view/pneumonia"
DATA_PATH = "dxy_{}.json".format(datetime.now().strftime("%m%d%H%M"))

res = requests.get(DXY_URL)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "lxml")
area_stat_match = re.search("\[.*\]", soup.find(id="getAreaStat").text)
if area_stat_match:
	area_stat_data = json.loads(area_stat_match.group())
	json.dump(area_stat_data, open(DATA_PATH, "w", encoding="utf-8"))
	print("Finished dumping data to {}".format(DATA_PATH))
else:
	raise Exception("No data found in {}".format(DXY_URL))
