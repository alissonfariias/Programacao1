# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Espaço por Vírgula

frase = raw_input()
inteiro_i = int(raw_input())
inteiro_j = int(raw_input())

string2 = ""
for i in range(inteiro_i,inteiro_j):
	if frase[i] == " ":
		if i == inteiro_j - 1:
			string2 += ','
		else:
			string2 += ', '
	else:
		if i == inteiro_j - 1:
			string2 += frase[i]
		else:
			string2 += frase[i] + " "

print string2
