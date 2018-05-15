# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210716
# Unidade: 3

ano = int(raw_input())

if ano % 400 == 0:
	print "%i é bissexto" % ano
elif ano % 4 == 0 and ano % 100 != 0:
	print "%i é bissexto" % ano
else:
	print "%i não é bissexto" % ano
