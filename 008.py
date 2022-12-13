#escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

#úsuario vai digitar um valor em metros 
n = int(input('Digite um valor em metros:'))

#centrimetros dividir o valor por 100
#miimetro dividir o valor por 1000
cem = n/100
mil = n/1000

#por fim mostrará o resutado o que era metros foi convertdo para centrimetros e milimetros
print('o valor',n,'em centrimetro é {} e milimetro {}'.format(cem,mil))