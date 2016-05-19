# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class V2exPostItem(scrapy.Item):
    source = "v2ex"
    type = "post"
    url = scrapy.Field()
    timestamp = scrapy.Field()
    document = scrapy.Field()

    user = scrapy.Field()
    tags = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    comments_num = scrapy.Field()
    comments = scrapy.Field()
