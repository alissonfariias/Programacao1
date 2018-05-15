# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Abaixo da Média

quant_valores = 0
soma_valores = 0.0
lista_valores = []
while True:
	valor = raw_input()
	if valor == 'fim':
		break	
	valor = int(valor)	
	lista_valores.append(valor)
	quant_valores += 1.0
	soma_valores += valor
	
media = soma_valores / quant_valores

print '%.2f' % media

for i in range(len(lista_valores)):
	if lista_valores[i] < media:
		print i+1, lista_valores[i]
