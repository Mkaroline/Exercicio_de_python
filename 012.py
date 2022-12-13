#faça um algoritmo que leia o preço de um produto e mostar seu novo preço, com 5% desconto
produto = float(input('Informe o preço do produto: '))

desconto = produto-(produto* 5/100)

print('O produto que custava R${}, na promoçâo com desconto de 5% vai custar R${:.2f}'.format(produto,desconto))