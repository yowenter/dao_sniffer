import logging
import random

import time

logger = logging.getLogger(__name__)

from dao_sniffer.spiders.v2ex_spider import V2exSpider


class V2exCheckRateLimit(object):
    def process_response(self, request, response, spider):
        if not isinstance(spider, V2exSpider):
            return response
        logger.info("V2ex Check api rate limit . . . request url`%s`", request.url)
        now = int(time.time())
        headers = response.headers
        if int(headers.get('X-Rate-Limit-Remaining', 360)) < 80:
            logger.warn("V2ex api rate limit `%s`", headers['X-Rate-Limit-Remaining'])
            time.sleep(random.randint(1, 60))

        if int(headers.get('X-Rate-Limit-Remaining', 360)) < 10:
            reset = int(headers.get('X-Rate-Limit-Reset'))
            s = reset - now
            logger.warning("V2ex api rate limited to 10 ...Will sleep  `%s` secs", s)
            time.sleep(s)

        return response
