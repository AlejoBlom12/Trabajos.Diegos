
#===========================================
'''         CONTRASEÑA + BOOLEANO        '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).'''

#CICLADO BOOLEANO:
while True:
    
    #CICLADO
    for i in range (5):
        import time
        
        #VARIABLE:
        
        contraseña = str(input("Introduce contraseña: "))
        time.sleep (2)
        
        #CONDICIONAL:
        
        if contraseña != "SAI":
            
            print ("Contraseña incorrecta")
            time.sleep (1)
            continue

        elif contraseña == "SAI":
            time.sleep (1)
            print("Contraseña correcta")
            time.sleep (2)
            print("     ")
            print("Bienvenido, SAI")
            time.sleep (1)
            break