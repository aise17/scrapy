'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from spi.items import MercadoItem

class MercadoSpider(CrawlSpider):
    name = 'mercado'
    item_count = 0
    allowed_domain = ['www.mercadolibre.com.mx']
    start_urls = ['http://listado.mercadolibre.com.mx/impresoras#D[A:impresoras,L:1]']

    rules = {
        # Para cada item
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="last-child"]/a'))),
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[@class="list-view-item-title"]')),
                            callback = 'parse_item', follow = False)
    }

    def parse_item(self, response):
        ml_item = MercadoItem()
        #info de producto
        ml_item['titulo'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/h1/text())').extract_first()
        ml_item['folio'] = response.xpath('normalize-space(//span[@class="id-item"]/text())').extract()
        ml_item['precio'] = response.xpath('normalize-space(//*[@id="productInfo"]/fieldset[1]/article/strong/text())').extract()
        ml_item['condicion'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/dl/div/dd[1]/text())').extract()
        ml_item['envio'] = response.xpath('normalize-space(//*[contains(@class,"shipping-method-title")]/text())').extract()
        ml_item['ubicacion'] = response.xpath('normalize-space(//span[@class="where"]/text())').extract()
        ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
        ml_item['ventas_producto'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/dl/div/dd[2]/text())').extract()
        #imagenes del producto
        ml_item['image_urls'] = response.xpath('//*[@id="gallery_dflt"]/div[1]/div[1]/a/img/@src').extract()
        ml_item['image_name'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/h1)').extract_first()
        #info de la tienda o vendedor
        ml_item['vendedor_url'] = response.xpath('//*[starts-with(@class, "reputation-view-more")]/@href').extract()
        ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[@class="reputation-seller-type"]/text())').extract()
        ml_item['reputacion'] = response.xpath('normalize-space(/html/body/main/div/section[3]/div/div[2]/div/dl/dd[1]/strong/text())').extract()
        ml_item['ventas_vendedor'] = response.xpath('normalize-space(/html/body/main/div/section[3]/div/div[2]/div/dl/dd[2]/strong/text())').extract()
        self.item_count += 1
        if self.item_count > 10:
            raise CloseSpider('item_exceeded')
        yield ml_itemss
'''