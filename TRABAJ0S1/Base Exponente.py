
#========================================================
'''        MOSTRAR BASE Y EXPONENTE INGRESADOS        '''
#========================================================

#INFORMACION DEL PROGRAMA:

'''Elabora un programa que le pida al usuario una base y un exponente, posteriormente
mostrar el  resultado  al usuario'''

#VARIABLES:

base = float(input("Ingrese un numero (""base""): "))
exponente = int(input("Ingrese un numero entero(""exponente""): "))

#ECUACION IMPORTANTE:

potenciacion = base ** exponente

#IMPRESION:
print(" ")
print("El resultado la potenciacion de base: " , base, ", con exponente: ", exponente, ", es igual a: ", potenciacion )
print(" ")