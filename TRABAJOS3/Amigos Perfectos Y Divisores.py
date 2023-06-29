
#===========================================
'''NUMEROS PERFECTOS, AMIGOS Y DEVISORES'''
#===========================================

#INFORMACION DEL PROGRAMA:

#CONTIENE 3 PROGRAMAS:

#1
'''Escribir una función que devuelva la suma de todos los divisores de un número n, sin
incluirlo.'''
#2
'''Usando la función anterior, escribir una función que imprima los primeros m números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m
números perfectos).'''
#3
'''Usando la primera función, escribir una función que imprima las primeras m parejas
de números (a,b), tales que la suma de los divisores de a es igual a b y la suma de los
divisores de b es igual a a (es decir las primeras m parejas de números amigos).
Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de
ejecución.'''

#Estructura del taller:
#Divisores:

def divisoresNegativos(n):
    suma = 0
    divisores = []
    for i in range(1, abs(n)):
        if n % i == 0:
            suma += i
            divisores.append("-" + str(i))
            
    print("Los divisores del numero ingresado es igual a: ", divisores)
    print ("          ")
    return suma

def divisoresPositivos(n):
    suma = 0
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            suma += i
            divisores.append(i)
            
    print("Los divisores del numero ingresado es igual a: ", divisores)
    print ("          ")     
    return suma

# funcion de numeros perfectos:

def perfectosPositivos(n):
    numeros_perfectos = []
    
    for numero in range(1, n):
        suma = 0
        
        for i in range(1, numero):
            
            if numero % i == 0:
                suma += i
                
        if suma == numero:
            numeros_perfectos.append(numero)
            
    return numeros_perfectos

def perfectosNegativos(n):
    numeros_perfectos = []
    
    for numero in range(1, abs(n)):
        suma = 0
        
        for i in range(1, abs(numero)):
            
            if numero % i == 0:
                suma += i
                
        if suma == abs(numero):
            numeros_perfectos.append("-" + str(numero))
            
    return numeros_perfectos

#Funcion de parejas de numeros amigo:

def divisoresPos(n):
    suma = 0
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            suma += i
            divisores.append(i)
    return suma

def numerosAmigosPositi(n):
    amigos = []
    for i in range(2, n):
        sum1 = divisoresPos(i)
        sum2 = divisoresPos(sum1)
        if i == sum2 and i != sum1:
            amigos.append((i, sum1))
    return amigos


def numerosAmigosNega(n):
    amigos = []
    for i in range(2, abs(n)):
        sum1 = divisoresPos(i)
        sum2 = divisoresPos(sum1)
        if i == sum2 and i != sum1:
            amigos.append("-" + str(i) + "," + "-" + str(sum1))
    return amigos

#Variables principal: 

numero = int(input("Ingresa un numero: "))

print("==============================================================================")
print("                          DIVISORES DEL NUMERO INGRESADO            ")
print("==============================================================================")

#Impresion con condiciones:
#Condiciones de numeros positivos:

if numero > 0: 
    resultado1 = divisoresPositivos (numero)
    print("===========================================================================")
    print("                             SUMA DE LOS DIVISORES                 ")
    print("===========================================================================")
    
    print("La suma de divisores del numero ", numero, ", es igual a: ", resultado1)
    
    print("===========================================================================")
    print("                               PAREJAS DE NUMEROS AMIGOS            ")
    print("===========================================================================")
    
    print("La pareja de numeros amigos antes de", numero, ":" , numerosAmigosPositi(numero))
    
    print("===========================================================================")
    print("                                 NUMEROS PERFECTOS           ")
    print("===========================================================================")
    
    if numero == resultado1:
        
        print("El numero ingresado es un numero perfecto.")
        if numero > 6:
            print("Los numeros perfectos que contiene son: ", perfectosPositivos(numero))
        True 
    else:
        print("Los numeros perfectos que contiene son: ", perfectosPositivos(numero))
        
#Condiciones de numeros negatios:

elif numero <= 0:
    resultado2 = divisoresNegativos(numero)
    print("===============================================================================================================")
    print("                                             SUMA DE LOS DIVISORES                 ")
    print("===============================================================================================================")
    print("    ")
    print("La suma de divisores del numero ", numero, ", es igual a: ", ("-" + str(resultado2)))
    
    print("===============================================================================================================")
    print("                                             PAREJAS DE NUMEROS AMIGOS            ")
    print("===============================================================================================================")
    print("   ")
    print("La pareja de numeros amigos antes de", numero, ":" , numerosAmigosNega(numero))
    
    print("===============================================================================================================")
    print("                                             NUMEROS PERFECTOS           ")
    print("===============================================================================================================")
    print("")
    if numero == -6 or numero == -28 or numero == -496 or numero == -8128:
        print("El numero ingresado es un numero perfecto.")
        if numero < -6:
            print("Los numeros perfectos que contiene son: ", perfectosNegativos(numero))
    else:
        print("Los numeros perfectos que contiene son: ", perfectosNegativos(numero))
        