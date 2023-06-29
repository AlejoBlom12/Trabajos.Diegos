
#===========================================
'''            NOMINA LABORAL            '''
#===========================================

#INFORMACION DEL PROGRAMA:

'''Se desea obtener la nómina semanal —salario neto— de los empleados de una
empresa cuyo trabajo se paga por horas y del modo siguiente:

    las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa
    determinada que se debe introducir por teclado al igual que el número de horas y el
    nombre del trabajador,
    las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas
    normales,
    los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
        sueldo <= 2.000, libre de impuestos,
        las siguientes 220 euros al 20 por 100,
        el resto, al 30 por 100.'''
        
#VARIABLES:

name = str(input("Nombre del trabajador: "))
hora = int(input("Introduce la cantidad de horas trabajadas: "))

tarifa = 15

#CONDICIONALES CON IMPRESIONES:

print(" ")
if hora <= 35: 
        salarioSemanal = hora * tarifa 
        
        print("Hola!!, " + str(name) + " el salario por tus horas trabajadas es de " , salarioSemanal, "euros", "/ Tu salario mensual es de ", salarioSemanal * 4, "euros")
elif hora > 35:
        salarioSemanal = 35 * tarifa 
        horasEx = (hora - 35)
        valorHorasEx = (horasEx * 20) * 1.5
        
        salarioConHorasEx = (valorHorasEx  + salarioSemanal) * 4
        
        
        if salarioConHorasEx <= 2000:
                print("Hola!!, " + str(name) + " el salario por tus horas trabajadas es de" , salarioConHorasEx *4 , "euros")

        elif 2000 < salarioConHorasEx <= 2220:
                impuesto = (20*salarioConHorasEx)/100
                salario = salarioConHorasEx - impuesto
                print("Hola!!, " + str(name) + " el salario por tus horas trabajadas es de " , salario, "euros")

        elif 2220 < salarioConHorasEx:
                impuesto = (30*salarioConHorasEx)/100 
                salario = salarioConHorasEx - impuesto
                print("Hola!!, " + str(name) + " el salario mensual por tus horas trabajadas es de " , salario, "euros")
print(" ")

