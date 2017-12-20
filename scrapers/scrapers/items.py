# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import item


class ScrapyItemCountry(item.Item):
    name = item.Field()


class ScrapyItemPopulation(item.Item):
    country = item.Field()
    estimate = item.Field()
    data_year = item.Field()


class ScrapyItemMinimumAmount(item.Item):
    country = item.Field()
    amount = item.Field()


class ScrapyItemPoverty(item.Item):
    country = item.Field()
    percent = item.Field()
    data_year = item.Field()

