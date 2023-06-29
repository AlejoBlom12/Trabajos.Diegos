
#================================================
'''    IDENTIFICA UN NUMERO ENTERO O REAL     '''
#================================================

#INFORMACION DEL PROGRAMA:

'''Empleo de estructura selectiva para detectar si un número es entero o real'''

#VARIABLE:

numero = input("Ingrese un número: ")

#CONDICIONAL CON IMPRESIONES:

print("  ")
if numero.isdigit():
    print("Es un número entero positivo.")

elif numero[0] == '-' and numero[1:].isdigit():
    print("Es un número entero negativo.")
else:
    
    #EXCEPCIONES:
    
    try:
        numero_real = float(numero)
        print("Es un número real.")
    except ValueError:
        print("No es un número válido.")
print("  ")
