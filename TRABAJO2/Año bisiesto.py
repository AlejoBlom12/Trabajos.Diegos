
#===========================================
'''              AÑO BISIESTO            '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Utiliza una Estructura selectiva para averiguar si un año leído de teclado es o no
bisiesto'''

#VARIABLE:

anio = int(input("Ingrese un año: "))

#CONDICIONAL CON IMPRESION:

print(" ")
if anio % 4 == 0:
    print(anio, "es un año bisiesto.")
else:
    print(anio, "no es un año bisiesto.")
print(" ")