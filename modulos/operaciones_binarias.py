def reglas_suma(a,b):
    acarreo=0
    resultado=0
    if (a=="0" and b=="0"):
        resultado="0" 
    elif (a=="0" and b=="1"): 
        resultado="1"
    elif(a=="1" and b=="0"): 
        resultado="1"
    else:
        resultado="0"
        acarreo="1" 
   
    return acarreo,resultado
def ordenar_cadena(vector):
    """
    concatena el contenido del vector en una cadena 

    """
    aux="" 
    for elemento in vector: 
        aux=aux+elemento
    return aux


class Binario:
    def __init__(self,numero): 
        self.numero=numero 
    
    def __add__(self,otro):
        pos_a=0
        pos_b=0
        a=0
        b=0
        resultado=[]
        acarreo="0"
        aux="0" 

        if(len(self.numero)>=len(otro.numero)): 
            a=list(self.numero)
            b=list(otro.numero)
        else:
            a=list(otro.numero)
            b=list(self.numero)
        
        pos_a=len(a)-1
        pos_b=len(b)-1

        while(pos_a>=0):
           
            if pos_b>=0:
                if acarreo!=0:
                    acarreo,aux=reglas_suma(acarreo,a[pos_a])
                    a[pos_a]=aux
                    acarreo,aux=reglas_suma(a[pos_a],b[pos_b])
                    resultado.append(aux)
                else:
                    acarreo,aux=reglas_suma(a[pos_a],b[pos_b])
                    resultado.append(aux)
            else:
                acarreo,aux=reglas_suma(acarreo,a[pos_a])
                resultado.append(aux)
            pos_a=pos_a-1
            pos_b=pos_b-1 
        
        
        
        
        resultado.reverse()        
        
        
        return ordenar_cadena(resultado)


        
        
    
    def __str__(self): 
        return str(self.numero)


a=Binario("0010")
b=Binario("0110") 
print(a+b)