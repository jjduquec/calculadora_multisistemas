

#cargamos los modulos de los sistemas para realizar las conversiones 
import sys 
sys.path.append("./modulos")

import binarios as bn   
import octal as oct 
import hexadecimal as hexa 
from logica_interfaz import *


def convertir_decimal(numero,tipo): 
	
	"""
	primero verificamos si el numero corresponde 
	al tipo indicado, si es correcto entonces  
	se procede a la conversion de el tipo a decimal 
	"""
	"""
		(BIN)
		(HEX)
		(OCT)
		(DEC)
	"""
	resultado=0
	no_error=True #asumimos que el tipo de numero es correcto

	if(tipo=="(BIN)"): 
		
		#verificamos el tipo 
		
		no_error=bn.es_binario(str(numero))
		if(no_error): 
			resultado=bn.binario_decimal(numero)
	
	elif(tipo=="(HEX)"): 
		#verificamos el tipo 
		no_error=hexa.es_hexadecimal(numero)
		if(no_error): 
			resultado=hexa.hexadecimal_decimal(numero)
			
	elif(tipo=="(OCT)"): 
		#verificamos el tipo 
		no_error=oct.es_octal(numero)
		if(no_error): 
			resultado=oct.decimal_octal(numero)
	elif(tipo=="(DEC)"): 
		resultado=int(numero)
	else:
		print(numero)
		no_error=False
	
	return no_error,resultado
		
def convertir_tipo(numero,tipo):
	resultado=0

	if(tipo=="(BIN)"): 
		
		#verificamos el tipo 		
		resultado=bn.decimal_binario(numero)
	
	elif(tipo=="(HEX)"): 
		#verificamos el tipo 
		resultado=hexa.hexadecimal_decimal(numero)
			
	elif(tipo=="(OCT)"): 
		#verificamos el tipo 		
		resultado=oct.octal_decimal(numero)
	elif(tipo=="(DEC)"): 
		resultado=int(numero)

	return resultado
	

		
		

		
		

	
		




def ejecutar_logica(cadena_separada,tipos_num,tipo_resultado): 
	
	cadena_ejecutar=''
	aux=''
	pos_potencia=0
	pos_tipo=0
	pos_pot=0
	tam_cad=0
	aux2=''
	no_error=True #Se asume que no hay error
	resultado=0
	for cadena in cadena_separada:
		tam_cadena=len(cadena)
		if(tam_cadena==1 and (cadena.isalpha()==False and cadena.isnumeric()==False)):
			# quiere decir que es un simbolo de operacion 
			cadena_ejecutar+=cadena
		else: 
			#buscamos  si hay simbolo de potencia
			pos_pot=cadena.find('*')
			if pos_pot!=-1:
				#encontro potencia
				aux=cadena[pos_pot:pos_pot+3]
				cadena=list(cadena)
				cadena=limpiar_cadena(cadena,aux)
				cadena=ordenar_cadena(cadena)
				if(tipos_num[pos_tipo]=="(DEC)"):
					cadena_ejecutar+=str(cadena)
				else:
					no_error,cadena=convertir_decimal(cadena,tipos_num[pos_tipo])										
					if(no_error==False):

						# hay un error con el tipo de dato indicado
						raise Exception('Dato no valido')
					else: 
					
						cadena_ejecutar+=str(cadena)						
						cadena_ejecutar+=aux
						pos_tipo+=1
			else: 
				no_error,cadena=convertir_decimal(cadena,tipos_num[pos_tipo])
				
				if(no_error==False):
					# hay un error con el tipo de dato indicado
					raise TypeError('Dato no valido')
				else: 
					
					cadena_ejecutar+=str(cadena)
					pos_tipo+=1
	resultado=eval(cadena_ejecutar)
	resultado=convertir_tipo(resultado,tipo_resultado)
	return resultado










	




