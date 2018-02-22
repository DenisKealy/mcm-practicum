# -*- coding: utf-8 -*-
import scrapy


class scentScraperSpider(scrapy.Spider):
    name = 'flavornet2'
    start_urls = ['file:///Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.html']

    def parse(self, response):
        i = 0
        while i <= 750:
            item = {
                'molecule_name': response.xpath("//td[@class='ch']/a/text()")[i].extract(),
                'CAS_no': response.xpath("//td[@class='ch']/a").xpath("@href")[i].extract()[30:-5],
                'percepts': response.xpath("//td[@class='sm']/text()")[i].extract(),
            }
            i += 1
            yield item

