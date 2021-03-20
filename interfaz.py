import tkinter as tk
from tkinter import *

lista_operaciones=list() #almacenamos las operaciones que se registren aqui

root=tk.Tk()
root.geometry("360x300")
root.title("Calculadora Sistemas Numericos")

entrada_operacion=tk.StringVar() 




operacion=tk.Entry(root,textvariable=entrada_operacion) 
operacion.pack()
operacion.place(width=320,height=30,x=20,y=50) 

#inicio botones indicadores sistema numerico
btdec=tk.Button(root,text="Dec") 
btdec.pack() 
btdec.place(x=20,y=100,width=80)

bthex=tk.Button(root,text="Hex") 
bthex.pack() 
bthex.place(x=100,y=100,width=80)

btoct=tk.Button(root,text="Oct") 
btoct.pack() 
btoct.place(x=180,y=100,width=80)

btbin=tk.Button(root,text="Bin") 
btbin.pack() 
btbin.place(x=260,y=100,width=80) 
#fin botones indicadores sistema numerico

#inicio botones alfabeticos 
bta=tk.Button(root,text="A") 
bta.pack()
bta.place(x=20,y=150,width=40)
btb=tk.Button(root,text="B") 
btb.pack()
btb.place(x=60,y=150,width=40)
btc=tk.Button(root,text="C") 
btc.pack()
btc.place(x=20,y=180,width=40)
btd=tk.Button(root,text="D") 
btd.pack()
btd.place(x=60,y=180,width=40)
bte=tk.Button(root,text="E") 
bte.pack()
bte.place(x=20,y=210,width=40)
btf=tk.Button(root,text="F") 
btf.pack()
btf.place(x=60,y=210,width=40)
#Fin botones alfabeticos  

#Inicio botones numericos 
bt1=tk.Button(root,text="1")
bt1.pack()
bt1.place(x=110,y=150,width=40)
bt2=tk.Button(root,text="2")
bt2.pack()
bt2.place(x=150,y=150,width=40)
bt3=tk.Button(root,text="3")
bt3.pack()
bt3.place(x=190,y=150,width=40)
#------------------------------
bt4=tk.Button(root,text="4")
bt4.pack()
bt4.place(x=110,y=180,width=40)
bt5=tk.Button(root,text="5")
bt5.pack()
bt5.place(x=150,y=180,width=40)
bt6=tk.Button(root,text="6")
bt6.pack()
bt6.place(x=190,y=180,width=40)
#-------------------------------
btclr=tk.Button(root,text="CLR")
btclr.pack()
btclr.place(x=110,y=210,width=40)
bt0=tk.Button(root,text="0")
bt0.pack()
bt0.place(x=150,y=210,width=40)
btcall=tk.Button(root,text="Call")
btcall.pack()
btcall.place(x=190,y=210,width=40)
#Fin botones numericos 

#Inicio botones operacionales 
btsum=tk.Button(root,text="+")
btsum.pack()
btsum.place(x=240,y=150,width=40)
btrest=tk.Button(root,text="-")
btrest.pack()
btrest.place(x=280,y=150,width=40)
#---------------------
btmult=tk.Button(root,text="*")
btmult.pack()
btmult.place(x=240,y=180,width=40)
btdiv=tk.Button(root,text="/")
btdiv.pack()
btdiv.place(x=280,y=180,width=40)

#------------------------
btpow=tk.Button(root,text="**")
btpow.pack()
btpow.place(x=240,y=210,width=40)
bteq=tk.Button(root,text="=")
bteq.pack()
bteq.place(x=280,y=210,width=40)

#Fin botones operacionales 


#Inicio botones adicionales

btcreditos=tk.Button(root,text="Creditos")
btcreditos.pack()
btcreditos.place(x=20,y=260,width=80)

btinstrucciones=tk.Button(root,text="Instrucciones") 
btinstrucciones.pack()
btinstrucciones.place(x=200,y=260,width=100)

#Fin botones adicionales



root.mainloop()