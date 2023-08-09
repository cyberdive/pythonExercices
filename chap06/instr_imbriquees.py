#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Instructions compos�es <while> - <if> - <elif> - <else>

print ('Choisissez un nombre de 1 a 3 (ou zero pour terminer) ')
a=input()
print (a)
a=int(a)
print (a)
while a != 0:           # l'op�rateur != signifie "diff�rent de"
    if a == 1:
        print ("Vous avez choisi un :")
        print ("le premier, l'unique, l'unite ...")
    elif a == 2:
        print ("Vous preferez le deux :")
        print ("la paire, le couple, le duo ...")
    elif a == 3:
        print ("Vous optez pour le plus grand des trois :")
        print ("le trio, la trinite, le triplet ...")
    else :
        print ("Un nombre entre UN et TROIS, s.v.p.")
    print ('Choisissez un nombre de 1 a 3 (ou zero pour terminer) ')
    a = input()
    a=int(a)
    print (a)
print ("Vous avez entre zero :")
print ("L'exercice est donc termine.")
