import json


class Percepts:
    data = json.load(open('/Users/admin/workspace/ScentScraper/scrapy_env/scrapyScent/flavornet.json'))

    percepts = set()
    perceptFrequency = {}

    for molecule in data:
        string = molecule['percepts']
        if ',' in string:
            strings = string.split(', ')
            for percept in strings:

                percepts.add(percept)
                # add the percept to frequencies or plus one if it occurred already
                if percept in perceptFrequency.keys():
                    perceptFrequency[percept] += 1
                else:
                    perceptFrequency[percept] = 1

        else:
            percepts.add(string)
            # add the percept to frequencies or plus one if it occurred already
            if string in perceptFrequency.keys():
                perceptFrequency[string] += 1
            else:
                perceptFrequency[string] = 1

    perceptGroupsFrequency = {}
    perceptGroupsSet = set()
    perceptGroupsList = []

    for molecule in data:
        perceptGroupsSet.add(molecule['percepts'])
        perceptGroupsList.append(molecule['percepts'])

    #  Print - exploring the data in the interpreter
    #  print(perceptGroupsSet)
    #  print(perceptFrequency)

    print(len(percepts).__str__() + ': number of unique percepts')  # number of unique percepts
    print(len(perceptGroupsSet).__str__() + ': number of unique mappings')  # number of unique mappings
    print(len(perceptGroupsList).__str__() + ': number of total mappings')  # number of total mappings

    # Manipulating the data for input into our vizualsation
    nodes = []

    for node in perceptFrequency:
        # Discount smells that only occur once in the database
        if perceptFrequency[node] > 1:
            nodes.append({'id': node, 'freq': perceptFrequency[node]})

    print(len(nodes))

    coocList = []
    tupleList = []
    links = []

    for mapping in perceptGroupsList:
        #  Only consider percepts that occured with others to create links for co-occurance network
        if ',' in mapping:
            perceptsPerceivedTogether = mapping.split(', ')
            perceptsPerceivedTogether.sort()
            coocList.append(perceptsPerceivedTogether)

    # Only consider up to 4 percepts, some entries have 5+ but I am ignoring these cases for simplicity
    for mapping in coocList:
        if len(mapping) is 2:
            tupleList.append(mapping)
        if len(mapping) is 3:
            tupleList.append([mapping[0], mapping[1]])
            tupleList.append([mapping[0], mapping[2]])
            tupleList.append([mapping[1], mapping[2]])
        if len(mapping) is 4:
            tupleList.append([mapping[0], mapping[1]])
            tupleList.append([mapping[0], mapping[2]])
            tupleList.append([mapping[0], mapping[3]])
            tupleList.append([mapping[1], mapping[2]])
            tupleList.append([mapping[1], mapping[3]])
            tupleList.append([mapping[2], mapping[3]])

    coocFreq = {}

    for t in tupleList:
        if t[0] + "--" + t[1] in coocFreq.keys():
            coocFreq[t[0] + "--" + t[1]] += 1
        else:
            coocFreq[t[0] + "--" + t[1]] = 1
    # print(coocFreq)

    for pairing in coocFreq:
        pair = pairing.split("--")
        links.append({"source": pair[0], 'target': pair[1], 'value': coocFreq[pairing]})

    output = {'nodes': nodes, 'links': links}

    with open('smells-nodes-links.json', 'w') as outfile:
        json.dump(output, outfile)

