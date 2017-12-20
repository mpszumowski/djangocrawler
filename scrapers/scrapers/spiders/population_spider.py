from scrapy.loader import ItemLoader
import scrapy
from scrapers.items import ScrapyItemPopulation


class PopulationSpider(scrapy.Spider):
    name = "population"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapers.pipelines.PopulationPipeline': 300
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
        for row in rows:
            country = row.css('td.country div a::text').extract_first()
            estimate = row.css('td:nth-child(3) div::text').extract_first()
            l = ItemLoader(item=ScrapyItemPopulation(), response=response)
            l.add_value('country', country)
            l.add_value('estimate', estimate)
            l.add_value('data_year', 2016)
            yield l.load_item()