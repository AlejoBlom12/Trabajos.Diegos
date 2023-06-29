
#===========================================
'''       ORDENADOS MAYOR A MENOR        '''
#===========================================

#INFORMACION DEL PROGRAMA: 

'''Elabora un programa que lea 3 números por  teclado y me los muestre  organizado de
mayor a menor por ejemplo si ingreso 53, 10 Y 24 deberá mostrar, "los números
ingresados  son  53, 10 Y 24 y organizados de forma descendente son  53, 24, 10'''

#vARIABLES:

numero1 = int(input("Introducir numero: "))
numero2 = int(input("Introducir numero: "))
numero3 = int(input("Introducir numero: "))

#CONDICIONALES CON IMPRESIONES:
print("  ")
if numero1 > numero3 and numero1 > numero2:
     if numero3 > numero2:
          print("Los numeros de mayor a menor son: " ,  numero1 , "/" , numero3 , "/" , numero2)
     else:
          print("Los numeros de mayor a menor son: " ,  numero1 , "/" , numero2 , "/" , numero3)

if numero2 > numero1 and numero2 > numero3:
     if numero1 > numero3:
          print("Los numeros de mayor a menor son: " ,  numero2 , "/" , numero1 , "/" , numero3)
     else:
          print("Los numeros de mayor a menor son: " ,  numero2 , "/" , numero3 , "/" , numero1)

if numero3 > numero1 and numero3 > numero2:
     if numero1 > numero2:
          print("Los numeros de mayor a menor son: " ,  numero3 , "/" , numero1 , "/" , numero2)
     else:
          print("Los numeros de mayor a menor son: " ,  numero3 , "/" , numero2 , "/" , numero1)
print("  ")
        




