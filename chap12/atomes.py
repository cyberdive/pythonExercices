#! /usr/bin/env python
# -*- coding: Latin-1 -*-

class Atome:
    """atomes simplifi�s, choisis parmi les 10 premiers �l�ments du TP""" 
    table =[None, ('hydrog�ne',0),('h�lium',2),('lithium',4),
            ('b�ryllium',5),('bore',6),('carbone',6),('azote',7),
            ('oxyg�ne',8),('fluor',10),('n�on',10)]
            
    def __init__(self, nat):
        "le n� atomique d�termine le n. de protons, d'�lectrons et de neutrons" 
        self.np, self.ne = nat, nat           # nat = num�ro atomique
        self.nn = Atome.table[nat][1]
        
    def affiche(self):
        print
        print ("Nom de l'�l�ment :", Atome.table[self.np][0])
        print ("%s protons, %s �lectrons, %s neutrons" % \
                  (self.np, self.ne, self.nn))
               
class Ion(Atome):
    """les ions sont des atomes qui ont gagn� ou perdu des �lectrons"""
     
    def __init__(self, nat, charge):
        "le n� atomique et la charge �lectrique d�terminent l'ion"
        Atome.__init__(self, nat)
        self.ne = self.ne - charge
        self.charge = charge
    
    def affiche(self):
        Atome.affiche(self)
        print ("Particule �lectris�e. Charge =", self.charge   )     
        
### Programme principal : ###     

a1 = Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.affiche()
a2.affiche()
a3.affiche()                      
        
    
              
