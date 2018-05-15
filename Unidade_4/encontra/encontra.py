# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Encontra Elemento

numero = raw_input()

lista = []
for i in numero:
	seq = raw_input().split()
	lista.append(seq)

for i in lista:
	if numero in lista:
		print 'sim'
	else:
		print 'não'
