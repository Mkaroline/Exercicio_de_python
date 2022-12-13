#faça um programa que leia um número e mostra na tela o seu antecessor e sucessor.
#úsuario vai digitar um número
n1 = int(input('Digite um Número: '))
#usei a subtracao, ou seja, a variável (n1 - 1) para descobrir o antecessor 
subtraçâo = n1 - 1

#usei a soma, ou seja, a variável(n1 +1) para descobrir o sucessor
soma = n1 + 1

#um printf para mostra o resultado ex:5, vai mostra o antecessor 4 e seu sucessor 6
print('o Antecessor de {} é {} e o seu Sucessor é {}'.format(n1, subtraçâo, soma))

