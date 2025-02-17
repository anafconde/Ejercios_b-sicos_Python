# Alvaro Luzon Muñoz
#---version 1.0----
#Calcular el perímetro y área de un rectángulo dada su base y su altura.

Base = float(input("dame la base: "))
altura = float(input("dame la altura: "))

perimetro = Base*2 + altura*2 
area = Base * altura

print("El perimetro es:" ,perimetro)
print("El area es:" ,area)