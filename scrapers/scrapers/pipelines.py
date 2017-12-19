# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
sys.path.insert(0, '/home/maciej/workspace/sCrapProject/')
from crawler.models import MinimumAmount


class ScrapersPipeline(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        # model = MinimumAmount()
        # for item in self.items:
        #     print(object)
        #     model.country = item["country"]
        #     model.amount = item["amount"]
        #     model.save()
        bulk = []
        for item in self.items:
            print(item)
            obj = MinimumAmount(country=item["country"][0],
                                amount=item["amount"][0])
            bulk.append(obj)
        MinimumAmount.objects.bulk_create(bulk)
