from scrapy.loader import ItemLoader
import scrapy
from ..items import ScrapyItemCountry


class CountriesSpider(scrapy.Spider):
    name = "countries"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapers.pipelines.CountryPipeline': 100
        }
    }

    def start_requests(self):

        urls = [
            'http://wdi.worldbank.org/table/2.1',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css('#scrollTable tbody')
        rows = data.css('tr')
        exclude = [
            'Hong Kong SAR, China', 'Macao SAR, China',
            'Sint Maarten (Dutch part)', 'St. Martin (French part)',
            'Turks and Caicos Islands'
        ]
        for row in rows:
            name = row.css('td.country div a::text').extract_first()
            if name in exclude:
                continue
            l = ItemLoader(item=ScrapyItemCountry(), response=response)
            l.add_value('name', name)
            yield l.load_item()