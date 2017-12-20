from scrapy.loader import ItemLoader
import scrapy
from scrapers.items import ScrapyItemPoverty


class PovertySpider(scrapy.Spider):
    name = "poverty"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapers.pipelines.PovertyPipeline': 300
        }
    }

    def start_requests(self):

        urls = [
            'http://wdi.worldbank.org/table/1.2',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css('#scrollTable tbody')
        rows = data.css('tr')
        for row in rows:
            country = row.css('td.country div a::text').extract_first()
            percent = row.css('td:nth-last-child(2) div::text').extract_first()
            l = ItemLoader(item=ScrapyItemPoverty(), response=response)
            l.add_value('country', country)
            l.add_value('percent', percent)
            yield l.load_item()
