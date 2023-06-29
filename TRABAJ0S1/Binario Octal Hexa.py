
#==========================================================
'''     CONVERTIR DECIMAL A BINARIO, OCTAL, HEXADECIMAL '''
#==========================================================

#INFORMACION DEL PROGRAMA:

'''SE ENCUENTRAN DOS TALLERES UNIDOS:'''

#1
'''Elaborar un programa  que  convierta  un  numero decimal ingresado  por teclado a
numero  binario, al final  deberá mostrar cual es su equivalencia'''

#2 
'''Realiza un  programa que  convierta un  numero  decimal  a binario, octal y
hexadecimal, al final  deberá mostrar cual es su resultado'''


#FUNCIONES CON CICLADOS:

#FUNCION BINARIO:

def binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        digito = numero % 2
        binario = str(digito) + binario
        numero //= 2
    
    return binario

#FUNCION OCTAL:

def octal(numero):
    if numero == 0:
        return '0'
    
    octal = ''
    while numero > 0:
        digito = numero % 8
        octal = str(digito) + octal
        numero //= 8
    
    return octal

#FUNCION HEXADECIMAL:

def hexadecimal(numero):
    if numero == 0:
        return '0'
    
    hexadecimal = ''
    while numero > 0:
        digito = numero % 16
        if digito < 10:
            hexadecimal = str(digito) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + digito - 10) + hexadecimal
        numero //= 16
    
    return hexadecimal

#VARIABLES:

numero = int(input("Ingresa un número: "))

binario = binario(numero)
octal = octal(numero)
hexadecimal = hexadecimal(numero)

#IMPRESION:
print(" ")
print("Binario de" , numero, ":", list(binario))
print(" ")
print("Octal de", numero , ":" ,list(octal))
print(" ")
print("Hexadecimal de",numero, ":" ,list(hexadecimal))
print(" ")