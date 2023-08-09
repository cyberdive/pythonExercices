#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Petit exercice utilisant la librairie graphique Tkinter

from tkinter import *

# proc�dure g�n�rale de d�placement :
def avance(gd, hb):
    global x1, y1
    x1, y1 = x1 +gd, y1 +hb
    can1.coords(oval1, x1, y1, x1+30, y1+30)
      
# d�finition des gestionnaires d'�v�nements :
def depl_gauche():
    avance(-10, 0)

def depl_droite():
    avance(10, 0)    

def depl_haut():
    avance(0, -10)
        
def depl_bas():
    avance(0, 10)    

#------ Programme principal -------

# les variables suivantes seront utilis�es de mani�re globale :
x1, y1 = 10, 10		# coordonn�es initiales
# Cr�ation du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")
# cr�ation des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
Button(fen1,text='Gauche',command=depl_gauche).pack()
Button(fen1,text='Droite',command=depl_droite).pack()
Button(fen1,text='Haut',command=depl_haut).pack()
Button(fen1,text='Bas',command=depl_bas).pack()
# d�marrage de l'observateur d'�v�nements (boucle principale) :
fen1.mainloop()
