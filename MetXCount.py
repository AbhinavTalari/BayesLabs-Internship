import json
from rdkit  import Chem
import pandas as pd
from copy import copy,deepcopy


def reactant_product_pair():
    file=open('Knowledge Base for Metabolites\MetXBioDB-1-0.json',encoding='utf8')
    biosys_set=set()
    
    reactants=[]
    reaction_product_pairs=[]
    data=json.load(file,encoding='utf8') 
    for i in data['biotransformations']:
        entry_rp={}
        entry_rp['Substrate_Name']=data['biotransformations'][i]['Substrate']['Name']
        substrate_mol=Chem.inchi.MolFromInchi(str(data['biotransformations'][i]['Substrate']['InChI']))
        entry_rp['SubstrateMolecule']=substrate_mol
        entry_rp['METXBIODB_ID']=str(data['biotransformations'][i]['Substrate']['METXBIODB_ID'])
        entry_rp['Enzymes']=list(str(data['biotransformations'][i]['Enzyme(s)']).split(";"))
        entry_rp['BioTransformer_type']=data['biotransformations'][i]['Biotransformation type']
        biosys_set.add(entry_rp['BioTransformer_type'])
        
        entry_rp['BioSystem']=data['biotransformations'][i]['Biosystem']
    
        for x in data['biotransformations'][i]['Products']:
            products=[]
            entry_product={}
            entry_product['Product_Name']=x.get('Name')
            prodcut_mol=Chem.inchi.MolFromInchi(str(x.get('InChI')))
            entry_product['Product_Molecule']=prodcut_mol
            products.append(entry_product)
       
        
        entry_rp['Products']=products 
        rc={}
        for j in entry_rp.keys():
            if j!='Products':
                rc[str(j)]=entry_rp[str(j)]
    
   
        reaction_product_pairs.append(entry_rp)  
        reactants.append(rc)
    return reactants,biosys_set
    
reactants,biosys=reactant_product_pair()
# print(len(reactants))
def club_biosys(reactants):
    hp1=[]
    hp2=[]
    hgm=[]
    for x in reactants:
        if x['BioTransformer_type']=='Human Phase I':
            hp1.append(x)
        if x['BioTransformer_type']=='Human Phase II':
            hp2.append(x)
        if x['BioTransformer_type']=='Human Gut Microbial':
            hgm.append(x)
    return hp1,hp2,hgm
            
hp1,hp2,hgm=club_biosys(reactants)
print(len(hp1))
print(len(hp2))
print(len(hgm))
print(biosys)

def Extract_Phase1(reactants):
    phase_1=[]
    for x in reactants:
        if x['BioTransformer_type']=='Human Phase II':
            # print(x)
            phase_1.append(x)
    print(len(phase_1))
Extract_Phase1(reactants)

