# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Maiores e Menores

pivot = int(raw_input())

lista_menores = []
lista_maiores = []
while True:
	seq = int(raw_input())
	if seq < 0:
		break
	if seq <= pivot:
		lista_menores.append(seq)
	else:
		lista_maiores.append(seq)

print lista_menores
print pivot
print lista_maiores
