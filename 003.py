#crie um script python que leia dois número e tenta mostra a soma entre eles.

n1 = int(input('informe o primeiro numero:\n'))
n2 = int(input('informe o segundo numero:\n'))

#lembrando que devemos mostra o tipo dessa variaveis no caso essa é do tipo inteiro

#uma variavel s onde ira soma a as variaveis n1 e n2 ou seja o numero em que o usuario digitou anteriomente será somado
s = n1+n2

#mostra o resutado da soma 
print('A soma entre {} e {} vale: {}'.format(n1, n2, s))