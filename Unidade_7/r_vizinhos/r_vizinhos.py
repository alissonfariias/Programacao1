# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Resolve Vizinhos

def resolve_vizinhos(seq):
	for i in range(len(seq)-1):
		if seq[i] == seq[i+1]:
			seq[i] += 1
			if seq[i] == seq[i-1] and i != 0:
				seq[i] += 1

seq = [1,2,5,5,8,4]
resolve_vizinhos(seq)
assert seq == [1,2,6,5,8,4]
