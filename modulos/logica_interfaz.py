import sys 

sys.path.append("./logica")

import logica as lg
#inicio funciones previas ejecutar logica
def encontrar_operandos(cadena_operaciones): 
    """
    recibe una cadena de caracteres y busca en ella
    todos los simbolos que indican operaciones matematicas
    retorna un vector con las posiciones de cada operando

    """
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
    """
    Separa la cadena que recibe desde la entrada de operaciones 
    y la retorna como un vector 
    """
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


def ordenar_cadena(cadena):
    """
    elimina los corchetes de una cadena de caracteres
    que fue convertida en lista y se desea que vuelva 
    a ser string 
    """
    aux=""
    caracter=""
    for caracter in cadena: 
        if((caracter!='[') or (caracter!=']')): 
            aux+=caracter 
    return aux

def limpiar_cadena(cadena,cadena_aux): 
    """
    cadena_aux contiene los caracteres que queremos remover  
    de la lista  

    ejemplo : cadena['1','0','1','(','B','I','N',')'] cadena_aux(BIN)
    devuelve ['1','0','1']
    """
    for caracter in cadena_aux:
                    cadena.remove(caracter) 
    return cadena
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
    caracter=""
    cadena_aux=""
    while(pos<tam):
        cadena=cadena_sep[pos]
        if(len(cadena)>1):
            parent_inicial=cadena.find('(')
            if(parent_inicial==-1 ):                                
                error=True
                break
            else:
                parent_final=cadena.find(')')+1
                cadena_aux=cadena[parent_inicial:parent_final]
                tipos_num.append(cadena_aux)
                cadena=list(cadena)
                #eliminamos el tipo de numero de la cadena
                cadena=limpiar_cadena(cadena,cadena_aux)
                cadena=ordenar_cadena(cadena)
                cadena_sep[pos]=cadena 
                

        pos+=1
    return error,cadena_sep,tipos_num



def ejecutar_cadena(cadena,tipo_resultado):
    """
    recibe las operaciones y los numeros en forma de cadena
    la separa, evalua si los datos son correctos y transfiere 
    a la parte logica de la calculadora para emitir los resultados
    """
    if(cadena==""):
        print("cadena vacia")
        return "ERROR LOGICO"
    else:
        
        cadena_separada=separar_cadena(cadena)
        error,cadena_separada,tipos_num=verificar_numeros(cadena_separada)
        if(error):
            return "ERROR LOGICO"
            
        else: 
            return lg.ejecutar_logica(cadena_separada,tipos_num,tipo_resultado)
        
        """
        parametros a enviar: 
        cadena_separada 
        tipos_num
        """
    
   

    


#Fin funciones previa ejecutar logica 