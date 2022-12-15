#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabaho dos alunos
#faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada

#podemos iniciar esse programa com dois jeito usando o (import random)
import random
#ou podemos iniciar com (from random import shuffle) ou seja apenas escolhendo apenas a função que vai usar ou seja d
#shuflle 

a = str(input('Digite o nome do primeiro aluno : \n'))
b = str(input('Digite o nome do segundo  aluno : \n'))
c = str(input('Digite o nome do terceiro aluno : \n'))
d = str(input('Digite o nome do quarto   aluno : \n'))

lista = [a,b,c,d]

#função que serve para embaralhar 
random.shuffle(lista)
#shuffle(lista) 

print('A ordem de apresentação será ')
print(lista) 


