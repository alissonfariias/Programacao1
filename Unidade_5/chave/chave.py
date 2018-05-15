# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Analisa Chave

senha = raw_input()

senha_valida = True
cont_vogais = 0
for i in range(len(senha)-2):
	if senha[i] == senha[i+1] and senha[i] == senha[i+2]:
		print 'Chave insegura. 3 caracteres consecutivos iguais.'
		senha_valida = False
		break
	if senha[i] in 'AEIOUaeiou':
		cont_vogais += 1
		if cont_vogais > 5:
			print 'Chave insegura. 6 vogais.'
			senha_valida = False
			break

if senha_valida:	
	print 'Chave segura!'
