# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Busca Linear

def busca(seq, valor):
	for i in range(len(seq)):
		if seq[i] == valor:
			return i
	return -1
