# CH01 - Python开发环境配置

Python作为主流编程之一，要想学好python，就不得不把自己当作一个专业的程序员认真对待，正所谓“工欲善其事必先利其器”，准备好所有的利器，才能更好地帮助我们冲锋陷阵，完成使命。


因此，本章，我们将主要围绕本系列主题《Python+财务教程》介绍一下财经领域学习Python所要准备的一些开发工具和相关视野。


## Get to know Github and .md
首先介绍Github，因为GitHub 是目前全球最大的开源代码库，以下是官网的截图：


[![image.png](https://cdn.nlark.com/yuque/0/2020/png/633627/1579019855091-dacd701d-e7f0-4e72-8cc8-dee504abea77.png#align=left&display=inline&height=273&name=image.png&originHeight=407&originWidth=1113&size=42849&status=done&style=none&width=746)](https://github.com/about)


可以说，学习编程的第一步和最后一步，都是Github，因为它是连接程序员的桥梁，它是如此重要，以至于你必须把它在浏览器里加个显眼的书签以表明自己无时无刻不在关注程序员世界的最新动态，某种意义上，这也是世界最先进生产力的窗口之一（如果不去计较那些军方的、大学的实验室的话）。


因此，打开任意一款Github


- [Typora — a markdown editor, markdown reader.](https://typora.io/)
### 
## IDE的选择与配置
我们推荐使用** ****Anaconda + PyCharm + Sublime**** **的组合学习Python，这能帮助你应对绝大多数情况下的开发问题，具有极强的扩展能力。当然，**Anaconda 下的Spyder可部分取代PyCharm，VSCode和Sublime也是互为替代品**（VSCode比Sublime更强大一些），感兴趣的朋友可自行了解使用。


其中，Spyder和PyCharm都属于IDE（Integrated Development Environment，集成开发环境），即提供编写、编译、运行的一整套开发环境（一条龙服务）。而Sublime和VSCode都属于编辑器，就是提供很多扩展功能的比Windows的记事本更高级的记事本。


再说一说Anaconda，它是一个数据分析领域最流行的软件平台。当你安装完Anaconda之后，你的电脑便已经内置了一个Python环境，更准确地说是一个Python的安装包。它还内置了conda这个强大的包管理器，你可以启动Anaconda Navigator可视化地管理电脑中已经安装的python相关的安装包。有意思的是，严格意义上python是conda的一个子集，因为conda也管理着python这个安装包。


当然，最重要的是，Anaconda提供了Jupyter Notebook这个强大的交互式笔记本，和Spyder这样一个基本完备的IDE环境。尤其是Jupyter Notebook，这正是数以千万计的数据科学家无法抗拒的工作平台，也是PyCharm无法完全取代Anaconda的重要原因，以至于PyCharm内置了Jupyter Notebook的实现方式，你可以有趣地发现两个完全不一样的公司开发的产品，它们之间相互影响、相互结合，共同为Python开发者们创造了一个几乎完美的开发环境。


### PyCharm的安装与激活
#### What's PyCharm
PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。（来自百度百科）
> 在清华大学的软件工程公开课内，老师们使用的Python开发环境正是PyCharm。



#### 安装PyCharm
P.F.A项目PyCharm2019专业版网盘（如失效请联系P.F.A.C）：

- 链接：https://pan.baidu.com/s/1oZ_r9D8KFjnQFEz-2vPUug
- 提取码：vgt8



直接下载专业版PyCharm双击安装到默认（或自定义）路径后，注意以下几项：

- 左1是创建64位的桌面运行快捷方式，建议勾选
- 右1是在系统/用户环境变量中添加PyCharm，一般来说当安装一些编程软件时，提示是否添加路径变量都是要勾选的，因为这可以方便程序（有时也是必须）找到可执行的文件，尤其是当装的软件并不多的时候也不大会出现变量冲突的问题，当然了如果不断地重装可能会引发一些问题
- 左2是在资源管理器中的文件夹上右击时显示一个“在Pycharm中打开文件夹”的选项，这是一个很有用的功能，当我们想深入研究一个Package的时候
- 左3是将Pycharm与.py类型的文件进行关联，不建议勾选，因为PyCharm的启动速度很慢，它更适合处理工程项目，而非单独查看某个.py的文件内容，我们更推荐使用SubLime、VSCode或IDLE等更轻量级的编辑器去打开.py文件



![图片.png](https://cdn.nlark.com/yuque/0/2020/png/633627/1579066336809-5b0c9cde-05cb-4537-abe0-effb1639593a.png#align=left&display=inline&height=400&name=%E5%9B%BE%E7%89%87.png&originHeight=390&originWidth=503&size=15265&status=done&style=none&width=516)


一路next后就会安装完成，之后会提示手动或自动重启，重启之后PyCharm就正式安装好了。


#### 激活PyCharm
在安装完PyCharm后重启打开PyCharm，选好配色等工作操作完就会出现一个软件授权界面，在这里，网上流传最多的是一些激活码（非常长），以及让你修改host文件屏蔽JB（PyCharm厂商），但基本都已经没用了（至少2020年1月份这个节点我尝试了网上很多比如标题带有“亲测有用”的帖子都无一例外失效了，因为JB貌似加大了对软件盗版的打击力度）。


在此，我们并不推荐大家用激活码方式，由于本教程的受众大多数是学生，因此强烈推荐大家使用自己学校配给自己的教育网邮箱去官网注册账号，填写今年或者明年毕业的信息，然后邮箱确认后就可以得到一个一年有效期的专业版账号。在此，给JB的大方点赞，高等教育的知识群体理应拥有使用先进生产力的权力，这也是JB奉行的理念之一。


以下，给出JB教育账号申请的链接：[JetBrains Products for Learning](https://www.jetbrains.com/shop/eform/students)


注册好，邮箱确认通过后（**确认邮件可能会在垃圾箱内**），可以在PyCharm的启动界面内输入相关信息，并得到一个License了。


如果不知道自己的教育网账号的可以询问一下身边的同学，或者老师。


如果自己学校没有配给教育网账号的话，可以先使用free trial模式，可以坚持一个月，先凑合着吧（或者再过半个月就又有网上流出可以使用的激活码了）。


![image.png](https://cdn.nlark.com/yuque/0/2020/png/633627/1579068163712-dd26ffef-fe6d-4a93-bc67-9aa24087978f.png#align=left&display=inline&height=400&name=image.png&originHeight=480&originWidth=725&size=29749&status=done&style=none&width=604)






## 附录






