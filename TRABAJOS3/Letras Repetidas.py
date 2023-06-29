
#=========================================
'''         CANTIDAD DE LETRAS        '''
#=========================================

#INFORMACION DEL PROGRAMA:

'''El usuario ingresa por teclado una oración por ejemplo 'Las cuentas claras y el
chocolate espeso' el programa debe permitir buscar la  letra que el usuario quiere
buscar y contar cuantas letras hay; Ejemplo: letra a buscar 's'; 'Las cuentas claras y
el chocolate espeso' posee 4 letras 's' '''

#VARIABLES:

oracion = input("Introduce una frase: ")
letra = input("Introduce la letra que deseas buscar en la frase: ")

#LISTA:

cLetra= []

#CICLADO:

for j in oracion:
    if j.lower() == letra.lower():
        cLetra.append(j)

#INPRESION:

print(" ")
print("En la frase", oracion, "encontramos la letra " , letra,",", len(cLetra), "veces.")
print(" ")
