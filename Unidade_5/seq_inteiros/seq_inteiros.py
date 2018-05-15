# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Imprime Sequencias de Números Inteiros

numero_alvo = int(raw_input())
seque_maiores = []
numeros = []
count = 1
while True:
	sequencia = raw_input().split()
	if sequencia[0] == 'fim':
		break
	maiores = 0
	menores = 0
	for i in range(len(sequencia)):
		if int(sequencia[i]) > numero_alvo:
			maiores += 1
		else:
			menores += 1
	if maiores > menores:
		seque_maiores.append(sequencia)
		numeros.append(count)
	count += 1

for i in range(len(seque_maiores)):
	string = ""
	for e in range(len(seque_maiores[i])):
		string += seque_maiores[i][e] + " "
	print "sequencia %i: %s" %(numeros[i],string.strip())
