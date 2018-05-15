# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Caixa Preta Descartando Leituras

cont_peso = 0
cont_combustivel = 0
cont_altitude = 0
while True:
	dados = raw_input().split()
	peso = int(dados[0])
	combustivel = int(dados[1])
	altitude = int(dados[2])
	if peso >= 0:
		cont_peso += 1
		if combustivel >= 0:
			cont_combustivel += 1
			if altitude >= 0:
				cont_altitude += 1
	if peso < 0:
		print 'dado inconsistente. peso negativo.'
		break
	if combustivel < 0:
		print 'dado inconsistente. combustível negativo.'
		break
	if altitude < 0:
		print 'dado inconsistente. altitude negativa.'
		break

print 'peso: %i' % cont_peso
print 'combustível: %i' % cont_combustivel
print 'altitude: %i' % cont_altitude
