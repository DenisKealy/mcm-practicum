# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.shell import inspect_response


class Mole2Spider(scrapy.Spider):
    name = 'mole2'
    allowed_domains = ['http://michem.disat.unimib.it']
    data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.json'))

    def start_requests(self):
        i = 0
        for molecule in self.data:
            if i < 1:
                request = scrapy.FormRequest(
                    'http://michem.disat.unimib.it/mole_db/query.php?r=0',
                    dont_filter=True,
                    formdata={'cas_val': molecule['CAS_no']}
                )
                i += 1
                print(molecule['CAS_no'])
                yield request

    def parse(self, response):
        inspect_response(response, self)
