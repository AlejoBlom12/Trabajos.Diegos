
#===========================================
'''            NUMERO CENTRAL            '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Elabora un programa que Dados tres números deduzca cuál es el central'''

#VARIABLES:

numero1 = float(input("Introducir numero: "))
numero2 = float(input("Introducir numero: "))
numero3 = float(input("Introducir numero: "))

#CONDICIONALES:

print(" ")
if numero1 > numero3 and numero1 > numero2:
     if numero3 > numero2:
          print("El numero central es: " , numero3)
     else:
          print("El numero central es: " , numero2)
          

if numero2 > numero1 and numero2 > numero3:
     if numero1 > numero3:
          print("El numero central es: " , numero1)
     else:
          print("El numero central es: " ,numero3)

if numero3 > numero1 and numero3 > numero2:
     if numero1 > numero2:
          print("El numero central es: " ,   numero1 )
     else:
          print("El numero central es: " ,   numero2 )
print(" ")