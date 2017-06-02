from scrapy import Field, Spider, Item, Selector 

class Post(Item):
    url = Field()
    title = Field()

class PythonizameSpider(Spider):
   name, start_urls = 'PythonizameSpider', ['http://sapiensrunner.es']
   #url_allow = 'pythoniza.me'
   def parse(self, response):
       sel = Selector(response)
       sites = sel.xpath('//div[@id="blog"]//h2')
       items = []

       for site in sites:
           post = Post()
           post['title'] = site.xpath('a/text()').extract()
           post['url'] = site.xpath('a/@href').extract()
           items.append(post)
       return items