# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Pesquisa Hotéis

valores = [999999,'marca']
tamanhos = [0,'']
confortos = [0,'']
marcas = []
while True:
	seq = raw_input().split(",")
	if seq[0] == "---":
		break
	valor, tamanho, conforto, marca = seq
	if float(valor) < valores[0]:
		valores = [float(valor),marca]
		
	if float(tamanho) > tamanhos[0]:
		tamanhos = [float(tamanho),marca]
		
	if float(conforto) > confortos[0]:
		confortos = [float(conforto),marca]

while True:
	fim = raw_input()
	if fim == 'fim':break
	elif fim == 'valor':print valores[1]
	elif fim == 'conforto':print confortos[1]
	elif fim == 'tamanho':print tamanhos[1]
