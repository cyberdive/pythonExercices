#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from tkinter import *
fen1 = Tk()

# cr�ation de widgets Label(), Entry(), et Checkbutton() :
Label(fen1, text = 'Premier champ :').grid(sticky =E)
Label(fen1, text = 'Second :').grid(sticky =E)
Label(fen1, text = 'Troisi�?me :').grid(sticky =E)
entr1 = Entry(fen1)
entr2 = Entry(fen1)                 # ces widgets devront certainement
entr3 = Entry(fen1)                 # �tre  r�f�renc�s plus loin :
entr1.grid(row =0, column =1)       # il faut donc les assigner chacun
entr2.grid(row =1, column =1)       # � une variable distincte
entr3.grid(row =2, column =1)
chek1 = Checkbutton(fen1, text ='Case � cocher, pour voir')
chek1.grid(columnspan =2)

# cr�ation d'un widget 'Canvas' contenant une image bitmap :
can1 = Canvas(fen1, width =160, height =160, bg ='white')
photo = PhotoImage(file ='Martin_P.gif')
can1.create_image(80,80, image =photo)
can1.grid(row =0, column =2, rowspan =4, padx =10, pady =5)

# d�marrage :
fen1.mainloop()
