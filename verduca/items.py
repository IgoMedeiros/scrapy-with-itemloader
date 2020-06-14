# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from w3lib.html import remove_tags

from scrapy.loader.processors import Join, TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class VeducaItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    lectures_in = MapCompose(remove_tags, str.strip)


class VerducaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        output_processor=Join(' ')
    )
    headline = scrapy.Field(
        output_processor=Join(' ')
    )
    url = scrapy.Field()
    instructors = scrapy.Field(
        output_processor=Join(' , ')
    )
    lectures = scrapy.Field()
    image = scrapy.Field()
