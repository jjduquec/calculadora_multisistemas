#Octal
def es_octal(numero):
    """
    recibimos el numero como una cadena de caracteres  
    recorremos cada elemento revisando que contenga unicamente 
   digitos entre 0 y 7, si hay algun elemento diferente a (0,1,2,3,4,5,6,7)
    se devuelve false indicando que no es un numero binario
    de lo contrario devuelve true 
    """

    caracter=""
    esoctal=True
    for caracter in numero: 
        if((caracter!="0") and (caracter!="1")and (caracter!="2")and (caracter!="3")and (caracter!="4")and (caracter!="5")and (caracter!="6")and (caracter!="7")): 
           esoctal=False
           break
    return esoctal


def decimal_octal(numero): 
    """
    recibimos un numero entero 
    y realizamos divisiones sucesivas 
    hasta obtener el numero en octal,  
    retornamos el numero octal
    """
    octal="" 
    aux=""
    pos_octal=0 

    while(numero>=1):
        octal+=str(numero%8) 
        numero=int(numero/8)
    pos_octal=len(octal)-1
    while(pos_octal>=0): 
        aux+=octal[pos_octal] 
        pos_octal-=1 
    octal=aux 
    return octal 


def octal_decimal(numero): 
    """
    recibimos un numero binario como cadena de caracteres 
    recorremos de derecha a izquierda  
    por cada caracter que encontramos se incrementa la potencia 
     entonces se calcula 8 elevado a la potencia
    y se acumula en la variable decimal
    retornamos decimal
    """

    decimal=0 
    potencia=0
    pos_cadena=len(numero)-1 #empezamos en la ultima posicion  
    #se recorre la cadena de derecha a izquierda  
    caracter="" 
    while(pos_cadena>=0): 
        
        decimal+=int(numero[pos_cadena])*(8**potencia)
        potencia+=1
        pos_cadena-=1 

    return decimal

#Fin Octal


