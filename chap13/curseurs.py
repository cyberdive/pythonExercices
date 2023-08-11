#! /usr/bin/env python
# -*- coding: Latin-1 -*-

##################################################
#                 Curseurs.py                    #
#  Widget contenant un groupe de curseurs pour   #
#  contr�ler trois param�tres (f,phi,a).         #
#  Un �v�nement sp�cifique est g�n�r� � chaque   #
#  modification, pour informer le widget ma�tre  #
#  qui peut alors r�agir en cons�quence          #
#                                                #
#      Auteur : G.Swinnen (Li�ge, Belgium)       #
#           16/03/2002 - Licence GPL             #
##################################################

from tkinter import *
from math import pi

class ChoixVibra(Frame):
    """Curseurs pour choisir fr�quence, phase & amplitude d'une vibration"""
    def __init__(self, maitre=None, coul='red'):
        Frame.__init__(self)        # constructeur de la classe parente
        # D�finition de quelques attributs d'instance :
        self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
        # Variable d'�tat de la case � cocher :
        self.chk = IntVar()                 # 'objet-variable' Tkinter
        Checkbutton(self, text='Afficher', variable=self.chk,
                    fg = self.coul, command=self.setCurve).pack(side=LEFT)
        # D�finition des 3 widgets curseurs :
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Fr�quence (Hz) :', from_=1., to=9., tickinterval =2,
              resolution =0.25,
              showvalue =0, command = self.setFrequency).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =15,
              label ='Phase (degr�s) :', from_=-180, to=180, tickinterval =90,
              showvalue =0, command = self.setPhase).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Amplitude :', from_=2, to=10, tickinterval =2,
              showvalue =0, command = self.setAmplitude).pack(side=LEFT, pady =5)

    def setCurve(self):
        self.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq = float(f)
        self.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp =float(p)
        self.phase = pp*2*pi/360        # conversion degr�s -> radians
        self.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.event_generate('<Control-Z>')

#### Code pour tester la classe : ###

if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text = '%s - %s - %s - %s' %
                         (fra.chk.get(), fra.freq, fra.phase, fra.ampl))
    root = Tk()
    fra = ChoixVibra(root,'navy')
    fra.pack(side =TOP)
    lab = Label(root, text ='test')
    lab.pack()
    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
