# -*- coding: utf-8 -*-
import scrapy


class ProofSpider01Spider(scrapy.Spider):
    name = 'proof_spider01'
    allowed_domains = ['comprarseguridad.com']
    start_urls = ['http://comprarseguridad.com/']

    def parse(self, response):
        pass
