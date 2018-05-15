# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Classificação de Elementos Utilizando a Média dos Extremos

quantidade = int(raw_input())

lista = []
for i in range(quantidade):
	numero = int(raw_input())
	lista.append(numero)

maior = 0
menor = 
for j in lista:
	if j > maior:
		maior = j
	elif j < menor:
		menor = j

media = float(maior) / 2.0

abaixo = 0
acima = 0
for k in lista:
	if k < media:
		abaixo += 1
	elif k > media:
		acima += 1

print 'Menor número: %i' % menor
print 'Maior número: %i' % maior
print 'Média dos extremos: %.2f' % media
print '%i número(s) abaixo da média' % abaixo
print '%i número(s) acima da média' % acima
