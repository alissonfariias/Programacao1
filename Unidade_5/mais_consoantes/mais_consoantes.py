# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Mais consoantes

quant_vogais = 0
quant_consoantes = 0
cont = 0
while True:
	palavra = raw_input()
	quant_vogais = 0
	quant_consoantes = 0
	cont += 1
	for i in palavra:
		if i in 'aeiouAEIOU':
			quant_vogais += 1
		else:
			quant_consoantes += 1
	if quant_consoantes > quant_vogais:
		break
	
print cont
