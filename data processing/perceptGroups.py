import json


class PerceptGroups:

    data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.json'))

    perceptGroupsSet = set()
    perceptGroupsList = []

    for molecule in data:
        perceptGroupsSet.add(molecule['percepts'])
        perceptGroupsList.append(molecule['percepts'])

    print(perceptGroupsSet)
    print(len(perceptGroupsSet).__str__())  # number of unique mappings
    print(len(perceptGroupsList).__str__())  # number of total mappings
