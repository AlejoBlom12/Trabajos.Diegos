
#======================================================
'''      CALCULAR EL AREA DE UN TRIANGULO         '''
#======================================================

#INFORMACION DEL PROGRAMA:

'''Crea un programa que  permita calcular el área del triangulo'''

#VARIABLES: 

base = float(input("ingrese la base: " ))
print("  ")
altura = float (input ("ingrese la altura: "))

#ECUACION:

area = (base * altura)/2

#CONDICIONALES CON IMPRESION:

print("  ")
if altura > 0 and base > 0:
    print(" El area de el triangulo con los datos dados es: " + str(area))
else:
    print("Los datos son inesistentes")
print("  ")
