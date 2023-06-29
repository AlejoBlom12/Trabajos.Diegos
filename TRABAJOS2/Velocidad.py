
#======================================================
'''         DISTANCIA, VELOCIDAD Y TIEMPO         '''
#======================================================

#INFORMACION DEL PROGRAMA:

'''Construye un programa que Si distancia es mayor que 20 y menos que 35, leer un
valor para tiempo y calcular  la  Velocidad si   Distancia = Velocidad * Tiempo'''

#VARIABLE: 

distancia = float(input("Introducir distancia en metros: "))

#CONDICIONAL:
print(" ")
if distancia > 20 and distancia < 35:
    tiempo = float (input("Introducir valor de tiempo en segundos: "))
    
    #ECUACION:
    
    velocidad = distancia / tiempo
     
    print(" ")
    print("Con una distancia de ", distancia , "m , en un tiempo de ", tiempo , "s , se alcanzó un velocidad de" , velocidad, "m/s")

else: 
    print("No se puede hacer el proceso, ya que la distancia debe se mayora 20 m y menor que 35 m.")
print(" ")