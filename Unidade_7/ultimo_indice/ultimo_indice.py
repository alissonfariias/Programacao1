# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Último Índice

def ultimo_indice(num, lista):

	for i in range(len(lista)):
		if num not in lista:
			resultado = int('-1')
		if num == lista[i]:
			resultado = i
	
	return resultado

assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
