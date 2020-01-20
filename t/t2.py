# -*-           coding: utf-8               -*- 
# ---------------------------------------------
# @Project:     Daily-Python-Learning
# @File:        t2.py
# @Date:        2020/1/20
# @IDE:         PyCharm
# @Author:      Mark Shawn
# @Email:       shawninjuly@gmail.com
# ---------------------------------------------

a = """|            | 创始人                                  | 时间 | 国                 家 | 主要应用                                                     |
| ---------- | --------------------------------------- | ---- | --------------------- | ------------------------------------------------------------ |
| Python     | Gudio van Rossum                        | 1991 | 荷兰                  | 大数据的挖掘和处理，开发web，系统运维，云计算，金融理财分析，人工智能等 |
| C          | Dennis MacAlistair  Ritchie             | 1978 | 美国                  | 主要用于像操作系统一类偏底层的应用开发，包括像  Windows/Linux 这样的大型商业操作系统，以及嵌入式操作系统、嵌入式设备上的应用 |
| C++        | Bjarne Stroustrup                       | 1982 | 美国                  | 应用软件，基础软件和高级语言的运行时环境，业务型应用软件的后台 |
| C#         | Anders Hejlsberg                        | 1998 | 丹麦                  | 多用于开发桌面应用程序、Web应用程序、RIA应用程序（Silverlight），智能手机应用程序 |
| Java       | James Gosling                           | 1990 | 加拿大                | 用于开发大中型商业应用，桌面应用，消费和嵌入式领域           |
| JavaScript | Brendan Eich                            | 1995 | 美国                  | 唯一一种在所有主流平台都被原生支持的编程语言，因此在所有主流平台都可以用于进行插件开发。常见的有浏览器插件和扩展程序 |
| Go         | Rob Pike,Ken  Thompson,Robert Griesemer | 2009 | 美国                  | 可解决面向对象程序设计的麻烦，帮助程序设计师处理琐碎但重要的内存管理问题 |
"""


import re
m_list = re.findall('(|.*?)+|(|[\s-]*?)+|((|.*?)+|)+', a)
print(m_list.groups())
