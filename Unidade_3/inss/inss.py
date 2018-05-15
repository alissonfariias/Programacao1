# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

salario = float(raw_input())
inss_empregador = (salario * 12) / 100
print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador
if salario <= 1317.07:
	inss_empregado = (salario * 8) / 100
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado
elif salario > 1317.08 and salario <= 2195.12:
	inss_empregado = (salario * 9) / 100
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado
elif salario > 2195.12:
	inss_empregado = (salario * 11) / 100
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado
