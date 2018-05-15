# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Quem acertou menos

numero = int(raw_input())

l = []
maximo = 0
aluno = 0

for i in range(numero):
	resultado = raw_input()
	cont = 0
	for j in resultado:
		if j == 'f':
			cont += 1
	l.append(cont)

for e in range(len(l)):
	if l[e] > maximo:
		maximo = l[e]
		aluno = e + 1
print "O aluno %i errou %i teste(s)." % (aluno,maximo)
