# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem


class RuSpider(scrapy.Spider):
    name = 'RU'
    allowed_domains = ['ru.unb.br']
    start_urls = ['http://ru.unb.br/index.php/cardapio-refeitorio']

    def parse(self, response):
        result = []
        for element in response.css(".container .item-page p a"):
            path = element.css("a::attr(href)").extract_first()
            text = element.css("a::text").extract_first()
            if len(text) <= 1:
                text = element.css("a>span::text").extract_first()
            if not text:
                text = element.css("a>span>span::text").extract_first()
            if path and text:
                pdf = response.follow(path).url
                item = CrawlerItem(text=text, path=path, url=pdf)
                yield item
