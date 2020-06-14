# -*- coding: utf-8 -*-
import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from verduca.items import VerducaItem, VeducaItemLoader

class VeducaSpider(scrapy.Spider):
    name = 'veduca'
    allowed_domains = ['veduca.org']
    start_urls = ['https://www.play.veduca.org/cursos']

    def parse(self, response):
        course_list = response.xpath("//div[contains(@class, 'cardCurso')]//a")
        for course_item in course_list:
            url = course_item.xpath(".//@href").extract_first()
            yield scrapy.Request(
                url=url,
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        loader = VeducaItemLoader(VerducaItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('title', '//*[contains(@class, "tituloBanner")]/h2/text()')
        loader.add_xpath('headline', '//*[contains(@class, "textoBanner")]/p/text()')
        loader.add_xpath('instructors', '//*[contains(@class, "ministradoPor")]/h2/text()')
        loader.add_xpath('lectures', '//div[contains(@class, "listaConteudo")]/ul')

        yield loader.load_item()