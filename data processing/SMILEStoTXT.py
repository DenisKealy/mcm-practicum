import json


class SmilesToTxt:

    file = json.load(open('/Users/admin/workspace/2018-mcm-kealyd2/data/KellerCAStoSMILES.json'))

    smilesList = []

    for molecule in file:
        smilesList.append(molecule['SMILES'])

    with open('KellerSmiles.txt', 'w') as o:
        for string in smilesList:
            o.write(string + '\n')
