
#================================================
'''          INDENTIFICA EL NUMERO MAYOR      '''
#================================================

#INFORMACION DEL PROGRAMA:

'''Elabora  un programa que  me muestre en pantalla cual de los dos números
ingresados por  teclado es mayor'''

#VARIABLES:

n1 = float(input("Ingresa un numero: "))
n2 = float(input("Ingresa numero: "))
print(" ")
#CONDICIONALES:

if n1 > n2:
    print("EL numero mayor entre", n1 , "y", n2 ,"es :", n1)
    
elif n2 > n1:
    print("EL numero mayor entre", n1 , "y", n2 ,"es :", n2)
    
else:
    print("Los numeros que ingreso son iguales.")

