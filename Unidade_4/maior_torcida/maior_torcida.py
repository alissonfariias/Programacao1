# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Maior Torcida

soma_1 = 0
soma_2 = 0
for i in range(1,6):
	primeiro_time = int(raw_input())
	segundo_time = int(raw_input())
	soma_1 += primeiro_time
	soma_2 += segundo_time

if soma_1 > soma_2:
	print 'O primeiro time leva mais torcedores ao estádio.'
elif soma_1 < soma_2:
	print 'O segundo time leva mais torcedores ao estádio.'
else:
	print 'Empate.'
