# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 6, Questão: Soma e Diminui Vizinhos!

quant_numeros = int(raw_input())

aceitos = []
descartados = []
for i in range(quant_numeros):
	seq = raw_input()
	for i in range(len(seq)):
		if int(seq[i]) == i:
			descartados.append(seq)
			break
		else:
			aceitos.append(seq)
			break
print '---'
print '%i aceito(s)' % len(aceitos)
for i in aceitos:
	print i
print '%i descartado(s)' % len(descartados)
for i in descartados:
	print i
