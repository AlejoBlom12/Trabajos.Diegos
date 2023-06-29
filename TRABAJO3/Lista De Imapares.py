
#===========================================
'''       IMPARES PREDETERMINADOS        '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Realiza un programa que muestre los numeros impares desde un numero
predeterminado hasta otro numero predeterminado'''

# VARIABLES:

numero1 = int(input("Ingrese un numero natural: "))
numero2 = int(input("Ingrese un numero natural: "))

#FUNCION CON CICLADO:

def listaPares (num1, num2):
    pares = []
    if num1 % 2 != 0 and num2 % 2 != 0:
        if num1 >= num2:
            for i in range (num2 , num1+2, 2):
                pares.append(i)
                
        else:
            for i in range (num1 , num2+2 , 2):
                pares.append(i)
                     
    elif num1 % 2 == 0 and num2 % 2 != 0: 
        num1 = num1 + 1 
          
        if num1 >= num2:
            for i in range (num2 , num1 , 2):
                pares.append(i)
                
        else:
            for i in range (num1 , num2+2 , 2):
                pares.append(i)
                
    elif num1 % 2 != 0 and num2 % 2 == 0: 
        num2 = num2 + 1 
          
        if num1 >= num2:
            for i in range (num2 , num1 , 2):
                pares.appendprint(i)
                
        else:
            for i in range (num1 , num2+2 , 2):
                pares.append(i)
    else: 
        num1 = num1 + 1 
        num2 = num2 + 1 
          
        if num1 >= num2:
            for i in range (num2 , num1 , 2):
                pares.append(i)
                
        else:
            for i in range (num1 , num2 , 2):
                pares.append(i)
    return pares

#IMPRESION:
print(" ")                
print("La lista de numeros pares entre el numero", numero1, "Hasta", numero2, "es", listaPares (numero1, numero2))
print(" ")                
