# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Desenhando uma Árvore de Natal

altura = int(raw_input())

lista = []
elemento = 'o'
for i in range(altura):
	lista.append(elemento)
	elemento += 'oo'

for j in range(len(lista)):
	print (' ' * (altura - j - 1)) + lista[j] 
print ' ' * (altura - 1) + 'o'
