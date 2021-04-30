import tkinter as tk
from tkinter import *
import sys
sys.path.append("./modulos")
from modulos import logica_interfaz as lg 

cadena_operacion=""
tipo_resultado=""
pos_par=0

def registrar_entrada(caracter):
   
    aux=entrada_operacion.get() 
    aux+=caracter 
    entrada_operacion.set(aux)

def limpiar_entrada():
    entrada_operacion.set("") 

def eliminar_caracter(): 
    aux=entrada_operacion.get() 
    aux=aux[:len(aux)-1] 
    entrada_operacion.set(aux)

def eventos(event):
    texto=event.widget.cget("text")
    global cadena_operacion
    
    if(texto=="="):
        #Ejecucion de operaciones
        cadena_operacion=entrada_operacion.get()
        entrada_operacion.set("En que sistema desea recibir el numero?")
        
    elif(texto=="AC"):
        #Limpiar entrada 
        limpiar_entrada()
    elif(texto=="DEL"): 
        eliminar_caracter()
    elif(texto=="Enter"):
        tipo_resultado=entrada_operacion.get() 
        pos_par=tipo_resultado.find('(')
        tipo_resultado=tipo_resultado[pos_par:] 
        entrada_operacion.set(lg.ejecutar_cadena(cadena_operacion,tipo_resultado))
        
    else:
        #agrega caracter
        registrar_entrada(texto)
    



root=tk.Tk()
root.title("Calculadora Sistemas Numericos")
ventana=tk.Frame(root) 
ventana.config(width=350,height=350,bg="blue")
entrada_operacion=tk.StringVar()



operacion=tk.Entry(ventana,textvariable=entrada_operacion,state="readonly") 
operacion.place(width=320,height=30,x=20,y=50)



#inicio botones indicadores sistema numerico
btdec=tk.Button(ventana,text="(DEC)")  
btdec.bind('<Button-1>',eventos)
btdec.place(x=20,y=100,width=80)

bthex=tk.Button(ventana,text="(HEX)") 
bthex.bind('<Button-1>',eventos)
bthex.place(x=100,y=100,width=80) 

btoct=tk.Button(ventana,text="(OCT)") 
btoct.place(x=180,y=100,width=80)
btoct.bind('<Button-1>',eventos)

btbin=tk.Button(ventana,text="(BIN)") 
btbin.place(x=260,y=100,width=80)
btbin.bind('<Button-1>',eventos) 
#fin botones indicadores sistema numerico

#inicio botones alfabeticos 
bta=tk.Button(ventana,text="A") 
bta.place(x=20,y=150,width=40)
bta.bind('<Button-1>',eventos)

btb=tk.Button(ventana,text="B") 
btb.place(x=60,y=150,width=40)
btb.bind('<Button-1>',eventos)

btc=tk.Button(ventana,text="C") 
btc.place(x=20,y=180,width=40)
btc.bind('<Button-1>',eventos)

btd=tk.Button(ventana,text="D") 
btd.place(x=60,y=180,width=40)
btd.bind('<Button-1>',eventos)

bte=tk.Button(ventana,text="E") 
bte.place(x=20,y=210,width=40)
bte.bind('<Button-1>',eventos)

btf=tk.Button(ventana,text="F") 
btf.place(x=60,y=210,width=40)
btf.bind('<Button-1>',eventos)
#Fin botones alfabeticos  

#Inicio botones numericos 
bt1=tk.Button(ventana,text="1")
bt1.place(x=110,y=150,width=40)
bt1.bind('<Button-1>',eventos)

bt2=tk.Button(ventana,text="2")
bt2.place(x=150,y=150,width=40)
bt2.bind('<Button-1>',eventos)

bt3=tk.Button(ventana,text="3")
bt3.place(x=190,y=150,width=40)
bt3.bind('<Button-1>',eventos)
#------------------------------
bt4=tk.Button(ventana,text="4")
bt4.place(x=110,y=180,width=40)
bt4.bind('<Button-1>',eventos)

bt5=tk.Button(ventana,text="5")
bt5.place(x=150,y=180,width=40)
bt5.bind('<Button-1>',eventos)

bt6=tk.Button(ventana,text="6")
bt6.place(x=190,y=180,width=40)
bt6.bind('<Button-1>',eventos)

bt7=tk.Button(ventana,text="7")
bt7.place(x=110,y=210,width=40)
bt7.bind('<Button-1>',eventos)

bt8=tk.Button(ventana,text="8")
bt8.place(x=150,y=210,width=40)
bt8.bind('<Button-1>',eventos)

bt9=tk.Button(ventana,text="9")
bt9.place(x=190,y=210,width=40)
bt9.bind('<Button-1>',eventos)

#-------------------------------
btdel=tk.Button(ventana,text="DEL")
btdel.place(x=110,y=240,width=40)
btdel.bind('<Button-1>',eventos)

bt0=tk.Button(ventana,text="0")
bt0.place(x=150,y=240,width=40)
bt0.bind('<Button-1>',eventos)

btac=tk.Button(ventana,text="AC")
btac.place(x=190,y=240,width=40)
btac.bind('<Button-1>',eventos)
#Fin botones numericos 

#Inicio botones operacionales 
btsum=tk.Button(ventana,text="+")
btsum.place(x=240,y=150,width=40)
btsum.bind('<Button-1>',eventos)

btrest=tk.Button(ventana,text="-")
btrest.place(x=280,y=150,width=40) 
btrest.bind('<Button-1>',eventos)
#---------------------
btmult=tk.Button(ventana,text="*")
btmult.place(x=240,y=180,width=40)
btmult.bind('<Button-1>',eventos)

btdiv=tk.Button(ventana,text="/")
btdiv.place(x=280,y=180,width=40)
btdiv.bind('<Button-1>',eventos)

#------------------------
btpow=tk.Button(ventana,text="**")
btpow.place(x=240,y=210,width=40)
btpow.bind('<Button-1>',eventos)

bteq=tk.Button(ventana,text="=")
bteq.place(x=280,y=210,width=40)
bteq.bind('<Button-1>',eventos)


btenter=tk.Button(ventana,text="Enter") 
btenter.place(x=240,y=240,width=80)
btenter.bind('<Button-1>',eventos)
#Fin botones operacionales 





ventana.pack()
root.mainloop()



