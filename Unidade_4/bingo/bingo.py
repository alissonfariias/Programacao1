# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Bingo

cartela1 = raw_input().split()
cartela2 = raw_input().split()

pontos1 = 0
pontos2 = 0
while True:
	num_sorteado = int(raw_input())
	for i in range(len(cartela1)):
		if num_sorteado == int(cartela1[i]):
			pontos1 += 1
		if num_sorteado == int(cartela2[i]):
			pontos2 += 1
	if pontos1 == len(cartela1) and pontos2 == len(cartela2):
		print 'Empate.'
		break
	elif pontos1 == len(cartela1) and pontos2 < len(cartela2):
		print 'Bingo! Jogador 1 venceu.'
		break
	elif pontos1 < len(cartela1) and pontos2 == len(cartela2):
		print 'Bingo! Jogador 2 venceu.'
		break
