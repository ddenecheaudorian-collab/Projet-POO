from Cartes_De import *
from Effets_Cartes import Effets

E = Etablissement("Verger")
print(E.type)
print(type(E))
print(E.cout_construction)

M = Monument("Tour Radio")
print(M.type)
print(M.cout_construction)
M.effet_carte(5,43)