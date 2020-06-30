import json
from rdkit  import Chem


file=open('Knowledge Base for Metabolites\MetXBioDB-1-0.json',encoding='utf8')

reaction_product_pairs=[]
data=json.load(file,encoding='utf8') 
for i in data['biotransformations']:
    entry_rp={}
    entry_rp['Substrate_Name']=data['biotransformations'][i]['Substrate']['Name']
    substrate_mol=Chem.inchi.MolFromInchi(str(data['biotransformations'][i]['Substrate']['InChI']))
    entry_rp['SubstrateMolecule']=substrate_mol
    entry_rp['Enzymes']=list(str(data['biotransformations'][i]['Enzyme(s)']).split(";"))
    entry_rp['BioTransformer_type']=data['biotransformations'][i]['Biotransformation type']
    entry_rp['BioSystem']=data['biotransformations'][i]['Biosystem']
    
    for x in data['biotransformations'][i]['Products']:
        products=[]
        entry_product={}
        entry_product['Product_Name']=x.get('Name')
        prodcut_mol=Chem.inchi.MolFromInchi(str(x.get('InChI')))
        entry_product['Product_Molecule']=prodcut_mol
        products.append(entry_product)
       
        
    entry_rp['Products']=products 
   
    reaction_product_pairs.append(entry_rp)   
    
    
print(reaction_product_pairs)

    
