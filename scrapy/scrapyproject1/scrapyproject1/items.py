# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapyproject1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_title = scrapy.Field()
    text = scrapy.Field()
    print('item操作')##相当于是弄了一个字典,把你想要加的字段放进这个字典里面，之后在pipeline可以直接进行调用

    pass
