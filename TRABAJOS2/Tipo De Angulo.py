
#===========================================
'''            TIPO DE ANGULOS           '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90
grados y recto si es igual a 90 grados. Utilizando esta información, escribir un
algoritmo que acepte un ángulo en grados y visualice el tipo de ángulo
correspondiente a los grados introducidos'''

#VARIABLE:

angulo = float(input("Ingrese un ángulo en grados: "))

#CONDICIONALES: 

print(" ")
if angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
   print("El ángulo es llano.")
else:
   print("El ángulo es cóncavo.")
   
print(" ")