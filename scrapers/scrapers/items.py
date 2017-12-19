# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import item


class MinimumAmount(item.Item):
    country = item.Field()
    amount = item.Field()

