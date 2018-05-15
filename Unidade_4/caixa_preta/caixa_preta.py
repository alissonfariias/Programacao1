# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Caixa Preta

qtd = int(raw_input())

cont = 0
dadosValidos = True
for i in range(qtd):
	medicoes = raw_input().split()
	peso = int(medicoes[0])
	combustivel = int(medicoes[1])
	altitude = int(medicoes[2])
	if dadosValidos:
		if peso < 0:
			print 'dado inconsistente. peso negativo.'
			dadosValidos = False
		elif combustivel < 0:
			cont += 1
			dadosValidos = False
			print 'dado inconsistente. combustível negativo.'
		elif altitude < 0:
			cont += 2
			dadosValidos = False
			print 'dado inconsistente. altitude negativa.'
		else: 
			cont += 3
print '%i dados válidos.' % cont
