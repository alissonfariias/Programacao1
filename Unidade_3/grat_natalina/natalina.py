# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

codigo_cargo = int(raw_input())

if codigo_cargo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
elif codigo_cargo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
elif codigo_cargo == 3:
	gratificacao_por_dia = 2.00
	numero_faltas = int(raw_input())
	gratificacao_total = (235 - numero_faltas) * gratificacao_por_dia
	salario = 8000.00 + gratificacao_total
	print "Valor da gratificação R$ %.2f." % gratificacao_por_dia
	print "Deverá receber em dezembro R$ %.2f." % salario
elif codigo_cargo == 4:
	gratificacao_por_dia = 1.00
	numero_faltas = int(raw_input())
	gratificacao_total = (235 - numero_faltas) * gratificacao_por_dia
	salario = 5000.00 + gratificacao_total
	print "Valor da gratificação R$ %.2f." % gratificacao_total
	print "Deverá receber em dezembro R$ %.2f." % salario
elif codigo_cargo == 5:
	gratificacao_por_dia = 0.8510638298
	numero_faltas = int(raw_input())
	gratificacao_total = (235 - numero_faltas) * gratificacao_por_dia
	salario = 2800.00 + gratificacao_total
	print "Valor da gratificação R$ %.2f." % gratificacao_total
	print "Deverá receber em dezembro R$ %.2f." % salario

