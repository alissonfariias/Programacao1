# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Porta Eletrônica

lista_registros = []
lista_contagens = []
while True:
	dados = raw_input().split()
	if dados[0] == 'S':
		break
	if dados[0] == 'R':
		lista_registros.append(dados[1][0])
	if dados[0] == 'P':
		pesquisa = dados[1]
		cont = 0
		for i in lista_registros:
			if i == pesquisa:
				cont += 1
		lista_contagens.append(cont)
		if i != pesquisa:
			cont += 1

for i in range(len(lista_contagens)):
	print lista_contagens[i]
