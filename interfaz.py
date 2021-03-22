import tkinter as tk
from tkinter import *


#inicio funciones previas ejecutar logica
def encontrar_operandos(cadena_operaciones): 
    pos_operaciones=[]
    tam_cadena=len(cadena_operaciones) 
    caracter=''
    pos_actual=0
    while(pos_actual<tam_cadena):
        caracter=cadena_operaciones[pos_actual] 
        if(caracter=='+'):
            pos_operaciones.append(pos_actual) 
        elif(caracter=='-'):
            pos_operaciones.append(pos_actual) 
        elif(caracter=='/'):
            pos_operaciones.append(pos_actual) 
        elif(caracter=='*'):
            if pos_actual+1<tam_cadena:
                if cadena_operaciones[pos_actual+1]=='*':
                    pos_actual+=2
                    print(pos_actual)
                else: 
                    pos_operaciones.append(pos_actual)
        pos_actual=pos_actual+1
    return pos_operaciones

def separar_cadena(cadena):  
    vector_op=encontrar_operandos(cadena) #contiene orden operandos
    inicio=0 
    fin=vector_op[0] 
    pos_vector=0
    cadena_separada=[]
    tam_vector=len(vector_op)
    while(pos_vector<tam_vector):
        cadena_separada.append(cadena[inicio:fin]) 
        cadena_separada.append(cadena[fin])
        if(pos_vector+1==tam_vector):
            cadena_separada.append(cadena[fin+1:])
        inicio=fin
        pos_vector+=1
        if pos_vector<tam_vector:
            fin=vector_op[pos_vector]
        
        
            

    return cadena_separada
def verificar_numeros(cadena_sep): 
    """
    Esta funcion determina si los numeros cuentan con su respectivo
    sistema numerico , en caso de que un numero no cuente con el 
    sistema numerico indicado, señalara un error
    en caso que los numeros se encuentren indicados correctamente 
    esta funcion retornara : negativo para errores, numeros sin sistema,
    lista con los tipos de sistemas encontrados

    """
    parent_inicial=0
    parent_final=0
    tipo=""
    pos=0
    tam=len(cadena_sep)
    error=False
    cadena=""
    tipos_num=[]
    while(pos<tam):
        caena=cadena_sep[pos]
        if(len(cadena)>1):
            parent_inicial=cadena.find('(')
            if(parent_inicial==-1):
                error=True
                break
            else:
                parent_final=cadena.find(')')
                tipos_num.append(cadena[parent_inicial:parent_final])
                cadena=list(cadena)
                #eliminamos el tipo de numero de la cadena
                for parent_inicial in range(parent_final+1): 
                    cadena.pop(parent_inicial)
                cadena=str(cadena)
                cadena_sep[pos]=cadena
        pos+=1
    return error,cadena_sep,tipos_num



def ejecutar_cadena(cadena):
    if(cadena==""):
        entrada_operacion.set("ERROR LOGICO")
    else:
        #indentacion
        cadena_separada=separar_cadena(cadena)
        error,cadena_separada,tipos_num=verificar_numeros(cadena_separada)
        if(error):
            entrada_operacion.set("ERROR LOGICO")

    

    


#Fin funciones previa ejecutar logica 

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
    if(texto=="="):
        #Ejecucion de operaciones
        ejecutar_cadena(entrada_operacion.get())
    elif(texto=="AC"):
        #Limpiar entrada 
        limpiar_entrada()
    elif(texto=="DEL"): 
        eliminar_caracter()
    else:
        #agrega caracter
        registrar_entrada(texto)
    



root=tk.Tk()
root.title("Calculadora Sistemas Numericos")
ventana=tk.Frame(root) 
ventana.config(width=350,height=350,bg="purple")
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
#Fin botones operacionales 


#Inicio botones adicionales

btcreditos=tk.Button(ventana,text="Creditos")
btcreditos.place(x=40,y=290,width=80)

btinstrucciones=tk.Button(ventana,text="Instrucciones") 
btinstrucciones.place(x=200,y=290,width=100)

#Fin botones adicionales


ventana.pack()
root.mainloop()
