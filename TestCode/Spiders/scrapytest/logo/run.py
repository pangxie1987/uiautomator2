# https://www.cnblogs.com/moon-future/p/5545828.html
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'logo', '-o', 'items.json'])

