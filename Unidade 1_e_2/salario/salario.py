# coding: utf-8

salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())
print "Salário Bruto =", salario_bruto
hora_bruta = salario_bruto / horas_de_trabalho
print "Hora Bruta =", hora_bruta
desconto_ir = salario_bruto*11/100
print "Desconto IR =", desconto_ir
desconto_inss = salario_bruto*8/100
print "Desconto INSS =", desconto_inss
sindicato = salario_bruto*5/100
print "Desconto Sindicato =", sindicato
salario_liquido = salario_bruto - desconto_ir - desconto_inss - sindicato
print "Salário Líquido =", salario_liquido
hora_liquida = salario_liquido / horas_de_trabalho
print "Hora Líquida =", hora_liquida
