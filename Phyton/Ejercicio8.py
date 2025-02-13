# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado: Ejercicio 8: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Ingresa el sueldo base del vendedor: "))


venta1 = float(input("Ingresa el monto de la primera venta: "))
venta2 = float(input("Ingresa el monto de la segunda venta: "))
venta3 = float(input("Ingresa el monto de la tercera venta: "))


comision_venta1 = venta1 * 0.10
comision_venta2 = venta2 * 0.10
comision_venta3 = venta3 * 0.10


total_comisiones = comision_venta1 + comision_venta2 + comision_venta3


ingreso_total = sueldo_base + total_comisiones


print("\n--- Resultados ---")
print(f"Comisiones por la primera venta: ${comision_venta1}")
print(f"Comisiones por la segunda venta: ${comision_venta2}")
print(f"Comisiones por la tercera venta: ${comision_venta3}")
print(f"Total de comisiones del mes: ${total_comisiones}")
print(f"Ingreso total del mes (sueldo + comisiones): ${ingreso_total}")
