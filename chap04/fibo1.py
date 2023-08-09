#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.�.d. une suite
# de nombres dont chaque terme est �gal � la somme des deux pr�c�dents.

print ("Suite de Fibonacci :")

a,b,c = 1,1,1              # a & b servent au calcul des termes successifs
                           # c est un simple compteur
print (1)                # affichage du premier terme
while c<15:                # nous afficherons 15 termes au total
    a,b,c = b,a+b,c+1
    print (b)
