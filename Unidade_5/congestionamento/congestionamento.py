# coding: utf-8

lista = []
cont = 0
while True:
	entrada = raw_input()
	for letra in entrada:
		if letra == 'v':
			cont += 1
		elif letra != 'v':
			lista.append(cont)
			cont = 0
	lista.append(cont)
	maior = 0
	for num in lista:
		if num > maior:
			maior = num
	print maior
	lista = []
	break
