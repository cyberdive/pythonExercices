#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Petit exercice utilisant la librairie graphique Tkinter

from tkinter import *

# d�finition des gestionnaires d'�v�nements :

def move():
    "d�placement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >210:
        x1, dx, dy = 210, 0, 15
    if y1 >210:
        y1, dx, dy = 210, -15, 0
    if x1 <10:
        x1, dx, dy = 10, 0, -15
    if y1 <10:
        y1, dx, dy = 10, 15, 0
    can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0: 
        fen1.after(50,move)		# boucler apr�s 50 millisecondes

def stop_it():
    "arret de l'animation"
    global flag    
    flag =0

def start_it():
    "d�marrage de l'animation"
    global flag
    if flag ==0:	# pour �viter que le bouton ne puisse lancer plusieurs boucles 
       flag =1
       move()

#========== Programme principal =============

# les variables suivantes seront utilis�es de mani�re globale :
x1, y1 = 10, 10		# coordonn�es initiales
dx, dy = 15, 0		# 'pas' du d�placement
flag =0			# commutateur

# Cr�ation du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")
# cr�ation des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=250,width=250)
can1.pack(side=LEFT)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='D�marrer',command=start_it)
bou2.pack()
bou3 = Button(fen1,text='Arr�ter',command=stop_it)
bou3.pack()
# d�marrage de l'observateur d'�v�nements (boucle principale) :
fen1.mainloop()
