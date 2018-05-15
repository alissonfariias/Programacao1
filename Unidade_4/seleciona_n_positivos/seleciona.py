# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Seleciona os Números Ímpares Positivos

numero = int(raw_input())

for i in range(numero):
	if i % 2 != 0:
		print i
