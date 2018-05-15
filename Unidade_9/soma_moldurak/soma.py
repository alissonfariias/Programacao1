# coding: utf-8
# Universidade Federal de Campina Grande
# Período : 2017.2
# Aluno: Walisson Nascimento de Farias 		Matrícula: 117210716
# Unidade: 9	Questão: Soma Moldura k

M = [[1,  2,  3,  4 ],
     [5,  6,  7,  8 ],
     [9,  10, 11, 12],
     [14, 15, 16, 17]]

soma = 0
for i in range(len(M)):
	if i == 0 or i == len(M)-1 :
		for j in range(len(M[i])):
			soma += M[i][j]
	else:
		soma += M[i][0]
		soma += M[i][-1]

print soma
