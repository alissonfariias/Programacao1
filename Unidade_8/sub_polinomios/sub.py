# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Subtração de Polinomios

def subtrai_polinomios(l1,l2):
	while len(l1) < len(l2):
		l1.append(0)
	while len(l1) > len(l2):
		l2.append(0)
		
	saida = []
	for i in range(len(l1)):
		saida.append(l1[i] - l2[i])
	while saida[-1] == 0:
		saida.pop()
	return saida
p1 = [-5, 4, 3]
p2 = [-1, 0, 2, 0, 0, 0, 5]
assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]
