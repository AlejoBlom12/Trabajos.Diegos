
#========================================
'''         ALEATORIO NUMERO      '''
#========================================

#INFORMACION DEL PROGRAMA:

''' Utilizando la función randrange del módulo random, escribir un programa que obtenga
un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
sin son menores o mayores que el número a adivinar, hasta que el usuario ingrese el
número correcto.''' 

#FUNCION:

def random ():
    import random
    
    aleatorio = random.randint(1, 10)
    
    #CILCADO:
    
    while aleatorio:
        
        #VARIABLE:
        
        numero = int(input("ingresa un numero: "))
        
        #CONDICIONAL:
        
        if numero < aleatorio:
            print("El numero" , numero , "es menor que le numero ramdon, ingresa otro.")
        elif numero > aleatorio:
            print("El numero" , numero , "es mayor que le numero ramdon, ingresa otro.")
        else:
            print("Increible, acertaste, el numero aleatorio es: " , aleatorio )
            break
random()
