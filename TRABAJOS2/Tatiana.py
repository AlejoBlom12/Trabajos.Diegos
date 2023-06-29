
#===========================================
'''            GASTOS DE TATIANA         '''
#===========================================

#INFORMACION DEL PROGRAMA: 

'''Tatiana tiene  ganas  de salir  con su amiga Paola a tomar un cafe  pero ella  sabe
que si va al  centro comercial Campanario deberá pagar transporte ida y regreso  y los
cafes de ambas, pero  si va a Terraplaza se ahorra el transporte,  pero  tambien debe
tener encuenta que  el  cafe  en Terraplaza es 2 veces mas costoso que en
campanario el cual  tiene un costo de 4000 y tambien cuenta con  20000 el  tranporte
seria en bus por un valor  de 1600  el  programa le debe decir a Tatiana cual seria la
mejor opcion que debe tomar'''

#VARIABLES:

cuenta = float(input("Ingresa tu cantidad de dinero: "))

#FUNCIONES:

def calcularCampanario (a): 
    transporte = (1600 * 2) * 2
    cafe = 4000 * 2
    gastos = transporte + cafe
    return  a - gastos
     
   

def calcularTerraplaza (a): 
    transporte = (0 * 2) * 2
    cafe = 8000 * 2
    gastos = transporte + cafe
    return  a - gastos 
    
#LLAMAR FUNCIONES:
  
campanario = calcularCampanario(cuenta)
terraplaza = calcularTerraplaza(cuenta)

#CONDICIONALES CON IMPRESION:

print(" ")
if campanario > terraplaza:
    print("Es recomendable ir a campanario ya que te sobra ", campanario , ", mientras que en terraplaza te sobra ", terraplaza)
else:
    print("Es recomendable ir a terraplaza ya que te sobra ", terraplaza , ", mientras que en campanario te sobra ", campanario)
print(" ")