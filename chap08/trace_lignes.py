#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Petit exercice utilisant la librairie graphique Tkinter

# d�finition des fonctions gestionnaires d'�v�nements :
def drawline():
    "Trac� d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)

    # modification des coordonn�es pour pr�parer la ligne suivante :
    y2, y1 = y2+10, y1-10

def changecolor():
    "Changement al�atoire de la couleur du trac�"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)        # => g�n�re un nombre al�atoire de 0 � 7
    coul = pal[c]

#------ Programme principal -------
from tkinter import *
from random import randrange

# les variables suivantes seront utilis�es de mani�re globale :
x1, y1, x2, y2 = 10, 190, 190, 10   # coordonn�es de la ligne
coul = 'dark green'                 # couleur de la ligne

# Cr�ation du widget principal ("parent") :
fen1 = Tk()
# cr�ation des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)

bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()

# d�marrage de l'observateur d'�v�nements (boucle principale) :
fen1.mainloop()
fen1.destroy()
