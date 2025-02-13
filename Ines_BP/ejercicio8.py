#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

base=float(input("Introduce el sueldo base: "))
c1=float(input("Introduce la venta 1: "))
c2=float(input("Introduce la venta 2: "))
c3=float(input("Introduce la venta 3: "))

total=base+(c1*0.1)+(c2*0.1)+(c3*0.1)

print(f"El sueldo total asciende a {total}")