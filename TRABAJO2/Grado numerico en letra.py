
#======================================================
'''             GRADO NUMERICO EN LETRA             '''
#======================================================

#INFORMACION DEL PROGRAMA:

'''El sistema de calificación americano (de Estados Unidos) se suele calcular de
acuerdo al siguiente cuadro: (Utilizando esta información, escribir un algoritmo que
acepte una calificación numérica del estudiante (0-100), convierta esta calificación a
su equivalente en letra y visualice la calificación correspondiente en letra)
    Grado numérico Grado en letra
    Grado mayor o igual a 90    A
    Menor de 90 pero mayor o igual a 80  B
    Menor de 80 pero mayor o igual a 70  C
    Menor de 70 pero mayor o igual a 69  D
    Menor de 69     F'''

#VARIABLE:

numero = int(input("Introduce tu calificacion Americana 1-100: "))

#CONDICIONAL:

print(" ")
if numero <= 100 and numero >= 0:

    if numero >= 90: 
        print("Tu calificacion es un A.")

    elif numero < 90  and numero >= 80: 
        print("Tu calificacion es un B.")

    elif numero < 80  and numero >= 70: 
        print("Tu calificacion es un C.")

    elif numero < 70  and numero >= 69: 
        print("Tu calificacion es un D.")

    elif numero < 69: 
        print("Tu calificacion es un F.")

else: 
    print ("La calificacion Americada es del 0 - 100, no se permite otros numeros.")
print(" ")