#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Descrição: Usado para o estudo do funcionamento básico do circuito integrado 555.
Autor: Eduardo S. Pereira;
e-mail: edu.estelar@gmail.com
Data: 19/05/2010
Distribuido sobre a licensa: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.
Detalhes da licensa em: http://www.softwarelivre.gov.br/Licencas/gnu-lesser-general-public-license
'''
from Tkinter import *
from os import getcwd
from calcMMA import *
from Exe555 import *


                                 
        

class MyApp():
    '''Classe que definine a aparencia do programa Py555
Metodos:
'''

    def __init__(self,parente):
        '''Inicializa a classe'''
        self.loc = str(getcwd())+'/figuras'        
        self.parente = parente
        self.parente.title("Py555 V1")

        menubar = Menu(self.parente)
        helpmenu = Menu(menubar)
        helpmenu.add_command(label="Sobre",command=self.sobre)
        helpmenu.add_separator
        menubar.add_cascade(label="Ajuda",menu=helpmenu)
        self.parente.config(menu=menubar)

        self.frame0=Frame(self.parente)
        self.frame0.pack()
        texto0 ='''
Conheça o CI 555, clique nos numeros
abaixo para obter a funcionalidade
de cada terminal.

'''
        self.L0_1 = Label(self.frame0,text=texto0)
        self.L0_1.pack()
        
        self.frame01=Frame(self.parente)
        self.frame01.pack()
        self.B01_1 = Button(self.frame01,width=1,text='8',command=self.Termi_8)
        self.B01_1.pack(side=LEFT)
        self.L01_1=Label(self.frame01,text='   ')
        self.L01_1.pack(side=LEFT)
        self.B01_2 = Button(self.frame01,width=1,text='7',command=self.Termi_7)
        self.B01_2.pack(side=LEFT)
        self.L01_2=Label(self.frame01,text='   ')
        self.L01_2.pack(side=LEFT)
        self.B01_3 = Button(self.frame01,width=1,text='6',command=self.Termi_6)
        self.B01_3.pack(side=LEFT)
        self.L01_3=Label(self.frame01,text='    ')
        self.L01_3.pack(side=LEFT)
        self.B01_4 = Button(self.frame01,width=1,text='5',command=self.Termi_5)
        self.B01_4.pack(side=LEFT)
        
        self.frame02 =Frame(self.parente)
        self.frame02.pack()
        self.L00 = Label(self.frame02,bitmap='@'+self.loc+'/555.xbm')
        self.L00.pack()

        self.frame03=Frame(self.parente)
        self.frame03.pack()
        self.B03_1 = Button(self.frame03,width=1,text='1',command=self.Termi_1)
        self.B03_1.pack(side=LEFT)
        self.L03_1=Label(self.frame03,text='   ')
        self.L03_1.pack(side=LEFT)
        self.B03_2 = Button(self.frame03,width=1,text='2',command=self.Termi_2)
        self.B03_2.pack(side=LEFT)
        self.L03_2=Label(self.frame03,text='   ')
        self.L03_2.pack(side=LEFT)
        self.B03_3 = Button(self.frame03,width=1,text='3',command=self.Termi_3)
        self.B03_3.pack(side=LEFT)
        self.L03_3=Label(self.frame03,text='   ')
        self.L03_3.pack(side=LEFT)
        self.B03_4 = Button(self.frame03,width=1,text='4',command=self.Termi_4)
        self.B03_4.pack(side=LEFT)

        self.frame04=Frame(self.parente)
        self.frame04.pack()
        texto01 ='''
Abaixo e possivel acessar alguns
exemplos de utilização do 555:

'''
        self.L04_1 = Label(self.frame04,text=texto01)
        self.L04_1.pack()
        
        self.frame05= Frame(self.parente)
        self.frame05.pack()
        self.L03 = Label(self.frame05,width='21',text="Circuito  Temporizador  \n(Multivibrador Monoestável)  ")
        self.L03.pack(side=LEFT)
        self.botao01 = Button(self.frame05,text="ex.",command=self.Temporizador)
        self.botao01.pack(side=LEFT)

        self.frame06= Frame(self.parente)
        self.frame06.pack()
        self.L06_1 = Label(self.frame06,width='21',text="Circuito  Oscilado  \n(Multivibrador astável)  ")
        self.L06_1.pack(side=LEFT)
        self.botao06_1 = Button(self.frame06,text="ex.",command=self.Oscilador)
        self.botao06_1.pack(side=LEFT)

        self.frame07= Frame(self.parente)
        self.frame07.pack()
        self.L07_1 = Label(self.frame07,width='21',text="\nCalculadora de Valores \npara Multivibrador \nMonoestável e Astável")
        self.L07_1.pack()
        self.botao07_1 = Button(self.frame07,text="Calc MMA.",command=self.Calc555)
        self.botao07_1.pack()

        self.TempoOb = None
        self.FreqOb=None
        self.CalcOb = None


    def Temporizador(self):
        self.TempoOb = Temp555(self.parente)

    def Oscilador(self):
        self.FreqOb = Freq555(self.parente)

    def Calc555(self):
        self.CalcOb = Calculadora(self.parente)

    def Termi_1(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 1')
        texto = '''Negativo da alimentação( 0 Volts).
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_2(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 2')
        texto = '''Entrada de Disparo ou gatilho.
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_3(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 3')
        texto = '''Saída, com capacidade de cerca de 200 miliampéres,
pode acionar diretamente cargas ligadas
tanto no negativo da alimentação
quanto ao positivo.
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_4(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 4')
        texto = '''Reset ou pino de rearmar.
No caso de uso como temporizador, esse pino deve ser mantido diretamente ligado
ao terminal positivo de entrada, seja diretamente ou através de um botao de pressão.
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_5(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 5')
        texto = '''Entrada de voltagem de controle. Pode ser ligado a
linha de zero volts através de um capacitor de 0.01 microfaradey
para previnir instabilidades ou captações espúrias de ruídos.
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_6(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 6')
        texto = '''Sensor de nível de voltagem.
'''
        L = Label(win,text=texto)
        L.pack()
        
    def Termi_7(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 7')
        texto = '''Pino de descarga do capacitor externo.
'''
        L = Label(win,text=texto)
        L.pack()

    def Termi_8(self):
        win = Toplevel(self.parente)
        win.wm_title('Teminal 8')
        texto = '''Positivo da alimentação, sendo aceitas
tensões entre 5 a 15 volts C.C.
'''
        L = Label(win,text=texto)
        L.pack()

    def sobre(self):
        win = Toplevel(self.parente)
        texto ='''Py555- programa de estudo do funcionamento
basico do circuito integrado 555.
Desenvolvido por: Eduaro S. Pereira.
e-mail: edu.estelar@gmail.com
V 1.0
'''
        L0 = Label(win,text=texto)
        win.wm_title('Sobre')
        L0.pack()



if __name__ == "__main__":
    win = Tk()
    Nwin = MyApp(win)
    win.mainloop()
    
