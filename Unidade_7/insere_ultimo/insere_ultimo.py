# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Inserção ordenada do último elemento de uma lista

def insere_ordenado_ultimo(l1):
	if l1[0] > l1[-1]:
		l1[0], l1[-1] = l1[-1], l1[0]
	for i in range(len(l1)):
		if l1[i] < l1[-1] and l1[i+1] > l1[-1]:
			l1[i+1], l1[-1] = l1[-1], l1[i+1]

