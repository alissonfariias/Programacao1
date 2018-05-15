# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Busca Todos em Matriz

def busca_matriz(m, e):

	lista = []
	for i in range(len(m)):
		for j in range(len(m[i])):
			if e not in m[i]:
				return []
			if m[i][j] == e:
				lista.append((i, j))
	
	return lista

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
