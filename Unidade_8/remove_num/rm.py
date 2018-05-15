# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Remove Números Opostos Adjacentes

def anula(lista):
	i = 0
	fim = len(lista)-1
	while i < fim:
		if lista[i] + lista[i+1] == 0:
			lista.pop(i)
			lista.pop(i)
			fim -= 2
			if i != 0:
				i -= 1
		else:
			i += 1

lista1 = [1, 2, -2, 3, 4]
assert anula(lista1) == None
assert lista1 == [1, 3, 4]

lista2 = [1, 2, -2, -1, 4]
assert anula(lista2) == None
assert lista2 == [4]
