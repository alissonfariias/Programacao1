# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Um Passo do Algoritmo BubbleSort

def meu_split(sequencia):
	
	delimitador = ' '
	nova_palavra = ''
	lista = []
	for i in range(len(sequencia)):
		if sequencia[i] != delimitador:
			nova_palavra += sequencia[i]
		else:
			lista.append(int(nova_palavra))
			nova_palavra = ''
	lista.append(int(nova_palavra))
	return lista

lista = []
while True:
	sequencia = raw_input()
	if sequencia[0] == 'fim':
		break
	else:
		sequencia = meu_split(sequencia)
		for i in range(len(sequencia)-1):
			if sequencia[i] > sequencia[i+1]:
				sequencia[i+1], sequencia[i] = sequencia[i], sequencia[i+1]
		
		nova_string = ''
		for j in range(len(sequencia)):
			if j == (len(sequencia)-1):
				nova_string += str(sequencia[j])
			else:
				nova_string += str(sequencia[j]) + ' '
		lista.append(nova_string)

for i in lista:
	print i
