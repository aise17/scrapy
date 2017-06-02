# -*- coding: utf-8 -*-
import scrapy


class ComprarseguridadSpider(scrapy.Spider):
    name = 'comprarseguridad'
    allowed_domains = ['comprarseguridad.es']
    start_urls = ['http://comprarseguridad.es/']

    def parse(self, response):
        pass
