# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy



class BrickSetSpider(scrapy.Spider):
	

	name = 'scrapy1'
	allowed_domains = ['comprarseguridad.es/es/']
	start_urls = ['http://www.comprarseguridad.es',]

	def start_request(self, response):

		NEXT_PAGE_SELECTOR = 'ul.sf-menu a::attr(href)'
		for next_page in response.css(NEXT_PAGE_SELECTOR):
			self.start_urls.append(next_page.extract())
			for url in self.start_urls:
				scrapy.Request(url=url, callback=self.parse)
		print self.start_urls



	def parse(self, response):

		self.start_request(response)
	


	
		SET_SELECTOR = 'div.product-container'
		for res in response.css(SET_SELECTOR):

			NAME_SELECTOR = 'a.product-name::text'
			PIECES_OLD_SELECTOR = 'span.price::text'
			PIECES_REGEX = '(\d{0,4}\,\d{0,2}) (\\u20ac)'
			PIECES_NEW_SELECTOR = 'span.old-price::text'
			IMAGE_SELECTOR = 'img ::attr(src)'

			yield {
				'name': res.css(NAME_SELECTOR).extract_first(),
				'piece_old': res.css(PIECES_OLD_SELECTOR).extract_first(),
				'piece_new': res.css(PIECES_NEW_SELECTOR).extract_first(),			
				'image': res.css(IMAGE_SELECTOR).extract_first(),
			}





