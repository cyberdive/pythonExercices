#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# D�tection et positionnement d'un clic de souris dans une fen�tre :

from tkinter import *

def pointeur(event):
    chaine.configure(text = "Clic d�tect� en X =" + str(event.x) +\
                            ", Y =" + str(event.y))

fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()
