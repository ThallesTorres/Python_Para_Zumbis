#Faça um programa que peça dois números inteiros e imprima a soma desses dois números
print('1 - Soma de dois números')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print(f'O resultado é: {n1 + n2}')

#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
print('2 - Conversor de Metros para Milímetros')
nmetros = float(input('Digite um número em metros: '))
print(f'{nmetros} m convertido para milímetros fica: {nmetros * 1000} mm')

#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
print('3 - Conversor de dias, horas, minutos e segundos para segundos ')
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
rdias = dias * 24 * 60 * 60
rhoras = horas * 60 * 60
rminutos = minutos * 60
rsegundos = rdias + rhoras + rminutos + segundos
print(f'A conversão para segundos fica: {rsegundos}')

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
print('4 - Aumento de salário ')
salario = float(input('Valor do salário: '))
porcentagem = float(input('Porcentagem do aumeto: '))
aumento = salario * porcentagem / 100
print(f'Aumento: ${aumento:.2f} \nSalário + Aumento: ${aumento + salario:.2f}')

# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
print('5 - Desconto')
preco = float(input('Preço da mercadoria: '))
desconto = float(input('Desconto: '))
resultado = preco * desconto / 100
total = preco - resultado
print(f'Valor do desconto: R${resultado}')
print(f'Total a pagar: R${total}')

#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
print('6 - Tempo de viagem')
d = float(input('Distância a percorrer (Km): '))
v = float(input('Velocidade média (Km/h): '))
t = d / v
print(f'O tempo de viagem será de: {t:.2f} hora(s)')

#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
print('7 - Conversão de Celsius para Fahrenheirt')
c = float(input('Informe a temperatura em °C: '))
f = c * 9 / 5 + 32
print(f'A temperatura de {c}°C corresponde a {f:.1f}°F')

#Faça agora o contrário, de Fahrenheit para Celsius
print('8 - Conversão de Fahrenheir para Celsius')
f = float(input('Informe a temperatura em °F: '))
c = (f - 32) * 5 / 9
print(f'A temperatura de {f}°F corresponde a {c:.1f}°C')

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
print('9 - Carro Alugado')
d = int(input('Quantidade de Dias alugado: '))
km = float(input('Quantidade de Km percorridos: '))
precod = d * 60
precokm = km * 0.15
print('-' * 5, 'Preços', '-' * 5, f'\nDia: R${precod:.2f} \nKm: R${precokm:.2f} \nTotal: R${precod + precokm:.2f}')

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias
print('10 - Redução do tempo de vida de um Fumante')
d = int(input('Quantidade de cigarros fumados por dia: '))
a = int(input('Por quantos anos? '))
ad = a * 365
th = int((d * 10) / 60)
tm = (d * 10) % 60
h = th + (0.01 * tm)
d = h / 24 * ad
print(f'{d:.0f} dia(s) de vida perdido, recomendamos parar de fumar.')

#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão
print('11 - Quantidade de Digitos')
r = 2 ** 1000000
print(f'2 elevado a 1 milhão tem {len(str(r))} digitos')
