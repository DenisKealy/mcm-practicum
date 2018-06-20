# -*- coding: utf-8 -*-
import scrapy
import json
import time
from scrapy.shell import inspect_response
import pandas


class MoleDBSpider(scrapy.Spider):
    name = 'MoleDB'
    start_urls = ['http://michem.disat.unimib.it/mole_db/']
    data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.json'))

    # Trying to overwrite the default start_requests method
    # def start_requests(self):
    #     i = 0
    #     for molecule in self.data:
    #         if i < 2:
    #             request = scrapy.FormRequest(
    #                 'http://michem.disat.unimib.it/mole_db/',
    #                 dont_filter=True,
    #                 formdata={'cas_val': molecule['CAS_no']}
    #             )
    #             request.meta['cas_val'] = molecule['CAS_no']
    #             i += 1
    #             yield request

    def parse(self, response):

        keller_data = pandas.read_excel('/Users/admin/workspace/ScentScraper/scrapy_env/data/KellerData.xlsx')

        # THIS GENERATES REQUESTS FOR EACH CAS IN THE KELLER DATASET - 332 Mappings from 480 total molecules
        values = keller_data['Keller and Vosshall: Raw psychophysical data from 55 subjects'].values
        keller_cas_values = set()
        for v in values[2:1005]:
            keller_cas_values.add(v)

        for cj, value in enumerate(keller_cas_values):
                form_request = scrapy.FormRequest.from_response(
                    response,
                    formdata={'cas_val': value},
                    callback=self.after_search,
                    meta={'cookiejar': cj}
                )
                form_request.dont_filter = True
                form_request.meta['CAS_no'] = value
                yield form_request

        # THIS GENERATE REQUESTS FOR EACH CAS FROM OUR FLAVORNET DATASET - 306 Mappings from 739 Total molecules
        # for cj, molecule in enumerate(self.data):
        #         form_request = scrapy.FormRequest.from_response(
        #             response,
        #             formdata={'cas_val': molecule['CAS_no']},
        #             callback=self.after_search,
        #             meta={'cookiejar': cj}
        #         )
        #         form_request.dont_filter = True
        #         form_request.meta['CAS_no'] = molecule['CAS_no']
        #         yield form_request

    def after_search(self, response):
        if "No molecules found." in response.text:
            print('Nothing Found')
        else:
            hits = response.css('table')[2].xpath('.//tr')
            cas_no = hits[1].xpath('.//td[4]/text()').extract_first()
            mc_no = None
            if cas_no == response.meta['CAS_no']:
                mc_no = hits[1].xpath('.//td[3]/text()').extract_first()
                item = {
                                'CAS_no': cas_no,
                                'MC_no': mc_no
                            }
                yield item

            if mc_no is None:
                print('No Exact Match for ' + response.meta['CAS_no'])

        # Check if we get a hit for the CAS no
        # if len(response.css('table').extract()) > 2:
        #     inspect_response(response, self)
        #     hits = response.css('table')[2].xpath('.//tr')
        #     for row in hits:
        #         # If the CAS no matches exactly
        #         if row.xpath('.//td[4]/text()').extract_first() == response.meta['cas_val']:
        #             inspect_response(response, self)
        #             # Re-create the item - appending the MC number for that molecule
        #             item = {
        #                 'molecule_name': response.meta['cas_name'],
        #                 'CAS_no': response.meta['cas_val'],
        #                 'percepts': response.meta['percepts'],
        #                 'MC_no': row.xpath('.//td[3]/text()').extract_first()
        #             }
        #             yield item
        # else:
        #     item = {
        #             'molecule_name': response.meta['cas_name'],
        #             'CAS_no': response.meta['cas_val'],
        #             'percepts': response.meta['percepts'],
        #             'MC_no': 'Not Found'
        #         }
        #     yield item

