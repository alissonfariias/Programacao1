# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Filtrando Elementos e Alterando uma Lista

lista1 = [0,1,2,3,4,5,6]

for i in range(len(lista1)):
	if i % 2 != 0:
		lista1.pop(i)

print lista1
