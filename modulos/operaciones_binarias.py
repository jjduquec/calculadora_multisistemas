

class Binario:
    def __init__(self,numero): 
        self.numero=numero 
    def __add__(self,otro):
        a=self.numero
        b=otro.numero

        if(len(a)>len(b)): 
            b=b.zfill(len(a))
        elif(len(a)<len(b)): 
            a=a.zfill(len(b))
        
        aux_resultado=""
        resultado=""
        acarreo='0'
        for i in range(len(a)-1,-1,-1):
            acarreo,aux_resultado=reglas_suma(a[i],b[i])
            resultado=resultado+aux_resultado
            if(acarreo=='1'):
                resultado=resultado+'1'
            
        return resultado

    def __sub__(self,otro): 
        a=self.numero
        b=otro.numero
        b=complemento_dos(b)
        return a+b


    def __mul__(self,otro):
        resultado=""
        aux='0'
        a=self.numero
        b=otro.numero
        for i in range(len(a)):
            if a[i]=='1':
                resultado=self.numero+Binario(aux)




    def __truediv__(self,otro): 
        resultado='0'
        residuo='' 
        aux=""
        a=self.numero
        b=otro.numero 

        if int(a)<int(b): 
            resultado='0'
            residuo=a

        if int(a)>int(b): 
            aux=a[0:len(b)]
            for i in range(len(a)-len(b)+1):
                if int(aux)>=int(b): 
                    resultado=resultado+'1'
                    aux=self-otro
                else:
                    resultado=resultado+'0'
                    residuo=aux
                if i+len(b)<len(a):
                    aux=aux+a[i+len(b)]
        if a==b:
            resultado=='1'
        return resultado
                        
    
    def __str__(self): 
        #metodo usado para imprimir los numeros binarios
        return str(self.numero)

def reglas_suma(a,b):
   

    acarreo='0'
    resultado='0'
    if (a=="0" and b=="0"):
        resultado="0" 
    elif (a=="0" and b=="1"): 
        resultado="1"
    elif(a=="1" and b=="0"): 
        resultado="1"
    elif(a=="1" and b=="1"):
        resultado="0"
        acarreo="1"

   
    return acarreo,resultado 

def complemento_dos(numero):
    aux=""
    for caracter in numero: 
        if caracter=='1':
            aux+='0'
        elif caracter=='0':
            aux+='1'
    numero=Binario(aux)
    b=Binario('1')
    return numero+b


"10101111+1000011-11*1110000111"
a=Binario("101010")
b=Binario("10101")

print(a+b)





