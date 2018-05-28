# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

from crawler.items import CrawlerItem




class A1eSpider(scrapy.Spider):
    name = '1e'
    allowed_domains = ['17173.com']
    start_urls = ['http://news.17173.com/gameview/cos/']

    def parse(self, response):

        # 获取图片的原始地址, 需要逐步去解析
        aa = Selector(response=response).xpath('//div[@class="yxdy"]/ul/li/span/a/@href').extract()
        for ii in aa:
            yield Request(url=ii, callback=self.get_Image_real)
        next = Selector(response=response).xpath('//div[@class="pagination"]/ul/li/a/@href').extract()
        for i in next:
            yield Request(url=i, callback=self.parse)



    def get_Image_real(self, response):
        next = Selector(response=response).xpath('//div[@class="gb-final-mod-pagination-in"]/a/@href').extract()
        for i in next:
            yield Request(url=i, callback=self.get_Image_detail)


    def get_Image_detail(self, response):
        items = CrawlerItem()
        urls = Selector(response=response).xpath('//p[@class="p-image"]/a/img/@src').extract()
        titles = Selector(response=response).xpath('//div[@class="gb-final-mod-article gb-final-mod-article-p2em"]/p[@style="text-align: center;"]/text()').extract()

        if len(urls) > len(titles):
            urls = urls[0: len(titles)-1]

        elif len(urls) < len(titles):
            titles = titles[0: len(urls) - 1]

        items["Rurl"] = urls
        items["title"] = titles


        return items

        #
        # for i in titles:
        #     print("***" * 10)
        #     print(i)
