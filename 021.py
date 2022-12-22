# crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todos as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('digite seu nome completo :\n')).strip()
print('Analisando o seu nome....')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)- nome.count(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letra'.format(separa[0], len(separa[0])))

