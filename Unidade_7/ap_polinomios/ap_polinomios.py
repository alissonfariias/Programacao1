# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Aplicação Polinômios

def cria_polinomio(string):
	lista = []
	polinomios = string.split()
	for i in range(1,len(polinomios)):
		lista.append(int(polinomios[i]))
	return lista

polinomios = raw_input()
while polinomios != 'fim':
	print 'novo polinomio'
	while True:
		x = raw_input()
		if x == 'fim':
			polinomios = 'fim'
			break
		if x[0] == 'p':
			polinomios = x
			break
		polinomio_atual = cria_polinomio(polinomios)
		
		soma = 0
		for i in range(len(polinomio_atual)):
			soma += polinomio_atual[i] * int(x) ** i
		print soma
