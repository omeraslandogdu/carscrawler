from scrapy import Spider, Request
from crawler.items import CrawlerItem
import re



class Cars(Spider):
    name = 'cars'
    allowed_domains = ['cars.com']

    # start_urls = ['http://cars.com/']

    def __init__(self, **kwargs):
        self.brand = kwargs.pop('brand')
        if self.brand == 'BMW':
            self.start_urls = ["https://www.cars.com/for-sale/searchresults.action/?mkId=20005&page=1&perPage=100&rd=20&searchSource=NEW_SEARCH&sort=relevance&zc=90006"]
        elif self.brand == 'FORD':
            self.start_urls = ["https://www.cars.com/for-sale/searchresults.action/?mkId=20015&page=1&perPage=100&rd=20&searchSource=NEW_SEARCH&sort=relevance&zc=90006"]
        super().__init__(**kwargs)  # python3

    def parse(self, response):

        blocks = response.xpath('//*[@id="srp-listing-rows-container"]/div[@class="shop-srp-listings__listing-container"]')

        for i,block in enumerate(blocks):

            car = block.xpath('.//h2[@class="listing-row__title"]/text()').extract_first().strip()

            year = car[0:4]

            try:
                price = block.xpath('.//span[@class="listing-row__price "]/text()').extract_first().strip().replace('$','').replace(',', '')
            except AttributeError:
                price = block.xpath('.//span[@class="listing-row__price new"]/text()').extract_first().strip().replace('$', '').replace(',', '')

            if price == '':
                price = 0
            else:
                price = int(price)

            brand = self.brand
            ext_color = block.xpath('.//ul[@class="listing-row__meta"]//text()').extract()[3].strip()
            int_color = block.xpath('.//ul[@class="listing-row__meta"]//text()').extract()[7].strip()
            transmission = block.xpath('.//ul[@class="listing-row__meta"]//text()').extract()[11].strip()
            drivetrain = block.xpath('.//ul[@class="listing-row__meta"]//text()').extract()[15].strip()

            try:
                mileage = block.xpath('.//span[@class="listing-row__mileage"]/text()').extract_first().strip()
            except:
                mileage = None

            detail_url = block.xpath('//div[@class="shop-srp-listings__listing-container"][{}]/a/@href'.format(i + 1)).extract_first()

            item = CrawlerItem()
            item['brand'] = brand
            item['url'] = 'https://cars.com' + detail_url
            item['year'] = year
            item['price'] = price
            item['mileage'] = mileage
            item['ext_color'] = ext_color
            item['int_color'] = int_color
            item['transmission'] = transmission
            item['drivetrain'] = drivetrain

            yield item

