# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
somatorio = numero1 + numero2 + numero3
if somatorio % 3 == 0 and somatorio % 5 == 0:
	print 'plifplof'
elif somatorio % 3 == 0:
	print 'plif'
elif somatorio % 5 == 0:
	print 'plof'
