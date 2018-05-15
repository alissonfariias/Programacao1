# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Unidade: 7	Questão: Números Oscilantes

entrada = raw_input()

def numero(entrada):
	if int(entrada[0]) % 2 == 0:
		valor = 'p'
	else:
		valor = 'i'
	for i in range(1,len(entrada)):
		if int(entrada[i]) % 2 == 0 and valor == 'i':
			valor = 'p'
		elif int(entrada[i]) % 2 != 0 and valor == 'p':
			valor = 'i'
		else:
			return 'falso'
	return 'verdadeiro'

print '{}: {} algarismos.'.format(numero(entrada), len(entrada))
