import json

file=open('Knowledge Base for Metabolites\metabolicReactions.json')

data=json.load(file)
modified_data={}   
for i in data['reactions']:
    data_dict={}
    for x in data['reactions'][i]:
        
        if x !='smarts' and x!='negativeSmarts':
            data_dict[x]=str(data['reactions'][i][x])
        
    modified_data[i]=data_dict    
with open('simplified.json','a+') as write_file:
    json.dump(modified_data,write_file,indent=4)


