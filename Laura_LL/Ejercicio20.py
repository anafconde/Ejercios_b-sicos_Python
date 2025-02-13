#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)

e2=int(input("Introduce cuantas monedas de 2 euros tiene: "))
e1=int(input("Introduce cuantas monedas de 1 euro tiene: "))
c50=int(input("Introduce cuantas monedas de 50 cent tiene: "))
c20=int(input("Introduce cuantas monedas de 20 cent tiene: "))
c10=int(input("Introduce cuantas monedas de 10 cent tiene: "))

total=((e2*200)+(e1*100)+(c50*50)+(c20*20)+(c10*10))/100

print(f"El dinero total que tiene sumando todas sus monedas es: {total}")