
#===========================================
'''           ACCESO PARA ENTRAR         '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Elabora un programa para una discoteca que necesita controlar el acceso a las
personas la  cual pida el nombre a una persona y su edad, en caso  que  sea  mayor
de  18  lo deje ingresar, si es  menor  de edad debe  mostrar un  mensaje diciendole
que no puede ingresar y si  tiene 18 años  debera  preguntar por su  identificación'''

#VARIABLES:

name = str(input("Escriba su nombre: "))
edad = int(input("Introduce tu edad: "))

#CONCICIONALES CON IMPRESIONES:

print(" ")
if edad > 18:
    print(" Bienvenido a la Discoteca,", name )

elif edad == 18: 
    print(name , ", muestrame tu documento para verificar." )

else:
    print(" Lo lamentamos ", name,", no puedes ingresar a la discoteca." )
print(" ")
    
