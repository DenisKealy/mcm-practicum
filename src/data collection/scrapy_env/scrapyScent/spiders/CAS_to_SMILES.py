# -*- coding: utf-8 -*-
import scrapy
import pandas
import json


class CasToSmilesSpider(scrapy.Spider):
    name = 'CAS_to_SMILES'
    allowed_domains = ['https://cactus.nci.nih.gov/']
    start_urls = []



    def start_requests(self):

        flavornet_data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.json'))

        for molecule in flavornet_data:
            url = self.allowed_domains[0] + 'chemical/structure/' + molecule['CAS_no'].__str__() + '/smiles'
            request = scrapy.Request(
                url,
                dont_filter=True
            )
            request.meta['CAS_no'] = molecule['CAS_no']
            yield request
        #
        # keller_data = pandas.read_excel('/Users/admin/workspace/ScentScraper/scrapy_env/data/KellerData.xlsx')
        #
        # values = keller_data['Keller and Vosshall: Raw psychophysical data from 55 subjects'].values
        # keller_cas_values = set()
        #
        # #  Molecules are tested at 2 volumes of intensity in this dataset.
        # #  By adding them to a set we get a total of 480 unique molecules.
        # for v in values[2:1005]:
        #     keller_cas_values.add(v)
        #
        # for cas in keller_cas_values:
        #     url = self.allowed_domains[0] + 'chemical/structure/' + cas.__str__() + '/smiles'
        #     request = scrapy.Request(
        #         url,
        #         dont_filter=True
        #     )
        #     request.meta['CAS_no'] = cas
        #     yield request

    def parse(self, response):
        item = {
            'CAS_no': response.meta['CAS_no'],
            'SMILES': response.body.__str__().lstrip("b'").rstrip("'")
        }
        yield item
