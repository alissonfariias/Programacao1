# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Conjunto com mais elementos

cont = 0
lista = []
while True:
	numero = raw_input()
	cont += 1
	if numero == 'fim':
		break
	if int(numero) < 0:
		indices = 1
		lista.append(cont-1)
		cont = 0

maximo = 0
indice = 0
for i in range(len(lista)):
	if lista[i] > maximo:
		maximo = lista[i]
		indice = i+1



if maximo > 0:
	print 'Conjunto %i - %i elemento(s)' % (indice,maximo)
