# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import base64

from dao_sniffer.spiders.v2ex_spider import V2exSpider

from .elastic_search_client import index_elastic_search


class V2exElasticSearchPipeline(object):
    def process_item(self, item, spider):
        if not isinstance(spider, V2exSpider):
            return

        index_elastic_search("v2ex", generate_id(item), item.type, dict(item))


def generate_id(item):
    return base64.b64encode(item['url'])
