# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.shell import inspect_response
from scrapy.item import Item, Field


class MolDescriptorsSpider(scrapy.Spider):
    name = 'mol_descriptors'
    allowed_domains = ['http://michem.disat.unimib.it/mole_db/']
    start_urls = []

    data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/data/cas_mc_map.json'))

    list_of_molecules = []
    descriptor_values = {}
    descriptor_descriptions = {}

    def start_requests(self):
        i = 0
        for cj, mapping in self.data:
            group = 0
            if i < 1:  # Limit the amount of requests
                while group < 20:  # There are 13 categories of descriptor; the final category is on page 20
                    url = self.allowed_domains[0] + 'desc_values.php?id=' + mapping['MC_no'] + \
                          '&desc_group=' + self.group.__str__()
                    request = scrapy.Request(
                        url,
                        dont_filter=True,
                        meta={'cookiejar': cj}
                    )
                    request.meta['CAS_no'] = mapping['CAS_no']
                    group += 1
                    yield request
            i += 1

    def parse(self, response):
        inspect_response(response, self)
        d_values = []

        # Ignore responses from the error page - 7 responses per molecule
        if "Problemi nel caricamento dati" in response.text:
            pass
        else:
            hits = response.css('table')[2].xpath('.//tr')
            i = 0
            for hit in hits:
                if i == 0:  # Used to skip the header row of the table
                    i += 1
                else:
                    d_values.append({hit.xpath('td[2]/text()').extract(): hits[1].xpath('td[3]/text()').extract()})
            for mol in self.list_of_molecules:
                if response.meta['CAS_no'] == mol['CAS_no']:
                    mol['descriptor_values'].extend(d_values)
                else:
                    self.list_of_molecules.append(Molecule(CAS_no=response.meta['CAS_no'], descriptor_values=d_values))
# in the code above I tried to create a list of all molecules
# perhaps best to scraped items in the form:
# item = {cas_no:str, descriptor_values:dict}  ## This way we can recombine the objects later using the CAS number

class Molecule(Item):
    CAS_no = Field()                    # String
    descriptor_values = Field()         # Dictionary
