# 01 - Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print('--Seja Bem Vindo--')
m1 = float(input('Informe a 1° Medida do triângulo: '))
m2 = float(input('Informe a 2° Medida do triângulo: '))
m3 = float(input('Informe a 3° Medida do triângulo: '))
if m1 == m2 == m3:
    n = 'EQUILÁTERO'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')
elif (m1 + m2) < m3 or (m1 + m3) < m2 or (m2 + m3) < m1:
    print('De acordo com as medidas informadas, é impossivel ser um triângulo.')
elif m1 == m2 or m1 == m3 or m2 == m3:
    n = 'ISÓSCELES'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')
else:
    n = 'ESCALENO'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')
print('--Obrigado pelo uso--')

# 02 - Determine se um ano é bissexto. Verifique no Google como fazer isso...
from datetime import date
print('--Seja Bem Vindo--')
ano = int(input('Que ano quer analisar? (coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é um ano BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é um ano BISSEXTO.')
print('--Obrigado pelo uso--')

# 03 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.
print('--Seja Bem Vindo--')
peso = float(input('Digite o peso total (Kg): '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Excesso (Kg): {excesso:.2f} \nMulta (R$): {multa:.2f}')
else:
    print(f'Excesso (Kg): 0 \nMulta (R$): 0')
print('--Obrigado pelo uso--')

# 04 - Faça um programa que leia três números e mostre o maior deles.
print('--Seja Bem Vindo--')
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3
print(f'O Maior número é o {maior}')
print('--Obrigado pelo uso--')

# 05 - Faça um Programa que leia três números e mostre o maior e o menor deles.
print('--Seja Bem Vindo--')
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3
menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print('--Obrigado pelo uso--')

# 06 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido
print('--Seja Bem Vindo--')
ganho_por_hora = float(input('Ganho por hora: '))
horas_por_mes = float(input('Número de horas trabalhadas no mês: '))
ganho_total = ganho_por_hora * horas_por_mes
imposto_de_renda = ganho_total * 11 / 100
inss = ganho_total * 8 / 100
sindicato = ganho_total * 5 /100
salario_liquido = ganho_total - imposto_de_renda - inss - sindicato
print(f'Salário Bruto:              R$ {ganho_total}')
print(f'Imposto de Renda (11%):     R$ {imposto_de_renda:.2f} ')
print(f'INSS (8%):                  R$ {inss:.2f}')
print(f'Sindicato (5%):             R$ {sindicato:.2f}')
print(f'Salário Liquido:            R$ {salario_liquido:.2f}')
print('--Obrigado pelo uso--')

# 07 -Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
print('--Seja Bem Vindo--')
tamanho_area = float(input('Tamanho da Área (m²):'))
if tamanho_area % 54 == 0:
    latas = tamanho_area / 54
else:
    latas = int(tamanho_area / 54) + 1
preco = latas * 80
print(f'{latas} Latas')
print(f'Preço Total: R$ {preco}')
print('--Obrigado pelo uso--')
