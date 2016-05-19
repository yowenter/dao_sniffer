import scrapy
import json
import logging
import time
from functools import partial
from dao_sniffer.items import V2exPostItem

logger = logging.getLogger(__name__)


class V2exSpider(scrapy.Spider):
    name = "v2ex"
    start_urls = [
        "http://v2ex.com"
    ]

    def __init__(self, recent_limit=3, *args, **kwargs):
        self.recent_limit = int(recent_limit)
        self.recent_posts_api = "https://www.v2ex.com/api/topics/latest.json"
        self.comments_api = "https://www.v2ex.com/api/replies/show.json"

        super(V2exSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        return [scrapy.Request(url="{}?p={}".format(self.recent_posts_api, i + 1)) for i in range(self.recent_limit)]

    def parse(self, response):
        resp = json.loads(response.body_as_unicode())
        for post in resp:
            f = partial(self.to_document, post_data=post)
            yield scrapy.Request(url="{}?topic_id={}".format(self.comments_api, post['id']), callback=f)

    def to_document(self, replies_resp, post_data=None, *args, **kwargs):
        replies_data = json.loads(replies_resp.body_as_unicode())

        yield V2exPostItem(url=post_data['url'],
                           timestamp=int(time.time()),
                           document=dict(
                               create_ts=post_data['created'],
                               update_ts=post_data['last_modified'],
                               last_comment_ts=post_data['last_touched'],
                               user=dict(id=post_data['member']['id'], name=post_data['member']['username']),
                               tags=[post_data['node']['name']],
                               title=post_data['title'],
                               content=post_data['content'],
                               comments_num=post_data['replies'],
                               comments=[
                                   dict(content=reply['content'],
                                        user=dict(id=reply['member']['id'], name=reply['member']['username']),
                                        zaned=reply['thanks']
                                        ) for reply in replies_data
                                   ]
                           )
                           )
