# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Flip

l1 = [1, 2, 3, 4, 5, 6, 7]
i = 2
j = 5

for n in range(len(l1)-1,-1,-1):
	if n == j:
		for k in range(n, i, -1):
			l1[k], l1[k-1] = l1[k-1], l1[k]
print l1
