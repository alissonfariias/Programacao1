# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Aluno: Walisson Nascimento de Farias - 117210716
# Programação I
# Unidade: 4	Questão: Palavras com Vogais Adjacentes

quant_palavras = int(raw_input())
vogais = 'aeiouAEIOU'

quant = 0
for i in range(quant_palavras):
	palavra = raw_input()
	for i in range(len(palavra)):
		if palavra[i] in vogais and i != (len(palavra)-1):
			if palavra[i+1] in vogais:
				quant += 1
				break

print quant
