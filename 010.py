#crie um programa que leia quanto dinheiro uma pessoa tem  na carteira e mostre quantos dólares ela pode comprar
#considere US$ 1,00 = R$ 5,26

real = float (input('digite a quantidade de dinheiro que você tem na carteira? R$ \n'))

dolar = real / 5.26

print ('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real,dolar))