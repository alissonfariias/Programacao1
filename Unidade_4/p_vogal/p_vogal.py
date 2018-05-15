# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Primeira Vogal

palavra = raw_input()
tem_vogal = False
for i in range(len(palavra)):
	if palavra[i] in 'aeiouAEIOU' :
		vogal = palavra[i]
		tem_vogal = True
		break
		
if tem_vogal == True:
	print vogal
else:
	print '-'
