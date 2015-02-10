from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector 
#from tuiorial.items import DmozItem 
from tutorial.items import DmozItem
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
  #      filename = response.url.split("/")[-2]
  #      open(filename, 'wb').write(response.body)
        sel = HtmlXPathSelector(response)
        sites = sel.select('//fieldset/ul/li')
        items =[]
        for site in sites:
            item= DmozItem()
            #item= TutorialItem()
            item['title']=site.select('a/text()').extract()
            item['link']=site.select('a/@href').extract()
            item['desc']=site.select('text()').extract()
            items.append(item)
        return items
