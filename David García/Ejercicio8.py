#Ejercicio 8
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

ventas = float(input("Introduce el valor total de las ventas: "))
porcentaje_comision = float(input("Introduce el porcentaje de comisión: "))

comision = ventas * (porcentaje_comision / 100)
sueldo_total = ventas + comision

print("La comisión es: {}".format(comision))
print("El sueldo total es: {}".format(sueldo_total))