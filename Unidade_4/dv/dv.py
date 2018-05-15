# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Calcula DV

numero = raw_input()
soma_par = 0
soma_impar = 0
for i in range(len(numero)):
	if i % 2 == 0:
		soma_par += int(numero[i])
	else:
		soma_impar += int(numero[i])

calculo = soma_par * soma_impar
resto = calculo % 11
if resto == 10:
	print '%s-X' % numero
else:
	print '%s-%i' % (numero,resto)
