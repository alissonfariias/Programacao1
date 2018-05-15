# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: Meu Split

def meu_split(delimitador, palavra):

	nova_palavra = ''
	lista = []
	for i in range(len(palavra)):
		if palavra[i] != delimitador:
			nova_palavra += palavra[i]
		else:
			lista.append(nova_palavra)
			nova_palavra = ''
	lista.append(nova_palavra)
	return lista

print meu_split('*', 'comida*mouse*computador*abacate')
