# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: MinMax Sort = Selection Sort Duplicado

def minmax_sort(lista):
	lista_aux = []
	for i in range(len(lista)/2):
		
		indice_do_menor = i
		indice_do_maior = len(lista)-i-1
		
		for j in range(i+1, len(lista)-i):
			if lista[j] < lista[indice_do_menor]:
				indice_do_menor = j
		lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
		
		for k in range(i+1, len(lista)-i):
			if lista[k] > lista[indice_do_maior]:
				indice_do_maior = k
		lista[len(lista)-i-1], lista[indice_do_maior] = lista[indice_do_maior], lista[len(lista)-i-1]
		
		local = lista[:]
		lista_aux.append(local)
	return lista_aux
