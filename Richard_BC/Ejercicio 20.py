#autor:Richard Bustamante Carreño
#version:1.0

#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

sum = ((m2*200)+(m1*100)+(c50*50)+(c20*20)+(c10*10))/100

print(f"La cantidad total es: {sum}")