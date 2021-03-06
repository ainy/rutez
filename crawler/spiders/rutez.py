from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from crawler.items import Sinset
from scrapy.contrib.loader import XPathItemLoader

class Rutez(CrawlSpider):
    name = "rutez"
    allowed_domains = ["labinform.ru"]
    start_urls = [
        "http://www.labinform.ru/ruthes/c/15/000/106646.htm"
    ]
    rules = [Rule(SgmlLinkExtractor(deny=('te',)), callback='parse_item', follow=True)]

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        for conc in hxs.select('//div[@class="conc-block"]'):
          item = Sinset()
          item['name'] = conc.select('b/text()').extract()[0]
          item['words'] = conc.select('div/a/text()').extract()
          item['rels'] = []
          for rel in conc.select('div/span'):
            item['rels'].append((rel.select('span/text()').extract()[0], rel.select('a/text()').extract()[0]))
          yield item 
