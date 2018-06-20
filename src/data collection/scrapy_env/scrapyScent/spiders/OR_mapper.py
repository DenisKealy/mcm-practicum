# -*- coding: utf-8 -*-
import scrapy


class OrMapperSpider(scrapy.Spider):
    name = 'OR_mapper'
    allowed_domains = ['']
    start_urls = ['http://file:///Users/admin/Google%20Drive/College/Masters%20-%20MCM/CA685%20-%20Practicum/Data%20Sets/OR%20Responses%2071%20Mols/Table%201_%20Log%20EC50s%20for%20all%20OR_odor%20pairs%20that%20pass%20the%20three%20statistical%20criteria%20outlined%20in%20the%20methods.html/']

    def parse(self, response):
        pass
