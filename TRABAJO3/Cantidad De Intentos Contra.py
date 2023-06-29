
#===========================================
'''         CONTRASEÑA + INTENTOS       '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.'''

#CICLO:
for i in range (5):
    
    #VARIABLE:  
    contraseña = str(input("Introduce contraseña: "))
    
    #CONDICIONALES:    
    if contraseña != "SAI":
        
        print ("Contraseña incorrecta")
        print("Has utilizado ", str(i+1) + "/5 intentos")
        continue
    

    elif contraseña == "SAI":
      
        print("Contraseña correcta")
        
        print("     ")
        print("Bienvenido, SAI")
        
        break