#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from tkinter import *
from math import *

# d�finition de l'action � effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il �dite le champ d'entr�e :

def evaluate(event):
    chaine.configure(text = "R�sultat = " + str(eval(entree.get())))

# ----- Programme principal : -----

fenetre = Tk()

entree = Entry(fenetre, bd=2, relief =GROOVE)
entree.bind("<Return>",evaluate)
entree.pack(padx =10, pady =5)

chaine = Label(fenetre)
chaine.pack(padx =10, pady =5)

fenetre.mainloop()
