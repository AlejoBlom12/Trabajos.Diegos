
#===========================================
'''            LISTA DE NUMEROS          '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Elabora un programa que muestre una lista de números la cual pida al usuario desde
que numero quiere y hasta que numero quiere mostrar por ejemplo si  ingresa  2  y 10
debería mostrar  2,3,4,5,6,7,8,9,10 o si  ingresa  2  y -10  debería mostrar
2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10'''

#VARIABLES:

numero1 = int(input("Ingresas desde donde quieres que comience la lista: "))
numero2 = int(input("Ingresas hasta donde quieres que termine la lista: "))

#LISTA:

numero =  []

#CONDICIONAL CON CICLADO:

print(" ")
if numero1 > numero2:
    while numero1 >= numero2:
        numero1 -= 1
        numero.append(numero1 + 1)

elif numero1 < numero2:
    while numero1 <= numero2:
        numero1 += 1
        numero.append(numero1 - 1)

#IMPRESION: 

print("La lista de los numeros ingresados es: ", numero)
print(" ")