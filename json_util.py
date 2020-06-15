# @Author: Abhinav T.

import json
file=open('Knowledge Base for Metabolites\metabolicReactions.json')

data=json.load(file)  #opens json file
modified_data={}    #keeps the extracted data in a dict
for i in data['reactions']:  #extracts the names of reactions
    data_dict={}
    for x in data['reactions'][i]:
        
        if x !='smarts' and x!='negativeSmarts':  #extracts the commonName, btmrID, smirks
            data_dict[x]=str(data['reactions'][i][x])
        
    modified_data[i]=data_dict     #stores the each dict as a value to the Reaction name as key 
with open('simplified.json','a+') as write_file:  #writes it into the json file.
    json.dump(modified_data,write_file,indent=4)


#Change the Directory and filen names if you use it again somewhere