# -*-           coding: utf-8               -*- 
# ---------------------------------------------
# @Project:     Daily-Python-Learning
# @File:        show_img.py
# @Date:        2020/1/19
# @IDE:         PyCharm
# @Author:      Mark Shawn
# @Email:       shawninjuly@gmail.com
# ---------------------------------------------

from .CONST import *

import requests
from PIL import Image
from io import BytesIO


def show_img_url(img_url: str, use_matplotlib=False, save=False):
    res = requests.get(img_url, headers={"User-Agent": USER_AGENT})
    if res.status_code != 200:
        raise Exception("Not connected, STATUS CODE: {}".format(res.status_code))

    img = Image.open(BytesIO(res.content))
    if not use_matplotlib:
        img.show()
    else:
        from matplotlib import pyplot as plt
        plt.imshow(img)
        plt.show()
