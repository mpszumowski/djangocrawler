# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
sys.path.insert(0, '/home/maciej/workspace/sCrapProject/')
from crawler.models import MinimumAmount, PovertyPercent


class FoodPipeline(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        bulk = []
        for item in self.items:
            print(item)
            obj = MinimumAmount(country=item["country"][0],
                                amount=item["amount"][0])
            bulk.append(obj)
        MinimumAmount.objects.bulk_create(bulk)


class PovertyPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        bulk = []
        for item in self.items:
            print(item)
            if
            obj = PovertyPercent(country=item["country"][0],
                                 percent=item["percent"][0])
            bulk.append(obj)
        PovertyPercent.objects.bulk_create(bulk)