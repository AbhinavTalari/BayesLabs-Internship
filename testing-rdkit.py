from rdkit  import Chem
m1=Chem.inchi.MolFromInchi("InChI=1S/C8H9NO2/c1-6(10)9-7-2-4-8(11)5-3-7/h2-5,11H,1H3,(H,9,10)")
print(m1)