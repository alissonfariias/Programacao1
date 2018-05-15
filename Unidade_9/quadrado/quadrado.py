# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: É Quadrado Mágico?

quadrado = [[2,7,6],[9,5,1],[4,3,8]]

lista = []
for i in quadrado:
	for j in i:
		if j not in lista:
			lista.append(j)

aux = []
for i in quadrado:
	for j in i:
		aux.append(j)

if lista == aux:
	for i in range(len(quadrado)):
		print quadrado[0][i]
