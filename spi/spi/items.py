# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name = scrapy.Field()
	piece_old = scrapy.Field()
	piece_new = scrapy.Field()
	image = scrapy.Field()
	reference = scrapy.Field()
	estado = scrapy.Field()
	descuento = scrapy.Field()
	detalle = scrapy.Field()
