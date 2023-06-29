
#======================================================
'''      CALCULAR EL AREA DE UN TRIANGULO         '''
#======================================================

#INFORMACION DEL PROGRAMA:

'''Crea un Algoritmo que nos calcule el área de un triángulo conociendo sus lados'''

#VARIABLES:

lado = float(input("Introducir lo que mide el lado: "))
base = float(input("Introducir lo que mide la base: "))

#CONDICIONALES:
print(" ")
if lado > base:
    if lado and base > 0: 

#FUNCIONES:

        def areaTriangulo (a , b):
            import math
            
            b1 = b / 2 
            #DIVIMOS LA BASE A LA MITAD PORQUE EL TRIANGULO AL PARTIRLO A LA MITAD, 
            #SE GENERA UN TRIANGULO RECTANGULO
            
            elevado1 = a ** 2
            elevado2 = b1 ** 2
   

            elevadoT = elevado1 - elevado2
        

            altura = math.sqrt(elevadoT)
        
            
    
            area = (b * altura)/2
            
            print(" El area de el triangulo con los lados dados es: " + str(area))
            
        #LLAMANDO LA FUNCION:
        
        areaTriangulo(lado, base)
    else:
        print("No pueden ser numeros que no signifiquen nada (Negativos y en cero).")

else:
    print("El lado debe ser mayor que la base.")
print(" ")

