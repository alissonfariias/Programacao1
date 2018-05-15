# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Organiza Lista pela Média

def organiza_por_media(lista):
	
	if len(lista) == 0:
		return lista
	soma = 0
	for i in lista:
		soma += i
	tamanho = len(lista)
	media = float(soma) / tamanho
	
	cont = 0
	cont2 = 0
	while cont < len(lista) - cont2:
		if lista[cont] > media:
			lista.append(lista.pop(cont))
			cont2 += 1
			cont -= 1
		cont += 1	
	return lista

p1 = [4,2]
assert organiza_por_media(p1) == [2,4]
