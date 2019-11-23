# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urlparse, urlunparse
from matplotlib.items import MatplotlibItem
from os.path import basename, dirname, join
from scrapy.pipelines.files import FilesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MatplotlibPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        temp = join(basename(dirname(path)), basename(path))
        return '%s/%s' % (basename(dirname(path)), basename(path))