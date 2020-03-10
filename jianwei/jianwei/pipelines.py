# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from datetime import datetime
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter



class MongoPipeline(object):

    collection_name = 'IPOS' + datetime.now().strftime('_%b%d_%H%M%S')

    def __init__(self, mongo_client, mongo_port, mongo_db):
        self.mongo_client = mongo_client
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.uri = pymongo.MongoClient(self.mongo_client, self.mongo_port)
        self.db = self.uri[self.mongo_db]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_client=crawler.settings.get('MONGO_CLIENT'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DB'),
        )

    def close_spider(self, spider):
        self.uri.close()

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Data Missing: %s" % data)
        self.db[self.collection_name].insert_one(dict(item))
        return item
