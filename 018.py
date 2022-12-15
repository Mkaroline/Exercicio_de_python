#faça um progrma que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

#pode ser assim de modo mais complexo de entende mais as duas sâo fácil de compreender
import math 
a = float(input('informe um angulo qualquer: \n'))

SENO = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a,SENO))

COSSENO = math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a,COSSENO))

TANGENTE = math.tan(math.radians(a))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(a,TANGENTE))


#pode ser de modo mais facil de entender
from math import radians, sin, cos,tan
a = float(input('informe um angulo qualquer: \n'))

SENO = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a,SENO))

COSSENO = cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a,COSSENO))

TANGENTE = tan(radians(a))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(a,TANGENTE))

