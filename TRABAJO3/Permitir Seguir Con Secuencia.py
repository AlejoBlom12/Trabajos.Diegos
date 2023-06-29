
#===========================================
'''           SECUENCIA NUMEROS          '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Realiza un programa que imprima una secuencia de numeros de uno en uno desde el
que el usuario desee, el programa debe pedirle al usuario después de que imprima un
numero en pantalla le pregunte si desea continuar o no mostrando en pantalla'''

#CICLADO BOOLEANO CON CONDICIONES:

while True:
    # VARIABLE:
    inicio = int(input("Ingrese el número para el inicio de la secuencia: "))
    fin = 1000000
    
    for num in range(inicio, fin + 1):
        print(num)
        
        respuesta = str(input("¿Desea Seguir con la secuencia? (s/n): "))
        if respuesta == "s" or respuesta == "S":
            continue
        else:
            break









    
