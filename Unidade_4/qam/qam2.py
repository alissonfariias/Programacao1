# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Quem acertou menos

numero = int(raw_input())
mais_f = 0
num_f = 0
for i in range(numero):
	resultado = raw_input()
	cont = 0
	for j in resultado:
		if j == 'f':
			cont += 1
	if cont > mais_f:
		mais_f = i+1
		num_f = cont

print "O aluno %i errou %i teste(s)." % (cont,num_f)
