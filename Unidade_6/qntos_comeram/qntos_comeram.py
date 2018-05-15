# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: Quantos Comeram?

def quantos_comeram(N, fila):
	quantidade_feijoada = int(N)
	quantidade_inicial = int(N)
	for i in range(len(fila)):
		if quantidade_feijoada < fila[i]:
			break
		quantidade_feijoada -= fila[i]
	return quantidade_inicial - quantidade_feijoada

assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
