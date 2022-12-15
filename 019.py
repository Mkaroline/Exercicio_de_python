#um professor quer sortear um dos seus quatros alunos para apagar o quadro faça
#um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
#funcao rendom serve para número aleatorio
a = str(input('aluno 1:\n'))
b =str(input(' aluno 2: \n'))
c = str(input('aluno 3:\n'))
d = str(input('aluno 4: \n'))

lista = [a, b, c, d]

#função que serve para radonizar ou seja permiter escolher um valor aleatorio
escolhido = random.choice(lista)

print('o aluno sorteado foi: {}'.format(escolhido))              
            