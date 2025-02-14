#Lidia Castro Gutiérrez
#Versión 1

# 8.Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base=float(input("Dime tu sueldo:"))
venta1=float(input("Dime tu primera venta:"))
venta2=float(input("Dime tu segunda venta:"))
venta3=float(input("Dime tu tercera venta:"))

comision=(venta1+venta2+venta3)*0.10

sueldo_total=comision+sueldo_base

print ("El total cobrado es ", sueldo_total)

print ("La comision es: ",comision)