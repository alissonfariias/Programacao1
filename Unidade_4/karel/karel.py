# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Karel, o Robô!

x = 0
y = 0
while True:
	comando = raw_input().split()
	lado = comando[0]
	move = int(comando[1])
	if move == 0:
		print 'Fim de jogo'
		break
	if lado == 'C':
		y += move
	elif lado == 'B':
		y -= move
	elif lado == 'E':
		x -= move
	elif lado == 'D':
		x += move
	if (abs(x) * 2) == abs(y) and x != 0:
		print 'Parabéns, conquista do portal (%i, %i)' % (x, y)
		break

