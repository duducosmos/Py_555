#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Descrição: Calc MMA - Calculadora Multivibrador Monoestável e Astável, parte do programa Py555.
Autor: Eduardo S. Pereira;
e-mail: edu.estelar@gmail.com
Data: 19/05/2010
Distribuido sobre a licensa: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.
Detalhes da licensa em: http://www.softwarelivre.gov.br/Licencas/gnu-lesser-general-public-license
'''

from Tkinter import *

class Calculadora():
    '''Calc MMA - Calculadora Multivibrador Monoestável e Astável'''
    def __init__(self,win):
        self.win=win
        self.Nwin = Toplevel(self.win)
        self.Ti = self.Nwin.title("Calc MMA")
        menubar = Menu(self.Nwin)
        helpmenu = Menu(menubar)
        helpmenu.add_command(label='Unidades de medida',command=self.unidades)
        helpmenu.add_separator
        helpmenu.add_command(label='Sobre',command=self.sobre)
        menubar.add_cascade(label='Ajuda',men=helpmenu)
        self.Nwin.config(menu=menubar)
        
        self.frame0 = Frame(self.Nwin)
        self.frame0.pack()
        self.e0_0 = Entry(self.frame0,width='50')
        self.e0_0.insert(0,'0')
        self.e0_0.pack()

        self.frame1 = Frame(self.Nwin)
        self.frame1.pack()
        self.L1_0 = Label(self.frame1,text='\nMultiibrador Monoestável - Temporizador')
        self.L1_0.pack()
        

        self.frame2 = Frame(self.Nwin)
        self.frame2.pack()
        self.L2_0 = Label(self.frame2,width='10',text='T')
        self.L2_0.pack(side=LEFT)
        self.L2_1 = Label(self.frame2,width='10',text='R')
        self.L2_1.pack(side=LEFT)
        self.L2_2 = Label(self.frame2,width='10',text='C')
        self.L2_2.pack(side=LEFT)
        
        self.frame3=Frame(self.Nwin)
        self.frame3.pack()
        self.e3_0= Entry(self.frame3,width='10')
        self.e3_0.insert(0,'0')
        self.e3_0.pack(side=LEFT)
        self.e3_1= Entry(self.frame3,width='10')
        self.e3_1.insert(0,'0')
        self.e3_1.pack(side=LEFT)
        self.e3_2= Entry(self.frame3,width='10')
        self.e3_2.insert(0,'0')
        self.e3_2.pack(side=LEFT)

        self.frame4=Frame(self.Nwin)
        self.frame4.pack()
        self.B4_0 = Button(self.frame4,width='10',text='obter Tempo',command=self.Tdu)
        self.B4_0.pack(side=LEFT)
        self.B4_1 = Button(self.frame4,width='10',text='Obter R',command=self.RV)
        self.B4_1.pack(side=LEFT)
        self.B4_2 = Button(self.frame4,width='10',text='Obter C',command=self.CV)
        self.B4_2.pack(side=LEFT)

        ###################################################################
        self.frame7 = Frame(self.Nwin)
        self.frame7.pack()
        self.L7_0 = Label(self.frame7,text='\nMultivibrador Astável - Oscilador\n')
        self.L7_0.pack()

        self.frame8 = Frame(self.Nwin)
        self.frame8.pack()
        self.L8_0 = Label(self.frame8,width='10',text='F')
        self.L8_0.pack(side=LEFT)
        self.L8_1 = Label(self.frame8,width='10',text='Ra')
        self.L8_1.pack(side=LEFT)
        self.L8_2 = Label(self.frame8,width='10',text='Rb')
        self.L8_2.pack(side=LEFT)
        self.L8_3 = Label(self.frame8,width='10',text='C')
        self.L8_3.pack(side=LEFT)

        self.frame9=Frame(self.Nwin)
        self.frame9.pack()
        self.e9_0= Entry(self.frame9,width='10')
        self.e9_0.insert(0,'0')
        self.e9_0.pack(side=LEFT)
        self.e9_1= Entry(self.frame9,width='10')
        self.e9_1.insert(0,'0')
        self.e9_1.pack(side=LEFT)
        self.e9_2= Entry(self.frame9,width='10')
        self.e9_2.insert(0,'0')
        self.e9_2.pack(side=LEFT)
        self.e9_3= Entry(self.frame9,width='10')
        self.e9_3.insert(0,'0')
        self.e9_3.pack(side=LEFT)

        self.frame10=Frame(self.Nwin)
        self.frame10.pack()
        self.B10_0 = Button(self.frame10,width='10',text='obter Freq.',command=self.FV)
        self.B10_0.pack(side=LEFT)
        self.B10_1 = Button(self.frame10,width='10',text='Obter Ra',command=self.RaV)
        self.B10_1.pack(side=LEFT)
        self.B10_2 = Button(self.frame10,width='10',text='Obter Rb',command=self.RbV)
        self.B10_2.pack(side=LEFT)
        self.B10_3 = Button(self.frame10,width='10',text='Obter C',command=self.CfV)
        self.B10_3.pack(side=LEFT)
        

    def Tdu(self):
        r = float(self.e3_1.get())
        c = float(self.e3_2.get())
        t= 1.1*r*c/1000.0
        texto='Duração do pulso de saída é de '+str(t)+' segundo'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)

    def RV(self):
        t=float(self.e3_0.get())
        c=float(self.e3_2.get())
        r=1000.0*t/(1.1*c)
        texto='O resistor deverá ter o valor de '+str(r)+' k ohms'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)
        
    def CV(self):
        t=float(self.e3_0.get())
        r=float(self.e3_1.get())
        c = 1000.0*t/(1.1*r)
        texto='O capacito deverá ter o valor de '+str(c)+' microfarads'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)

    def FV(self):
        c = float(self.e9_3.get())
        ra = float(self.e9_1.get())
        rb=float(self.e9_2.get())
        F= 1.44/(c*(ra+rb))
        texto ='O valor da frequência é de '+str(F)+' Hz'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)
        
    def RaV(self):
        c = float(self.e9_3.get())
        rb = float(self.e9_2.get())
        F=float(self.e9_0.get())
        ra=1.44/(F*c)-rb                
        texto ='O vloar do resistor A será de '+str(ra)+' Ohms'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)

    def RbV(self):
        c = float(self.e9_3.get())
        ra = float(self.e9_1.get())
        F=float(self.e9_0.get())
        rb=1.44/(F*c)-ra                
        texto ='O valor do resistor B será de '+str(rb)+' Ohms'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)

    def CfV(self):
        ra = float(self.e9_1.get())
        F=float(self.e9_0.get())
        rb= float(self.e9_2.get())
        c=1.44/(F*(ra+rb))
        texto ='O valor do capacitor será de '+str(c)+' farads'
        self.e0_0.delete(0,END)
        self.e0_0.insert(0,texto)

    #################################################################
    def unidades(self):
        Nwin = Toplevel(self.win)
        Nwin.wm_title('Unidades')
        texto='''
As unidades de tempo, resistor e capacitância, para o caso de calculos do uso do 555
como temporizador (Multivibrador monoestável) são dados em segundos, kOhms e microfarad respectivamente
Já as unidades para o caso do seu uso como oscilador (Multivibrador astável) as unidades
de frequência, resistores e do capacitor são respectivamente, Hertz, ohm e Farad.
Tenha muita atenção ao realizar os cálculos, pois as unidades de entrada irão interferir
no resultado final
'''
        L0 = Label(Nwin,text=texto)
        L0.pack()
    def sobre(self):
        win = Toplevel(self.win)
        texto ='''calcMMA- calculadora para o uso do circuito integrado 555
nos modos Multivibrador Monoestável e Astável
Desenvolvido por: Eduaro S. Pereira.
e-mail: edu.estelar@gmail.com
V 1.0
'''
        L0 = Label(win,text=texto)
        win.wm_title('Sobre')
        L0.pack()
        
        
