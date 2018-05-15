# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

numero_aposta = int(raw_input())
cor_aposta = str(raw_input())
numero_sorteado = int(raw_input())
cor_sorteada = str(raw_input())

if numero_aposta == numero_sorteado and cor_aposta == cor_sorteada:
	print '150'
elif numero_aposta == numero_sorteado and cor_aposta != cor_sorteada:
	print '100'
elif numero_aposta != numero_sorteado and cor_aposta != cor_sorteada:
	print '0'
elif cor_aposta == cor_sorteada:
	pontos = 50
	if numero_sorteado > numero_aposta:
		print pontos + 30
	elif numero_sorteado < numero_aposta:
		print pontos + 50
