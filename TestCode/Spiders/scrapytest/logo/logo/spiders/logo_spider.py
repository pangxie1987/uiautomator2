# -*- coding:utf-8 -*-
# import os
# import sys
# casepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 
# sys.path.append(casepath)

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from logo.items import LogoItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Spider

class LogoSpider(CrawlSpider):
    name = "logo"
    allowed_domains = ["pcauto.com.cn"]
    start_urls = ["http://www.pcauto.com.cn/zt/chebiao/faguo/",]
    rules = (
        Rule(LinkExtractor(allow = ('http://www.pcauto.com.cn/zt/chebiao/.*?/$')), follow = True, callback = 'parse_page'),
    )

    def parse_page(self, response):
        sel = Selector(response)
        item = LogoItem()
        item['country'] = ''.join(sel.xpath('//div[@class="th"]/span[@class="mark"]/a/text()').extract())
        item['carname'] = sel.xpath('//div[@class="dTxt"]/i[@class="iTit"]/a/text()').extract()
        item['imageurl'] = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@src').extract()

        return item

