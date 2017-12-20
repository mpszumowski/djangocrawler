from scrapy.loader import ItemLoader
import scrapy
from scrapers.items import ScrapyItemMinimumAmount


class FoodSpider(scrapy.Spider):
    name = "food"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapers.pipelines.FoodPipeline': 300
        }
    }

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
        # country name
        country = data.xpath('//span[@itemprop="name"]/text()').extract()[1]
        # unify and merge country values with those from WorldBank db
        merger = {
            'Brunei': 'Brunei Darussalam',
            'Yemen': 'Yemen, Rep.',
            'Venezuela': 'Venezuela, RB',
            'Syria': 'Syrian Arab Republic',
            'South Korea': 'Korea, Rep.',
            'Slovakia': 'Slovak Republic',
            'Saint Vincent And The Grenadines':
                'St. Vincent and the Grenadines',
            'Saint Lucia': 'St. Lucia',
            'Russia': 'Russian Federation',
            'Palestinian Territory': 'West Bank and Gaza',
            'Micronesia': 'Micronesia, Fed. Sts.',
            'Macedonia': 'Macedonia, FYR',
            'Kyrgyzstan': 'Kyrgyz Republic',
            'Laos': 'Lao PDR',
            'Kosovo (Disputed Territory)': 'Kosovo',
            'Ivory Coast': 'Cote d\'Ivoire',
            'Iran': 'Iran, Islamic Rep.',
            'Gambia': 'Gambia, The',
            'Egypt': 'Egypt, Arab Rep.',
            'Congo': 'Congo, Dem. Rep.',
            'Cape Verde': 'Cabo Verde',
        }
        for k, v in merger.items():
            if k == country:
                country = v
        # minimum $ for daily food ration
        amount = data.css('table:nth-of-type(2) '
                          + 'tr:nth-last-child(2) '
                          + 'td:nth-child(2)::text').extract_first(),
        amount = amount[0].strip('\u00a0$')
        l = ItemLoader(item=ScrapyItemMinimumAmount(), response=response)
        l.add_value('country', country)
        l.add_value('amount', amount)
        yield l.load_item()
