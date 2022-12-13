#faça um algoritmo que leia um salário de um funcionario e mostre seu novo salário, com 15% de aumento

salário = float (input('Digite o salário do funcionario: \n'))

novo = salário+(salário*15/100)

print('O salário do funcionario era {:.2f} e aumentou para {:.2f}.'.format(salário,novo))

