#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Descrição: Exe555 - Parte do programa Py555. Possui os exemplos de uso do 555 como oscilador e temporizador.
Autor: Eduardo S. Pereira;
e-mail: edu.estelar@gmail.com
Data: 17/05/2010
Distribuido sobre a licensa: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.
Detalhes da licensa em: http://www.softwarelivre.gov.br/Licencas/gnu-lesser-general-public-license
'''

from Tkinter import *
from os import getcwd
class Temp555():
    ''''''
    def __init__(self,win):
        self.loc = str(getcwd())+'/figuras'
        self.Nwin = Toplevel(win)        
        self.Ti =self.Nwin.title("Circuito temporizador simples")
        texto1='''
Circuito temporizador, mantem o LED acionado por um
tempo determinado, sendo tal tempo função de C e R. Os valores de R2 e R1 são
respectivamente 33k ohms e 470 ohms. É dado por:
T =1.1*C*R/1000
em segundos.

'''
        L0_1 = Label(self.Nwin,text=texto1)
        L0_1.pack()
        
        self.frame = Frame(self.Nwin)
        self.frame.pack()
        self.L0 = Label(self.frame,width='45',text='Digite o valor do resitor em kOhm: ')
        self.L0.pack(side=LEFT)
        self.e0 = Entry(self.frame,width='20')
        self.e0.pack(side=LEFT)

        self.frame1 = Frame(self.Nwin)
        self.frame1.pack()
        self.L1 = Label(self.frame1,width='45',text='Digite o valor do capacitor em microfarad: ')
        self.L1.pack(side=LEFT)
        self.e1 = Entry(self.frame1,width='20')
        self.e1.pack(side=LEFT)

        self.frame2 = Frame(self.Nwin)
        self.frame2.pack()
        Botao = Button(self.frame2,text='Calcular',command=self.resultado)
        Botao.pack()
        
        self.frame3=Frame(self.Nwin)
        self.frame3.pack()
        self.L3 = Label(self.frame3)
        self.L3.configure(text='\n\nO tempo que o LED permanecera aceso e de : ')
        self.L3.pack()
        self.canvas = Canvas(self.frame3,height="300",width="400")
        self.canvas.pack()
        self.canvas.create_bitmap(200,150,bitmap='@'+self.loc+'/temp3.xbm')
        self.canvas.create_text(360,95,text='R = ')
        self.canvas.create_text(360,175,text='C =  ')
        self.r= 0
        self.c= 0
        

    def resultado(self):
        self.canvas.delete('all')
        self.r= float(self.e0.get())
        self.c=float(self.e1.get())
        
        t= (1.1*self.r*self.c)/1000.0
        tm =t/60.0
        self.canvas.create_bitmap(200,150,bitmap='@'+self.loc+'/temp3.xbm')
        self.canvas.create_text(360,95,text='R = '+str(self.r))
        self.canvas.create_text(360,175,text='C =  '+str(self.c))
        self.L3.configure(text='\n\nO tempo que o LED permanecera aceso e de : '+str(t)+' segundos'+' ou '+str(tm)+' min.')
        
class Freq555():
    ''''''
    def __init__(self,win):
        self.Nwin = Toplevel(win)
        self.loc = str(getcwd())+'/figuras'
        self.Ti =self.Nwin.title("Oscilador - Multivibrador Astavel")
        texto1='''
Circuito oscilador - Multivibrador astável.
A frequência de oscilação irá depender dos valores dos
resistores RA e RB tal como do capacitor C.
A frequência é dada por:
F=1,44/(C*(RA+RB))
em Hertz

'''
        L0_1 = Label(self.Nwin,text=texto1)
        L0_1.pack()
        
        self.frame = Frame(self.Nwin)
        self.frame.pack()
        self.L0 = Label(self.frame,width='45',text='Digite o valor do resitor A em Ohm: ')
        self.L0.pack(side=LEFT)
        self.e0 = Entry(self.frame,width='20')
        self.e0.pack(side=LEFT)

        self.frame1 = Frame(self.Nwin)
        self.frame1.pack()
        self.L1 = Label(self.frame1,width='45',text='Digite o valor do resistor B em Ohm: ')
        self.L1.pack(side=LEFT)
        self.e1 = Entry(self.frame1,width='20')
        self.e1.pack(side=LEFT)

        self.frame2=Frame(self.Nwin)
        self.frame2.pack()
        self.L2 = Label(self.frame2,width='45',text='Digite o valor do capacitor em Farad: ')
        self.L2.pack(side=LEFT)
        self.e2 = Entry(self.frame2,width='20')
        self.e2.pack(side=LEFT)

        self.frame3 = Frame(self.Nwin)
        self.frame3.pack()
        Botao = Button(self.frame3,text='Calcular',command=self.resultado)
        Botao.pack()
        
        self.frame4=Frame(self.Nwin)
        self.frame4.pack()
        self.L3 = Label(self.frame4)
        self.L3.configure(text='\n\nA frequência de saída será de : ')
        self.L3.pack()
        self.canvas = Canvas(self.frame4,height="300",width="400")
        self.canvas.pack()
        self.canvas.create_bitmap(240,150,bitmap='@'+self.loc+'/oscil1.xbm')
        self.canvas.create_text(25,85,text='RA = ')
        self.canvas.create_text(25,130,text='RB = ')
        self.canvas.create_text(25,200,text='C =  ')
        
        

    def resultado(self):
        self.canvas.delete('all')
        self.ra= float(self.e0.get())
        self.rb=float(self.e1.get())
        self.c=float(self.e2.get())
        Ra = self.ra/1.e3
        Rb = self.rb/1.e3
        
        f=1.44/(self.c*(self.ra+self.rb))
        self.L3.configure(text='\n\nA frequência de saída será de : '+str(f)+'Hz')
        self.canvas.create_bitmap(240,150,bitmap='@'+self.loc+'/oscil1.xbm')
        self.canvas.create_text(35,85,text='RA = '+str(Ra)+'K')
        self.canvas.create_text(35,130,text='RB = '+str(Rb)+'K')
        self.canvas.create_text(35,200,text='C =  '+str(self.c))
