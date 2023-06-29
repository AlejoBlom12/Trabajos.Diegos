
#========================================================
'''            CONVERTIR BINARIO A DECIMAL          '''
#========================================================

#INFORMACION DEL PROGRAMA: 

''' Elaboraremos un programa  que  convierta  un  numero binario ingresado por teclado
a numero  decimal, al final  deberá mostrar cual es su equivalencia''' 

# VARIABLES:

binario = int(input("Ingresa un número binario: "))
decimal = 0
posicion = 0

#ESTRUCTURA CICLADA:

while binario != 0:
    digito = binario % 10
    decimal += digito * (2 ** posicion)
    binario //= 10
    posicion += 1
    
#IMPRESION: 
print("  ")
print("El número decimal equivalente es:", decimal)
print("  ")

