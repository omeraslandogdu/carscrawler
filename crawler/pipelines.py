# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from src.cars.models import Cars

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        cars = Cars()
        cars.brand = item['brand']
        cars.urlitem = ['url']
        cars.year = item['year']
        cars.priceitem = ['price']
        cars.mileage = item['mileage']
        cars.ext_color = item['ext_color']
        cars.int_coloritem = ['int_color']
        cars.transmissionitem = ['transmission']
        cars.drivetrain = item['drivetrain']

        cars.save()