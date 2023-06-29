
#===========================================
'''     NUMERO ACOMULADO + CANTIDAD      '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Al programa anterior debe modificarlo y agregarle que al final  muestre el numero
acumulado y la cantidad de numeros ingresados por el usuario'''

#VARIABLES:

acumulado = 0
cantidad = 0

#CICLO BOOLEANO::

while True:
    
    #VARIABLE:
    
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    else:
        acumulado += numero
        cantidad += 1

#IMPRESION:
print(" ")        
print("El número acumulado es: ", acumulado)
print(" ")        
print("La cantidad de numeros acumulados es de: ", cantidad)
print(" ")        