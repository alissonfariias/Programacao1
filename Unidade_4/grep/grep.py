# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Grep

palavra_chave = str(raw_input())
n = int(raw_input())

for i in range(n):
	frase = str(raw_input())
	if palavra_chave in frase:
		print frase
