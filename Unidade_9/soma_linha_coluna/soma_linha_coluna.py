# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: Soma Linha e Coluna

def soma_linha_e_coluna(matriz,l,c):
	
	soma = 0
	for i in range(len(matriz[l])):
		if i != c:
			soma += matriz[l][i]
	
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if j == c and i != l:
				soma += matriz[i][j]
	
	return soma

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]

assert soma_linha_e_coluna(matriz,1,1) == 20
assert soma_linha_e_coluna(matriz,0,0) == 18
