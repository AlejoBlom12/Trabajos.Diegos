
#==========================================================
'''                  MINI CALCULADORA                   '''
#==========================================================

#INFORMACION DEL PROGRAMA:

'''Elabore una minicalculadora que al ingresar 2 numeros me calcule el resultado de la
suma, resta, producto, division, exponenciaxion, modulo de la division'''

#VARIABLES:

x = float (input("Introducir primer numero: "))
y = float (input("Introducir segundo numero: "))





informacion =  print('''¿Que quieres hacer? Escoge con la siguiente informacion.
                    1) sumar
                    2) restar
                    3) multiplicar 
                    4) dividir
                    5) potenciar''')


informacion = int(input("Elige una accion de los anteriores: "))

#CONDICONES Y IMPRESIONES:
print (" ")
if informacion == 1:
   print("Resultado de la suma entre: ", x ,"+",y,"es igual: " , x + y )

elif informacion == 2:
   print("Resultado de la resta entre: ", x ,"-",y,"es igual: " , x - y )
   
elif informacion == 3:
   print("Resultado de la multiplicacion entre: ", x ,"x",y,"es igual: " , x * y )

elif informacion == 4:
   
#EXCEPCIONES:

   try:
      operacion = x / y
      print("Resultado de la division entre: ", x ,"/",y,"es igual: ", operacion)
   except :
      print("La divicion por cero no se puede hacer ")

elif informacion == 5:
   print("Resultado de la potenciacion entre: ", x ,"^",y,"es igual: " , x ** y )
print("  ")