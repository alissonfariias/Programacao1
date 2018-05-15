# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Tabela de Quadrados

x = int(raw_input())
y = int(raw_input())

if x > y:
	print "---"

for i in range(x,y+1):
	print i, i ** 2
