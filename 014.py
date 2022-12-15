#convertendo a temperatura de celsius para fahrenheit

c  = float(input('informe a temperatura em °C: \n'))
F = (9*c)/5 + 32
print('A temperatura em {}°C corresponde a {}°F '.format(c,F)) 

#convertendo a temperatura de fahrenheit para celsius
f = float(input('informe a temperatura em °F: \n'))
C = (5*(f-32)/9)
print('A temperatura em {}°F corresponde a {}°C '.format(f ,C))

#convertendo a temperatura de celcius para kelven
celsius = float(input('informe a temperatura em °C: \n'))
K = celsius + 273
print('A temperatura em {}°C corresponde a {}°K \n'.format(celsius, K))

