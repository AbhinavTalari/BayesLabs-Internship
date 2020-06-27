import json
file=open('MetXBioDB-1-0.json')

data=json.load(file)  #opens json file

for i in data['transformations']:
    print(i)
    print("\n")