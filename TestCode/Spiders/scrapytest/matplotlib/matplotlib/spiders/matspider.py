import re
from scrapy.spider import Spider, CrawlSpider, Rule
from urllib.parse import urlparse, urlunparse
from matplotlib.items import MatplotlibItem
from scrapy.linkextractors import LinkExtractor
from scrapy import Request

class matSpider(Spider):
    name = 'matplotlib'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html',]

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="matplotlib-examples"]/div',deny='/index.html$')
        for link in le.extract_links(response):
            yield Request(link.url, callback=self.parse_link)

    def parse_link(self,response):
        pattern=re.compile('href=(.*\.py)')
        div=response.xpath('/html/body/div[4]/div[1]/div/div')
        p=div.xpath('//p')[0].extract()
        link=re.findall(pattern,p)[0]
        if ('/') in link:      #针对包含文件，图片的下载链接方式生成：http://matplotlib.org/examples/pyplots/whats_new_99_mplot3d.py
            href='https://matplotlib.org/'+link.split('/')[2]+'/'+link.split('/')[3]+'/'+link.split('/')[4]
        else:     #针对只包含文件的下载链接方式生成：http://matplotlib.org/mpl_examples/statistics/boxplot_demo.py
            link=link.replace('"','')
            scheme=urlparse(response.url).scheme
            netloc=urlparse(response.url).netloc
            temp=urlparse(response.url).path
            path='/'+temp.split('/')[1]+'/'+temp.split('/')[2]+'/'+link
            combine=(scheme,netloc,path,'','','')
            href=urlunparse(combine)
#            print href,os.path.splitext(href)[1]
        file=MatplotlibItem()
        file['file_urls']=[href]
        return file