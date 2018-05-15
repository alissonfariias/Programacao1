# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210716

nome1 = str(raw_input())
dia1 = int(raw_input())
mes1 = int(raw_input())
ano1 = int(raw_input())
nome2 = str(raw_input())
dia2 = int(raw_input())
mes2 = int(raw_input())
ano2 = int(raw_input())

if ano1 < ano2:
	print nome1
elif ano1 < ano2 and mes1 < mes2:
	print nome1
elif ano1 < ano2 and mes1 < mes2 and dia1 < dia2:
	print nome1
elif ano1 == ano2 and mes1 < mes2:
	print nome1
elif ano1 == ano2 and mes1 == mes2 and dia1 < dia2:
	print nome1
elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
	print "nenhuma"
else:
	print nome2
