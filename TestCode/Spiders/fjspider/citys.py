# -*- coding:utf-8 -*-
'''
获取房价信息，并做成趋势图
解决python3.6 scrapy 的安装问题
https://blog.csdn.net/liuweiyuxiang/article/details/68929999
'''
import os
import json
import scrapy

class FjSpider(scrapy.Spider):
    '获取城市的url，存入本地文件'
    name = 'fjspider'
    allowed_domains = ['gz.fangjia.com']
    start_urls = []
    start_urls.append("http://gz.fangjia.com/zoushi?cityName=广州&__s=1&keyword=")

    def parse(self, reaponse):
        items = []
        headings = reaponse.xpath('//*[@id="moreCity"]')
        for content in headings:
            for i in range(0, 23):
                print(i)
                cnname = content.xpath('./div['+str(i)+']/a/text()').extract()
                enname = content.xpath('./div['+str(i)+']/a/@name').extract()
                url = content.xpath('./div[' + str(i) + ']/a/@href').extract()
                for j in range(len(cnname)):
                    item = HeadingItem()
                    item['cnname'] = cnname[j]
                    item['enname'] = enname[j]
                    item['url'] = url[j]
                    items.append(item)
                    return items

class FjSpider2(scrapy.Spider):
    '请求历史房价信息，使用分多次下载，防止频繁请求而出现验证码限制的情况'
    name = 'fjspider2'
    allowed_domains = []
    start_urls = []
    city = []
    base_dir = os.path.dirname(__file__)
    
    num = 0
    is_download = {}
    download_file = os.path.join(base_dir + '/download.txt')
    print(download_file)
    with open (download_file, "r") as f:
        for line in f:
            is_download[line] = 1
            num = num+1
            filename = base_dir + '/fsspider.txt'
            index = 0
            with open(filename, "r") as f:
                for line in f:
                    if not line in is_download:
                        info = line.split('|')
                        http = info[2].replace("/zoushi", "").replace("","")
                        url = http+"/trend/year2Data?defaultCityName="+info[0]+"&districtName=&region=&block=&keyword="
                        start_urls.append(info[0])
                        city.append(info[0])
                        with open(download_file, 'a') as ff:
                            ff.write("%s" % (line))
                            index = index + 1
                            if index > num +50:
                                break
    
    def parse(self, response):
        items = []
        values = json.loads(response.body_as_unicode())
        city = values['series'][0]['name']
        array = values['series'][0]['data']
        for i in range(len(array)):
            item = HeadingItem()
            item['time'] = int(array[i][0]/1000)
            item['value'] = array[i][1]
            item['city'] = city
            item.append(item)
            return items


if __name__ == '__main__':
    FjSpider2()
