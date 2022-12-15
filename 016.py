from math import floor
#floor arredondamento pra baixo
n = float(input('digite um número qualquer: \n'))
print('A parte inteira do número {} é {}'.format(n,floor(n)))

#sqrt para raiz quadrada
from math import sqrt
n1 = float(input('digite um número qualquer: \n'))
print('A raiz quadrado do número {} é {:.2f}'.format(n1,sqrt(n1)))

#ceil arredondamento para cima 
from math import ceil
n2 = float(input('digite um número qualquer: \n'))
print('O  arredondamento do número  {} é {}'.format(n2,ceil(n2)))

#trunc elemina os números depois da vírgula
from math import trunc
n3 = float (input('Digite um número qualquer \n'))
print('O número {} sem a virgula para frente é {} '.format(n3,trunc(n3)))

#
from math import pow
n4 = float(input('Digite um número qualquer: \n'))
print('A potência do número é {}'.format(n4,(n4)))
