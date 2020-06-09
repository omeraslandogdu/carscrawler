# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['cars.com']
    #start_urls = ['http://cars.com/']

    def __init__(self, brand='', **kwargs):
        if brand == 'bmw':
            self.start_urls = [f'http://www.cars.com/for-sale/searchresults.action/?mkId=20005&perPage=100']
        elif brand == 'ford':
            self.start_urls = [f'http://www.cars.com/for-sale/searchresults.action/?mkId=20015&perPage=100']
        else:
            self.start_urls = [f'http://www.cars.com/for-sale/searchresults.action/?page=1&perPage=100']
        super().__init__(**kwargs)  # python3

    def parse(self, response):

        hxs = Selector(response)
