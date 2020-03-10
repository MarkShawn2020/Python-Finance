# -*- coding: utf-8 -*-

import re
import time
import hashlib
from scrapy.spiders import Spider
from scrapy.http import FormRequest
from jianwei.items import JianweiItem
from bs4 import BeautifulSoup, element
from scrapy.utils.project import get_project_settings
from scrapy.shell import inspect_response
from datetime import datetime

Settings = get_project_settings()


class SpiderXmlSpider(Spider):

    name = 'spider_xml'
    allowed_domains = ['jianweidata.com']
    login_url = 'https://www.jianweidata.com/data/api/User/UserLogin'
    search_url = 'https://www.jianweidata.com/data/api/TestSearch/SearchMainFiling/'

    def __init__(self, title_must='招股说明书', title_must_not='意见 摘要 公告 确认 附录'):
        super().__init__()
        self.login_uid = Settings['LOGIN_UID']
        self.login_pwd = Settings['LOGIN_PWD']
        self.page_num = 0
        self.stack_count = 0
        self.total = 9999
        self.start_time = time.time()
        self.token = ''
        self.title_must = title_must
        self.title_must_not = title_must_not

    '''
    核心程序1：登陆并获取Token
    '''
    def start_requests(self):
        pwd = hashlib.md5(self.login_pwd.encode('utf-8')).hexdigest()
        user_pwd = hashlib.md5((self.login_uid + self.login_pwd).encode('utf-8')).hexdigest()

        return [FormRequest(
            self.login_url,
            method='POST',
            formdata={
                'Platform': 'web',
                'RegistrationId': self.login_uid,
                'uid': self.login_uid,
                'pwd': pwd,
                'userPwd': user_pwd,
            },
            callback=self.parse,
        )]

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'xml')
        self.token = soup.find('Token', text=re.compile(r'\w+'))
        response_code = soup.ResponseCode.string
        response_msg = soup.ResponseMessage.string

        '''
        调用Scrapy Shell调试Response
        '''
        if not response_code.startswith(('20', '10', '0')):
            self.logger.warning('---\nErrorCode: %s, ErrorMsg: %s' % (response_code, response_msg))
            self.logger.warning('---\nLoginUID: %s, LoginPWD: %s\n' % (self.login_uid, self.login_pwd))
            inspect_response(response, self)

        '''
        新建files文件夹，保存CSV数据以及一些其他自定义文件
        '''
        import os
        if 'files' not in os.listdir():
            os.mkdir('files')

        '''
        获取XML类型页面的所有不重复字段，并存为txt文件，可删除
        '''
        if self.page_num < 2:
            with open('./files/soup字段.txt',
                      'a', encoding='utf-8') as f:
                print(self.get_soup_structure(soup), file=f)

        '''
        实时打印输出窗口，可删除
        '''
        time_used = (time.time() - self.start_time)/60
        self.logger.info('Pages: %3d, Times: %6.2f m, Average %6.2f items/m.'
                         % (self.page_num, time_used, self.page_num*20/time_used))

        '''
        核心程序2：输出ITEM
        '''
        if self.page_num > 0:
            item = JianweiItem()
            self.total = int(soup.Total.string)
            for source in soup.select('Source'):
                item['publish_date'] = source.PublishDate.text
                item['stock_code'] = source.StockCode.text
                item['stock_ticker'] = source.StockTicker.text
                item['key'] = source.Key.text
                item['href'] = response.urljoin(source.Href.text)
                item['pdf_url'] = source.Url.text
                item['title'] = source.Title.text
                item['notice_type'] = source.NoticeType.text
                item['market_type'] = source.MarketType.text
                item['file_type'] = source.FileType.text
                item['industry'] = source.Industry.text
                item['parent_industry'] = source.ParentIndustry.text
                item['source_path'] = source.SourcePath.text
                item['preview'] = source.Preview.text
                item['availability'] = source.Availability.text
                self.stack_count += 1
                yield item

        '''
        核心程序3：循环调用
        '''
        if self.stack_count < 20:
            self.page_num += 1
            yield FormRequest(
                url=self.search_url,
                method='POST',
                formdata={
                    # 过滤，{'1': '市场类型', '2': '公告类型', '3': '行业统计', '4': '地域分布'}
                    'filters[0][field]': str(2),
                    'filters[0][label]': str('首次公开发行及上市'),
                    'filters[0][value]': str(5),

                    # 证券格式: '[\d+ \s+]'，组合格式: '组合: \s+'，组合会出现一个新的字段叫 assets[]
                    'label': '',
                    'titleMust': self.title_must,
                    'titleMustNot': self.title_must_not,
                    'titleShould': '',

                    # {'0':'同篇', '1':'同段','2':'同句','3':'同句过滤否定'}
                    'nearMode': str(0),
                    'pageNum': str(self.page_num),
                    'pageSize': str(1),
                    'searchType': str(1),
                    'sector': str(1),
                    'sort': str(2),
                    'isLockedAsset': str(False),

                    # {'False': 高级搜索， 'True': '简单搜索'}
                    'isSimpleQuery': str(False),
                    'token': self.token,

                    'contentMust': '',
                    'contentMustNot': '',
                    'contentShould': '',
                    'startDate': '2000/1/1',
                    'endDate': '2018/8/15',
                    'query': '',
                },
                callback=self.parse,
                dont_filter=True,
            )

    '''
    获取页面的所有不重复字段，函数声明部分
    '''
    def get_soup_structure(self, soup, length=20):
        str_print = ''
        str_set = set()
        for node in soup.descendants:
            if not isinstance(node, element.NavigableString):
                if node.find() is None:
                    path = [i.name[:length] for i in node.parents][-2::-1]
                    path.append(node.name[:length])
                    if node.string is None:
                        path.append('Null')
                    str_line = ''
                    for i, j in enumerate(path):
                        str_line += '{0}: {1:{2}}\t'.format(i, j, length)
                    str_set.add(str_line)
        for str_line in str_set:
            str_print += str_line + '\n'
        return str_print
