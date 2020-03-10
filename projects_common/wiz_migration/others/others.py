import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image


def show_driver_elment(ele):
    img_b = ele.screenshot_as_png  # 二进制形式的图片信息
    img = Image.open(BytesIO(img_b))  # 二进制转化成内存流，并通过Image读取成真实图片格式
    plt.axis("off")  # 关于图片的坐标轴显示
    plt.imshow(img)


def show_full_screen(driver):
    plt.imshow(Image.open(BytesIO(driver.get_screenshot_as_png())))


# ## 登陆

# - 调用本地默认图片浏览器打开，直观但无法记录
# ```img.show()```
#
# - 使用Matplotlib直接在程序中渲染，尤其适合和JupyterNotebook的交互
# ```plt.imshow(img)```


# ## 下载附件

# - 直接使用requests.get下载，不分流，大文件会堵塞
#
# ```
# res = requests.get(file_href, headers={"Cookie": header_cookie})
#
# with open(r"python.exe", "wb") as f:
#     f.write(res.content)
# ```



# ## 文章内容提取

# - 通过不断按下键，滚动滑条，也是一种方案，但不太好判断什么时候停止
#
# ```
# from selenium.webdriver.common.keys import Keys
#
# for i in range(5):
#     pg = driver.page_source
#     scroller_ele = driver.find_element_by_id("note-list-scroller")
#     scroller_ele.send_keys(Keys.DOWN)
# ```