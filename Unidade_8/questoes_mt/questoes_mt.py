# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Questões para mt

def seleciona_questoes(todas, utilizadas):
	for i in range(len(utilizadas)-1,-1,-1):
		for j in range(len(todas)-1,-1,-1):
			if utilizadas[i] == todas[j]:
				todas.pop(j)
