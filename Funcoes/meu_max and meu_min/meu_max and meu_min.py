# coding: utf-8

def meu_max(argumento):
	maior = 0
	for i in range(len(argumento)):
		if argumento[i] > maior:
			maior = argumento[i]
	return maior

def meu_min(argumento):
	menor = argumento[0]
	for i in range(len(argumento)):
		if argumento[i] < menor:
			menor = argumento[i]
	return menor
