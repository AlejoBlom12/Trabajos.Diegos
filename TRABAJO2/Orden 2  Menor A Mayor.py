
#===========================================
'''       ORDENADOS MENOR A MAYOR        '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Elabora un programa que me muestre en pantalla de forma ordenada de menor a
mayor dos números ingresados por teclado, por ejemplo si ingreso 5 Y 4 deberá
mostrar, "los números ingresados  son  5 y 4 y organizados  son  4, 5"'''

#VARIABLES:

numero1 = int(input("Introducir numero: "))
numero2 = int(input("Introducir numero: "))
print("  ")

#CONDICIONALES:

if numero1 < numero2: 
    print("Los numeros ingresados son: " + str(numero1) + " y " + str(numero2))
    print("  ")
    print("Los numeros ingresados de menor a mayor son: " + str(numero1) + " y " + str(numero2))

elif numero1 > numero2: 
    print("Los numeros ingresados son: " + str(numero1) + " y " + str(numero2))
    print("  ")
    print("Los numeros ingresados de menor a mayor son: " + str(numero2) + " y " + str(numero1))
elif numero1 == numero2: 
    print("Los numeros ingresados son: " + str(numero1) + " y " + str(numero2))
    print("  ")
    print("Los numeros ingresados son iguales")
print("  ")
