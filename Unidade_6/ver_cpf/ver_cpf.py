# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Ciência da Computação - Programação I
# Aluno: Walisson Nascimento de Farias	Matrícula: 117210716
# Unidade: 6	Questão: Dígitos de Verificação do CPF

def calcula_digitos_verificacao(digitos):
	
	cpf = ''
	for letra in digitos:
		cpf = letra + cpf
	
	mult_1 = 0
	mult_2 = 0
	for i in range(len(cpf)):
		mult_1 += int(cpf[i]) * (i+2) * 10
		mult_2 += int(cpf[i]) * (i+3)
	
	verificador_1 = mult_1 % 11
	
	if verificador_1 == 10:
		verificador_1 = 0
	
	verificador_2 = ((mult_2 + (verificador_1 * 2)) * 10) % 11
	
	if verificador_2 == 10:
		verificador_2 = 0
	
	digitos_verificadores = str(verificador_1) + str(verificador_2)
	return digitos_verificadores

assert calcula_digitos_verificacao('153245875') == '40'
