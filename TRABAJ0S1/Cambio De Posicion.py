
#=====================================================
'''       CAMBIAR DIRECCION DE LOS VALORES        '''
#=====================================================

#INFORMACION DEL PROGRAMA:

'''Cree un algoritmo  que  permita intercambiar el valor de una variable a=3, b=2
deberá quedar a=2 y b=3'''

#VARIABLES:

n1 = input("Introduce palabra o numero: ")
n2 = input("Introduce palabra o numero: ")
print(" ")

#IMPRESION INICIAL:

print("Valores iniciales:")
print(" ")
print("Primer variable:", n1)
print("Segunda variable:", n2)

#CAMBIO DE POSICION:

x = n1
n1 = n2
n2 = x

#IMPRESION FINAL:
print(" ")
print("Valores intercambiados:")
print("  ")
print("Primer variable:", n1)
print("Segunda variable:", n2)
print("  ")
