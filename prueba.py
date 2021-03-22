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
    vector_op=encontrar_operandos(cadena) 
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
        
        
            

    return cadena_separada,vector_op



