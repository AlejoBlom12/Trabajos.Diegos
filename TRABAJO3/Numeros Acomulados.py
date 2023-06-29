
#===========================================
'''            NUMERO ACOMULADO          '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Realice un programa que acumule todo numero  ingresado  por  el  usuario, el
programa  deberá  finalizar cuando el  usuario ingrese el numero 0,  el  programa  al
final  debe mostrar cual  es el numero acumulado'''

#VARIABLE:

acumulado = 0

#CICLADO BOOLEANO:

while True:
    
    #VARIABLE:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    
    #CONDICIONAL:
    if numero == 0:
        break
    else:
        acumulado += numero

print("El número acumulado es: ", acumulado)
