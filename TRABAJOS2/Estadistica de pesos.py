
#======================================================
'''               ESTADISTICA DE PESOS             '''
#======================================================

#INFORMACION DEL PROGRAMA: 

''' Se desea realizar una estadística de los pesos de los alumnos de un colegio de
acuerdo a la siguiente tabla:

    Alumnos de menos de 40 kg.
    Alumnos entre 40 y 50 kg.
    Alumnos de más de 50 kg y menos de 60 kg.
    Alumnos de más o igual a 60 kg.''' 
    
#VARIABLES:

alumnos = int(input("Ingrese cantidad de alumnos: "))

#LISTAS:

peso1 = []
peso2 = []
peso3 = []
peso4 = []

#CICLADO CON CONDICIONALES:

for i in range (0, alumnos,1):
    
    peso =int(input("Introduce la masa en KG del alumno "+ str(i+1) +": "))
    

    if peso < 40: 
        peso1.append(peso)

    if peso > 39 and peso < 51:
        peso2.append(peso)

    if peso > 50 and peso < 60:
        peso3.append(peso)

    if peso >= 60:
        peso4.append(peso)

print("\n")
print (" ")
print ("La cantidad de alumnos con un peso menor de 40 Kg es igual a: ", len(peso1))
print (" ")
print ("La cantidad de alumnos con un peso entre 40 Kg y 50 kg: ", len(peso2))
print (" ")
print ("La cantidad de alumnos con un peso mayor a 50 Kg y menor a 60 Kg: ", len(peso3))
print (" ")
print ("La cantidad de alumnos con un peso mayor o igual a 60: ", len(peso4))
print (" ")



