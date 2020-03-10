# 见微数据爬取

## 该项目的开发用途？
- 程序化模拟自动登陆见微数据网站
- 自动获取所有符合要求的文件信息
- 自动导出到MongoDB数据库或是CSV文件

## 该项目的配置要求？
- Python V3.6+（必须）
- Scrapy（必须）
- PyMongo（如无，可选择其他存储形式）

## 该项目的启动设置？
1. 修改./jianwei/settings.py文件
    - 见微数据的用户名、密码（必须）
    ```python
    LOGIN_UID = 'your username'  # 账户名、手机号或者邮箱
    
    LOGIN_PWD = 'your password'  # 密码
    ```
    - MongoDB的存储、CSV导出的修改（如有必要）
    ```python
    FEED_FORMAT = 'csv'
    FEED_URI = './files/data.csv'
    FEED_EXPORT_ENCODING = 'utf-8'
    ```
    - 其他，比如下载延时（防止被封）等
    ```python
    DOWNLOAD_DELAY = 5  # 防止被封上限
    ```
2. 修改./jianwei/spiders/spider_xml.py文件
    - 修改是否自动生成字段.txt文件
    ```python
    '''
    获取XML类型页面的所有不重复字段，并存为txt文件，可删除
    '''
    if self.page_num < 2:
        with open('./files/soup字段.txt',
                  'a', encoding='utf-8') as f:
            print(self.get_soup_structure(soup), file=f)
    ```
    - 修改是否自动打印窗口实时输出
    ```python
    '''
    实时打印输出窗口，可删除
    '''
    time_used = (time.time() - self.start_time)/60
    self.logger.info('Pages: %3d, Times: %6.2f m, Average %6.2f items/m.'
                     % (self.page_num, time_used, self.page_num*20/time_used))
    ```
    - 修改下载的一些参数
    ```python
    def __init__(self, title_must='招股说明书', title_must_not='意见 摘要 公告 确认 附录'):
    ```
    - 修改 if... yield...语句（默认下载100多页的2000多只股票的IPO信息)
    ```python
    if self.stack_count < 20:
        self.page_num += 1
        yield FormRequest(
    ```
3. 其他

## TO-DO
- [ ] 更完善的搜索API配置
- [ ] PDF内容页的信息提取
- [ ] 其他  