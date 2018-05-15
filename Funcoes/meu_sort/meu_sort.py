# coding: utf-8:

lista = [9, 7, 1, 6, 3, 8, 1, 99, 0]
for i in range(len(lista)-1, 0, -1):
	if lista[i] < lista[i-1]:
		lista[i], lista[i-1] = lista[i-1], lista[i]
	print lista
	
