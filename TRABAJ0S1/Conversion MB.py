
#=========================================================
'''        CONVERTIR MB A (Bits, Bytes, Kb, GB)       '''
#=========================================================

#INFORMACION DEL PROGRAMA:

'''De acuerdo con la tabla realice un programa que convierta una unidad a otra unidad,
por  ejemplo  si el usuario ingresa 1 MB el  sistema  deberá  arrojar  el siguiente
resultado

    1MB son:
    8388608 Bits
    1048576 Bytes
    1024 Kb
    0.000976563 GB'''

# VARIABLE

n1= float(input("introducir numero: "))

#CONDICIONALES: 
print(" ")
if n1 >= 1:
    print("==============================================")
    print ("Las unidades incoorporado son: ", n1 ,"MB:")
    print("==============================================")
    print(n1*8388608, "Bits")
    print(n1*1048576 ,"Bytes")
    print(n1*1024 , "Kb")
    print(n1*0.000976563 , "GB")


else:
    print(" ")
    print ("No es posible hacer una ecuacion inexistente.")
print(" ")