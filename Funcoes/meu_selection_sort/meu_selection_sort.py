# Selection Sort:

for i in range(len(lista)-1):
	indice_do_menor = i
	for j in range(i+1, len(lista)):
		if lista[j] < lista[indice_do_menor]:
			indice_do_menor = j
	lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
	print lista
