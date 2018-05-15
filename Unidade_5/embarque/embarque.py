# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Embarque Organizado

sequencia = raw_input().split()
for i in range(len(sequencia)):
	sequencia[i] = int(sequencia[i])

test = 0
i = 0
while not(i == len(sequencia)-1):
	if sequencia[i] % 2 == 0:
		for j in range(i, len(sequencia)):
			if sequencia[j] % 2 != 0:
				test += 1
				
	i += 1
	
	if test == 0 and i == len(sequencia)-1:
		print 'ok'
	elif test > 0 and i == len(sequencia)-1:
		print 'erro'
