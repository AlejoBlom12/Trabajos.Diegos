
#===========================================
'''          200 NUMEROS PARES          '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Utiliza la forma matemática para calcular los numeros pares e impares imprimir la
secuencia de los  200 primeros numeros  pares partiendo desde 0'''

#CICLADO BOOLEANO:

while True: 
    par = 0
    
    #CONDICIONAL:
    
    if par % 2 == 0:
        for i in range (par , 200+1 , 2):

            print(i)
        break
    else:

        print("El número que ingresaste es impar.")
