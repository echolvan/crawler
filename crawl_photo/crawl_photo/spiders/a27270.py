# -*- coding: utf-8 -*-
import os

import scrapy

from crawl_photo.items import PicItem


class A27270Spider(scrapy.Spider):
    name = "27270"
    start_urls = ['http://www.27270.com/beautiful/zhuomianbeijing/2018/291522.html']

    def parse(self, response):
        item = PicItem()
        item['img_url'] = response.xpath('//p/a/img/@src').extract()[0]
        temp = response.xpath('//li[@id="nl"]/a/@href').extract()[0]
        # if temp == '##':
        #     return
        next = os.path.dirname(self.start_urls[0]) + '/' + temp
        yield item
        yield scrapy.Request(url=next)

