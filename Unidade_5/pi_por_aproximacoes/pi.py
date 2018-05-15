# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 5	Questão: Pi por aproximações

a = float(raw_input())

cont1 = 0
cont2 = 1
pi = 0
pi2 = 0
while True:
	if cont1 % 2 == 0:
		pi += (1.0 / cont2)
	elif cont1 % 2 != 0:
		pi -= (1.0 / cont2)
	
	print '%.6f' % (4*pi)
	
	if abs(pi2 - 4 * pi) <= a:
		break
	
	pi2 = 4 * pi
	cont1 += 1
	cont2 += 2
