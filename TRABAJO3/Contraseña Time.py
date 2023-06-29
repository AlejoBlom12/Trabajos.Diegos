
#===========================================
'''      TIME SLEEP + CONTRASEÑA         '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Modificar el programa anterior para que después de cada intento agregue una pausa
cada vez mayor, utilizando la función sleep del módulo time.'''

#CICLO:

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