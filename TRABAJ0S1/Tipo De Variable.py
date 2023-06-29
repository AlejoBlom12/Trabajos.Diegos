
#========================================================
'''             CLASE DE DATOS INGRESADOS             '''
#========================================================

#INFORMACION DEL PROGRAMA:

''' Elabore un  programa me muestre en  pantalla el  tipo de  dato  que el usuario  ha
ingresado, por  ejemplo si  ingresa Juan el  deberá decir que es texto, en caso  que
ingrese 2018 deberá decir que es  entero'''

#VARIABLES:

variable = input("Ingresa una variable: ")

#CONDICIONALES CON IMPRESION:
print (" ")
if variable.isnumeric():
    print("La variable es de tipo 'int'")
elif variable.replace('.', '', 1).isdigit():
    print("La variable es de tipo 'float'")
elif isinstance(variable, str):
    print("La variable es de tipo 'str'")
else:
    print("Tipo desconocido")
print (" ")

