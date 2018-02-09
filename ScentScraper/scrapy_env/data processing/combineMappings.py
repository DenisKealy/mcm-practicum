import json


class CombineMappings:

    flavornet = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/data/mappings.json'))
    keller = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/data/keller_mappings.json'))

    combined = []

    for mapping in flavornet:
        if mapping not in combined:
            combined.append(mapping)

    for mapping in keller:
        if mapping not in combined:
            combined.append(mapping)

    # Total of 507 molecules in combined dataset so far. len(combined) = 507
    # This is the number of molecules for which we can obtain
    # both the perceptual and the physical descriptors needed.
    with open('cas_mc_map.json', 'w') as outfile:
        json.dump(combined, outfile, indent=2)

