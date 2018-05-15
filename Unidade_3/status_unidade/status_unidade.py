# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

mtp = int(raw_input())

if mtp < 2:
	nota1 = float(raw_input())
	media = nota1 / 1
	print media
	print "Aluno ainda não aprovado na unidade"

elif mtp == 2:
	nota1 = float(raw_input())
	nota2 = float(raw_input())
	media = (nota1 + nota2) / 2
	if media < 6.0:
		print media
		print "Aluno ainda não aprovado na unidade"
	else:
		print media
		print "Aluno aprovado na unidade"

elif mtp > 2:
	nota1 = float(raw_input())
	nota2 = float(raw_input())
	nota3 = float(raw_input())
	media = (nota1 + nota2 + nota3) / 3
	media_nova = media - 0.5
	print media_nova
	if media_nova < 6.0:
		print "Aluno ainda não aprovado na unidade"
	else:
		"Aluno aprovado na unidade"
