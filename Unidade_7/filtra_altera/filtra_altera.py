# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Filtrando Elementos e Alterando uma Lista

def filtra_altera_lista(num, lista):

	for i in range(len(lista)-1,-1,-1):
		if i % num != 0:
			lista.pop(i)
	
	return lista

lista = [0,1,2,3,4,5,6]

filtra_altera_lista(2, lista)
assert lista == [0,2,4,6]

filtra_altera_lista(3, lista)
assert lista == [0,6]
