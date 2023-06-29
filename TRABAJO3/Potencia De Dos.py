
#========================================
'''      POTENCIA DE DOS NUMEROS      '''
#========================================

#FUNCIONES DEL PROGRAMA:

'''Escribir una función 'es_potencia_de_dos' que reciba como parámetro un número
natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
también incluir una función que, dados dos números naturales pasados como
parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar
la función es_potencia_de_dos, descrita en el punto anterior.'''

#FUNCION:
def es_potencia_de_dos(numero):
    
    #CONDICIONALES:
    
    if numero <= 0:
        return False
    
    exp = 0
    
    #CICLADO:
    
    while  (2**exp) <= numero:
        if (2**exp) == numero:
            potencia = True
        else:
            potencia = False
        exp = exp + 1
    return potencia 

def resultado (resultado, numero):
    if resultado:
        print("El", numero ,"es una potencia de 2")
    else:
        print("El" , numero ,"no es una potencia de 2")
        
def suma_potencias_de_dos(num1, num2):
    potenciador = []
    suma = 0
    for i in range(num1, num2 + 1):
        if es_potencia_de_dos(i) == True:
            suma = suma + i
            potenciador.append (i)
    print("Las potencias del 2 que se encuentran en medio de los dos limites son: ", potenciador)
    print ("         ")
    return suma
        
        
#================================================================================================

#VARIABLES:

numero1 = int(input("Ingrese un número natural: "))
numero2 = int(input("Ingrese un número natural: "))

#CONDICIONAL:
if numero1 <= 0 or numero2 <= 0:
    print("No es posibe potenciar un numero menor o igual a 0")
else:
    
    resultado1 = es_potencia_de_dos(numero1)
    resultado2 = es_potencia_de_dos(numero2)

    print("        ")

    resultado (resultado1, numero1)
    resultado (resultado2, numero2)

    print ("      ")

    if numero1 <= numero2:
        print("La suma de las potencias es igual a:", suma_potencias_de_dos(numero1 , numero2))
    else:
        print("La suma de las potencias es igual a: ", suma_potencias_de_dos(numero2 , numero1))



