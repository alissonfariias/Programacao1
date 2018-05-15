# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Unidade: 7	Questão: Inserção ordenada do primeiro elemento de uma lista

def insere_ordenado_primeiro(lista):
	for i in range(len(lista)-1):
		if lista[i] > lista[i+1]:
			lista[i], lista[i+1] = lista[i+1], lista[i]
l1 = [5,2,6,9,11,13]
insere_ordenado_primeiro(l1)
assert l1 == [2,5,6,9,11,13]

l2 = [3,1,2,4]
insere_ordenado_primeiro(l2)
assert l2 == [1,2,3,4]
