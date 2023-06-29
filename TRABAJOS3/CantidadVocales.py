
#=========================================
'''         CANTIDAD DE VOCALES        '''
#=========================================

#INFORMACION DEL PROGRAMA:

'''El  usuario ingresa por  teclado  una  oración por  ejemplo 'Estaba sentada la  pájara
pinta' el  programa debe  permitir contar cuantas vocales  hay en esa frase a = 9, e =
2, i = 1, o = 0, u = 0'''

#VARIABLE:

oracion = input("Introduce una frase: ")

#LISTAS:

a = []
e = []
i = []
o = []
u = []

#CICLADO:

for j in oracion:
    if j == "a" or j == "A":
        a.append(j)
        
    elif j == "e" or j == "E":
        e.append(j)
        
    elif j == "i" or j == "I":
        i.append(j)
        
    elif j == "o" or j == "O":
        o.append(j)
        
    elif j == "u" or j == "U":
        u.append(j)
        
#IMPRESIONES:

print("La oracion introducida contiene una cantidad de: ")
print("   ")
print("Vocal a :", len(a) )
print("Vocal e :", len(e) )
print("Vocal i :", len(i) )
print("Vocal o :", len(o) )
print("Vocal u :", len(u) )
print (" ")

