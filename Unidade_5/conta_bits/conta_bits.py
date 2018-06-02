# coding: utf-8

lista = []
while True:
	n_binario = raw_input()
	if n_binario == '0101010101':
		break
	n_binario = n_binario.split('0')
	for num in n_binario:
		if len(num) != 0:
			lista.append(len(num))
	string = ''
	for k in range(len(lista)):
		if k == len(lista)-1:
			string += str(lista[k])
		else:
			string += str(lista[k]) + ' '
	print string
	lista = []
