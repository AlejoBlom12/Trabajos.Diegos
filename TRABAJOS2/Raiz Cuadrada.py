
#===========================================
'''            RAIZ DE UN NUMERO       '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Calcular la raíz cuadrada de un número y escribir su resultado. Considerando el caso
en que el número sea negativo'''

# VARIABLE:

numero = int (input("Introducir numero: "))

#CONDICIONALES:
print(" ")
if numero >= 0: 

    import math
    raiz = math.sqrt(numero)
    print ("La raiz de numero ", numero, ", es igual a: ", raiz)

else:
    print("No se puede sacar raiz a un numeno negativo")
print(" ")