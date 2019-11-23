#  -*- coding:utf-8 -*-

import scrapy


class NextSpiderSpider(scrapy.Spider):
    name = "nextSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css('div.quote')
        
        for v in mingyan:  
            next_page = response.css('li.next a::attr(href)').extract_first()  

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)


            text = v.css('.text::text').extract_first()  
            autor = v.css('.author::text').extract_first()  
            tags = ','.join(tags)  

            fileName = '%s-mingyan.txt' % autor 

            with open(fileName, "a+") as f:  
                f.write(text)
                f.write('\n')  
                f.write('tags:' + tags)
                f.write('\n-------\n')
                f.close()


