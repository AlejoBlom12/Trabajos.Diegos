
#===========================================
'''        PICO Y PLACA VEHICULOS        '''
#===========================================

#INFORMACION DEL PROGRAMA: 

'''Realizar  un programa para saber que día tiene pico y placa su vehículo'''

#VARIABLE:

placa = input("Introducir placa: ")

#CONDICIONALES: 
print(" ")
if len(placa) == 6:

#EXCEPCIONES:

    try: 
        x = int (placa[5])
    except:
        x = int (placa[4])


    if x == 6 or x == 9:
        print("Tienes pico y placa el Lunes.")

    elif x == 5 or x == 7:
        print("Tienes pico y placa el Marte.")

    elif x == 1 or x == 4:
        print("Tienes pico y placa el Miercoles.")

    elif x == 8 or x == 0:
        print("Tienes pico y placa el Jueves.")

    elif x == 3 or x == 2:
        print("Tienes pico y placa el Viernes.")

else: 
    print ("Placa invalida, no es posible los espacios.")
print(" ")