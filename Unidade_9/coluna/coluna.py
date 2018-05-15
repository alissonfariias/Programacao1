# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: Coluna

def coluna(matriz, i):
	lista = []
	for k in range(len(matriz)):
		for j in range(len(matriz[k])):
			if j == i:
				lista.append(matriz[k][j])
	return lista

M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert coluna(M,0) == [1,2,3]
assert coluna(M,1) == [1,2,3]
assert coluna(M,2) == [1,2,3]
assert coluna(M,3) == [1,2,3]
