# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint


class RuSpider(scrapy.Spider):
    name = 'RU'
    allowed_domains = ['ru.unb.br']
    start_urls = ['http://ru.unb.br/index.php/cardapio-refeitorio']

    def parse(self, response):
        result = []
        for element in response.css(".container .item-page p"):
            link = element.css("a::attr(href)").extract_first()
            text = element.css("a::text").extract_first()
            if not text:
                text = element.css("a span span::text").extract_first()
            if link:
                yield {'link': link, 'text': text}
