#escreva um programa quue pergunta a quantidade de de KM percorridos, por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado.calcule o preço a pagar, sabendo que o carro custa R$60 por dia R$0.15 por KM rodado.



dias = int(input('informe a quantidade de dias alugados: \n'))
KM = float(input('informe o total de KM rodados: \n'))

preço = (dias * 60) + (KM * 0.15)

print('O total a pagar é R${:.2f}'.format(preço))


