# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Unidade: 7	Questão: Calculadora de Médias

while True:
	operacao = raw_input().split()
	if operacao[0] == 'Q':
		break
	numeros = raw_input().split()
	mult = 1
	soma = 0
	soma_i = 0
	for i in operacao:
		if i == 'MA':
			for i in numeros:
				soma += float(i)
			media_a = soma / len(numeros)
			print 'Média Aritmética: %.4f' % media_a
		elif i == 'MG':
			for j in numeros:
				mult *= float(j)
			media_g = mult ** (1.0 / (len(numeros)))
			print 'Média Geométrica: %.4f' % media_g
		elif i == 'MH':
			for k in numeros:
				soma_i += 1.0/float(k)
			media_h = len(numeros) / soma_i
			print 'Média Harmônica: %.4f' % media_h
	print '----'
