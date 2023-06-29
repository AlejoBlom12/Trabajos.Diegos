
#===========================================
'''              FACTORIAL               '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Calcular el factorial de un numero ingresado  por teclado, si el  factorial de un numero
se  representa de la siguiente forma n! = 1*2*3*4*5......(n-1)*n    Ejemplo 2: 4! =
1*2*3*4  = 24; tenga en cuenta que el  factorial de 0! es 1   0! = 1'''

#FUNCION CON CONDICONALES: 

def factorial_ciclado(n):
    if n <= 0:
        print("El factorial no está definido para números menores que 1.")
    
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            
        return factorial

# VARIABLE:

numero = int(input("Ingresar numero: "))

#IMPRESION:

resultado = factorial_ciclado(numero)
print("El factorial de" , numero, ", es" ,resultado)




