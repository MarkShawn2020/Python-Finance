# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    key = scrapy.Field()
    encryption_key = scrapy.Field()  # 没有该字段
    title = scrapy.Field()
    title2 = scrapy.Field()
    publish_date = scrapy.Field()
    stock_code = scrapy.Field()
    stock_ticker = scrapy.Field()
    pdf_url = scrapy.Field()
    href = scrapy.Field()
    response_code = scrapy.Field()
    response_message = scrapy.Field()
    total = scrapy.Field()
    took = scrapy.Field()
    token = scrapy.Field()
    message = scrapy.Field()
    eng_paragraphs = scrapy.Field()
    unigram_paragraphs = scrapy.Field()
    pages = scrapy.Field()
    subtitles = scrapy.Field()
    market_type = scrapy.Field()
    notice_type = scrapy.Field()
    file_type = scrapy.Field()
    industry = scrapy.Field()
    parent_industry = scrapy.Field()
    relevant_laws = scrapy.Field()
    source_path = scrapy.Field()
    total_page = scrapy.Field()
    availability = scrapy.Field()
    is_dir = scrapy.Field()
    preview = scrapy.Field()
    province = scrapy.Field()
