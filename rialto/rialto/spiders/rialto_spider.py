import scrapy

class AlibabaPid(scrapy.Spider):
    name = "alibabapid"
    allowed_domains = ["alibaba.com"]
    start_urls = [
        "http://www.alibaba.com/Products"
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        urls = sel.xpath('//ul[@class="sub-item-cont util-clearfix"]')
        for url in urls:
            print url.extract()