import sys
import os
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

dao_sniffer_pkg_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dao_sniffer")

sys.path.append(dao_sniffer_pkg_dir)

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    from dao_sniffer.spiders.v2ex_spider import V2exSpider

    process.crawl(V2exSpider, recent_limit=100)
    process.start()
