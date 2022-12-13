#crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

#o úsuario irá informa um valor
n = int(input('informe um valor: '))

# p ele mostra o dobro do valor
# p1 irá mostra o triplo do valor 
# p2 irá mostra a raiz quadrada do valor 

p = n * 2
p1 = n * 3
p2 = n**2

#mostra o resutado do dobro,triplo e a raiz quadrado do valor digitou anteriomente.
print('o dobro do número {} é {} e seu triplo {} e a raiz quadrada é {}'.format(n, p, p1, p2))