# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Limite de Gastos

media_mensal = float(raw_input())

medias_maiores = []
while True:
	sequencia = raw_input().split()
	if sequencia[0] == 'fim':
		break
	soma = 0
	for i in sequencia:
		soma += float(i)
	media = soma / len(sequencia)
	if media > media_mensal:
		medias_maiores.append(sequencia)
	if media_mensal / 2 > media:
		break

for i in range(len(medias_maiores)):
	string = ''
	for e in range(len(medias_maiores[i])):
		string += medias_maiores[i][e] + ' '
	print string.strip()
