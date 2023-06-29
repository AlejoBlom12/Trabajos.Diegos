
#===========================================
'''              CONTRASEÑA              '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Escribir un programa que contenga una contraseña inventada, que le pregunte al
usuario la contraseña, y no le permita continuar hasta que la haya ingresado
correctamente.'''
    
#VARIABLE:  
  
contraseña = str(input("Introduce contraseña: "))

#CICLADO CON CONDICIONALES:

while contraseña:  
        
    if contraseña != "SAI":
                
        print ("Contraseña incorrecta")
        contraseña = str(input("Introduce contraseña: "))   
        
        

    elif contraseña == "SAI":
        
        print("Contraseña correcta")
            
        print("     ")
        print("Bienvenido, SAI")
        break
        
    



