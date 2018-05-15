# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Soma os Divisores do Primeiro Elemento de uma Lista

soma = 0
referencia = int(raw_input())
for i in range(10):
	x = int(raw_input())
	if referencia % x == 0:
		soma += x

print soma
