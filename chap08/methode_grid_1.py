#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from tkinter import *

fen1 = Tk()

# cr�ation de widgets 'Label' et 'Entry' :
txt1 = Label(fen1, text = 'Premier champ :')
txt2 = Label(fen1, text = 'Second :')
txt3 = Label(fen1, text = 'Troisi�me :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)

# cr�ation d'un widget 'Canvas' contenant une image bitmap :
can1 = Canvas(fen1, width =160, height =160, bg ='white')
photo = PhotoImage(file ='Martin_P.gif')
item = can1.create_image(80, 80, image =photo)

# Mise en page � l'aide de la m�thode 'grid' :
txt1.grid(row =1,sticky =E)
txt2.grid(row =2,sticky =E)
txt3.grid(row =3,sticky =E)
entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)

# d�marrage :
fen1.mainloop()
