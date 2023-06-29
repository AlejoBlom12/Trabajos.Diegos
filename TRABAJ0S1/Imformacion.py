
#======================================================
''' MOSTRAR LA SIGUIENTE INFORMACION EN LA CONSOLA '''
#======================================================

#INFORMACION DEL PROGRAMA:
 
''' Cree las variables y asigne los siguientes valores y Muestre la información en consola
de los datos ingresados
nombre = “Andres”
edad = 18
identificacion = “1061555333”
mayor_de_edad = edad >= 18 '''

# VARIABLES:

print("==================== INGRESA TU NOMBRE ============================")
nombre = str(input("Aqui: "))
print("==================== INGRESA TU EDAD  ============================")
edad = int(input("Aqui: "))
print("================ INGRESA TU TRAJETA DE IDENTIDAD =================")
identidad = int(input("Aqui: "))

#CONDICION DE LA EDAD:
print(" ")
if edad >= 18:
    print("Holaa ", nombre ,", tienes" , edad , "Años, por lo tanto eres mayor de edad, tu numero de indentidad es: ", identidad )
else: 
    print("Holaa ", nombre, ", tienes" , edad ,"Años, por lo tanto eres menor de edad, tu numero de identidad es: " , identidad)
print(" ")