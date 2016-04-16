from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class AlibabaPid(CrawlSpider):
    name = "alibabacrawlspider"
    allowed_domains = ["alibaba.com"]
    start_urls = [
        "http://www.alibaba.com/Products"
    ]

    rules = (
        Rule(LinkExtractor(),
        'parse', 
        follow=True,
        ),
    )

    def parse(self, response):
        sel = Selector(response)
        titles = sel.xpath('//html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/h2')
        for title in titles:
            print title.extract()