#escreva um programa que leia o comprimento do cateto opsto e do cateto adjacente de um retângulo, calcule e mostre o comprimento da hipotenusa
#obs: podemos resolver esse programa com duas solucoes possivel 

#1podemos resolver com um jeito tradicional 
cateto_oposto = float (input('digite o comprimento do cateto oposto: \n'))
cateto_adjacente = float (input('digite o comprimento do cateto adjacente: \n'))

hipotenusa = (cateto_oposto **2 + cateto_adjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

#2 podemos resolver com um jeito mais fácil usando o import math

#from math import hypot
import math
co= float (input('digite o comprimento do cateto oposto: \n'))
ca = float (input('digite o comprimento do cateto adjacente: \n'))

h = math.hypot (co, ca)

print('A hipotenusa vai medir {:2.2f}'.format(h))
      