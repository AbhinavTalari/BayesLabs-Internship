

import rdkit

from rdkit import Chem

#take a smile molecule
smile=str(input("Enter a Smile ID")) 
sample_smile="C1=CC2=C(C=C1)C1=CC=CC=C21"
m = Chem.MolFromSmiles(smile)
print(type(m))
m
#Check no. of atoms

#Type of Atoms

#No. and types of bonds

#Charge on molecule

#Aromaticity
ri = m.GetRingInfo()
# You can interrogate the RingInfo object to tell you the atoms that make up each ring:
print("Which atoms make up the ring?")
print(ri.AtomRings())

# or the bonds that make up each ring:
print("Which bonds make up each ring?")
print(ri.BondRings())


# To detect aromatic rings, I would loop over the bonds in each ring and
# flag the ring as aromatic if all bonds are aromatic:
def isRingAromatic(mol, bondRing):
        for id in bondRing:
            if not mol.GetBondWithIdx(id).GetIsAromatic():
                return False
        return True
    


for i in range(0,len(ri.AtomRings())):
        print("Is Ring No "+str(i+1)+ " Aromatic?")    
        print(isRingAromatic(m, ri.BondRings()[i]))
    



# print(isRingAromatic(m, ri.BondRings()[1]))




