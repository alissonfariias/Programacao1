# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Conta Divisíveis

k = int(raw_input())
n = int(raw_input())

cont = 0
for i in range(n):
	numero = raw_input()
	if int(numero) % k == 0:
		cont += 1
	else:
		pass

porcentagem = cont * 100.0 / n
print '%i (%.1f%%)' % (cont,porcentagem)
