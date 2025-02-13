#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
print("Introduce la cantidad de las monedas que tienes")
m2=int(input("2 euros: "))
m1=int(input("1 euro: "))
c50=int(input("50 cent: "))
c20=int(input("20 cent: "))
c10=int(input("10 cent: "))

#Calcular la suma de todos los euros en centimos
sumc=((m2*200)+(m1*100)+(c50*50)+(c20*20)+(c10*10))/100

print(f"La cantidad total es: {sumc}")
