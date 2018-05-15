# coding: utf-8

def meu_count(sequencia, item):
	cont = 0
	for i in sequencia:
		if item == i:
			cont += 1
	return cont
