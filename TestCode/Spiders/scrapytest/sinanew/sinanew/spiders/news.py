# -*- coding:utf-8 -*-

import scrapy

class scrapyDoc(scrapy.Spider):
    'Scrapy jiaocheng'
    name = 'scrapydoc'
    start_urls = ['http://www.scrapyd.cn/jiaocheng/']
    def parse(self, response):
        news = response.css("ul.media-list")
        news = news.css("div.media-body")
        self.log('news===%s'%news)
        for new in news:
            title = new.css("h4::text").extract_first()
            if title == None:
                title = new.css("b::text").extract_first()
            content = new.css('p::text').extract_first()
            uptime = new.css("p.mbt")
            uptime1 = uptime.css("span::text").extract()[0]
            self.log('uptime1=====%s'%uptime1)

            with open('scrapy_doc.txt', 'a+') as f:
                f.write(title)
                f.write('\n')
                f.write(content)
                f.write('\n')
                f.write(uptime1)
                f.write('\n')
                f.write('\n')

        nextpage = response.css("ul.list-inline.pagesize")
        nextpage = nextpage.css("a::attr(href)").extract()[2]
        self.log('nextpage====%s'%nextpage)
        url = response.urljoin(nextpage)
        self.log('url====%s'%url)
        if url is not None:
            yield scrapy.Request(url, callback=self.parse)
        
        self.log('Save Sucess!!!')


class chinaNew(scrapy.Spider):
    'get china news'
    name = 'chinanew'
    start_urls = ['https://news.sina.com.cn/china/']
    def parse(self, response):
        news = response.xpath("//div[@class='main-content']")
        news = news.xpath("//div[@class='right-content']//li//a")
        #news = news.css("ul.news-1")
        # #links = news.css("a::attr(href)")
        # titles = news.css("a::text")
        self.log('titlessss===%s'%news)
        for title in news:
            links = title.xpath("@href").extract_first()
            titles = title.xpath("text()").extract_first()
            
            self.log('links===%s'%links)
            #title = title.extract()
            self.log('titles=====%s'%titles)
            with open('sina_news.txt', 'a+') as f:
                f.write(titles)
                f.write('\n')
                f.write(links)
                f.write('\n')
        self.log('Save Sucess!!!')


class worldNews(scrapy.Spider):
    'get world news'
    name = 'wdnew'
    start_urls = ['https://news.sina.com.cn/world/']
    def parse(self, response):
        '国际新闻'
        news = response.css('div.blk122')
        news = news.css('a::text')
        self.log('news====%s'%news)
        for new in news:
            title = new.extract()
            self.log('title===%s'%title)
            with open('wd_news.txt', 'a+') as f:
                f.write(title)
                f.write('\n')
                #f.close()
