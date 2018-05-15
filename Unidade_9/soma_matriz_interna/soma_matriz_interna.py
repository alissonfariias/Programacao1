# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: Soma Matriz Interna

# def somamatrizinterna(matriz, inicio, fim):

M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
p1 = (1,1)

for i in range(len(M2)):
	for j in range(len(M2[i])):
		if i == p1[0]:
			print j
