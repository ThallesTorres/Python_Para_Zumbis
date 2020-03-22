'''
01 - Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior
e o menor valor, sem usar as funções max e min.
'''

from random import randint

print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 01')
print('-=-' * 10, '\n')

lista = []
maior = 0
menor = 100

for a in range(10):
    numeros = randint(1, 100)
    lista.append(numeros)

    if numeros < menor:
        menor = numeros
    if numeros > maior:
        maior = numeros

lista.sort()
print(lista)
print(f'Menor: {menor} \nMaior: {maior} \n')

print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

'''
02 - Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números
pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três
listas.
'''

from random import randint

print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 02')
print('-=-' * 10, '\n')
 
lista, lista_par, lista_impar = [], [], []

for a in range(20):
    numeros = randint(0, 100)
    lista.append(numeros)

    if numeros % 2 == 0:
        lista_par.append(numeros)
        
    else:
        lista_impar.append(numeros)

lista.sort()
lista_impar.sort()
lista_par.sort()

print('--Dados')
print(f'Lista Bruta \n{lista}\n')
print(f'Lista Ímpar \n{lista_impar}\n')
print(f'Lista Par \n{lista_par}\n')

print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

'''
03 - Faça um programa que crie dois vetores com 10 elementos
aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados
dos dois outros vetores. Imprima os três vetores.
'''

print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 03')
print('-=-' * 10, '\n')

from random import randint

vetor1, vetor2, vetor3 = [], [], []

for x in range(10):
	vetor1.append(randint(1, 100))
	vetor2.append(randint(1, 100))
	vetor3.append(vetor1[x])
	vetor3.append(vetor2[x])

vetor1.sort()
vetor2.sort()
vetor3.sort()

print(f'1° Vetor:{vetor1}')
print(f'2° Vetor:{vetor2}')
print(f'3° Vetor:{vetor3} \n')

print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

'''
04 - Gere uma lista de palavras deste texto com split(), a seguir crie
uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes
os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''

print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 04')
print('-=-' * 10, '\n')

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our
community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.
'''#Eu poderia colocar eles aqui - .lower().replace('.', ' ').replace(',', ' ').replace(':', ' ').split()

texto = texto.lower()
texto = texto.replace('.', ' ').replace(',', ' ').replace(':', ' ')
texto = texto.split()

total = []

for p in texto:
  if p[0] in 'python' or p[-1] in 'python':
    total.append(p)

print(f'Total: {len(total)}')
print(f'Lista: {total} \n')

print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')

'''
 05 - Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
'''

print('-=-' * 10)
print('--Seja Bem Vindo')
print('--Exercício 05')
print('-=-' * 10, '\n')

texto = '''The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you.
'''.lower().replace('.', ' ').replace(',', ' ').replace(':', ' ')

texto = texto.split()
in_python = []
maior_q_4 = 0
lista_palavras = []

for s in texto:
	p = s
	if p[0] in "python":
		in_python.append(s);
		if(len(s) > 4): 
			maior_q_4 += 1
			lista_palavras += s
			

print (f"Total de {maior_q_4} palavras... \n")

print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
