
#=============================================
''' DESCOMPONER ENTEROS CON NUMEROS PRIMOS '''
#=============================================

#INFORMACION DEL PROGRAMA:

'''Escribir una aplicación que reciba un número entero k e imprima su descomposición
en factores primos.'''

#FUNCION CILCADA:

def descomponer(a):
    factores_primos = []
    divisor = 2

    while divisor <= a:
        if a % divisor == 0:
            factores_primos.append(divisor)
            a = a // divisor
        else:
            divisor += 1

    return factores_primos

#VARIABLE:

numero = int(input("Ingrese un número entero: "))

#IMPRESION:

factores = descomponer(numero)
print("Factores primos:", factores)