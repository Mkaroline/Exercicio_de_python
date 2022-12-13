#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta, pinta uma área de 2 metros ao quadrado.
largura=float(input(' informe a largura da parede: \n'))
altura = float(input('informe o comprimento da parede: \n'))

área = largura * altura
tinta = área / 2

print('A sua parede tem a dimensâo {}x{} e sua área é de {}m2.'.format(largura, altura,área))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))