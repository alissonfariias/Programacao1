# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: A Primeira Letra em Caixa Alta

def meu_split(string):
	lista = []
	aux = ''
	for c in string:
		if c == ' ':
			lista.append(aux)
			aux = ''
		else:
			aux += c
	lista.append(aux)
	return lista

def meu_join(lista):
	string = ''
	for i in range(len(lista)):
		if i != len(lista)-1:
			string += lista[i] + ' '
		else:
			string += lista[i]
	return string

def caixa_alta(string):
	lista = meu_split(string)
	alt = []
	for i in range(len(lista)):
		if len(lista[i]) < 2:
			alt.append(lista[i].lower())
		else:
			aux = lista[i][0].upper()
			for k in range(1, len(lista[i])):
				aux += lista[i][k]
			alt.append(aux)
	return meu_join(alt)

assert caixa_alta("A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
