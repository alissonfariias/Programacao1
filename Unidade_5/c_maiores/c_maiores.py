# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 5
# QUESTÃO: Conjuntos Maiores

limite = int(raw_input())
conjuntos = raw_input()

for k in conjuntos:
	soma = 0
	while True:
		valor = int(raw_input())
		if valor < 0:
			break
		else:
			soma += valor
	if soma > limite:
		print 'conjunto %i: %i' % ((int(k)+1),(soma))
