# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spi.items import SpiItem


class CseguridadSpider(CrawlSpider):
	

	name = 'comprarseguridad'
	allowed_domains = ['comprarseguridad.es']
	start_urls = ['http://www.comprarseguridad.es/es/defensas-extensibles/174-baston-extensible-53-cm-incluye-funda-rigida-esp.html',]
	'''
	rules = {

		Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="pagination_next"]/a/@href'))),
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]')), callback= 'parse_items', follow= False),

	}
	'''	

	def parse_items(self, response):

	
		SET_XPATH = '//*[@class="product-image-container"]/a/@href'
		PIECES_REGEX = '(\d{0,4}\,\d{0,2}) (\\u20ac)'

		for container in response.xpath('//*[@id="center_column"]/ul/li/div'):

			NAME_XPATH = '//*[@id="center_column"]/div/div/div[3]/h1/text()'
			PIECES_OLD_XPATH = '//*[@id="old_price_display"]/text()'
			PIECES_NEW_XPATH = '//*[@id="our_price_display"]/text()'
			IMAGE_XPATH = '//*[@id="bigpic"]/@src'
			REFERENCE_XPATH = '//*[@id="product_reference"]/span/text()'
			ESTADO_XPATH = '//*[@id="product_condition"]/span/text()'
			DESCUENTO_XPATH = '//*[@id="reduction_percent_display"]/text()'
			DETALLE_XPAT = '//*[@id="center_column"]/div/section[1]/div'
			ENTREGA_XPATH = '//*[@id="availability_value"]/text()'

			item = SpiItem()
			
			item['name'] = container.xpath(normalize-space(NAME_XPATH)).extract()
			item['piece_old'] = container.xpath(normalize-space(PIECES_OLD_XPATH)).extract()
			item['piece_new'] = container.xpath(normalize-space(PIECES_NEW_XPATH)).extract()
			item['image'] = container.xpath(normalize-space(IMAGE_XPATH)).extract()
			item['reference'] = container.xpath(normalize-space(REFERENCE_XPATH)).extract()
			item['estado'] = container.xpath(normalize-space(ESTADO_XPATH)).extract()
			item['descuento'] = container.xpath(normalize-space(DESCUENTO_XPATH)).extract()
			item['detalle'] = container.xpath(normalize-space(DETALLE_XPAT)).extract()
			yield item
			

		for nex_page in responseponse.xpath('//*[@id="pagination_next"]/a/@href'):
			yield respose.follow(nex_page, self.parse)
