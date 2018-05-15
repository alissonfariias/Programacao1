# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 5	Questão: Série (ímpare 1)

for i in range(1,102,2):
	if i % 3 == 0 or i % 5 == 0:
		print '*'
	else:
		print i
