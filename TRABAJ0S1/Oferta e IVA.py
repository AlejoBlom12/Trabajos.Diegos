
#==========================================================
'''           CALCULAR EL IVA O OTRA OFERTA            '''
#==========================================================

#INFORMACION DEL PROGRAMA:

'''Calcule el  valor  del  IVA 19% y el descuento de un producto ingresado por teclado'''

#VARIABLES:

valor = int(input("Valor del producto: "))
iva = 19


info = print ('''Que deseas hacer con aquel valor:
                            1. IVA 
                            2. Oferta en especifico''')

info = int(input("Ingrese que deseas hacer: "))
               
#CONDICIONES:
print(" ")         
if info == 1:
      
      ecu1 = (valor*iva)/100
      print(" ")
      print ("El valor con IVA es igual a: ", valor - ecu1 )
      print(" ")
elif info == 2:
      print("  ")
      oferta = int(input("ingrese la oferta del producto: "))
      oferta = (valor/100) * oferta
      print(" ")
      print("Le valor con la oferta indicada es igual a :", oferta)
print(" ")         