from scrapy.loader import ItemLoader
import scrapy
from scrapers.items import ScrapyItemMinimumAmount


class FoodSpider(scrapy.Spider):
    name = "food"

    def start_requests(self):

        urls = [
            'https://www.numbeo.com/food-prices/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        pages = response.css('.related_links a::attr(href)').extract()
        for page in pages:
            page = response.urljoin(page)
            page += '&displayCurrency=USD'
            yield scrapy.Request(page, callback=self.parse)

    def parse(self, response):
        data = response.css('div.innerWidth')
        country = data.xpath('//span[@itemprop="name"]/text()').extract()[1]
        print(country)
        amount = data.css('table:nth-of-type(2) '
                          + 'tr:nth-last-child(2) '
                          + 'td:nth-child(2)::text').extract_first(),
        amount = amount[0].strip('\u00a0$')
        l = ItemLoader(item=ScrapyItemMinimumAmount(), response=response)
        l.add_value('country', country)
        l.add_value('amount', amount)
        yield l.load_item()
