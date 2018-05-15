# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Custo Empregado

salario_base = float(raw_input())
dias_trabalhados = int(raw_input())
custo_diario_transporte = float(raw_input())

vale_transporte = dias_trabalhados * custo_diario_transporte

if vale_transporte > 0.06 * salario_base:
	salario_liquido = salario_base * 0.94
else:	

fgts_empregador = salario_base * 0.08
inss_empregador = salario_base * 0.12

if salario_base <= 1371.07:
	inss_empregado = salario_base * 0.08
elif salario_base >= 1317.08 and salario_base <= 2195.12:
	inss_empregado = salario_base * 0.09
else:
	inss_empregado = salario_base * 0.11
	
salario_liquido = salario_base - (vale_transporte + inss_empregado)
custo_empregador = salario_base + vale_transporte + fgts_empregador + inss_empregador

print "O salário base é R$ %.2f" % salario_base
print "O custo mensal para o empregador é de R$ %.2f" % custo_empregador
print salario_liquido
