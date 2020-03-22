# 01 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 01')
print('-=-' * 10, '\n')
cont = 0
nota = 0
while cont == 0:
    nota = float(input('Digite uma nota entre 0 (Zero) e 10 (Dez): '))
    if nota >=0 and nota <= 10:
        cont = cont + 1
    else:
        print('Valor Inválido, digite novamente.')
print(f'O número {nota:.1f} é válido.')
print('\n', '-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

# 02 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 02')
print('-=-' * 10, '\n')
nome = input('Nome de usuário  : ').capitalize()
senha = input('Senha            : ')
while senha.upper() == nome.upper():
    print('Senha Inválida. '
          '\nSua senha não pode ser igual ao nome de usuário... '
          '\nDigite novamente.')
    senha = input('Senha            : ')
print('Senha Válida!')
print('\n', '-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

# 03 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 03')
print('-=-' * 10, '\n')
pais1 = 80000
pais2 = 200000
cont = 0
while pais1 <= pais2:
    pais1 = pais1 + pais1 * 3 / 100
    pais2 = pais2 + pais2 * 1.5 / 100
    cont = cont + 1
print(f'Demorará {cont} anos para o país A ultrapassar o país B em total de habitantes...')
print('\n', '-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

# 04 - A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 04')
print('Sequência de Fibonacci')
print('-=-' * 10, '\n')
termo = int(input('Quantidade de termos: '))
valor1 = 0
valor2 = 1
print('-' * 5, 'Resultados')
print(f'{valor1} => {valor2}', end = '')
cont = 3
while cont <= termo:
    resultado = valor1 + valor2
    print(f' => {resultado}', end = '')
    valor1 = valor2
    valor2 = resultado
    cont = cont + 1
print('\n', '-' * 5, 'Fim da Sequência')
print('\n', '-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

# 05 - Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
# o algoritmo de Euclides. 
print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 05')
print('--MDC')
print('-=-' * 10, '\n')
valor1 = int(input('Digite o 1° valor: '))
valor2 = int(input('Digite o 2° valor: '))
mdc = valor1
while valor1 % mdc != 0 or valor2 % mdc != 0:
    mdc = mdc - 1
print(f'MDC {valor1, valor2} = {mdc}')
print('\n', '-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
