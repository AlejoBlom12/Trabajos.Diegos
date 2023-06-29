
#===========================================
'''          NATURALES + PRIMOS         '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Escribir una aplicación que reciba un número natural e imprima todos los números
primos que hay hasta ese número.'''

#FUNCIONES CON CICLADO Y CONDICIONALES:

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def listaPrimos(a):
    print("Números primos hasta: " ,a )
    for numero in range(2, a + 1):
        if primo(numero):
            print(numero)

#VARIABLE:
numero = int(input("Ingrese un número natural: "))
#IMPRESION:
listaPrimos(numero)