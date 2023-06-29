
#========================================================
'''        SUMA DE FRACCIONES Y DESCOMPOSICION        '''
#========================================================

#FUNCIONES:

def MCM(num1, num2, num3):
    maximo = max(num1, num2, num3)
    mcm = maximo

    while True:
        if mcm % num1 == 0 and mcm % num2 == 0 and mcm % num3 == 0:
            break
        mcm += maximo
        
    return mcm
def usoMCM (numero1,numero2 ):
    divisor = mcm / numero1
    numerador = divisor * numero2
    
    return numerador

def MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_numeros(num1, num2):
    mcd = MCD(num1, num2)
    simplificado1 = num1 // mcd
    simplificado2 = num2 // mcd
    return simplificado1, simplificado2

#VARIABLES:

n1 = int (input("Introduce el primer numerador: "))
d1 = int (input("Introduce el primer dividendo: "))
n2 = int (input("Introduce el segundo numerador: "))
d2 = int (input("Introduce el segundo dividendo: "))
n3 = int (input("Introduce el tercer numerador: "))
d3 = int (input("Introduce el tercer dividendo: "))

a,b,c = d1,d2,d3

#ESTRUCTURAS CONDICIONALES Y LLAMADAS DE FUNCIONES:

print("  ")
print("Las fraciones correspondientes son: ")
print(" ")
print(str(n1) + "/" + str(d1) + " , " + str(n2)+ "/" + str(d2) + " , " + str(n3) + "/" + str(d3))
print(" ")
mcm = MCM(a, b, c)
print(" ")
print("El mínimo común múltiplo de", a, ",", b, "y", c, "es:", mcm)
print(" ")
nume1 = usoMCM(d1, n1)
nume2 = usoMCM(d2, n2)
nume3 = usoMCM(d3, n3)

print("Despues de la division la factorizacion queda de la siguiente manera")
print("  ",nume1," ? ",nume2," ? ",nume3)
print("-------------------------- ")
print("          ",mcm,"          ")

print("  ")
print ('''Define que deseas hacer con los numeradores:
       1)Sumar todas las fracciones.
       2)Sumar los dos primeras fracciones y restar la ultima.
       3)Restar las dos primeras fraccion y sumar la ultima.
       4)Restar todas las fracciones.
       ''')
info = int(input("Introduce tu decision: "))
print(" ")
if info == 1:
    numeTotal= nume1 + nume2 + nume3
    
    print("  ",nume1," + ",nume2," + ",nume3, "      " , numeTotal)
    print("---------------------------- =", "-------")
    print("          ",mcm,"          ","      " ,mcm)
    
elif info == 2:
    
    numeTotal= nume1 + nume2 - nume3
    
    print("  ",nume1," + ",nume2," - ",nume3, "      " , numeTotal)
    print("---------------------------- =", "-------")
    print("          ",mcm,"          ","      " ,mcm)
    
elif info == 3:
    
    numeTotal= nume1 - nume2 + nume3
    print("  ",nume1," - ",nume2," + ",nume3, "      " , numeTotal)
    print("---------------------------- =", "-------")
    print("          ",mcm,"          ","      " ,mcm)
    
elif info == 4:
    
    numeTotal= nume1 - nume2 - nume3 
    print("  ",nume1," - ",nume2," - ",nume3, "      " , numeTotal)
    print("---------------------------- =", "-------")
    print("          ",mcm,"          ","      " ,mcm)
    
simplificado1, simplificado2 = simplificar_numeros(numeTotal, mcm)
print("  ")
print("Los números simplificados son:  ", simplificado1)
print("                               ", "----------")
print("                                 ", simplificado2)
    