# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: QUantas PAs?

razao = int(raw_input())
pasCont = 0
while True:
	cont = 0
	sequencias = raw_input().split()
	if sequencias[0] == 'fim':
			break
	for i in range(len(sequencias)-1):
		if int(sequencias[i]) + razao == int(sequencias[i+1]):
			cont += 1
	if len(sequencias) -1 == cont:
		pasCont += 1

print pasCont
