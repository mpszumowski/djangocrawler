# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sys
# sys.path.insert(0, '/home/maciej/workspace/sCrapProject/')
from datetime import datetime
from crawler.models import (Countries, MinimumAmount, Misfits,
                            CountryPopulation, PovertyPercent)


class CountryPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        country_bulk = []
        for item in self.items:
            obj = Countries(name=item["name"][0])
            country_bulk.append(obj)
        Countries.objects.bulk_create(country_bulk)


class PopulationPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        population_bulk = []
        misfits_bulk = []
        for item in self.items:
            country = Countries.objects.filter(name=item["country"][0])
            if country:
                obj = CountryPopulation(country=country,
                                        estimate=item["estimate"][0],
                                        data_year=item["data_year"][0],
                                        date_scraped=datetime.now())
                population_bulk.append(obj)
            else:
                obj = Misfits(name=item["country"][0],
                              population_estimate=item["estimate"][0],
                              population_year=item["data_year"][0],
                              date_scraped=datetime.now())
                misfits_bulk.append(obj)
            CountryPopulation.objects.bulk_create(population_bulk)
            Misfits.objects.bulk_create(misfits_bulk)


class FoodPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        min_amount_bulk = []
        misfits_bulk = []
        for item in self.items:
            country = Countries.objects.filter(name=item["country"][0])
            if country:
                obj = MinimumAmount(country=country,
                                    amount=item["amount"][0],
                                    date_scraped=datetime.now())
                min_amount_bulk.append(obj)
            else:
                obj = Misfits(name=item["country"][0],
                              minimum_amount=item["amount"][0],
                              date_scraped=datetime.now())
                misfits_bulk.append(obj)
        MinimumAmount.objects.bulk_create(min_amount_bulk)
        Misfits.objects.bulk_create(misfits_bulk)


class PovertyPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        poverty_bulk = []
        misfits_bulk = []
        for item in self.items:
            country = Countries.objects.filter(name=item["country"][0])
            if country:
                obj = PovertyPercent(country=country,
                                     percent=item["percent"][0],
                                     data_year=item["data_year"][0],
                                     date_scraped=datetime.now())
                poverty_bulk.append(obj)
            else:
                obj = Misfits(name=item["country"][0],
                              percent=item["percent"][0],
                              date_scraped=datetime.now())
                misfits_bulk.append(obj)
        PovertyPercent.objects.bulk_create(poverty_bulk)
        Misfits.objects.bulk_create(misfits_bulk)