# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import time
import hashlib
from scrapy.utils.python import to_bytes

from crawler.utils.CRM import DBCRM


class CrawlerPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # self.dirname = item["url"]
        for i in range(0, len(item['Rurl'])-1):

            try:
            #     print("now request: " + "*" * 30)
            #     print(item['Rurl'][i])
            #     print(item['title'][i])
            #     print("*" * 30)
            #
            #     print('现在保存图片开始.......')

                Rurl = item['Rurl'][i]
                url = hashlib.sha1(to_bytes(item['Rurl'][i])).hexdigest()+'.jpg'
                title = item['title'][i]

                items = {}
                items["Rurl"] = Rurl
                items["url"] = url
                items["title"] = title
                dbcrm = DBCRM()
                dbcrm.Coser_Save(items)

                print('图片原始地址: ' + Rurl)
                print('图片描述:    ' + title)
                print('图片本地地址: ' + url)
                print('图片保存结束..........................................')
                #
                yield Request(item['Rurl'][i])
            except Exception as e:
                print("-Error-" * 20)
                print(e)
            time.sleep(1)

    # def item_completed(self, results, item, info):
    #     image_paths = [[x['path'] for ok, x in results if ok]]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #
    #     print('现在保存图片开始.......')
    #     image_guid = hashlib.sha1(to_bytes(item['Rurl'][0])).hexdigest()
    #     title =  item['title'][0]
    #
    #     print('图片原始地址: ' + item['Rurl'][0])
    #     print('图片描述: ' + title)
    #     print('图片本地地址: '+ image_guid)
    #     print('图片保存结束..........................................')
    #
    #     return item

    #
    # def item_completed(self, results, item, info):
    #     if isinstance(item, dict) or self.images_result_field in item.fields:
    #         item[self.images_result_field] = [x for ok, x in results if ok]
    #     print('现在保存图片开始.......')
    #
    #     Rurl = item['Rurl'][0]
    #     url = str(hashlib.sha1(to_bytes(item['Rurl'][0])).hexdigest())+'.jpg'
    #     title =  item['title'][0]
    #
    #     items = {}
    #     items["Rurl"] = Rurl
    #     items["url"]  = url
    #     items["title"]= title
    #     dbcrm = DBCRM()
    #     dbcrm.Coser_Save(items)
    #
    #     print('图片原始地址: ' + item['Rurl'][0])
    #     print('图片描述: ' + title)
    #     print('图片本地地址: '+ url)
    #     print('图片保存结束..........................................')
    #     return item
    #
    #
    # def file_path(self, request, response=None, info=None):
    #     ## start of deprecation warning block (can be removed in the future)
    #     def _warn():
    #         from scrapy.exceptions import ScrapyDeprecationWarning
    #         import warnings
    #         warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
    #                       'please use file_path(request, response=None, info=None) instead',
    #                       category=ScrapyDeprecationWarning, stacklevel=1)
    #
    #     # check if called from image_key or file_key with url as first argument
    #     if not isinstance(request, Request):
    #         _warn()
    #         url = request
    #     else:
    #         url = request.url
    #
    #     # detect if file_key() or image_key() methods have been overridden
    #     if not hasattr(self.file_key, '_base'):
    #         _warn()
    #         return self.file_key(url)
    #     elif not hasattr(self.image_key, '_base'):
    #         _warn()
    #         return self.image_key(url)
    #     ## end of deprecation warning block
    #
    #     image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
    #     return '%s.jpg' % (image_guid)