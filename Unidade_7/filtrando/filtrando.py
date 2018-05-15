# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Filtrando Elementos em uma Lista

def  filtra_lista(num, lista):
	
	lista_nova = []
	for i in range(len(lista)):
		if i % num == 0:
			lista_nova.append(lista[i])
	return lista_nova
