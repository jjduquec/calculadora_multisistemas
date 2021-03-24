#Binarios 
def es_binario(numero):
    """
    recibimos el numero como una cadena de caracteres  
    recorremos cada elemento revisando que contenga unicamente 
    1 y 0, si hay algun elemento diferente a 1 o 0
    se devuelve false indicando que no es un numero binario
    de lo contrario devuelve true 
    """

    caracter=""
    esbinario=True
    for caracter in numero: 
        if((caracter!="0") and (caracter!="1")): 
           esbinario=False
           break
    return esbinario


def binario_decimal(numero): 
    """
    recibimos un numero binario como cadena de caracteres 
    recorremos de derecha a izquierda  
    por cada caracter que encontramos se incrementa la potencia 
    si se encuentra un 1, entonces se calcula 2 elevado a la potencia
    y se acumula en la variable decimal
    retornamos decimal
    """

    decimal=0 
    potencia=0
    pos_cadena=len(numero)-1 #empezamos en la ultima posicion  
    #se recorre la cadena de derecha a izquierda  
    caracter="" 
    while(pos_cadena>=0): 
        caracter=numero[pos_cadena] 
        if caracter=="1": 
            decimal+=2**potencia
        potencia+=1
        pos_cadena-=1 

    return decimal
def decimal_binario(numero): 
    numero=int(numero)
    """
    recibimos un numero entero 
    y realizamos divisiones sucesivas 
    hasta obtener el numero binario,  
    retornamos el numero binario 
    """
    binario="" 
    aux=""
    pos_binario=0 

    while(numero>=1):
        binario+=str(numero%2) 
        numero=int(numero/2)
    pos_binario=len(binario)-1
    while(pos_binario>=0): 
        aux+=binario[pos_binario] 
        pos_binario-=1 
    binario=aux 
    return binario


#Fin Binarios 







