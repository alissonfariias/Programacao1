# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Imprime Ranking (Cumulativo)

n_de_times = raw_input()

lista_nomes = []
lista_pontos = []
for i in range(int(n_de_times)):
	nome_times = raw_input()
	pontos_times = raw_input()
	lista_nomes.append(nome_times)
	lista_pontos.append(pontos_times)

posicao = 0
for l in lista_pontos:
	if lista_pontos[l] != posicao:
		posicao += 1

print posicao
