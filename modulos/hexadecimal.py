""" 	
**************************************
*  Decimal            Hexadecimal    
*  	0	|	0             
*	1	|	1             
*	2	|	2             
*	3	|	3             
*	4	|	4             
*	5	|	5             
*	6	|	6             
*	7	|	7             
*	8	|	8             
*	9	|	9             
*	10	|	A             
*	11	|	B             
*	12	|	C             
*	13	|	D             
*	14	|	E             
*	15	|	F             
**************************************				
	
"""

def numero_a_letra(numero): 
    if numero==10:
        return "A"
    elif numero==11: 
        return "B"
    elif numero==12: 
        return "C"
    elif numero==13: 
        return "D"
    elif numero==14: 
        return "E"
    elif numero==15: 
        return "F"
        
def letra_a_numero(letra):
    if letra=="A":
        return 10
    elif letra=="B": 
        return 11
    elif letra=="C": 
        return 12
    elif letra=="D": 
        return 13
    elif letra=="E": 
        return 14
    elif letra=="F": 
        return 15 


def decimal_hexadecimal(numero): 
    """
    recibe un numero decimal en entero  
    se hacen divisiones sucesivas por 16  
    el residuo es almacenado en el vector  
    numero es actualizado con el cociente 
    posteriormente se analiza cada uno  
    de los residuos obtenidos  
    el vector se analiza de derecha a izquierda
    si se encuentra un numero mayor o igual a 10 
    se envia dicho numero a la funcion letra  
    en dicha funcion se determina a que letra corresponde 
    dicho numero  
    y posteriormente se concatena con la cadena de caracteres 
    hexadecimal,si el numero no es mayor a 10, simplemente 
    se convierte en caracter y es concatenado  
    la funcion retorna el valor hexadecimal como cadena 
    de caracteres

    """
    hexadecimal="" 
    aux=[] 
    pos=0
    while(numero>=1): 
        aux.append(int(numero%16)) 
        numero=int(numero/16) 
    pos=len(aux)-1 
    
    while(pos>=0): 
        numero=aux[pos] 
        if numero>=10: 
            hexadecimal+=numero_a_letra(numero) 
        else: 
            hexadecimal+=str(numero) 
        pos-=1
    return hexadecimal  
   

def hexadecimal_decimal(hexadecimal):
    """ 
    primero convertimos el hexadecimal en un vector de caracteres
    recorremos cada posicion del vector hexadecimal  
    la funcion isalpha() nos ayuda a determinar si se trata de
    una letra o no , si se trata de una letra lo enviamos 
    a la funcion letra_a_numero() y nos devuelve el numero que 
    corresponde a la letra, en caso de que no sea una letra
    entonces simplemente convertimos el caracter a entero  

    para la transformacion a entero , recorremos el vector 
    aux de derecha a izquierda, cada numero sera multiplicado
    por 16 elevado a la potencia respectiva y sera acumulado
    en la variable decimal, la potencia incrementara con la
    cantidad de posiciones que vaya avanzando 

    retorna un numero entero(decimal)

    """

    hexadecimal=list(hexadecimal) 
    aux=[]
    potencia=0
    decimal=0
    posicion=0
    #recorremos la lista y si encontramos letras pues lo volvemos entero
    for x in hexadecimal: 
        if x.isalpha(): 
            aux.append(letra_a_numero(x)) 
        else: 
            aux.append(int(x)) 
    posicion=len(aux)-1 

    while(posicion>=0): 
        decimal+=(16**potencia)*aux[posicion]
        potencia+=1 
        posicion-=1

    return decimal

        


