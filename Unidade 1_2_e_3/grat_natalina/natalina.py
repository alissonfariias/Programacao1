# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

codigo_cargo = int(raw_input())
if codigo_cargo >= 3 and codigo_cargo <= 5:
	dias_faltou = int(raw_input())
if codigo_cargo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
if codigo_cargo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
if codigo_cargo == 3:
	if dias_faltou == 0:
		gratificacao = 500.00
		salario = 8000.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario 
	elif dias_faltou != 0:
		gratificacao = (235 - dias_faltou) * 2.00
		salario = 8000.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario 
if codigo_cargo == 4:
	if dias_faltou == 0:
		gratificacao = 300.00
		salario = 5000.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	elif dias_faltou != 0:
		gratificacao = (235 - dias_faltou) * 1.00
		salario = 5000.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
if codigo_cargo == 5:
	if dias_faltou == 0:
		gratificacao = 200.00
		salario = 2800.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	elif dias_faltou != 0:
		gratificacao = (235 - dias_faltou) * 0.70
		salario = 2800.00 + gratificacao
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
