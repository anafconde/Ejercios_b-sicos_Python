#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones

sueldo=float(input("Introduzca cuánto es su sueldo base: "))
venta1=float(input("Introduzca el importe de la primera venta: "))
venta2=float(input("Introduzca el importe de la segunda venta: "))
venta3=float(input("Introduzca el importe de la tercera venta: "))

comision=(venta1*0.1)+(venta2*0.1)+(venta3*0.1)
total=sueldo+(venta1*0.1)+(venta2*0.1)+(venta3*0.1)
print(f"En concepto de comisiones recibirá este mes {comision}€")
print(f"El total de dinero que recibirá este mes es: {total}€")