import json
from rdkit  import Chem
import pandas as pd
from copy import copy,deepcopy


def reactant_product_pair():
    file=open('Knowledge Base for Metabolites\MetXBioDB-1-0.json',encoding='utf8')
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
    return reactants
    

def EnzymeBuckets(reactants):
    enzy_grps ={}
    
    for x in reactants:
        if x['BioSystem']=='Human':
            y=deepcopy(x)
            del y['Enzymes']
            for i in x['Enzymes']:
                enzy_grps.setdefault(str(i),[]).append(y)
    return enzy_grps
    
     

def Extract_Phase1(reactants):
    phase_1=[]
    for x in reactants:
        if x['BioTransformer_type']=='Human Phase I':
            # print(x)
            phase_1.append(x)
    return phase_1
   
# reactants=reactant_product_pair()
# phase1=Extract_Phase1(reactants)
# print(phase1)
        
    

def Extract_MetX_from_Ref():
    file=open('Knowledge Base for Metabolites\metaboliteprediction_referencedataset.json',encoding='utf8')
    data=json.load(file,encoding='utf8')
    p_mol=0
    met_mol=0
    MetX=[]
    for x in data:
       if x['Parent molecule']['MetXBioDB ID'] is not None:
            MetX.append(x)    
    return MetX
       

def count_ref_MetX(reactants,MetX):
    rcph1=Extract_Phase1(reactants)
    
    
    rec=[]
    ref=[]
    
    for x in rcph1:
        rec.append(x['METXBIODB_ID'])
    for y in MetX:
        ref.append(y['Parent molecule']['MetXBioDB ID'])
    
    rf,rc=0,0
    for i in rec:
        
            if i not in  ref:
                rc=rc+1
            else :
                rf=rf+1
            
    print(rc)
    print(rf)      
        
    def nonMatchRf(reactants,MetX):
        rcph1=Extract_Phase1(reactants)
        
    
    # for x in rec:
    #     for y in MetX:
    #         print(y)
    #         if x['METXBIODB_ID'] not in y['Parent molecule']['MetXBioDB ID']:
    #             notMet.append(x)
    #         else :
    #             MetX.append(x)
    # print(len(notMet))
    # print(len(rec))

                
                

reactants=reactant_product_pair()
MetX=Extract_MetX_from_Ref()

count_ref_MetX(reactants,MetX)
print(len(reactants))