
#===========================================
'''        SECUENCIA HASTA UN NUMERO    '''
#===========================================

#FINFORMACION DEL PROGRAMA:

''' Dada la siguiente secuencia, hallar la expresión matemática para  realizar el  calculo
de tal forma que el  usuario  pueda  ingresar un numero y  la  calcule la secuencia
hasta ese numero ingresado1 2 4 8 16 32 64 128 256 512 1024 2048 ......si el  usuario
ingresa 200 debe mostrar la  secuencia  así,  1 2 4 8 16 32 64 128''' 


#FUNCION:

def calcular_secuencia(numero):
    secuencia = []
    for i in range(1, numero+1):
        termino = 2**(i-1)
        
        if termino > numero:
            break
        secuencia.append(termino)
    return secuencia

#VARIABLE:

numero = int(input("Ingrese un número: "))

#LLAMADA DE LA FUNCION:

secuencia_resultante = calcular_secuencia(numero)

#IMPRESION:
print(" ")
print("Secuencia:", secuencia_resultante)
print(" ")