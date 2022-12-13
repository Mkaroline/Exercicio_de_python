#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivos e todos
#as informaçôes possiveis sobre ela.

#úsuario vai digitar algo 
n = (input('Digite algo:\n'))

# de acordo com que o úsuario digitar vai mostra na tela o tipo primitivo ,ou seja ,se for int, float, str, bool e mostrará todas as informações sobre ela.

print('o tipo primitivo desse valor é ', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É um alfabético? ', n.isalpha())
print('É um alfanumérico? ', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())