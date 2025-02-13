#autor:Richard Bustamante Carreño
#version:1.0

# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese la primera venta: "))
venta2 = float(input("Ingrese la segunda venta: "))
venta3 = float(input("Ingrese la tercera venta: "))

comision = ((venta1+(venta1*0.1))+(venta2+(venta2*0.1))+(venta2+(venta2*0.1)))
resultado = base+comision

print("Comisión total: ", comision)
print("Sueldo total del mes: ", resultado)