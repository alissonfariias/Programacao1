# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Remove Palavras com Letras Iguais Consecutivas

def remove_consecutivas(lista):
	for i in range(len(lista)-1,-1,-1):
		encontrou = False
		for j in range(len(lista[i])-1):
			if lista[i][j] == lista[i][j+1]:
				encontrou = True
			elif lista[i][j].lower() == lista[i][j+1]:
				encontrou = True
			elif lista[i][j].upper() == lista[i][j+1]:
				encontrou = True
		if encontrou:
			lista.pop(i)

lista = ['arara', 'tv',   'bacia']
assert remove_consecutivas(lista) == None
assert lista == ['arara', 'tv',  'bacia']

lista1 = ['arara', 'arroba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'bacia']

lista2 = ['rrara', 'arobaa', 'rr']
assert remove_consecutivas(lista2) == None
assert lista2 == []

lista4 = ['bB', 'rrara', 'arobaa', 'rr']
assert remove_consecutivas(lista4) == None
assert lista4 == []
