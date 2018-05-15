# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Descarta Coincidente

quant_numeros = raw_input()

descartados = []
quant_descartados = 0
lista = []
for i in range(int(quant_numeros)):
	numero = raw_input()
	lista.append(numero)
	for j in range(len(numero)):
		if int(numero[j]) == j:
			descartados.append(numero)
			quant_descartados += 1
			break

print '---'

aceitos = []
quant_aceitos = 0
for i in range(len(lista)):
	if lista[i] in descartados:
		pass
	else:
		aceitos.append(lista[i])
		quant_aceitos += 1

print '%i aceito(s)' % quant_aceitos
for i in range(len(aceitos)):
	print aceitos[i]

print '%i descartado(s)' % quant_descartados
for i in range(len(descartados)):
	print descartados[i]
